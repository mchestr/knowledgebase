---
title: tuppr
type: entity
kind: software
aliases: [TalosUpgrade, KubernetesUpgrade]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, upgrades]
---

# tuppr

## Summary

A controller from home-operations that upgrades [[talos-linux]] and Kubernetes one node at a time ([[home-cluster-upgrade-procedures]]).

## Facts

- Target versions: `kubernetes/apps/system-upgrade/tuppr/upgrades/talos.yaml` and `kubernetes.yaml`. The cluster runs Talos 1.14 and Kubernetes 1.37. [[renovate]] opens PRs to change them. Merging the PR starts the upgrade ([[home-cluster-upgrade-procedures]]).
- Before each node, tuppr waits for [[rook-ceph]] `HEALTH_OK` and for no running [[volsync]] backup ([[home-cluster-upgrade-procedures]]).
- Talos upgrades power-cycle each node, so Ceph is degraded for a short time ([[home-cluster-upgrade-procedures]]).
- Bootstrap gets the Talos ISO version from the same `talos.yaml` ([[home-cluster-bootstrap]]).

## Before you merge an upgrade

1. Check that the Talos version supports the Kubernetes version. Upgrade Talos first.
2. Apply pending changes to `talos/controlplane.yaml` on each node: `task talos:apply-node NODE=m0`, then m1 and m2. `upgrade-k8s` fails on stale `extraManifests`.
3. Check `kubectl get nodes` and `kubectl rook-ceph ceph status`.

Source: [[home-cluster-upgrade-procedures]].

## Commands

| Task | Command |
| --- | --- |
| Progress | `kubectl get talosupgrade,kubernetesupgrade` and `kubectl -n system-upgrade get jobs,pods` |
| Reset a failed upgrade | `kubectl annotate talosupgrade talos tuppr.home-operations.com/reset="$(date)"` (same for `kubernetesupgrade kubernetes`) |
| Manual fallback | `task talos:upgrade-node NODE=<node> VERSION=<v>`, `task talos:upgrade-k8s` |

## Related

- [[renovate]].
