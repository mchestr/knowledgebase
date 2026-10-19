---
title: Rook-Ceph
type: entity
kind: software
aliases: [Rook, Ceph, ceph-block]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, storage]
---

# Rook-Ceph

## Summary

Distributed block storage for the [[home-cluster]]. One 2TB NVMe OSD on each node. Ceph traffic uses the [[thunderbolt-ring-network]] ([[home-cluster-networking]]).

## Facts

- The Rook toolbox pod is disabled. Use the `rook-ceph` kubectl plugin ([[home-cluster-storage-operations]]).
- Ceph keeps a copy of all data on each host. With one node down, the other 2 hosts have all data, but the data is degraded until the node returns ([[home-cluster-disaster-recovery]]).
- A `ceph-block` volume cannot attach to another node while its node is down. Use the out-of-service taint ([[node-failure-runbook]]).
- [[tuppr]] waits for `HEALTH_OK` before it upgrades each node ([[home-cluster-upgrade-procedures]]).
- Prometheus stores metrics on a 50Gi Ceph volume ([[home-cluster-observability]]).

## Commands

| Task | Command |
| --- | --- |
| Health | `kubectl rook-ceph ceph status`, `kubectl rook-ceph ceph health detail` |
| OSDs | `kubectl rook-ceph ceph osd tree`, `kubectl rook-ceph ceph osd df` |
| Pools | `kubectl rook-ceph ceph df` |
| Maintenance on | `kubectl rook-ceph ceph osd set noout` |
| Maintenance off | `kubectl rook-ceph ceph osd unset noout` |

## Remove a dead OSD

1. Scale the OSD to 0: `kubectl -n rook-ceph scale deploy rook-ceph-osd-<ID> --replicas 0`.
2. Purge it: `kubectl rook-ceph ceph osd purge <ID> --yes-i-really-mean-it`.
3. Delete its auth: `kubectl rook-ceph ceph auth del osd.<ID>`.
4. If you retire the node, remove it from CRUSH: `kubectl rook-ceph ceph osd crush remove <nodename>`.

Source: [[home-cluster-storage-operations]].

## OSD does not join after a disk move

1. Start a debug pod: `kubectl rook-ceph debug start rook-ceph-osd-<ID>`.
2. Read `/var/lib/ceph/osd/ceph-<ID>/keyring`.
3. Write `osd.export` with the key and the caps `mon "allow profile osd"`, `mgr "allow profile osd"`, `osd "allow *"`.
4. Import it: `kubectl rook-ceph ceph auth import -i osd.export`.
5. Stop the debug pod: `kubectl rook-ceph debug stop rook-ceph-osd-<ID>`.

Source: [[home-cluster-storage-operations]].

## Related

- [[volsync]], [[node-failure-runbook]].
