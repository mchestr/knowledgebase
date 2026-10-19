---
title: Node failure runbook
type: synthesis
question: What do I do when one home-cluster node goes down?
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, runbook]
---

# Node failure runbook

## Answer

With one of three nodes down, the [[home-cluster]] keeps working. etcd keeps quorum (2 of 3). [[rook-ceph]] has all data on the other 2 hosts. [[cloudnative-pg]] promotes a replica if the primary was on the failed node ([[home-cluster-disaster-recovery]]).

### Assess

1. Find the node that is down: `kubectl get nodes`.
2. Check that 2 etcd members are healthy: `talosctl --nodes m0,m1,m2 etcd status`. If 2 nodes are down, etcd has no quorum. Go to [[complete-cluster-loss-runbook]].
3. Check that each CNPG Cluster has a primary: `kubectl get cluster -n database`.

### Try to recover the node

1. If the node hangs, reboot it: `task talos:reboot-node NODE=<node>`.
2. If the Talos API does not answer, power-cycle it: `task talos:reboot-node NODE=<node> MODE=powercycle`, or use the PiKVM.
3. Diagnose with `talosctl -n <node> services` and `talosctl -n <node> dmesg | tail -50` ([[home-cluster-troubleshooting]]).

### Move stuck pods

Pods with a `ceph-block` volume on the failed node stay stuck, because the volume cannot attach to another node.

WARNING: Apply the out-of-service taint only when the node is powered off. If the node still runs, two nodes can write to the same volume and corrupt it.

1. Taint the node: `kubectl taint nodes <node> node.kubernetes.io/out-of-service=nodeshutdown:NoExecute`.
2. Kubernetes deletes the pods and detaches their volumes. Pods with `openebs-hostpath` volumes (CNPG instances, VolSync caches) cannot move.

### Bring the node back

1. If the node needs a full reinstall and its Talos API answers, reset it: `task talos:reset-node NODE=<node>`.
2. If the Talos API does not answer, boot the node from the Talos ISO ([[ms-01]] Secure Boot steps).
3. Apply the config: `task talos:apply-node NODE=<node>`. For a node in maintenance mode, the task adds `--insecure`.
4. Remove the taint if you applied it: `kubectl taint nodes <node> node.kubernetes.io/out-of-service=nodeshutdown:NoExecute-`.
5. Wait for the OSD to show `up`: `kubectl rook-ceph ceph osd tree`.
6. Wait for `HEALTH_OK`: `kubectl rook-ceph ceph status`. Data stays degraded until recovery ends.
7. If the OSD disk is dead, remove the OSD ([[rook-ceph]]).
8. Check that all 3 etcd members are healthy: `talosctl --nodes m0,m1,m2 etcd status`.

### After a reset

A reset wipes `EPHEMERAL`, which holds all `openebs-hostpath` volumes on that node.

1. List the local volumes of the node: filter `kubectl get pvc -A` on the `volume.kubernetes.io/selected-node` annotation and class `openebs-hostpath`.
2. For each CNPG instance, delete its PVC and pod: `kubectl delete -n database pvc/<instance> pod/<instance>`. CNPG makes a new replica.
3. For each `volsync-*-cache` PVC, delete the PVC. VolSync makes a new cache at its next run.
4. Leave the `*-runner-*-work` volumes. ARC makes new runners.

### Node never comes back

WARNING: Do not remove the etcd member of a node that can come back. Its etcd cannot start until you reset the node.

1. List members on a healthy node: `talosctl --nodes <healthy-node> etcd members`.
2. Remove the old member: `talosctl --nodes <healthy-node> etcd remove-member <member-id>`.
3. Remove its OSDs and delete the node ([[home-cluster-node-management]]).

## Analysis

The runbook merges the "Node Died" section of [[home-cluster-disaster-recovery]] with [[home-cluster-node-management]] and [[home-cluster-troubleshooting]]. The main risks are data corruption from the out-of-service taint on a running node, and a lost etcd member that is removed too early.

## Sources

- [[home-cluster-disaster-recovery]]
- [[home-cluster-node-management]]
- [[home-cluster-troubleshooting]]
