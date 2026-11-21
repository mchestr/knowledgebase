---
title: Incident 2026-11-21 — tuppr drain blocked by the Dragonfly spread rule
type: source
source: raw/2026-11-21-incident-tuppr-drain-dragonfly-spread.md
author: Mike Chester
published: 2026-11-21
url:
created: 2026-11-21
updated: 2026-11-21
tags: [home-cluster, incident, flux, upgrades, database]
---

# Incident 2026-11-21 — tuppr drain blocked by the Dragonfly spread rule

## Summary

The [[tuppr]] Talos v1.14.6 upgrade failed at the node drain and left the node cordoned. The [[cloudnative-pg]] replicas on that node stayed `Pending`, so [[flux]] blocked immich and 19 other apps. The drain failed because the DragonflyDB topology spread rule counted all Dragonfly instances in a namespace together. See [[tuppr-upgrade-fails-at-drain]].

## Key points

- tuppr upgraded m0, then failed on m2 at 07:13 UTC and left m2 cordoned for 8 hours.
- `immich-8` and `postgres17-10` use `openebs-hostpath` on m2, so they stayed `Pending`. `database/cloudnative-pg-cluster` failed its health check, and every Kustomization with `dependsOn` on it waited.
- A retry on m1 showed the cause: the eviction of `silo-dragonfly-2` timed out. The PDB allowed 0 disruptions, because the evicted `silo-dragonfly-1` could not schedule.
- The spread selector `app.kubernetes.io/part-of: dragonfly` matched the subs and silo pods together in `media`. home-cluster PR #6440 changed it to `app: ${APP}-dragonfly`.
- After the merge and a reset, tuppr upgraded all three nodes.

## Data and quotes

- tuppr: "Upgrade Job failed while node remained at v1.14.5; expected v1.14.6"
- Job log: "error draining node "m1": failed to drain node "m1": error when evicting pods/"silo-dragonfly-2" -n "media": ... context deadline exceeded"
- Pending pod: "1 node(s) were unschedulable, 2 node(s) didn't match pod topology spread constraints."
- Pod counts in `media` during the drain: m0 = 2, m1 = 1 (cordoned), m2 = 2.
- Final result: "Successfully upgraded 3 nodes".

## Connections

- The fix is in the DragonflyDB component of the [[app-deployment-pattern]].
- The local talosconfig of [[claude-code-remote-control]] had an expired client certificate. The machine CA came from [[external-secrets]]' 1Password Connect API, because the 1Password CLI was not signed in.

## Open questions

- Did the m2 failure have the same cause? tuppr deleted its Job, so no log exists.
- Did an alert fire while the node was cordoned and the Kustomizations were not ready?
