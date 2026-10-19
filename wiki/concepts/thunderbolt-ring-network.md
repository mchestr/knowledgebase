---
title: Thunderbolt ring network
type: concept
aliases: [TB4 ring]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, networking, storage]
---

# Thunderbolt ring network

## Definition

A full mesh of three nodes with Thunderbolt 4 cables. Each [[ms-01]] uses its two Thunderbolt ports to connect to the other two nodes. [[rook-ceph]] uses it ([[home-cluster-networking]]).

## Details

- Subnet: `169.254.255.0/24`. m0 `.10`, m1 `.11`, m2 `.12` ([[home-cluster-networking]]).

![[thunderbolt.png]]

## Check the ring

1. Open a shell on each node: `task kubernetes:node-shell NODE=m0` (and m1, m2).
2. Check the routes: `ip r | grep '169.254.255'`.
3. From each node, ping the other two, for example from m0: `ping 169.254.255.11` and `ping 169.254.255.12`.

Source: [[home-cluster-networking]].

## Evidence

- [[home-cluster-networking]].

## Related

- [[rook-ceph]].
