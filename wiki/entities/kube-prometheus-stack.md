---
title: kube-prometheus-stack
type: entity
kind: software
aliases: [Prometheus, Alertmanager, Grafana]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, observability, monitoring]
---

# kube-prometheus-stack

## Summary

The metrics and alerting stack of the [[home-cluster]]: Prometheus, Alertmanager and the standard monitoring CRDs ([[home-cluster-observability]]).

## Facts

- CRDs: ServiceMonitor, PodMonitor, PrometheusRule, ScrapeConfig ([[home-cluster-observability]]).
- Retention: 14 days on a 50Gi [[rook-ceph]] volume ([[home-cluster-observability]]).
- Grafana (Grafana operator) and kromgo read from `prometheus-operated.observability.svc.cluster.local:9090`. kromgo serves the README status badges ([[home-cluster-observability]], [[home-cluster-readme]]).
- Alertmanager sends alerts to Pushover ([[home-cluster-observability]]).
- The Alertmanager `Watchdog` alert pings Healthchecks.io every 5 minutes. If the pings stop, the alerting path is broken ([[home-cluster-observability]]).
- Named alerts in the sources: `AutheliaDown` ([[authelia]]), `KubeJobFailed` ([[volsync]] checks).

## Related

- [[victorialogs]], [[gatus]], [[triage-runbook]].
