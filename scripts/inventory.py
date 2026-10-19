#!/usr/bin/env python3
"""Print the home-cluster app inventory for a checkout, as the body of a raw source file.

Usage: inventory.py <checkout-dir> <commit-sha> [<date>]
Needs yq (mikefarah, v4) on PATH.
"""

from __future__ import annotations

import datetime as dt
import json
import subprocess
import sys
from pathlib import Path

HEADER = """# home-cluster app inventory at {short}

Generated on {date} from the Flux Kustomizations (`kubernetes/apps/*/*/ks.yaml`) and the YAML under each Kustomization `path`, with yq.
Gateway: `parentRefs` that name an `envoy-*` gateway. Main image: first two images in HelmRelease values.
NetworkPolicy: "gateway-only ingress" if the app path selects `gateway.envoyproxy.io/owning-gateway-name`; "kube-apiserver entity" if it admits the `kube-apiserver` Cilium entity; "other policy" for any other NetworkPolicy. Policies added through `components` (for example dragonfly) are not counted.
"""


def docs(path: Path) -> list[dict]:
    out = subprocess.run(["yq", "ea", "-o=json", "-I=0", "[explode(.)]", str(path)],
                         capture_output=True, text=True)
    if out.returncode:
        return []
    return [d for d in json.loads(out.stdout) if isinstance(d, dict)]


def walk(obj, key):
    if isinstance(obj, dict):
        for k, v in obj.items():
            if k == key:
                yield v
            yield from walk(v, key)
    elif isinstance(obj, list):
        for v in obj:
            yield from walk(v, key)


def table(root: Path) -> str:
    rows = []
    for ks in sorted(root.glob("kubernetes/apps/*/*/ks.yaml")):
        for k in docs(ks):
            if k.get("kind") != "Kustomization":
                continue
            meta, spec = k.get("metadata", {}), k.get("spec", {})
            ns = spec.get("targetNamespace") or meta.get("namespace")
            comps = [Path(c).name for c in spec.get("components", [])]
            deps = [d.get("name") for d in spec.get("dependsOn", [])]
            appdir = root / spec.get("path", "").lstrip("./")
            files = sorted(appdir.rglob("*.yaml")) if appdir.is_dir() else []
            all_docs = [d for f in files for d in docs(f)]
            oci = {d["metadata"]["name"]: d["spec"].get("url", "") for d in all_docs
                   if d.get("kind") == "OCIRepository" and "metadata" in d and "spec" in d}
            charts, images, gateways = [], [], set()
            for d in all_docs:
                if d.get("kind") == "HelmRelease":
                    s = d.get("spec", {})
                    ref = s.get("chartRef") or {}
                    if ref:
                        charts.append(oci.get(ref.get("name"), ref.get("name", "")).split("/")[-1] or ref.get("name"))
                    elif s.get("chart"):
                        charts.append(s["chart"].get("spec", {}).get("chart", ""))
                    for img in walk(s.get("values", {}), "image"):
                        if isinstance(img, dict) and img.get("repository"):
                            images.append(f'{img["repository"]}:{img.get("tag", "")}'.rstrip(":"))
                for refs in walk(d, "parentRefs"):
                    for r in refs if isinstance(refs, list) else []:
                        if isinstance(r, dict) and str(r.get("name", "")).startswith("envoy-"):
                            gateways.add(r["name"])
            text = " ".join(f.read_text(errors="ignore") for f in files)
            # app-template renders policies from `networkpolicies:` values, which have no `kind:` line.
            parts = []
            if "owning-gateway-name" in text:
                parts.append("gateway-only ingress")
            if "kube-apiserver" in text:
                parts.append("kube-apiserver entity")
            if not parts and ("networkpolicies:" in text or "NetworkPolicy" in text):
                parts.append("other policy")
            rows.append((ns, meta.get("name"), ", ".join(dict.fromkeys(charts)),
                         ", ".join(dict.fromkeys(images[:2])), ", ".join(sorted(gateways)),
                         ", ".join(comps), ", ".join(deps), " + ".join(parts)))

    lines = ["| Namespace | App | Chart | Main image | Gateway | Components | dependsOn | NetworkPolicy |",
             "| --- | --- | --- | --- | --- | --- | --- | --- |"]
    for r in sorted(rows, key=lambda r: (r[0] or "", r[1] or "")):
        lines.append("| " + " | ".join(x or "" for x in r) + " |")
    lines.append(f"\nTotal Kustomizations: {len(rows)}")
    return "\n".join(lines)


def main() -> int:
    root, sha = Path(sys.argv[1]), sys.argv[2]
    date = sys.argv[3] if len(sys.argv) > 3 else dt.date.today().isoformat()
    print(HEADER.format(short=sha[:7], date=date))
    print(table(root))
    return 0


if __name__ == "__main__":
    sys.exit(main())
