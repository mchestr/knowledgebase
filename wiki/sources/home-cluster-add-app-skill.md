---
title: home-cluster add-app skill
type: source
source: raw/2026-10-28-home-cluster-add-app-skill-2d78212.md
previous_sources:
  - raw/2026-10-18-home-cluster-add-app-skill.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/.claude/skills/add-app/SKILL.md
commit: 2d78212
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, agents, runbook]
---

# home-cluster add-app skill

## Summary

A Claude Code skill that adds an app: it writes the Flux files, builds and validates them, and opens a PR. It is the agent version of [[app-deployment-pattern]].

## Key points

- Reference app: `kubernetes/apps/media/tautulli`.
- `ks.yaml` uses `path: ./app`. Always set `APP` in `postBuild.substitute`.
- Use `reloader.stakater.com/auto: "true"` when the app reads a Secret or ConfigMap without a name hash. Routes use `sectionName: https`.
- A new namespace copies `kustomization.yaml` from another namespace. There is no top-level `kubernetes/apps/kustomization.yaml`.
- Build like Flux: `flux build kustomization <app> --namespace <ns> --path ./kubernetes/apps/<ns>/<app>/app --kustomization-file ./kubernetes/apps/<ns>/<app>/ks.yaml --dry-run`. `cluster-secrets` variables stay as `${...}` in a dry run.
- Then `kustomize build kubernetes/apps/<namespace>` and, if installed, `flate test all --path kubernetes/flux/cluster`.
- Commit `feat(<app>): add <app>` and push a branch. Open a PR with a short body: what the app is, how it is exposed, and what it stores. Fix failed checks.
- The risk assessment runs only on PRs that are not drafts ([[renovate-risk-review]]).

## Data and quotes

Version `2d78212` replaced the flux-local test with `flate test all`, renamed the CI check to Flate Test, and dropped the PR template headings.

## Connections

- [[app-deployment-pattern]], [[flux]], [[renovate-risk-review]].

## Open questions

- None.
