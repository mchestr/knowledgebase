---
title: VictoriaLogs
type: entity
kind: software
aliases: [VM Logs, VMAlert, VMRule]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, observability, logging]
---

# VictoriaLogs

## Summary

The log store of the [[home-cluster]]. Fluent Bit collects the logs. VictoriaLogs replaced Loki ([[home-cluster-observability]]).

## Facts

- Fluent Bit uses about 10 mCPU and 15MB RAM. It replaced vector and promtail ([[home-cluster-observability]]).
- The Fluent Bit chart comes from `oci://ghcr.io/fluent/helm-charts/fluent-bit` since 2026-10-28. The home-operations/charts-mirror copy stopped allowing pulls ([[incident-2026-10-28-fluent-bit-chart-mirror-403]], [[oci-chart-pull-denied]]).
- Reasons to leave Loki: no UI without Grafana, slow ad-hoc queries in Grafana, hard setup. VictoriaLogs has a built-in query UI ([[home-cluster-observability]]).
- Log alerts are `VMRule` objects (`vmrule.yaml` next to the app). A `VMAlert` evaluates them and sends to the Alertmanager of [[kube-prometheus-stack]]. They need the VictoriaMetrics operator CRDs ([[home-cluster-observability]]).
- Tail logs from a workstation with `stern -n <ns> -l app.kubernetes.io/name=<app>` ([[home-cluster-troubleshooting]]).

## Related

- [[kube-prometheus-stack]].
