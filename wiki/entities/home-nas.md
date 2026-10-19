---
title: Home NAS
type: entity
kind: hardware
aliases: [NAS, UNAS Pro 8]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, hardware, storage]
---

# Home NAS

## Summary

The network storage device next to the [[home-cluster]]. It receives the 4-hourly pg_dump of each app database ([[home-cluster-disaster-recovery]]).

## Facts

- Model: UniFi UNAS Pro 8 with 4x 28TB disks (112TB raw), UniFi OS ([[home-cluster-readme]], [[home-cluster-networking]]).
- NFS host for the Postgres dumps: `nebula.chestr.dev:/var/nfs/shared/cluster/apps/postgres-backup-local` ([[home-cluster-waitlist-readme]]).
- Address: `10.0.40.13` on the server subnet. 10Gb link to the USW-Pro-Aggregation switch ([[home-cluster-networking]]).
- Version `2ce9069` of the README listed a Synology DS920+. Version `e36a8c8` replaced it with the UNAS Pro 8 ([[home-cluster-readme]]).

- The [[cloudnative-pg]] `cnpg` component writes a pg_dump of each app database to the NAS every 4 hours ([[home-cluster-disaster-recovery]]).
- An NFS debug pod is available: `task kubernetes:nfs-pod NS=<namespace>` ([[home-cluster-troubleshooting]]).

## Related

- [[backup-strategy]].
