---
title: Home NAS
type: entity
kind: hardware
aliases: [NAS, UNAS Pro 8, Synology DS920+]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, hardware, storage]
---

# Home NAS

## Summary

The network storage device next to the [[home-cluster]]. It receives the 4-hourly pg_dump of each app database ([[home-cluster-disaster-recovery]]).

> [!warning] Contradiction
> [[home-cluster-readme]] lists a Synology DS920+ with 2x8TB and 2x16TB disks and 20GB RAM.
> [[home-cluster-networking]] lists a UNAS Pro 8 with 4x 28TB disks (112TB raw), on `10.0.40.x` with a 10Gb link.
> One document is probably out of date. Both are at commit `2ce9069`.

## Facts

- The [[cloudnative-pg]] `cnpg` component writes a pg_dump of each app database to the NAS every 4 hours ([[home-cluster-disaster-recovery]]).
- An NFS debug pod is available: `task kubernetes:nfs-pod NS=<namespace>` ([[home-cluster-troubleshooting]]).

## Related

- [[backup-strategy]].
