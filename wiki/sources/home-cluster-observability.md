---
title: home-cluster docs — Observability
type: source
source: raw/2026-10-18-home-cluster-observability.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/observability.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, observability]
---

# home-cluster docs — Observability

## Summary

Metrics, logs and alerts inside the [[home-cluster]], and the external services that watch it from outside.

## Key points

- Metrics: Prometheus from [[kube-prometheus-stack]]. Retention is 14 days on a 50Gi Ceph volume. Grafana (Grafana operator) and kromgo read from `prometheus-operated.observability.svc.cluster.local:9090`.
- Logs: Fluent Bit collects (about 10 mCPU and 15MB RAM). [[victorialogs]] stores. The author used vector and promtail before.
- Reasons to move from Loki to VictoriaLogs: Loki has no UI, ad-hoc queries in Grafana are slow, Loki is hard to set up, and VictoriaLogs has a built-in query UI.
- Alerts: Prometheus rules go to Alertmanager. Log alerts are `VMRule` objects, which a `VMAlert` evaluates against VictoriaLogs and sends to the same Alertmanager. These need the VictoriaMetrics operator CRDs.
- Push notifications go to Pushover ($5, one time).
- External checks:
  - UDM dynamic DNS updates a Cloudflare A record with the home IP.
  - Healthchecks.io: the Alertmanager `Watchdog` pings every 5 minutes. A second check watches the Gatus status page (status.chestr.dev).
  - UptimeRobot pings the dynamic DNS record every 5 minutes.

## Data and quotes

> "Loki is just a storage layer with no UI - you need Grafana to visualize logs"

## Connections

- [[kube-prometheus-stack]], [[victorialogs]], [[udm-pro-max]], [[triage-runbook]].

## Open questions

- None.
