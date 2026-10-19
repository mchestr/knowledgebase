---
title: VolSync
type: entity
kind: software
aliases: [Volsync, ReplicationSource, ReplicationDestination]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, backup]
---

# VolSync

## Summary

Backs up each app PVC to Cloudflare R2 each day with restic, and restores it ([[home-cluster-disaster-recovery]]).

## Facts

- The `volsync` component makes PVC `${APP}`, a ReplicationSource and a bootstrap ReplicationDestination ([[home-cluster-application-deployment]]).
- Variables: `APP`, `VOLSYNC_CAPACITY` (default 5Gi), `VOLSYNC_SCHEDULE`, `VOLSYNC_CACHE_CAPACITY`, `VOLSYNC_STORAGECLASS`, `VOLSYNC_ACCESSMODES`, `VOLSYNC_CLAIM`, `APP_UID`/`APP_GID`. The UID and GID must match the container user, or the app cannot read the restore ([[home-cluster-application-deployment]]).
- Retention: 7 daily, 4 weekly and 3 monthly snapshots ([[home-cluster-agents-md]]).
- Set `APP_UID`/`APP_GID` when the container user is not 1000, or the restic mover cannot read root-owned files ([[home-cluster-agents-md]]).
- Assumptions: the Kustomization, HelmRelease, PVC and ReplicationSource share one name; restic; Deployment or StatefulSet; one PVC for each app ([[home-cluster-disaster-recovery]]).
- After a complete cluster loss, each PVC restores by itself from its bootstrap ReplicationDestination ([[complete-cluster-loss-runbook]]).
- A monthly `<app>-volsync-check` CronJob runs `restic check --read-data-subset=10%`. A failure raises `KubeJobFailed` ([[home-cluster-disaster-recovery]]).
- Cache volumes are `volsync-*-cache` on `openebs-hostpath`. After a node reset, delete them. VolSync makes them again ([[home-cluster-disaster-recovery]]).
- [[tuppr]] waits until no VolSync backup runs before it upgrades a node ([[home-cluster-upgrade-procedures]]).

## Commands

| Task | Command |
| --- | --- |
| List snapshots | `task volsync:list APP=<app> NS=<ns>` |
| Snapshot now (waits up to 2 h) | `task volsync:snapshot APP=<app> NS=<ns>` |
| Restore | `task volsync:restore APP=<app> NS=<ns> PREVIOUS=<n>` (0 = newest) |
| Unlock repo | `task volsync:unlock` |
| Pause all | `task volsync:state-suspend` / `task volsync:state-resume` |
| Check now | `kubectl create job --from=cronjob/<app>-volsync-check <app>-volsync-check-manual -n <ns>` |

WARNING: Do not run `task volsync:snapshot` before a restore. A new snapshot changes the `PREVIOUS` count and can remove a good snapshot from the same day ([[home-cluster-volsync-restore-skill]]).

`volsync:list` shows the oldest snapshot first. Count `PREVIOUS` back from the last line ([[home-cluster-volsync-restore-skill]]).

## How a restore works

1. Suspend the Flux Kustomization and HelmRelease.
2. Scale the Deployment or StatefulSet to 0, or suspend the CronJob.
3. Wait for the pods to stop. For a CronJob, wait up to 5 minutes for a running Job.
4. Make a ReplicationDestination and restore the data.
5. Resume the CronJob and Flux. Reconcile the HelmRelease with `--force`.
6. Wait for the pods to be ready (not for a CronJob).

The task stops before any change when no Deployment, StatefulSet or CronJob has the app name, or when an `<app>-manual` ReplicationDestination still exists. If a step fails after step 4, Flux stays suspended, so the app does not start on partial data ([[home-cluster-disaster-recovery]]).

## After a restore

1. Check that the Flux Kustomization and HelmRelease are ready and not suspended.
2. Check that the pods are ready and the logs show no start with empty data.
3. List the files at the PVC mount path with `kubectl exec`.
4. Open the app and confirm the data from the snapshot time.

To start the app after a failed restore: `flux resume ks`, `flux resume hr`, then `flux reconcile hr --force` ([[home-cluster-volsync-restore-skill]]).

## Related

- [[backup-strategy]], [[rook-ceph]].
