---
title: Internal vs external gateway
type: concept
aliases: [gateway choice, envoy-internal vs envoy-external]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, security]
---

# Internal vs external gateway

## Definition

In the [[home-cluster]], the gateway an app's `HTTPRoute` uses decides who can reach the app and what protects it. It is a security decision ([[home-cluster-application-deployment]]).

## Details

| Gateway | IP | Reachable from | Auth in front |
| --- | --- | --- | --- |
| `envoy-internal` (default) | 10.0.20.100 | LAN and WireGuard only | [[authelia]] |
| `envoy-external` | 10.0.20.200 | Internet through the [[cloudflare-tunnel]], plus LAN | None. The app's own login |

Source: [[home-cluster-networking]].

Rules ([[home-cluster-networking]], [[home-cluster-application-deployment]]):

1. Use `envoy-internal` unless the app must be on the internet.
2. Put an app on `envoy-external` only if it authenticates users itself: its own accounts, or OIDC through Authelia.
3. Never put admin UIs, shells or editors on `envoy-external`.
4. Give each external app a NetworkPolicy that admits only the external gateway's Envoy pods.
5. Add a CiliumNetworkPolicy for the `kube-apiserver` entity, because cross-node gateway traffic is SNATed to a control-plane node.
6. Copy the policy from `kubernetes/apps/default/home-assistant/app/helmrelease.yaml`. `home-assistant` and `waitlist` are the reference implementations.
7. For an internal app whose own login should replace the Authelia prompt, add it to the Authelia `bypass` list.

External apps in the sources: Plex, Immich, Home Assistant, Radicale, Authelia. Internal apps: Frigate, Sonarr, Radarr ([[home-cluster-networking]]).

The internal gateway fails closed. When Authelia is down, all internal apps are unreachable ([[home-cluster-networking]]).

## Evidence

- [[home-cluster-networking]], [[home-cluster-application-deployment]].

## Related

- [[envoy-gateway]], [[split-horizon-dns]], [[cilium]].
