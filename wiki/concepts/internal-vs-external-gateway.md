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
6. Copy both policies from `kubernetes/apps/default/radicale/app/helmrelease.yaml` or from `waitlist` ([[home-cluster-application-deployment]], [[home-cluster-agents-md]]). App-template writes both policies under the `networkpolicies:` values key ([[home-cluster-app-inventory]]).
7. For an internal app whose own login should replace the Authelia prompt, add it to the Authelia `bypass` list.

`home-assistant` has the gateway policy but not the `kube-apiserver` rule, so it is not a complete example. Docs version `fa79b82` settled an earlier conflict about this ([[home-cluster-networking]]).

External apps in the sources: Plex, Immich, Home Assistant, Radicale, Authelia. Internal apps: Frigate, Sonarr, Radarr ([[home-cluster-networking]]). The full list and policy coverage are in [[security-posture]] and [[app-inventory]].

The internal gateway fails closed. When Authelia is down, all internal apps are unreachable ([[home-cluster-networking]]).

## Evidence

- [[home-cluster-networking]], [[home-cluster-application-deployment]].

## Related

- [[envoy-gateway]], [[split-horizon-dns]], [[cilium]].
