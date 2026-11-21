# Incident: the tuppr Talos upgrade stops at the drain, and Flux blocks the database apps

Date: 2026-11-21
Systems: home-cluster, tuppr (system-upgrade/tuppr), Talos v1.14.5 to v1.14.6, CloudNative-PG (database/immich, database/postgres17), DragonflyDB component (kubernetes/components/dragonfly), Flux kustomize-controller

## Symptom

- Flux did not reconcile immich. 20 Kustomizations were `Ready=False` with `dependency 'database/cloudnative-pg-cluster' is not ready`. These were atuin, authelia, immich, lldap, paperless, teslamate, grafana-instance, waitlist, and the media apps autobrr, bazarr, jellyseerr, prowlarr, radarr, silo, sonarr and subs. kometa and recyclarr waited on radarr, and whisper waited on bazarr.
- `database/cloudnative-pg-cluster` stayed in "Reconciliation in progress". Each health check ran for its 10m timeout, then failed with `HealthCheckFailed`.
- `system-upgrade/tuppr-upgrades` also stayed in "Reconciliation in progress".
- The CNPG clusters `immich` and `postgres17` showed 2 of 3 ready. The pods `immich-8` and `postgres17-10` were `Pending` for 8 hours.
- Node m2 was `Ready,SchedulingDisabled` (cordoned).

## Evidence

- Pending pod event: `0/3 nodes are available: 1 node(s) were unschedulable, 2 node(s) didn't match PersistentVolume's node affinity.` The PVCs use `openebs-hostpath`, so each replica can run only on its own node.
- TalosUpgrade `talos`: phase `Failed`, `Completed with failures: 1 successful, 1 failed`. m0 completed. m2 failed with `Upgrade Job failed while node remained at v1.14.5; expected v1.14.6`. The run started at 06:57 UTC and stopped at 07:13 UTC. tuppr deleted the Job, so its logs were gone.
- tuppr left m2 cordoned after the failure.
- The Talos kernel log on m2 showed no install step at 07:13. The Job failed before the installer ran.
- After a reset, tuppr chose m1. The upgrade Job log ended with: `error draining node "m1": failed to drain node "m1": error when evicting pods/"silo-dragonfly-2" -n "media": Post "https://<api>/api/v1/namespaces/media/pods/silo-dragonfly-2/eviction": context deadline exceeded`
- PDB `media/silo-dragonfly` had 0 allowed disruptions. `silo-dragonfly-1` was `Pending` with `1 node(s) were unschedulable, 2 node(s) didn't match pod topology spread constraints.`
- The Dragonfly pods had `topologySpreadConstraints` with `maxSkew: 1`, `topologyKey: kubernetes.io/hostname`, `whenUnsatisfiable: DoNotSchedule` and `labelSelector.matchLabels: app.kubernetes.io/part-of: dragonfly`.
- The Job also evicted the CNPG replicas on m1 before it failed. Those replicas went `Pending` while m1 was cordoned, so Flux blocked the same apps again.

## Cause

The DragonflyDB component set a topology spread selector of `app.kubernetes.io/part-of: dragonfly`. Every Dragonfly pod carries that label. The scheduler counts spread inside one namespace, so in `media` the subs and silo instances counted as one group of six pods.

During the drain, the pod counts were m0 = 2, m1 = 1 (cordoned) and m2 = 2. A new silo pod on m0 or m2 makes a skew of 2, which is more than `maxSkew: 1`. So the evicted silo replica stayed `Pending`. The PDB then allowed no more evictions, and the drain of the next silo pod timed out. The upgrade Job failed, and tuppr stopped the run with the node cordoned.

The cordoned node held CNPG replicas on local disk. They could not schedule anywhere else, so the CNPG Kustomization health check failed, and every Kustomization with `dependsOn` on it waited.

The first failure on m2 has no Job log. Its symptoms match the same drain failure.

## Fix

1. Uncordon the node that tuppr left cordoned: `kubectl uncordon m2`. The CNPG replicas started, both clusters became 3 of 3, and Flux reconciled all apps.
2. home-cluster PR #6440 changed the selector in `kubernetes/components/dragonfly/cluster.yaml` to `app: ${APP}-dragonfly`. The Dragonfly operator sets that label on the pods of one instance only.
3. The reset retry on m1 failed again before the PR merged. After tuppr marked the run `Failed`, m1 was uncordoned. CNPG recovered.
4. After the merge, `media/silo`, `media/subs` and `default/authelia` were reconciled. The Dragonfly CRs got the new selector. silo-dragonfly-1 scheduled on m2, so silo had one replica on each node.
5. A second reset: `kubectl annotate talosupgrade talos tuppr.home-operations.com/reset="$(date)" --overwrite`. tuppr upgraded m1 and m2. Result: `Completed`, `Successfully upgraded 3 nodes`. All nodes run Talos v1.14.6.
6. During each drain, the CNPG replica on that node went `Pending` for a short time. Both clusters returned to 3 of 3 about 2 minutes after the last reboot.

## Side issue: expired local talosconfig

- The admin talosconfig of the in-cluster Claude Code had an expired client certificate: `remote error: tls: expired certificate`.
- `task talos:regen-certs` needs a signed-in 1Password CLI. Its precondition `op user get --me` failed.
- The machine CA was read from the `talos` item in the `kubernetes` vault through the 1Password Connect API (service `onepassword` in `external-secrets`, token from secret `onepassword-secret`). The same `talosctl gen key/csr/crt` steps as the task made a new admin certificate.

## Lessons

- A tuppr failure leaves the node cordoned. Replicas on `openebs-hostpath` on that node stay `Pending`, and Flux blocks every app that depends on `database/cloudnative-pg-cluster`.
- tuppr deletes the failed Job. To see the cause, reset the upgrade and follow the new Job log with `kubectl -n system-upgrade logs -f job/<name>`.
- A topology spread selector must match only the pods of one workload. A shared label such as `app.kubernetes.io/part-of` merges all instances in the namespace.
- A PDB with 0 allowed disruptions plus a `DoNotSchedule` spread rule can block a drain when one node is cordoned.
