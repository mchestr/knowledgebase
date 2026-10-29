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

## [2026-10-18] ingest | home-cluster docs at e36a8c8

- Source: home-cluster commit e36a8c8, "docs: replace the Synology DS920+ with the UNAS Pro 8 in the README". Only `README.md` and `networking.md` changed.
- New raw files: `raw/2026-10-18-home-cluster-readme-e36a8c8.md`, `raw/2026-10-18-home-cluster-networking-e36a8c8.md`.
- Updated sources: home-cluster-readme, home-cluster-networking (`source` now points to the new raw files; old files in `previous_sources`).
- Updated: home-nas (contradiction settled; UNAS Pro 8 at 10.0.40.13), home-cluster (removed the unsourced "media" claim), overview, index.

## [2026-10-18] ingest | home-cluster repository prose and app inventory at e36a8c8

- Source: 14 markdown files outside `docs/` (AGENTS.md, Claude agent and skills, renovate-risk prompt, component READMEs) and a generated app inventory of 98 Flux Kustomizations. Skipped: issue and PR templates, the 11-byte CLAUDE.md, all YAML.
- Created sources: home-cluster-agents-md, -ops-agent, -add-app-skill, -renovate-review-skill, -renovate-risk-prompt, -volsync-restore-skill, -claude-code-readme, -claude-code-agent-instructions, -authelia-readme, -cilium-config-readme, -rook-ceph-readme, -waitlist-readme, -cnpg-component-readme, -terraform-readme, -app-inventory.
- Created entities: claude-code-remote-control, litellm, memini, lldap, waitlist, gatus, cloudflare-terraform.
- Created concepts: in-cluster-ai-stack, renovate-risk-review.
- Created syntheses: security-posture, app-inventory.
- Updated: home-cluster, authelia, cilium, udm-pro-max, rook-ceph, cloudnative-pg, home-nas, volsync, renovate, flux, talos-linux, cloudflare-tunnel, kube-prometheus-stack, internal-vs-external-gateway, bgp-load-balancing, app-deployment-pattern, gitops, overview, index.
- Contradiction: NetworkPolicy reference app (docs say home-assistant, AGENTS.md and code say radicale).
- Lint: wikilink targets now drop the trailing backslash of `[[page\|alias]]` in tables.

## [2026-10-18] ingest | home-cluster at fa79b82

- Source: home-cluster commits 470f9f8 "chore(waitlist): remove the README" and fa79b82 "docs(networking): name radicale as the NetworkPolicy reference".
- New raw files: `raw/2026-10-18-home-cluster-{networking,application-deployment,authelia-readme}-fa79b82.md`.
- Updated sources: home-cluster-networking, home-cluster-application-deployment, home-cluster-authelia-readme (new versions), home-cluster-waitlist-readme (removed upstream), home-cluster-agents-md.
- Updated: internal-vs-external-gateway and security-posture (contradiction settled: radicale is the reference), waitlist, overview, index.
- Schema: added the `removed_upstream` rule to CLAUDE.md and the kb-ingest skill.

## [2026-10-22] ingest | Incident: a Plex user cannot sign in to Seerr

- Schema: added the `issue` and `sop` page types, `wiki/issues/`, `wiki/sops/`, their templates, the "Issues and SOPs" rules and the personal-information rule to CLAUDE.md, the lint and the kb-ingest and kb-query skills.
- New raw file: `raw/2026-10-22-incident-seerr-plex-signin.md`.
- Created source: incident-2026-10-22-seerr-plex-signin.
- Created entities: seerr, plex-manager.
- Created issue: seerr-plex-user-cannot-sign-in.
- Created SOP: look-up-a-plex-user.
- Updated: index.

## [2026-10-28] ingest | Incident: the Fluent Bit chart mirror denies pulls

- New raw file: `raw/2026-10-28-incident-fluent-bit-chart-mirror-403.md`.
- Created source: incident-2026-10-28-fluent-bit-chart-mirror-403.
- Created issue: oci-chart-pull-denied.
- Updated: victorialogs, flux, index.

## [2026-10-28] ingest | home-cluster at 2d78212

- Source: home-cluster `fa79b82..2d78212`, including PR #6313 (CI moves from flux-local to flate) and the windmill removal.
- New raw files: `raw/2026-10-28-home-cluster-{add-app-skill,renovate-review-skill,renovate-risk-prompt,agents-md,readme,application-deployment,upgrade-procedures,claude-code-readme,claude-code-agent-instructions,app-inventory}-2d78212.md`.
- Updated sources (new versions): home-cluster-add-app-skill, -renovate-review-skill, -renovate-risk-prompt, -agents-md, -readme, -application-deployment, -upgrade-procedures, -claude-code-readme, -claude-code-agent-instructions, -app-inventory.
- Updated: flux, renovate, renovate-risk-review, app-deployment-pattern, gitops, claude-code-remote-control, cloudflare-terraform, home-cluster, authelia, lldap, security-posture, app-inventory, overview, index.
- Fixed: the app inventory source page said 18 Kustomizations in `media` at `e36a8c8`; the raw table has 19.
