---
title: Backup strategy
type: concept
aliases: [backups]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, backup]
---

# Backup strategy

## Definition

Where each kind of [[home-cluster]] state is kept, and how it comes back ([[home-cluster-disaster-recovery]]).

## Details

| State | Backup | Frequency | Restore |
| --- | --- | --- | --- |
| Cluster config | Git ([[gitops]]) | Each commit | [[flux]] reconcile |
| Secrets | 1Password ([[external-secrets]]) | Live | ESO sync |
| PVC data | [[volsync]] restic to Cloudflare R2 | Daily | Automatic after full loss; `task volsync:restore` |
| Postgres | [[cloudnative-pg]] WAL + base backup to R2 | WAL continuous (5 min timeout), base daily | Manual: new Cluster and new `serverName` |
| Postgres (second copy) | pg_dump to [[home-nas]] | Every 4 hours | Only if R2 has no usable backup |

Checks:

- [[volsync]]: a monthly `restic check --read-data-subset=10%` for each app. A failure raises `KubeJobFailed`.
- [[cloudnative-pg]]: a recovery test into a scratch Cluster each quarter.

Not covered: `openebs-hostpath` volumes are node-local. CNPG rebuilds its replicas from the primary. VolSync rebuilds its caches ([[home-cluster-disaster-recovery]]).

## Evidence

- [[home-cluster-disaster-recovery]], [[home-cluster-application-deployment]].

## Related

- [[complete-cluster-loss-runbook]], [[node-failure-runbook]].
