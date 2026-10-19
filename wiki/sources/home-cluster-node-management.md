---
title: home-cluster docs — Node Management
type: source
source: raw/2026-10-18-home-cluster-node-management.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/node-management.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, talos, runbook]
---

# home-cluster docs — Node Management

## Summary

How to configure, reboot, maintain, add and remove [[talos-linux]] nodes in the [[home-cluster]].

## Key points

- Three nodes m0, m1, m2. Each is an [[ms-01]] control-plane node that also runs workloads.
- Apply config: `task talos:apply-node NODE=<node>`. `MODE` is `auto` (default), `no-reboot`, `staged` or `try` (rolls back after 1 minute unless confirmed). `reboot` was removed in Talos 1.14. Use `task talos:reboot-node` after the apply.
- Config files: `talos/controlplane.yaml` (base), `talos/controlplane/m0.yaml`–`m2.yaml` (node patches), `talos/schematic.yaml`.
- Reboot: `task talos:reboot-node NODE=<node>`. Add `MODE=powercycle` for a hard reboot.
- Shut down all nodes: `task talos:shutdown-cluster`. Power on to start again.
- Node maintenance:
  1. Check `kubectl get nodes` and `kubectl rook-ceph ceph status`.
  2. `kubectl rook-ceph ceph osd set noout`.
  3. `kubectl cordon <node>` and `kubectl drain <node> --ignore-daemonsets --delete-emptydir-data`.
  4. Do the maintenance.
  5. `kubectl uncordon <node>`.
  6. `kubectl rook-ceph ceph osd unset noout`.
- Reset a node: `task talos:reset-node NODE=<node>`. Reset all nodes: `task talos:reset-cluster`.
- Add a node: install Talos with Secure Boot, write `talos/controlplane/<node>.yaml`, apply it, and watch `kubectl get nodes -w`. Rook makes OSDs on its disks.
- Remove a node: drain it, remove its OSDs, `kubectl delete node <node>`, and optionally reset it.
- Privileged node shell: `task kubernetes:node-shell NODE=<node>`.

## Data and quotes

> "`reboot` was removed in Talos 1.14; use `task talos:reboot-node` afterwards instead"

## Connections

- [[talos-linux]], [[rook-ceph]], [[node-failure-runbook]].

## Open questions

- None.
