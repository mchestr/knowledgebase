---
title: Cilium
type: entity
kind: software
aliases: []
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking]
---

# Cilium

## Summary

The CNI of the [[home-cluster]]. It also allocates LoadBalancer IPs and advertises them over BGP ([[home-cluster-networking]]).

## Facts

- Bootstrap installs Cilium first, because Talos runs with `cluster.network.cni.name: none` ([[home-cluster-bootstrap]]).
- LB-IPAM pool: `10.0.20.0/24` ([[bgp-load-balancing]]).
- BGP peer: the [[udm-pro-max]] ([[home-cluster-networking]]).
- Router side: `router bgp 64513`, router-id `10.0.40.1`, peer group `k8s` with `remote-as 64514` and neighbors `10.0.40.10`–`.12`, `next-hop-self`, `soft-reconfiguration inbound` ([[home-cluster-cilium-config-readme]]).
- `dnsProxy.dnsRejectResponseCode` is set for [[waitlist]] ([[home-cluster-waitlist-readme]]).
- External-gateway apps need a CiliumNetworkPolicy for the `kube-apiserver` entity, because cross-node gateway traffic is SNATed to a control-plane node ([[home-cluster-networking]]).

## Commands

```bash
kubectl -n kube-system exec -it ds/cilium -- cilium status
kubectl -n kube-system exec -it ds/cilium -- cilium bgp peers
kubectl get svc -A | grep LoadBalancer
```

Source: [[home-cluster-troubleshooting]].

## Related

- [[envoy-gateway]], [[internal-vs-external-gateway]].
