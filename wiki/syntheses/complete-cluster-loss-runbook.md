---
title: Complete cluster loss runbook
type: synthesis
question: How do I rebuild the home-cluster from nothing?
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, runbook, backup]
---

# Complete cluster loss runbook

## Answer

Use this when 2 or more nodes are lost and etcd has no quorum, or when all nodes are new. Git, 1Password and R2 hold everything needed ([[backup-strategy]]).

WARNING: Postgres does not restore by itself. Prepare the CNPG recovery before `task bootstrap:apps`, or you get empty databases and the app restores fail their migrations.

1. Install Talos on each node with Secure Boot ([[ms-01]], [[home-cluster-bootstrap]]).
2. Apply the config to each node: `task talos:apply-node NODE=m0`, then m1 and m2.
3. Prepare the Postgres recovery: do steps 5 to 12 of "Recover a Cluster" in [[cloudnative-pg]] for `postgres17` and `immich`. This uncomments `bootstrap.recovery` and `externalClusters` in `cluster17.yaml` and `immich.yaml`, and increases `serverName` (for example `postgres17-v1` to `postgres17-v2`).
4. Bootstrap Talos: `task bootstrap:talos`.
5. Bootstrap the apps: `task bootstrap:apps ROOK_DISK=<disk-model>`. This installs [[cilium]], CoreDNS, cert-manager, [[external-secrets]], kubelet-csr-approver, spegel and [[flux]].
6. Flux applies everything from Git ([[gitops]]).
7. [[volsync]] restores each PVC from R2 through its bootstrap ReplicationDestination. No action is needed.
8. Do steps 16 to 20 of "Recover a Cluster" in [[cloudnative-pg]]: watch the recovery, check the databases, and make a new base backup.
9. Check [[rook-ceph]] health and the [[triage-runbook]] quick checks.

## Analysis

The bootstrap page says the cluster "should come up based on the last available Volsync snapshot" ([[home-cluster-bootstrap]]). This is true for PVCs only. Postgres is the one manual dependency ([[home-cluster-disaster-recovery]]).

## Sources

- [[home-cluster-disaster-recovery]]
- [[home-cluster-bootstrap]]
