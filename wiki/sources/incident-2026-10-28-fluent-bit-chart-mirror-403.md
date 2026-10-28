---
title: Incident 2026-10-28 — Fluent Bit chart mirror denies pulls
type: source
source: raw/2026-10-28-incident-fluent-bit-chart-mirror-403.md
author: Mike Chester
published: 2026-10-28
url:
created: 2026-10-28
updated: 2026-10-28
tags: [home-cluster, incident, flux, ci, observability]
---

# Incident 2026-10-28 — Fluent Bit chart mirror denies pulls

## Summary

The Fluent Bit chart in home-operations/charts-mirror stopped allowing anonymous pulls. The Fluent Bit `OCIRepository` in the [[home-cluster]] went `Ready=False`, and every CI run failed to render the chart. The fix was to point the `OCIRepository` at the upstream OCI chart, with the same tag. See [[oci-chart-pull-denied]].

## Key points

- charts-mirror stopped copying fluent-bit on 2026-01-22 (commit e8f3b5cf, "feat: deprecate fluent-bit"). The ghcr.io package later began to return `403 denied`. The date of that change is unknown.
- [[flux]] source-controller, flux-local and flate all failed with `403: denied: requested access to the resource is denied` for `ghcr.io/home-operations/charts-mirror/fluent-bit`.
- The fluent project publishes the same chart at `oci://ghcr.io/fluent/helm-charts/fluent-bit`, including tag 0.55.0.
- home-cluster PR #6314 changed only the `url`. After the merge, the source was `Ready=True` and the Fluent Bit release upgraded to v17 with the same chart version.
- fluent-bit was the only chart in the repository that used charts-mirror.

## Data and quotes

- source-controller: "failed to determine artifact digest: GET https://ghcr.io/token?scope=repository%3Ahome-operations%2Fcharts-mirror%2Ffluent-bit%3Apull&service=ghcr.io: DENIED: requested access to the resource is denied"
- Anonymous token request: HTTP 403 for `charts-mirror/fluent-bit`, HTTP 200 for another chart in the mirror.
- New source revision: `0.55.0@sha256:4da7b482491d64387c63000ada116abe2a0974c2d7dc7705931420b90b3ead09`.
- The fix PR's "Flux Local Test" passed. "Flux Diff (helmrelease)" and "Image Pull - Extract Images (default)" failed until the merge, because they also render the default branch.

## Connections

- Fluent Bit sends the cluster's logs to [[victorialogs]].
- The CI render failure also blocked [[renovate]] automerge and the [[renovate-risk-review]] for each update branch.
- The failure was found while testing the flate migration (home-cluster PR #6313).

## Open questions

- Did a Flux alert fire while the `OCIRepository` was `Ready=False`?
- When did the charts-mirror package stop allowing anonymous pulls?
