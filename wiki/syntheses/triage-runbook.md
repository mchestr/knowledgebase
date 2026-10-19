---
title: Triage runbook
type: synthesis
question: Something in the home-cluster is broken. Where do I start?
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, runbook, troubleshooting]
---

# Triage runbook

## Answer

### Is the alerting path alive?

1. Check Healthchecks.io. If the Alertmanager `Watchdog` stopped, alerting is broken ([[kube-prometheus-stack]]).
2. Check UptimeRobot. If the home DNS record is down, the home network is unreachable from outside ([[home-cluster-observability]]).
3. Check status.chestr.dev (Gatus).

### Quick checks

```bash
kubectl get nodes -o wide
kubectl get pods -A
kubectl get events -A --sort-by='.lastTimestamp' | tail -20
flux get all -A | grep -i false
kubectl rook-ceph ceph status
```

Source: [[home-cluster-troubleshooting]].

### Symptom table

| Symptom | First check | Page |
| --- | --- | --- |
| Internal apps all down | Authelia pods, `AutheliaDown` alert | [[authelia]] |
| External apps down, internal OK | `cloudflared` pod, tunnel | [[cloudflare-tunnel]] |
| LoadBalancer IPs unreachable | `cilium bgp peers` | [[bgp-load-balancing]] |
| DNS fails in pods | CoreDNS pods, `nslookup kubernetes.default` | [[home-cluster-troubleshooting]] |
| Pod `ContainerCreating`: secret not found | ExternalSecret status | [[external-secrets]] |
| Pod `Pending`: PVC not bound | Ceph health, storage class | [[rook-ceph]] |
| HelmRelease stuck | `task kubernetes:hr:restart` | [[flux]] |
| Upgrade stuck | `kubectl get talosupgrade,kubernetesupgrade` | [[tuppr]] |
| Node `NotReady` | `talosctl -n <node> services` | [[node-failure-runbook]] |
| Certificate not ready | `kubectl describe certificate`, Cloudflare credentials | [[home-cluster-troubleshooting]] |
| App data corrupt | `task volsync:list` then `volsync:restore` | [[volsync]] |
| Something deleted | `task kubernetes:reconcile` | [[gitops]] |

### Last resort

1. Check recent commits in the repository.
2. Read the upstream docs for Talos, Flux, Cilium and Rook.
3. Ask in the Kubernetes @Home Discord.

## Analysis

This page joins the diagnostics in [[home-cluster-troubleshooting]] with the failure behavior from the other docs, for example the fail-closed internal gateway.

## Sources

- [[home-cluster-troubleshooting]]
- [[home-cluster-observability]]
- [[home-cluster-networking]]
