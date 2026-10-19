---
title: Envoy Gateway
type: entity
kind: software
aliases: [envoy-internal, envoy-external]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, ingress]
---

# Envoy Gateway

## Summary

The Gateway API implementation of the [[home-cluster]]. It runs two gateways: `envoy-internal` and `envoy-external` ([[home-cluster-readme]], [[internal-vs-external-gateway]]).

## Facts

- `envoy-internal`: `10.0.20.100`. It is the default. The `internal-secure` SecurityPolicy sends an ext-auth check to [[authelia]] for each request ([[home-cluster-networking]]).
- `envoy-external`: `10.0.20.200`. The [[cloudflare-tunnel]] sends internet traffic to it. LAN clients can also reach it ([[home-cluster-networking]]).
- An app picks its gateway in the HelmRelease `route.parentRefs` (namespace `networking`, section `https`) ([[home-cluster-application-deployment]]).

## Related

- [[cilium]], [[split-horizon-dns]].
