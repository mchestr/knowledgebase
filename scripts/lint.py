#!/usr/bin/env python3
"""Structural lint for the wiki. Uses only the standard library, so CI needs no install step.

Exit code is 1 when there are errors (or warnings with --strict), else 0.
"""

from __future__ import annotations

import argparse
import datetime as dt
import json
import re
import sys
from collections import defaultdict
from dataclasses import asdict, dataclass, field
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
WIKI = ROOT / "wiki"
RAW = ROOT / "raw"

SPECIAL = {"index", "log"}
TYPE_DIRS = {
    "overview": WIKI,
    "source": WIKI / "sources",
    "entity": WIKI / "entities",
    "concept": WIKI / "concepts",
    "synthesis": WIKI / "syntheses",
}
CITING_TYPES = {"entity", "concept", "synthesis"}
REQUIRED = ("title", "type", "created", "updated")
LOG_OPS = {"ingest", "query", "lint", "update"}
ASSET_EXTS = {
    ".png", ".jpg", ".jpeg", ".gif", ".svg", ".webp",
    ".pdf", ".csv", ".json", ".txt", ".mp3", ".mp4",
}
STALE_DAYS = 180

FRONTMATTER = re.compile(r"\A---\n(.*?)\n---[ \t]*\n?", re.S)
WIKILINK = re.compile(r"(!?)\[\[([^\]|#]+)(?:#[^\]|]*)?(?:\|[^\]]*)?\]\]")
INLINE_CODE = re.compile(r"`[^`\n]*`")
LOG_HEADING = re.compile(r"^## \[(\d{4}-\d{2}-\d{2})\] (\w+) \| (\S.*)$")


@dataclass
class Issue:
    severity: str
    code: str
    path: str
    message: str
    line: int | None = None


@dataclass
class Page:
    path: Path
    name: str
    meta: dict | None
    links: list[tuple[str, int, bool]] = field(default_factory=list)

    @property
    def type(self) -> str | None:
        return (self.meta or {}).get("type")


def rel(path: Path) -> str:
    return path.relative_to(ROOT).as_posix()


def scalar(value: str) -> str:
    value = value.strip()
    if len(value) >= 2 and value[0] == value[-1] and value[0] in "\"'":
        return value[1:-1]
    return value


def parse_frontmatter(text: str) -> tuple[dict | None, str, int]:
    """Parse the YAML subset the wiki uses: scalars, inline lists and block lists."""
    match = FRONTMATTER.match(text)
    if not match:
        return None, text, 1
    data: dict = {}
    key = None
    for line in match.group(1).splitlines():
        stripped = line.strip()
        if not stripped or stripped.startswith("#"):
            continue
        if stripped.startswith("- ") and key is not None:
            if not isinstance(data[key], list):
                data[key] = []
            data[key].append(scalar(stripped[2:]))
            continue
        k, sep, v = line.partition(":")
        if not sep or line[0].isspace():
            raise ValueError(f"cannot parse frontmatter line {line!r}")
        key = k.strip()
        v = v.strip()
        if v.startswith("[") and v.endswith("]"):
            data[key] = [scalar(x) for x in v[1:-1].split(",") if x.strip()]
        else:
            data[key] = scalar(v)
    body = text[match.end():]
    return data, body, text[: match.end()].count("\n") + 1


def extract_links(body: str, first_line: int) -> list[tuple[str, int, bool]]:
    links = []
    in_fence = False
    for offset, line in enumerate(body.splitlines()):
        if line.lstrip().startswith(("```", "~~~")):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for embed, target in WIKILINK.findall(INLINE_CODE.sub("", line)):
            links.append((target.strip(), first_line + offset, embed == "!"))
    return links


def parse_date(value) -> dt.date | None:
    try:
        return dt.date.fromisoformat(str(value))
    except ValueError:
        return None


