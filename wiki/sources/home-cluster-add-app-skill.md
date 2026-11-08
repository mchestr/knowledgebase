---
title: home-cluster add-app skill
type: source
source: raw/2026-11-08-home-cluster-add-app-skill-924c31d.md
previous_sources:
  - raw/2026-10-18-home-cluster-add-app-skill.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/924c31d581b9010658ac58e4022448e7d6bf5ba9/.claude/skills/add-app/SKILL.md
commit: 924c31d
created: 2026-10-18
updated: 2026-11-08
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
- Commit `feat(<app>): add <app>`, push a branch, open a PR with a short body (what the app is, how it is exposed, what it stores), and fix failed checks. CI runs Flate Test and Flux Diff.
- The risk assessment runs only on PRs that are not drafts ([[renovate-risk-review]]).

## Data and quotes

Version `924c31d` replaced `flux-local` with `flate` and replaced the `.github/PULL_REQUEST_TEMPLATE.md` headings with a short free-form PR body. Version `e36a8c8` used `flux-local test --enable-helm --all-namespaces --path kubernetes/flux/cluster --sources flux-system` and "Flux Local".

## Connections

- [[app-deployment-pattern]], [[flux]], [[renovate-risk-review]].

## Open questions

- None.
