---
title: home-cluster README
type: source
source: raw/2026-10-18-home-cluster-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/README.md
commit: 2ce9069
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
| Synology DS920+ (2x8TB & 2x16TB, 20GB RAM) | 1 | NAS ([[home-nas]]) |
| MS-01 i9-13900H (1TB OS, 2TB data, 96GB RAM) | 3 | Control plane ([[ms-01]]) |

## Connections

- [[home-cluster]], [[gitops]], [[home-nas]], [[ms-01]].

## Open questions

- The NAS in this table does not match the NAS in [[home-cluster-networking]]. See [[home-nas]].
