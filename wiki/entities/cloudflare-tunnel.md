---
title: Cloudflare Tunnel
type: entity
kind: service
aliases: [cloudflared]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, cloudflare]
---

# Cloudflare Tunnel

## Summary

The only internet entry into the [[home-cluster]]. A `cloudflared` pod holds a tunnel to the Cloudflare edge for `*.chestr.dev` and sends traffic to `envoy-external` ([[home-cluster-networking]]).

## Facts

- Path: user, Cloudflare DNS, Cloudflare edge, tunnel, `cloudflared` pod, `envoy-external` (`10.0.20.200`), app ([[home-cluster-networking]]).
- `task bootstrap:apps` applies the tunnel resources in `bootstrap/resources.yaml` ([[home-cluster-bootstrap]]).
- `CLOUDFLARE_TUNNEL_ID` and `CLOUDFLARE_ACCOUNT_ID` come from the `cluster-secrets` Secret ([[home-cluster-secrets-management]]).
- Cloudflare also hosts the domains, issues certificates through DNS challenges, and stores backups in R2 ([[home-cluster-readme]]).
- [[cloudflare-terraform]] manages the tunnel, rulesets and zone settings ([[home-cluster-agents-md]]).

## Related

- [[envoy-gateway]], [[split-horizon-dns]], [[internal-vs-external-gateway]].
