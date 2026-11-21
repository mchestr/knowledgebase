---
title: tuppr upgrade fails at the drain and Flux blocks database apps
type: issue
aliases: [Upgrade Job failed while node remained, dependency 'database/cloudnative-pg-cluster' is not ready, error draining node]
systems: [tuppr, flux, cloudnative-pg, dragonfly]
created: 2026-11-21
updated: 2026-11-21
tags: [home-cluster, upgrades, flux, database]
---

# tuppr upgrade fails at the drain and Flux blocks database apps

## Symptom

- Many Kustomizations are `Ready=False` with `dependency 'database/cloudnative-pg-cluster' is not ready` ([[incident-2026-11-21-tuppr-drain-dragonfly-spread]]).
- `database/cloudnative-pg-cluster` stays in "Reconciliation in progress" and fails its health check after 10m.
- A CNPG cluster shows 2 of 3 ready. One replica is `Pending` with `didn't match PersistentVolume's node affinity`.
- One node is `SchedulingDisabled`.
- The TalosUpgrade is `Failed` with `Upgrade Job failed while node remained at <old>; expected <new>`.

## Cause

[[tuppr]] cordons and drains each node before the upgrade. If the drain fails, the Job fails and tuppr leaves the node cordoned. [[cloudnative-pg]] replicas use `openebs-hostpath`, so they cannot move off that node. The CNPG health check fails, and [[flux]] blocks every app that depends on it.

| Cause of the drain failure | Sign |
| --- | --- |
| A Dragonfly topology spread selector matched all Dragonfly instances in the namespace, so an evicted replica could not schedule and the PDB blocked the next eviction | Job log `error when evicting pods/"<app>-dragonfly-N"`, PDB with 0 allowed disruptions, and a Dragonfly pod `Pending` with `didn't match pod topology spread constraints` |

## Check

1. Find the cordoned node and the failed upgrade:

   ```bash
   kubectl get nodes
   kubectl get talosupgrade talos -o jsonpath='{.status.failedNodes}'
   ```

2. Find the `Pending` CNPG replicas:

   ```bash
   kubectl -n database get clusters.postgresql.cnpg.io,pods
   ```

3. tuppr deletes the failed Job. To see the drain error, reset the upgrade (see Fix) and follow the new Job:

   ```bash
   kubectl -n system-upgrade get jobs
   kubectl -n system-upgrade logs -f job/<name>
   ```

4. If the log shows an eviction error, read the PDB and the pods of that workload:

   ```bash
   kubectl get pdb -A
   kubectl -n <namespace> describe pod <pending-pod>
   ```

5. Read the `topologySpreadConstraints` of the pod. Make sure that its `labelSelector` matches only the pods of one workload.

## Fix

WARNING: Do not uncordon a node while tuppr is in the `Upgrading` phase for it. Wait until the phase is `Failed`.

1. Uncordon the node that the failed run left cordoned:

   ```bash
   kubectl uncordon <node>
   ```

2. Wait until each CNPG cluster shows 3 of 3. Then reconcile:

   ```bash
   flux reconcile ks cloudnative-pg-cluster -n database
   ```

3. Fix the cause of the drain failure. For the Dragonfly selector, the component uses `app: ${APP}-dragonfly` since home-cluster PR #6440.
4. Reconcile the apps that use the changed component, then make sure that the blocked pod is `Running`.
5. Reset the upgrade:

   ```bash
   kubectl annotate talosupgrade talos tuppr.home-operations.com/reset="$(date)" --overwrite
   ```

6. Wait for the phase `Completed`. During each drain, the CNPG replica on that node is `Pending` for a short time, and Flux blocks the database apps. This is normal.

## Prevention

- Give each topology spread selector a label that only one workload has. Do not use a shared label such as `app.kubernetes.io/part-of`.
- Before you merge a Talos upgrade, make sure that no pod is `Pending` and that each PDB allows at least 1 disruption.

## Related

- [[tuppr]]
- [[cloudnative-pg]]
- [[flux]]
- [[home-cluster-upgrade-procedures]]
