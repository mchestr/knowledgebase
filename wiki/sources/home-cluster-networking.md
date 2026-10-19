---
title: home-cluster docs — Home Network Setup
type: source
source: raw/2026-10-18-home-cluster-networking.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/networking.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking]
---

# home-cluster docs — Home Network Setup

## Summary

The home network, the subnets, the ingress design and the Thunderbolt ring. It has two Mermaid diagrams: the physical network and the ingress paths.

## Key points

- Subnets: `192.168.1.0/24` LAN, `192.168.33.0/24` WireGuard, `10.0.10.0/24` IoT (VLAN 10), `10.0.20.0/24` Cilium LoadBalancer pool, `10.0.40.0/24` servers.
- Nodes: m0 `10.0.40.10`, m1 `10.0.40.11`, m2 `10.0.40.12`. Ring addresses `169.254.255.10`–`.12`. Each node has a 10Gb LACP link to the USW-Pro-Aggregation.
- [[cilium]] allocates LoadBalancer IPs from `10.0.20.0/24` and advertises them to the [[udm-pro-max]] over BGP (ASN 64514 to 64513). See [[bgp-load-balancing]].
- Two gateways: `envoy-internal` `10.0.20.100` and `envoy-external` `10.0.20.200`. See [[internal-vs-external-gateway]].
- External traffic goes through Cloudflare DNS, the Cloudflare edge and the [[cloudflare-tunnel]] to the external gateway.
- Internal traffic resolves at the UDM to the gateway IP. On the internal gateway, [[authelia]] approves each request.
- External-DNS writes HTTPRoute hostnames to Cloudflare and to the UDM ([[split-horizon-dns]]).
- Home Assistant, Frigate, ESPHome, matter-server and govee2mqtt have a second interface on the IoT VLAN through Multus. That leg has no gateway and no NetworkPolicy. A UDM firewall rule controls it.
- [[thunderbolt-ring-network]] connects each node to the other two for [[rook-ceph]] traffic.

## Data and quotes

Service IPs in the LoadBalancer pool: Mosquitto MQTT `10.0.20.50`, Frigate streams `10.0.20.60`, Jellyfin `10.0.20.70`, qBittorrent `10.0.20.80`, Plex `10.0.20.110`, PostgreSQL `10.0.20.17`.

IoT VLAN: Home Assistant `10.0.10.250`, Frigate NVR `10.0.10.239`, ESPHome `10.0.10.245`, Zigbee2MQTT, Z-Wave JS UI.

Storage: "UNAS Pro 8, 4x 28TB (112TB raw)" on `10.0.40.x`, 10Gb to the aggregation switch ([[home-nas]]).

Management: PiKVM V4 Mini, CyberPower UPS, UniFi PDU Pro.

![[thunderbolt.png]]

## Connections

- [[home-cluster]], [[envoy-gateway]], [[ms-01]].

## Open questions

- The NAS here does not match the NAS in [[home-cluster-readme]]. See [[home-nas]].
- The source says the external-gateway NetworkPolicy work is not complete. Only `home-assistant` and `waitlist` have it.
