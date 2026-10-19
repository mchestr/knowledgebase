#!/usr/bin/env python3
"""Track upstream sources and save new versions to raw/ for kb-ingest.

Commands:
  check             Print the tracked changes since the last ingest. Exit 0.
  fetch --plan F    Save changed and added files to raw/, run generators,
                    update sources.json, and write the ingest plan to F.
  verify --plan F   Fail if the working tree changes anything outside wiki/
                    and the files that fetch wrote.

Uses only the standard library. Set GH_TOKEN for private repositories and a
higher GitHub API rate limit.
"""

from __future__ import annotations

import argparse
import datetime as dt
import fnmatch
import hashlib
import json
import os
import re
import subprocess
import sys
import tarfile
import tempfile
import urllib.parse
import urllib.request
from pathlib import Path, PurePosixPath

ROOT = Path(__file__).resolve().parent.parent
CONFIG = ROOT / "sources.json"
SOURCES = ROOT / "wiki" / "sources"
API = "https://api.github.com"
COMPARE_FILE_LIMIT = 300


def request(url: str, accept: str = "application/vnd.github+json") -> tuple[bytes, str]:
    headers = {"Accept": accept, "User-Agent": "knowledgebase-sources"}
    token = os.environ.get("GH_TOKEN") or os.environ.get("GITHUB_TOKEN")
    if token and url.startswith(API):
        headers["Authorization"] = f"Bearer {token}"
    with urllib.request.urlopen(urllib.request.Request(url, headers=headers), timeout=120) as resp:
        return resp.read(), resp.headers.get("Content-Type", "")


def gh_json(path: str):
    return json.loads(request(API + path)[0])


def gh_file(repo: str, sha: str, path: str) -> str:
    quoted = urllib.parse.quote(path)
    return request(f"{API}/repos/{repo}/contents/{quoted}?ref={sha}", "application/vnd.github.raw")[0].decode()


def matches(path: str, patterns: list[str]) -> bool:
    return any(fnmatch.fnmatchcase(path, p) for p in patterns)


