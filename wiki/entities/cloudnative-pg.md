---
title: CloudNativePG
type: entity
kind: software
aliases: [CNPG, postgres17, immich cluster]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, database, backup]
---

# CloudNativePG

## Summary

The PostgreSQL operator of the [[home-cluster]]. It runs two Clusters, `postgres17` and `immich`, in the `database` namespace ([[home-cluster-disaster-recovery]]).

## Facts

- Manifests: `kubernetes/apps/database/cloudnative-pg/cluster/cluster17.yaml` and `immich.yaml` ([[home-cluster-disaster-recovery]]).
- Service IP: PostgreSQL `10.0.20.17` ([[home-cluster-networking]]).
- Instances use `openebs-hostpath` volumes, so they cannot move to another node ([[home-cluster-disaster-recovery]]).
- If the primary is on a failed node, CNPG promotes a replica ([[home-cluster-disaster-recovery]]).
- Backups: WAL and a daily base backup to R2 at `s3://cloudnative-pg/<serverName>/` (barman). `archive_timeout` is `5min`. The `cnpg` component also writes a pg_dump of each app database to the [[home-nas]] every 4 hours ([[home-cluster-disaster-recovery]]).
- The `cnpg` component adds a database, `${APP}-pguser-secret`, `${APP}-initdb-secret` and a backup CronJob. `CNPG_NAME` defaults to `postgres17`. Make the credentials in 1Password first ([[home-cluster-application-deployment]]).
- Apps with database migrations use `RetryOnFailure`, not rollback ([[home-cluster-upgrade-procedures]]).
- The CNPG 1.30 operator warns that 1.31.0 removes `barmanObjectStore` ([[home-cluster-disaster-recovery]]).

## Recovery rules

- CNPG reads `bootstrap` only when it makes the first instance of a new Cluster. A recovery always needs a new Cluster.
- One bootstrap method only. In `immich.yaml`, comment out `initdb` when you uncomment `recovery`.
- The new `serverName` must be empty in R2, or the Cluster stays in `Setting up primary` with `Expected empty archive`.
- Without `recoveryTarget`, CNPG restores the newest base backup and replays all WAL.

WARNING: Do not set `cnpg.io/skipEmptyWalArchiveCheck`. Two Clusters that write to one `serverName` can destroy its backups.

Source: [[home-cluster-disaster-recovery]].

## Recover a Cluster

`<cluster>` is `postgres17` or `immich`. `<file>` is `cluster17.yaml` or `immich.yaml`. The step numbers match [[home-cluster-disaster-recovery]].

1. If the Cluster still runs, do a test recovery first.
2. Read the recovery window: `kubectl cnpg status <cluster> -n database`.
3. Suspend Flux: `flux suspend kustomization cloudnative-pg-cluster -n database`.
4. If the Cluster still runs, send the current WAL: `kubectl cnpg psql <cluster> -n database -- -c 'SELECT pg_switch_wal();'`.
5. In `<file>`, read the value of `serverName: &currentCluster`, for example `postgres17-v1`.
6. Set `source: &previousCluster` to that value.
7. Uncomment the `recovery` lines and the `externalClusters` block.
8. In `immich.yaml` only, comment out `initdb` and its `postInitSQL` lines.
9. Increase the version in `serverName: &currentCluster` by one, for example `postgres17-v1` to `postgres17-v2`.
10. Optional: add `recoveryTarget.targetTime` (UTC) under `recovery`, before the bad change.
11. Check the build: `kustomize build kubernetes/apps/database/cloudnative-pg/cluster`.
12. Commit and push.

WARNING: Step 13 deletes the Cluster PVCs and all data on them.

13. Delete the Cluster: `kubectl delete cluster <cluster> -n database`.
14. Make Flux get the commit: `task kubernetes:reconcile`.

WARNING: Resume Flux only after you delete the Cluster. Flux must make a new Cluster, not change the running one.

15. Resume Flux: `flux resume kustomization cloudnative-pg-cluster -n database`.
16. Watch for `redo done`: `kubectl logs -n database job/<cluster>-1-full-recovery -f`.
17. Wait for `Cluster in healthy state`: `kubectl get cluster <cluster> -n database -w`. The Kustomization can show a health check timeout until then.
18. Check the databases: `kubectl cnpg psql <cluster> -n database -- -c '\l+'`.
19. Make a base backup in the new `serverName`: `kubectl cnpg backup <cluster> -n database`.
20. Keep the recovery block, without `initdb`, in `<file>`. The next recovery starts at step 5.

If the log shows `Expected empty archive`, do step 3, increase `serverName` again, and do steps 11 to 15.

CNPG applies `retentionPolicy` only to the current `serverName`. The old `serverName` stays in R2 until you delete it.

After a complete cluster loss, do steps 5 to 12 before `task bootstrap:apps`, and steps 16 to 20 after it ([[complete-cluster-loss-runbook]]).

## Quarterly recovery test

Recover the newest backups into a scratch Cluster `<cluster>-restore-test` with one instance and no `backup` section. Compare `\l+` with the live Cluster. For immich, check the `vchord` extension. Delete the scratch Cluster after the test ([[home-cluster-disaster-recovery]]).

WARNING: Do not add a `backup` section to the scratch Cluster. It would write to R2 next to the live backups.

## Related

- [[backup-strategy]], [[complete-cluster-loss-runbook]].
