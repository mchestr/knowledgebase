---
title: home-cluster add-app skill
type: source
source: raw/2026-10-18-home-cluster-add-app-skill.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/.claude/skills/add-app/SKILL.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
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
- Then `kustomize build kubernetes/apps/<namespace>` and, if installed, `flux-local test --enable-helm --all-namespaces --path kubernetes/flux/cluster --sources flux-system`.
- Commit `feat(<app>): add <app>`, push a branch, open a PR with `.github/PULL_REQUEST_TEMPLATE.md` headings, and fix failed checks.
- The risk assessment runs only on PRs that are not drafts ([[renovate-risk-review]]).

## Data and quotes

None.

## Connections

- [[app-deployment-pattern]], [[flux]], [[renovate-risk-review]].

## Open questions

- None.
