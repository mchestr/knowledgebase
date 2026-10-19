---
title: home-cluster README
type: source
source: raw/2026-10-18-home-cluster-readme-e36a8c8.md
previous_sources:
  - raw/2026-10-18-home-cluster-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, kubernetes]
---

# home-cluster README

## Summary

The front page of the [[home-cluster]] repository. It lists the core components, the observability stack, the in-cluster AI services, the cloud dependencies and the hardware. Flux applies the `kubernetes/` folder to the cluster ([[gitops]]).

## Key points

- Core components: [[authelia]] (with lldap as the user directory), [[volsync]], [[cilium]], [[cloudnative-pg]], Dragonfly, [[envoy-gateway]], [[external-secrets]], [[tuppr]], cert-manager, external-dns, [[rook-ceph]], [[talos-linux]].
- Observability: Fluent Bit, Grafana, Alertmanager, Pushover, Gatus, [[victorialogs]], Prometheus. See [[kube-prometheus-stack]].
- AI services use hosted models, not local GPUs: an in-cluster Claude Code Remote Control server, LiteLLM (routes to OpenRouter), memini, and text-embeddings-inference.
- CI: each pull request and [[renovate]] branch is built with flux-local. A risk assessment of the rendered diff gates Renovate automerge. New images are pre-pulled onto the nodes.
- Cloud dependencies: 1Password, AWS SES (email), Cloudflare (tunnels, certificates, domains), Cloudflare R2 (backups), OpenRouter, Pushover. Total cost is about $150 each year.
- Repository directories: `bootstrap/`, `docs/`, `kubernetes/{flux,components,apps}`, `talos/`, `terraform/` (Cloudflare).
- The repository started from `onedr0p/cluster-template`.

## Data and quotes

Hardware table:

| Device | Count | Purpose |
| --- | --- | --- |
| UDM-Pro-Max | 1 | Router ([[udm-pro-max]]) |
| USW-Pro-Aggregation | 1 | Switch |
| USW-Pro-Max-24-PoE | 1 | Switch |
| UAP-AC-Lite | 1 | WiFi AP |
| ER-10X | 1 | Switch |
| PiKVM V4 Mini | 1 | KVM |
| TESmart HDMI KVM Switch 8 Ports | 1 | KVM switch |
| CyberPower CP1500PFCRM2U | 1 | UPS |
| USP-PDU-Pro | 1 | PDU |
| UNAS Pro 8 (4x28TB, UniFi OS) | 1 | NAS ([[home-nas]]) |
| MS-01 i9-13900H (1TB OS, 2TB data, 96GB RAM) | 3 | Control plane ([[ms-01]]) |

Version `e36a8c8` changed only the NAS row. Version `2ce9069` listed a Synology DS920+ with 2x8TB & 2x16TB disks, 20GB RAM and DSM.

## Connections

- [[home-cluster]], [[gitops]], [[home-nas]], [[ms-01]].

## Open questions

- None. Version `e36a8c8` settled the NAS conflict with [[home-cluster-networking]].
