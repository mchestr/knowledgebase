---
title: home-cluster docs — Disaster Recovery
type: source
source: raw/2026-10-18-home-cluster-disaster-recovery.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/disaster-recovery.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, backup, runbook]
---

# home-cluster docs — Disaster Recovery

## Summary

The backup design and the recovery procedures for app data, a failed node, a complete cluster loss and Postgres. The longest and most detailed page in the docs. See [[backup-strategy]].

## Key points

- Backups: [[volsync]] to Cloudflare R2 each day with restic. [[cloudnative-pg]] WAL and a daily base backup to R2 (barman), plus a pg_dump of each app database to the NAS every 4 hours. Cluster state in Git. Secrets in 1Password.
- VolSync assumptions: Kustomization, HelmRelease, PVC and ReplicationSource share one name. Restic. Deployment or StatefulSet. One PVC for each app.
- VolSync tasks: `volsync:list`, `volsync:snapshot` (waits up to 2 hours), `volsync:restore ... PREVIOUS=<n>`, `volsync:unlock`, `volsync:state-suspend|resume`.
- A monthly `<app>-volsync-check` CronJob runs `restic check --read-data-subset=10%`. A failure raises `KubeJobFailed`.
- Node failure: the cluster keeps working with one node down. See [[node-failure-runbook]].
- Complete cluster loss: see [[complete-cluster-loss-runbook]].
- Postgres recovery always needs a new Cluster and a new `serverName`. See [[cloudnative-pg]].
- A recovery test for `postgres17` and `immich` runs each quarter in a scratch Cluster with no `backup` section.
- A deleted resource comes back with `task kubernetes:reconcile`. After Flux makes a deleted PVC again, run `task volsync:restore ... PREVIOUS=0`.

## Data and quotes

> "WARNING: Do not set `cnpg.io/skipEmptyWalArchiveCheck`. Two Clusters that write to one `serverName` can destroy its backups."

> "The CNPG 1.30 operator warns that CNPG 1.31.0 removes `barmanObjectStore`."

## Connections

- [[backup-strategy]], [[volsync]], [[cloudnative-pg]], [[rook-ceph]], [[node-failure-runbook]], [[complete-cluster-loss-runbook]].

## Open questions

- The migration from `barmanObjectStore` to the Barman Cloud Plugin is not done. The recovery blocks must change with it.
