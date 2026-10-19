---
title: VictoriaLogs
type: entity
kind: software
aliases: [VM Logs, VMAlert, VMRule]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, observability, logging]
---

# VictoriaLogs

## Summary

The log store of the [[home-cluster]]. Fluent Bit collects the logs. VictoriaLogs replaced Loki ([[home-cluster-observability]]).

## Facts

- Fluent Bit uses about 10 mCPU and 15MB RAM. It replaced vector and promtail ([[home-cluster-observability]]).
- Reasons to leave Loki: no UI without Grafana, slow ad-hoc queries in Grafana, hard setup. VictoriaLogs has a built-in query UI ([[home-cluster-observability]]).
- Log alerts are `VMRule` objects (`vmrule.yaml` next to the app). A `VMAlert` evaluates them and sends to the Alertmanager of [[kube-prometheus-stack]]. They need the VictoriaMetrics operator CRDs ([[home-cluster-observability]]).
- Tail logs from a workstation with `stern -n <ns> -l app.kubernetes.io/name=<app>` ([[home-cluster-troubleshooting]]).

## Related

- [[kube-prometheus-stack]].
