---
title: Split-horizon DNS
type: concept
aliases: [split horizon]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, dns]
---

# Split-horizon DNS

## Definition

One hostname resolves to different addresses for different clients. In the [[home-cluster]], internet clients get Cloudflare and home clients get the gateway IP directly ([[home-cluster-networking]]).

## Details

- External-DNS writes each HTTPRoute hostname to Cloudflare and to the [[udm-pro-max]] ([[home-cluster-networking]]).
- Internet clients resolve `app.chestr.dev` to the Cloudflare edge. Traffic goes through the [[cloudflare-tunnel]] ([[home-cluster-networking]]).
- Home clients resolve `app.chestr.dev` at the UDM to `10.0.20.100` or `10.0.20.200`. BGP routes those IPs to the nodes ([[bgp-load-balancing]]).
- Home clients reach both gateways directly. Only internet clients use the tunnel ([[home-cluster-networking]]).

## Evidence

- [[home-cluster-networking]].

## Related

- [[internal-vs-external-gateway]], [[envoy-gateway]].
