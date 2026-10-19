---
title: Renovate
type: entity
kind: software
aliases: [renovatebot]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, upgrades, ci]
---

# Renovate

## Summary

Keeps the chart, image, Talos and Kubernetes versions in the [[home-cluster]] repository current. It merges low-risk updates by itself ([[home-cluster-readme]]).

## Facts

- Automerge: minor, patch and digest updates. PR for review: majors, `0.x` minors, core infrastructure (CNI, storage, Flux, Talos/Kubernetes, app-template, cert-manager, external-secrets) and apps with database migrations ([[home-cluster-upgrade-procedures]]).
- Rules: `.github/renovate/autoMerge.json5` ([[home-cluster-upgrade-procedures]]).
- CI builds each Renovate branch with flux-local and risk-assesses the rendered diff before automerge ([[home-cluster-readme]]).
- Renovate bumps the [[tuppr]] target versions and the Talos `extraManifests` URLs ([[home-cluster-upgrade-procedures]]).

> [!warning] Contradiction
> [[home-cluster-application-deployment]] says Renovate automerges "once the risk assessment passes".
> [[home-cluster-upgrade-procedures]] says it automerges "once they're 2 days old".
> Both conditions can apply. Neither page states both. Check `.github/renovate/autoMerge.json5`.

## Commands

| Task | Command |
| --- | --- |
| List PRs | `task github:pr:list` |
| Merge one | `task github:pr:merge ID=<id>` |
| Merge all | `task github:pr:merge:all` |

## Related

- [[flux]], [[gitops]].