def slugify(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def source_pages() -> dict[str, dict]:
    """Map each source page's upstream key (repo:path or URL) to the page."""
    pages = {}
    for page in sorted(SOURCES.glob("*.md")):
        meta = dict(re.findall(r"^(url|source|removed_upstream): *(.*)$", page.read_text(), re.M))
        url = meta.get("url", "").strip()
        info = {"page": page.stem, "raw": meta.get("source", "").strip(), "removed": bool(meta.get("removed_upstream"))}
        m = re.match(r"https://github\.com/([^/]+/[^/]+)/blob/[0-9a-f]{7,40}/(.+)$", url)
        pages[f"{m[1]}:{m[2]}" if m else url] = info
    return pages


def raw_name(prefix: str, path: str, current_raw: str, version: str, today: str, ext: str = ".md") -> str:
    if current_raw:
        base = re.sub(r"^raw/\d{4}-\d{2}-\d{2}-", "", current_raw)
        base = re.sub(r"(-[0-9a-f]{7})?\.[a-z]+$", "", base)
    else:
        p = PurePosixPath(path)
        stem = p.stem.lower()
        name = f"{p.parent.name}-{stem}" if stem in {"readme", "skill", "claude", "agents"} and p.parent.name else stem
        base = f"{prefix}-{slugify(name)}" if prefix else slugify(name)
    return f"raw/{today}-{base}-{version}{ext}"


def github_changes(entry: dict, pages: dict) -> dict:
    repo, base = entry["repo"], entry["ingested"]
    head = gh_json(f"/repos/{repo}/commits/{entry.get('branch', 'main')}")["sha"]
    result = {"repo": repo, "base": base, "head": head, "files": [], "generators": [], "truncated": False}
    if head == base:
        return result
    cmp = gh_json(f"/repos/{repo}/compare/{base}...{head}")
    files = cmp.get("files", [])
    result["truncated"] = len(files) >= COMPARE_FILE_LIMIT
    changed = []
    for f in files:
        if f["status"] == "renamed":
            changed += [(f["previous_filename"], "removed"), (f["filename"], "added")]
        else:
            changed.append((f["filename"], f["status"]))
    for path, status in changed:
        page = pages.get(f"{repo}:{path}")
        tracked = page is not None or (matches(path, entry.get("paths", []))
                                       and not matches(path, entry.get("exclude", [])))
        if not tracked:
            continue
        if status == "removed":
            if page and not page["removed"]:
                result["files"].append({"kind": "removed", "path": path, "page": page["page"]})
            continue
        kind = "changed" if page else "added"
        result["files"].append({"kind": kind, "path": path, "page": page and page["page"],
                                "previous_raw": page and page["raw"]})
    for gen in entry.get("generators", []):
        if gen.get("generated") != head and any(matches(p, gen["trigger"]) for p, _ in changed):
            result["generators"].append(gen["name"])
    return result


def url_changes(entry: dict, pages: dict) -> dict:
    body, ctype = request(entry["url"], "*/*")
    digest = hashlib.sha256(body).hexdigest()
    page = pages.get(entry["url"])
    result = {"url": entry["url"], "sha256": digest, "files": [], "body": body}
    if digest != entry.get("sha256"):
        kind = "changed" if page else "added"
        result["files"].append({"kind": kind, "path": entry["url"], "page": page and page["page"],
                                "previous_raw": page and page["raw"], "content_type": ctype})
    return result


def collect(config: list[dict]) -> list[tuple[dict, dict]]:
    pages = source_pages()
    return [(e, github_changes(e, pages) if "repo" in e else url_changes(e, pages)) for e in config]


def cmd_check(args) -> int:
    found = False
    for entry, res in collect(json.loads(CONFIG.read_text())):
        label = res.get("repo") or res.get("url")
        items = res["files"] + [{"kind": "generate", "path": g} for g in res.get("generators", [])]
        if res.get("truncated"):
            print(f"{label}: WARNING: compare returned {COMPARE_FILE_LIMIT} files; some changes can be missing")
        if not items:
            print(f"{label}: no tracked changes")
            continue
        found = True
        span = f" {res['base'][:7]}..{res['head'][:7]}" if "head" in res else ""
        print(f"{label}{span}:")
        for item in items:
            print(f"  {item['kind']:8} {item['path']}" + (f"  -> {item['page']}" if item.get("page") else ""))
    if out := os.environ.get("GITHUB_OUTPUT"):
        with open(out, "a") as fh:
            fh.write(f"changed={'true' if found else 'false'}\n")
    return 0


def table_part(text: str) -> str:
    """Drop the header, whose date changes on every run."""
    return text[text.find("| Namespace"):].strip()


def run_generator(entry: dict, gen: dict, head: str, today: str, plan: list, written: list) -> None:
    if gen["name"] != "app-inventory":
        raise SystemExit(f"unknown generator {gen['name']}")
    pages = source_pages()
    page = next(v for v in pages.values() if v["page"] == gen["page"])
    with tempfile.TemporaryDirectory() as tmp:
        tarball = Path(tmp) / "repo.tgz"
        tarball.write_bytes(request(f"{API}/repos/{entry['repo']}/tarball/{head}")[0])
        checkout = Path(tmp) / "repo"
        checkout.mkdir()
        with tarfile.open(tarball) as tar:
            top = tar.getnames()[0].split("/")[0]
            tar.extractall(checkout, filter="data")
        body = subprocess.run([sys.executable, str(ROOT / "scripts" / "inventory.py"), str(checkout / top), head, today],
                              capture_output=True, text=True, check=True).stdout
    gen["generated"] = head
    if table_part((ROOT / page["raw"]).read_text()) == table_part(body):
        return
    name = raw_name("", "", page["raw"], head[:7], today)
    url = f"https://github.com/{entry['repo']}/tree/{head}/kubernetes/apps"
    (ROOT / name).write_text(f"{url}\n\n{body}")
    written.append(name)
    plan.append({"kind": "changed", "path": f"generated:{gen['name']}", "page": gen["page"],
                 "previous_raw": page["raw"], "raw": name, "version": head[:7]})


def cmd_fetch(args) -> int:
    config = json.loads(CONFIG.read_text())
    today = dt.date.today().isoformat()
    plan, written = [], ["sources.json"]
    for entry, res in collect(config):
        if res.get("truncated"):
            raise SystemExit(f"{entry['repo']}: the compare hit {COMPARE_FILE_LIMIT} files; ingest by hand, then set 'ingested'")
        if "repo" in entry:
            for item in res["files"]:
                if item["kind"] != "removed":
                    name = raw_name(entry.get("slug_prefix", ""), item["path"], item["previous_raw"], res["head"][:7], today)
                    url = f"https://github.com/{entry['repo']}/blob/{res['head']}/{item['path']}"
                    (ROOT / name).write_text(f"{url}\n\n{gh_file(entry['repo'], res['head'], item['path'])}")
                    item["raw"] = name
                    written.append(name)
                item.update(url=f"https://github.com/{entry['repo']}/blob/{res['head']}/{item['path']}",
                            version=res["head"][:7])
                plan.append(item)
            for gen in entry.get("generators", []):
                if gen["name"] in res["generators"]:
                    run_generator(entry, gen, res["head"], today, plan, written)
            entry["ingested"] = res["head"]
        else:
            for item in res["files"]:
                ext = ".html" if "html" in item.get("content_type", "") else ".md"
                current = item["previous_raw"] or f"raw/{today}-{entry['slug']}.md"
                name = raw_name("", "", current, res["sha256"][:7], today, ext)
                (ROOT / name).write_text(f"{entry['url']}\n\n{res['body'].decode(errors='replace')}")
                item.update(raw=name, url=entry["url"], version=res["sha256"][:7])
                written.append(name)
                plan.append(item)
            entry["sha256"] = res["sha256"]
    CONFIG.write_text(json.dumps(config, indent=2) + "\n")
    Path(args.plan).write_text(json.dumps({"date": today, "items": plan, "written": written}, indent=2) + "\n")
    if out := os.environ.get("GITHUB_OUTPUT"):
        with open(out, "a") as fh:
            fh.write(f"items={len(plan)}\n")
    print(f"{len(plan)} items in {args.plan}")
    for item in plan:
        print(f"  {item['kind']:8} {item['path']}" + (f"  -> {item['raw']}" if item.get("raw") else ""))
    return 0


def cmd_verify(args) -> int:
    allowed = set(json.loads(Path(args.plan).read_text())["written"]) | {args.plan, ".reingest-report.md"}
    status = subprocess.run(["git", "status", "--porcelain", "--untracked-files=all"],
                            cwd=ROOT, capture_output=True, text=True, check=True).stdout
    paths = [line[3:].split(" -> ")[-1].strip('"') for line in status.splitlines()]
    bad = [p for p in paths if not p.startswith("wiki/") and p not in allowed]
    for path in bad:
        print(f"not allowed: {path}")
    return 1 if bad else 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("check")
    for name in ("fetch", "verify"):
        sub.add_parser(name).add_argument("--plan", default=".reingest.json")
    args = parser.parse_args()
    return {"check": cmd_check, "fetch": cmd_fetch, "verify": cmd_verify}[args.cmd](args)


if __name__ == "__main__":
    sys.exit(main())
