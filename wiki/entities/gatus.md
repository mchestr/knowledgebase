---
title: Gatus
type: entity
kind: software
aliases: [gatus-sidecar, status page]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, observability]
---

# Gatus

## Summary

The public status page of the [[home-cluster]] at `status.chestr.dev` ([[home-cluster-agents-md]]).

## Facts

- `gatus-sidecar` builds the checks from every HTTPRoute. Set `gatus.home-operations.com/enabled: "false"` on a route to leave it out ([[home-cluster-agents-md]]).
- A Healthchecks.io check watches that the status page is up ([[home-cluster-observability]]).
- Gatus is on `envoy-external` with no NetworkPolicy ([[home-cluster-app-inventory]]).

## Related

- [[kube-prometheus-stack]], [[security-posture]].
