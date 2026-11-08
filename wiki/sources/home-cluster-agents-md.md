---
title: home-cluster AGENTS.md
type: source
source: raw/2026-11-08-home-cluster-agents-md-924c31d.md
previous_sources:
  - raw/2026-10-18-home-cluster-agents-md.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/924c31d581b9010658ac58e4022448e7d6bf5ba9/AGENTS.md
commit: 924c31d
created: 2026-10-18
updated: 2026-11-08
tags: [home-cluster, agents, conventions]
---

# home-cluster AGENTS.md

## Summary

Guidance for AI coding agents in the [[home-cluster]] repository. `CLAUDE.md` imports it. It is the most complete single summary of the repository conventions.

## Key points

- Task commands for Flux, [[volsync]], [[talos-linux]], Terraform ([[cloudflare-terraform]]), GitHub PRs and bootstrap.
- `kubernetes/components/common/` holds the namespace, shared repositories, `cluster-secrets` and alert configs.
- HelmReleases use `oci://ghcr.io/bjw-s-labs/helm/app-template` through the `OCIRepository` in `components/common/repos/app-template/`.
- The patch in `kubernetes/flux/cluster/ks.yaml` rolls back failed upgrades and replaces chart CRDs on every upgrade. Do not add per-app remediation blocks. The Helm timeout is 5 minutes ([[flux]]).
- Gateway rules match [[internal-vs-external-gateway]]. The reference implementations of the external-gateway policy are `default/radicale` and `waitlist`. "Not every app has one yet."
- [[authelia]] default: two-factor for `admin`, deny for everyone else, `bypass` for apps with their own login.
- `cluster-secrets` variables reach child Kustomizations through `postBuild.substituteFrom`.
- [[volsync]] keeps 7 daily, 4 weekly and 3 monthly snapshots. Set `APP_UID`/`APP_GID` when the container user is not 1000. Extra variables: `VOLSYNC_CACHE_STORAGECLASS`, `VOLSYNC_SNAPSHOTCLASS`.
- The `dragonfly` component adds a network policy and a pod monitor. Use `DRAGONFLY_REPLICAS: 3` for anything that must survive a node reboot.
- Storage classes: `ceph-block` (RWO, default) and `openebs-hostpath` (VolSync caches, CNPG, ARC runner work volumes).
- Talos configs are Jinja2 templates, rendered with `minijinja-cli` and filled with `op inject`. `talosctl apply-config --dry-run` shows a change first.
- [[in-cluster-ai-stack]]: [[litellm]] (OpenRouter, no local GPU), text-embeddings (TEI, `bge-small-en-v1.5`), [[memini]] at `memini.chestr.dev`.
- [[gatus]] status page at `status.chestr.dev`, fed by `gatus-sidecar` from every HTTPRoute. Opt out with `gatus.home-operations.com/enabled: "false"`.
- Commit scopes: `feat|fix(container)` (`feat` for minor, `fix` for patch and digest), `feat|fix(helm)`, `chore(github-release)`, `ci(github-action)`, `feat|fix(<app>)`, `chore:`. Majors and `0.x` minor bumps use `!`. The types and scopes come from the `home-operations/renovate-presets` preset.
- [[renovate]] runs in the cluster through `renovate-operator`, each hour, as the `mchesterbot` GitHub App. Renovate's own majors also automerge. The rules are in `.renovaterc.json5`.
- CI: `.github/workflows/ci.yaml` runs every PR check and reports one `CI Success` status. It runs Flate Test (flate builds every Kustomization and renders every HelmRelease), the risk assessment, Flux Diff (a PR comment with changed `HelmRelease` and `Kustomization` resources), image pre-pulls, actionlint and zizmor. The `Changed Files` job also validates `.renovaterc.json5`. Each job runs only when its files change.
- Knowledge base: common issues, SOPs and incident history live in the `mchestr/knowledgebase` wiki. Agents read `wiki/index.md` and the matching `wiki/issues/` and `wiki/sops/` pages before they troubleshoot, follow an SOP when one exists, and offer to record a new problem with the `kb-ingest` skill. Do not write personal information there, because the repository is public.

## Data and quotes

> "Images and OCI charts outside Docker Hub get no minimum age and merge once the risk assessment passes."

Version `924c31d` added the "Knowledge Base" section, replaced `flux-local` and `flux-diff` with `ci.yaml`, changed the commit-type table, and moved the Renovate rules from `.github/renovate/autoMerge.json5` to `.renovaterc.json5`. Version `e36a8c8` listed `chore(container)` and `feat|fix(github-release)`.

## Connections

- [[home-cluster]], [[app-deployment-pattern]], [[security-posture]], [[renovate-risk-review]].

## Open questions

- None. The Renovate rules file moved to `.renovaterc.json5`; [[home-cluster-upgrade-procedures]] now agrees. Docs version `fa79b82` now also names `radicale`.