def lint(today: dt.date) -> list[Issue]:
    issues: list[Issue] = []

    def add(severity, code, path, message, line=None):
        issues.append(Issue(severity, code, rel(path), message, line))

    pages: dict[str, Page] = {}
    for path in sorted(WIKI.rglob("*.md")):
        if path.name.startswith("."):
            continue
        name = path.stem
        if name in pages:
            add("error", "duplicate-name", path,
                f"name also used by {rel(pages[name].path)}, so [[{name}]] is ambiguous")
            continue
        text = path.read_text(encoding="utf-8")
        try:
            meta, body, first_line = parse_frontmatter(text)
        except ValueError as exc:
            add("error", "frontmatter-invalid", path, str(exc))
            meta, body, first_line = None, text, 1
        pages[name] = Page(path, name, meta, extract_links(body, first_line))

    for name in ("index", "log"):
        if name not in pages:
            issues.append(Issue("error", "missing-file", f"wiki/{name}.md", "required file is missing"))

    source_refs: set[str] = set()
    for page in pages.values():
        if page.name in SPECIAL:
            continue
        meta = page.meta
        if meta is None:
            add("error", "frontmatter-missing", page.path, "page has no YAML frontmatter")
            continue
        for key in REQUIRED:
            if not meta.get(key):
                add("error", "missing-field", page.path, f"frontmatter field '{key}' is missing or empty")
        ptype = meta.get("type")
        if ptype and ptype not in TYPE_DIRS:
            add("error", "bad-type", page.path,
                f"type '{ptype}' is not one of: {', '.join(sorted(TYPE_DIRS))}")
        elif ptype and page.path.parent != TYPE_DIRS[ptype]:
            add("error", "wrong-dir", page.path, f"type '{ptype}' pages go in {rel(TYPE_DIRS[ptype])}/")

        created, updated = parse_date(meta.get("created")), parse_date(meta.get("updated"))
        for key, value in (("created", created), ("updated", updated)):
            if meta.get(key) and value is None:
                add("error", "bad-date", page.path, f"'{key}' is not a YYYY-MM-DD date")
        if created and updated:
            if updated < created:
                add("error", "bad-date", page.path, "'updated' is before 'created'")
            if updated > today:
                add("error", "bad-date", page.path, "'updated' is in the future")
            elif (today - updated).days > STALE_DAYS and ptype != "source":
                add("warning", "stale", page.path,
                    f"not updated for {(today - updated).days} days; check claims against newer sources")

        if ptype == "source":
            src = meta.get("source")
            if not src:
                add("error", "missing-field", page.path, "source pages need a 'source' field (path under raw/)")
            elif not str(src).startswith("raw/") or not (ROOT / src).is_file():
                add("error", "missing-source", page.path, f"source file '{src}' does not exist under raw/")
            else:
                source_refs.add(str(src))

    files = {p.name for base in (RAW, WIKI) for p in base.rglob("*") if p.is_file()}
    inbound: dict[str, set[str]] = defaultdict(set)
    index_targets: set[str] = set()
    cites_source: set[str] = set()
    for page in pages.values():
        for target, line, embed in page.links:
            target = target.split("/")[-1]
            if target.endswith(".md"):
                target = target[:-3]
            if embed or Path(target).suffix.lower() in ASSET_EXTS:
                if target not in files and target not in pages:
                    add("error", "broken-link", page.path, f"embedded file '{target}' does not exist", line)
                continue
            if target not in pages:
                add("error", "broken-link", page.path,
                    f"[[{target}]] has no page; create it or remove the link", line)
                continue
            if page.name == "index":
                index_targets.add(target)
            elif page.name != "log" and target != page.name:
                inbound[target].add(page.name)
            if pages[target].type == "source":
                cites_source.add(page.name)

    for page in pages.values():
        if page.name in SPECIAL or page.meta is None:
            continue
        if "index" in pages and page.name not in index_targets:
            add("error", "not-in-index", page.path, f"add [[{page.name}]] to wiki/index.md")
        if page.type != "overview" and not inbound[page.name]:
            add("warning", "orphan", page.path, "no other page links here (index and log do not count)")
        if page.type in CITING_TYPES and page.name not in cites_source:
            add("warning", "uncited", page.path, "page does not link to any source page")

    for path in sorted(RAW.rglob("*")):
        if not path.is_file() or path.name.startswith(".") or (RAW / "assets") in path.parents:
            continue
        if rel(path) not in source_refs:
            add("warning", "uningested", path, "no source page refers to this file; run the kb-ingest skill")

    if "log" in pages:
        log = pages["log"].path
        previous = None
        for number, line in enumerate(log.read_text(encoding="utf-8").splitlines(), 1):
            if not line.startswith("## "):
                continue
            match = LOG_HEADING.match(line)
            if not match:
                add("error", "log-format", log, "heading must be '## [YYYY-MM-DD] <op> | <title>'", number)
                continue
            date, op = parse_date(match.group(1)), match.group(2)
            if op not in LOG_OPS:
                add("error", "log-format", log, f"op '{op}' is not one of: {', '.join(sorted(LOG_OPS))}", number)
            if date is None:
                add("error", "log-format", log, "date is not valid", number)
            elif previous and date < previous:
                add("error", "log-order", log, "entry is older than the entry above it; log is append-only", number)
            else:
                previous = date

    issues.sort(key=lambda i: (i.severity != "error", i.path, i.line or 0, i.code))
    return issues


def render(issues: list[Issue], fmt: str) -> str:
    errors = sum(i.severity == "error" for i in issues)
    warnings = len(issues) - errors
    if fmt == "json":
        return json.dumps({"errors": errors, "warnings": warnings,
                           "issues": [asdict(i) for i in issues]}, indent=2)
    if fmt == "markdown":
        lines = ["## Wiki lint", "", f"**{errors} errors, {warnings} warnings**", ""]
        if issues:
            lines += ["| Severity | Code | Location | Message |", "| --- | --- | --- | --- |"]
            for i in issues:
                loc = f"{i.path}:{i.line}" if i.line else i.path
                message = i.message.replace("|", r"\|")
                lines.append(f"| {i.severity} | `{i.code}` | `{loc}` | {message} |")
        return "\n".join(lines)
    out = []
    for i in issues:
        loc = f"{i.path}:{i.line}" if i.line else i.path
        out.append(f"{loc}: {i.severity} [{i.code}] {i.message}")
    out.append(f"{errors} errors, {warnings} warnings")
    return "\n".join(out)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--format", choices=("text", "markdown", "json"), default="text")
    parser.add_argument("--strict", action="store_true", help="fail on warnings too")
    parser.add_argument("--today", type=dt.date.fromisoformat, default=dt.date.today(),
                        help="override today's date (YYYY-MM-DD)")
    args = parser.parse_args()
    issues = lint(args.today)
    print(render(issues, args.format))
    failing = {"error", "warning"} if args.strict else {"error"}
    return 1 if any(i.severity in failing for i in issues) else 0


if __name__ == "__main__":
    sys.exit(main())
