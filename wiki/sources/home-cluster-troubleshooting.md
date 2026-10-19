---
title: home-cluster docs — Troubleshooting
type: source
source: raw/2026-10-18-home-cluster-troubleshooting.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/troubleshooting.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, troubleshooting, runbook]
---

# home-cluster docs — Troubleshooting

## Summary

Diagnostic commands and fixes for common pod, Flux, node, network, DNS and certificate problems. See [[triage-runbook]].

## Key points

- Quick checks: `kubectl get nodes -o wide`, `kubectl get pods -A`, recent events sorted by `.lastTimestamp`, `flux get all -A | grep -i false`.
- Pending pods: resources, node selector, unbound PVC, taints.
- ContainerCreating: image pull, volume mount, missing secret (check the ExternalSecret).
- CrashLoopBackOff: `kubectl logs --previous`.
- Clean failed pods: `task kubernetes:cleanse-pods`.
- Stuck HelmRelease: `task kubernetes:hr:restart`, or `flux suspend` and `flux resume`.
- Node NotReady: `talosctl -n <node> services`, `dmesg`, `service kubelet restart`.
- Node unreachable: `task talos:reboot-node`, then a power cycle through IPMI/KVM.
- Network: `cilium status` and `cilium bgp peers` in `ds/cilium`. List LoadBalancer services.
- DNS: check CoreDNS pods (`k8s-app=kube-dns`), then `nslookup kubernetes.default` from busybox.
- Certificates: check `certificate` and `certificaterequest` objects. Common causes: Cloudflare credentials for the DNS challenge, rate limits, wrong domain.
- Last resort: external monitoring, recent commits, upstream docs, the Kubernetes @Home Discord.

## Data and quotes

None.

## Connections

- [[triage-runbook]], [[cilium]], [[flux]], [[talos-linux]].

## Open questions

- None.
