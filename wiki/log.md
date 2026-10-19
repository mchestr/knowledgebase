# Log

Append-only record of wiki operations. Add new entries at the bottom.
Heading format: `## [YYYY-MM-DD] <op> | <title>`. Ops: `ingest`, `query`, `lint`, `update`.
Find recent entries with `grep '^## \[' wiki/log.md | tail -5`.

## [2026-10-18] update | Initialize knowledge base

- Created the repository structure, schema, skills and lint workflows.

## [2026-10-18] ingest | home-cluster docs and README

- Source: https://github.com/mchestr/home-cluster/tree/2ce9069c102d7eda4c430078c05a2c400befe730/docs and README.md. 12 raw files, plus `raw/assets/thunderbolt.png`.
- Created sources: home-cluster-readme, -workstation-setup, -bootstrap, -networking, -observability, -storage-operations, -node-management, -application-deployment, -secrets-management, -upgrade-procedures, -troubleshooting, -disaster-recovery.
- Created entities: home-cluster, ms-01, home-nas, udm-pro-max, talos-linux, flux, cilium, rook-ceph, envoy-gateway, authelia, cloudflare-tunnel, external-secrets, volsync, cloudnative-pg, tuppr, renovate, victorialogs, kube-prometheus-stack.
- Created concepts: gitops, internal-vs-external-gateway, split-horizon-dns, bgp-load-balancing, thunderbolt-ring-network, backup-strategy, app-deployment-pattern.
- Created syntheses: triage-runbook, node-failure-runbook, complete-cluster-loss-runbook.
- Updated: index, overview.
- Contradictions: NAS model (home-nas), Renovate automerge condition (renovate). Unverified: current Talos version (talos-linux).
