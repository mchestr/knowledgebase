---
title: BGP load balancing
type: concept
aliases: [LB-IPAM, Cilium BGP]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking]
---

# BGP load balancing

## Definition

[[cilium]] gives each Kubernetes `LoadBalancer` Service an IP from a pool and advertises the IP to the router over BGP. The router then sends traffic for that IP to the nodes ([[home-cluster-networking]]).

## Details

- Pool: `10.0.20.0/24` ([[home-cluster-networking]]).
- Peers: cluster nodes ASN 64514, [[udm-pro-max]] ASN 64513 ([[home-cluster-networking]]). The router config is in [[home-cluster-cilium-config-readme]].
- Fixed IPs in the pool: Postgres `.17`, MQTT `.50`, Frigate streams `.60`, Jellyfin `.70`, qBittorrent `.80`, internal gateway `.100`, Plex `.110`, external gateway `.200` ([[home-cluster-networking]]).
- Check: `cilium bgp peers` in `ds/cilium`, and `kubectl get svc -A | grep LoadBalancer` ([[home-cluster-troubleshooting]]).

## Evidence

- [[home-cluster-networking]], [[home-cluster-troubleshooting]].

## Related

- [[split-horizon-dns]], [[envoy-gateway]].
