---
title: home-cluster Cilium network configuration README
type: source
source: raw/2026-10-18-home-cluster-cilium-config-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/kube-system/cilium/config/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking]
---

# home-cluster Cilium network configuration README

## Summary

The BGP configuration on the UniFi router that peers with [[cilium]]. See [[bgp-load-balancing]].

## Key points

- `router bgp 64513`, `bgp router-id 10.0.40.1`, `no bgp ebgp-requires-policy`.
- Peer group `k8s` with `remote-as 64514`. Neighbors `10.0.40.10`, `10.0.40.11`, `10.0.40.12`.
- IPv4 unicast: `next-hop-self` and `soft-reconfiguration inbound` for the peer group.

## Data and quotes

The ASNs match [[home-cluster-networking]].

## Connections

- [[cilium]], [[udm-pro-max]], [[bgp-load-balancing]].

## Open questions

- None.
