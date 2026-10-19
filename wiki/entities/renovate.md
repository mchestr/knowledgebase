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

- Automerge: minor, patch and digest updates, after the flux-local risk assessment passes ([[home-cluster-application-deployment]]).
- Minimum age: 2 days for Docker Hub, GitHub, Helm repositories and npm. 3 days for GitHub Actions. No minimum age for images and OCI charts on other registries, because they have no release dates ([[home-cluster-upgrade-procedures]]).
- PR for review: majors, `0.x` minors, core infrastructure (CNI, storage, Flux, Talos/Kubernetes, app-template, cert-manager, external-secrets) and apps with database migrations ([[home-cluster-upgrade-procedures]]).
- Rules: `.github/renovate/autoMerge.json5` ([[home-cluster-upgrade-procedures]]).
- Exception: Renovate's own majors (`renovatebot/renovate`) also automerge ([[home-cluster-agents-md]]).
- Renovate runs in the cluster: `renovate-operator` in the `renovate` namespace starts a job each hour for each repository in `discoveryFilters` of `renovatejob.yaml`, as the `mchesterbot` GitHub App. The UI is `renovate.chestr.dev` ([[home-cluster-agents-md]]).
- Commit scopes: `feat|fix|chore(container)`, `feat|fix(helm)`, `feat|fix(github-release)`. Majors add `!` ([[home-cluster-agents-md]]).
- The AI [[renovate-risk-review]] rates each PR before automerge.
- A red flux-local check on any PR holds back every automerge ([[home-cluster-waitlist-readme]]).
- CI builds each Renovate branch with flux-local and risk-assesses the rendered diff before automerge ([[home-cluster-readme]]).
- Renovate bumps the [[tuppr]] target versions and the Talos `extraManifests` URLs ([[home-cluster-upgrade-procedures]]).

Both conditions apply. Version `eff692f` of the docs settled an earlier conflict between the two pages.

## Commands

| Task | Command |
| --- | --- |
| List PRs | `task github:pr:list` |
| Merge one | `task github:pr:merge ID=<id>` |
| Merge all | `task github:pr:merge:all` |

## Related

- [[flux]], [[gitops]].
