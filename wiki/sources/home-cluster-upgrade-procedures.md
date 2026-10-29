---
title: home-cluster docs — Upgrade Procedures
type: source
source: raw/2026-10-28-home-cluster-upgrade-procedures-2d78212.md
previous_sources:
  - raw/2026-10-18-home-cluster-upgrade-procedures-eff692f.md
  - raw/2026-10-18-home-cluster-upgrade-procedures.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/docs/src/notes/upgrade-procedures.md
commit: 2d78212
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, upgrades, runbook]
---

# home-cluster docs — Upgrade Procedures

## Summary

How [[talos-linux]], Kubernetes, Flux and Helm charts are upgraded, and how to roll back. [[tuppr]] automates Talos and Kubernetes upgrades. [[renovate]] opens or merges the version bumps.

## Key points

- Before an upgrade: check `kubectl get nodes` and `kubectl rook-ceph ceph status`. Optionally take a snapshot: `task volsync:snapshot APP=<app> NS=<ns>`.
- Target versions: `kubernetes/apps/system-upgrade/tuppr/upgrades/talos.yaml` and `kubernetes.yaml`. Merging the Renovate PR starts the upgrade.
- tuppr upgrades one node at a time. Before each node it waits for Ceph `HEALTH_OK` and for no running VolSync backup. Talos upgrades power-cycle each node.
- The cluster runs Talos 1.14 and Kubernetes 1.37. The versions are in `tuppr/upgrades/talos.yaml` and `kubernetes.yaml`.
- Upgrade Talos before Kubernetes. Example: Talos 1.13 supports Kubernetes 1.31–1.36. Kubernetes 1.37 needs Talos 1.14.
- Apply pending changes to `talos/controlplane.yaml` (including `extraManifests` URL bumps) before an upgrade. `upgrade-k8s` fails on stale `extraManifests`.
- Reset a failed tuppr upgrade with the `tuppr.home-operations.com/reset` annotation.
- Manual fallback: `task talos:upgrade-node NODE=m0 VERSION=v1.14.3` (version from `tuppr/upgrades/talos.yaml`) and `task talos:upgrade-k8s`.
- Renovate merges minor, patch and digest updates after the risk assessment passes. Updates from Docker Hub, GitHub, Helm repositories and npm must also be 2 days old (3 days for GitHub Actions). Other registries have no release dates, so they have no minimum age. Majors, `0.x` minors, core infrastructure and apps with migrations get a PR. Rules: `.renovaterc.json5`.
- ARC needs `task kubernetes:upgrade-arc` because of CRDs.
- Rollback: Talos keeps the previous install in the boot menu. Helm rolls back by itself when probes fail. Migration apps use `RetryOnFailure`; fix forward. Else `git revert`.
- Stuck Helm upgrade: scale the deployments to 0, then `flux reconcile hr -n <ns> <app> --force`.

## Data and quotes

> "Updates from Docker Hub, GitHub, Helm repos and npm must also be 2 days old (3 days for GitHub Actions). Images and OCI charts on other registries have no release dates, so they get no minimum age."

Version `2d78212` changed only the rules file, from `.github/renovate/autoMerge.json5` to `.renovaterc.json5`. Version `eff692f` changed the Renovate rules, the current Talos and Kubernetes versions, and the manual upgrade example. Version `2ce9069` said only "once they're 2 days old" and used `v1.13.10` in the example.

## Connections

- [[tuppr]], [[renovate]], [[talos-linux]], [[flux]], [[rook-ceph]].

## Open questions

- None. Version `eff692f` states the current Talos version.
