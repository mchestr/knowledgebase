---
title: Talos Linux
type: entity
kind: software
aliases: [Talos, talosctl]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, os]
---

# Talos Linux

## Summary

The immutable, API-driven Kubernetes operating system on all [[home-cluster]] nodes. Each node boots a Secure Boot image from the Talos image factory ([[home-cluster-bootstrap]]).

## Facts

- Config: `talos/controlplane.yaml`, node patches in `talos/controlplane/<node>.yaml`, factory schematic in `talos/schematic.yaml` ([[home-cluster-node-management]]).
- The built-in CNI and CoreDNS are disabled. [[cilium]] and a Flux-managed CoreDNS replace them ([[home-cluster-bootstrap]]).
- Machine secrets come from 1Password with `op inject` ([[home-cluster-secrets-management]]).
- `TALOSCONFIG` is `talos/talosconfig`. `task talos:regen-certs` makes it again ([[home-cluster-workstation-setup]]).
- [[tuppr]] upgrades Talos. Upgrade Talos before Kubernetes ([[home-cluster-upgrade-procedures]]).
- Talos keeps the previous install. Select it in the boot menu to roll back ([[home-cluster-upgrade-procedures]]).
- A reset wipes the `EPHEMERAL` partition, which holds `/var/mnt/extra` and all `openebs-hostpath` volumes ([[home-cluster-disaster-recovery]]).
- When a node with an empty etcd folder joins, Talos removes the old etcd member with the same hostname ([[home-cluster-disaster-recovery]]).
- Current versions: Talos 1.14 and Kubernetes 1.37. The [[tuppr]] target files hold the exact versions ([[home-cluster-upgrade-procedures]]).

## Commands

| Task | Command |
| --- | --- |
| Apply config | `task talos:apply-node NODE=<node> [MODE=auto\|no-reboot\|staged\|try]` |
| Reboot | `task talos:reboot-node NODE=<node> [MODE=powercycle]` |
| Shut down all | `task talos:shutdown-cluster` |
| Reset node | `task talos:reset-node NODE=<node>` |
| New kubeconfig | `task talos:kubeconfig` |
| etcd health | `talosctl --nodes m0,m1,m2 etcd status` |
| Services | `talosctl -n <node> services` |

## Related

- [[ms-01]], [[node-failure-runbook]], [[complete-cluster-loss-runbook]].
