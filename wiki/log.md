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

## [2026-10-18] ingest | home-cluster docs at eff692f

- Source: home-cluster commit eff692f, "docs: align Renovate automerge rules and Talos version with the repo". Only `application-deployment.md` and `upgrade-procedures.md` changed.
- New raw files: `raw/2026-10-18-home-cluster-application-deployment-eff692f.md`, `raw/2026-10-18-home-cluster-upgrade-procedures-eff692f.md`.
- Updated sources: home-cluster-application-deployment, home-cluster-upgrade-procedures (`source` now points to the new raw files; old files in `previous_sources`).
- Updated: renovate (contradiction settled), talos-linux (version confirmed: Talos 1.14, Kubernetes 1.37), tuppr, overview, index.
- Still open: NAS model (home-nas).
- Schema: added the `previous_sources` rule to CLAUDE.md, the lint and the kb-ingest skill.

