---
title: home-cluster docs — Upgrade Procedures
type: source
source: raw/2026-10-18-home-cluster-upgrade-procedures.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/upgrade-procedures.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, upgrades, runbook]
---

# home-cluster docs — Upgrade Procedures

## Summary

How [[talos-linux]], Kubernetes, Flux and Helm charts are upgraded, and how to roll back. [[tuppr]] automates Talos and Kubernetes upgrades. [[renovate]] opens or merges the version bumps.

## Key points

- Before an upgrade: check `kubectl get nodes` and `kubectl rook-ceph ceph status`. Optionally take a snapshot: `task volsync:snapshot APP=<app> NS=<ns>`.
- Target versions: `kubernetes/apps/system-upgrade/tuppr/upgrades/talos.yaml` and `kubernetes.yaml`. Merging the Renovate PR starts the upgrade.
- tuppr upgrades one node at a time. Before each node it waits for Ceph `HEALTH_OK` and for no running VolSync backup. Talos upgrades power-cycle each node.
- Upgrade Talos before Kubernetes. Example: Talos 1.13 supports Kubernetes 1.31–1.36. Kubernetes 1.37 needs Talos 1.14.
- Apply pending changes to `talos/controlplane.yaml` (including `extraManifests` URL bumps) before an upgrade. `upgrade-k8s` fails on stale `extraManifests`.
- Reset a failed tuppr upgrade with the `tuppr.home-operations.com/reset` annotation.
- Manual fallback: `task talos:upgrade-node NODE=m0 VERSION=v1.13.10` and `task talos:upgrade-k8s`.
- Renovate merges minor, patch and digest updates after they are 2 days old. Majors, `0.x` minors, core infrastructure and apps with migrations get a PR. Rules: `.github/renovate/autoMerge.json5`.
- ARC needs `task kubernetes:upgrade-arc` because of CRDs.
- Rollback: Talos keeps the previous install in the boot menu. Helm rolls back by itself when probes fail. Migration apps use `RetryOnFailure`; fix forward. Else `git revert`.
- Stuck Helm upgrade: scale the deployments to 0, then `flux reconcile hr -n <ns> <app> --force`.

## Data and quotes

> "Renovate automerges minor, patch and digest updates once they're 2 days old."

## Connections

- [[tuppr]], [[renovate]], [[talos-linux]], [[flux]], [[rook-ceph]].

## Open questions

- The manual example uses Talos `v1.13.10`. [[home-cluster-node-management]] refers to Talos 1.14 behavior. The current Talos version is not stated.
