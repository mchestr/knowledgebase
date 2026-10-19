---
title: UniFi Dream Machine Pro Max
type: entity
kind: hardware
aliases: [UDM Pro Max, UDM, UDM-Pro-Max]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, hardware]
---

# UniFi Dream Machine Pro Max

## Summary

The home gateway and router. It routes all subnets, peers with the cluster over BGP, and serves the internal DNS records ([[home-cluster-networking]]).

## Facts

- Addresses: `192.168.1.1` (LAN) and `10.0.40.1` (servers) ([[home-cluster-networking]]).
- BGP ASN 64513. The cluster nodes use ASN 64514 ([[bgp-load-balancing]]).
- External-DNS writes HTTPRoute hostnames to the UDM for internal clients ([[split-horizon-dns]]).
- Firewall rules on the UDM control what the IoT VLAN (`10.0.10.0/24`) can reach. The cluster repository does not define these rules ([[home-cluster-networking]]).
- Dynamic DNS on the UDM updates a Cloudflare A record with the home public IP. UptimeRobot pings that record ([[home-cluster-observability]]).

## Related

- [[cilium]], [[home-cluster]].
