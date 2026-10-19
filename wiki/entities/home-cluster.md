---
title: home-cluster
type: entity
kind: system
aliases: [home Kubernetes cluster, mchestr/home-cluster]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, kubernetes]
---

# home-cluster

## Summary

Mike Chester's home Kubernetes cluster and the Git repository that defines it (github.com/mchestr/home-cluster). Three [[ms-01]] nodes run [[talos-linux]]. [[flux]] applies the repository to the cluster ([[gitops]]) ([[home-cluster-readme]]).

## Facts

- Nodes: m0, m1, m2. All are control-plane nodes that also run workloads ([[home-cluster-node-management]]).
- Network: [[cilium]] CNI with BGP LoadBalancer IPs to the [[udm-pro-max]] ([[bgp-load-balancing]]). Ingress through [[envoy-gateway]] with an internal and an external gateway ([[internal-vs-external-gateway]]) ([[home-cluster-networking]]).
- Storage: [[rook-ceph]] on 3 × 2TB NVMe over the [[thunderbolt-ring-network]]. `openebs-hostpath` for node-local volumes. A NAS for media and database dumps ([[home-nas]]).
- Secrets: 1Password through [[external-secrets]] ([[home-cluster-secrets-management]]).
- Auth: [[authelia]] with lldap as the user directory ([[home-cluster-readme]]).
- Backups: [[volsync]] and [[cloudnative-pg]] to Cloudflare R2 ([[backup-strategy]]).
- Upgrades: [[tuppr]] for Talos and Kubernetes. [[renovate]] for charts and images.
- Observability: [[kube-prometheus-stack]] for metrics and alerts, [[victorialogs]] for logs ([[home-cluster-observability]]).
- Public domain: `chestr.dev`. Status page: status.chestr.dev.
- Cloud cost is about $150 each year ([[home-cluster-readme]]).
- Started from `onedr0p/cluster-template` ([[home-cluster-readme]]).

## Runbooks

- First response: [[triage-runbook]].
- One node down: [[node-failure-runbook]].
- All nodes lost: [[complete-cluster-loss-runbook]].
- New app: [[app-deployment-pattern]].
- Workstation tools: [[home-cluster-workstation-setup]].

## Related

- [[gitops]], [[backup-strategy]].
