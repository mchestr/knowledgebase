---
title: home-cluster docs — Cluster Bootstrap
type: source
source: raw/2026-10-18-home-cluster-bootstrap.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/bootstrap.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, bootstrap, runbook]
---

# home-cluster docs — Cluster Bootstrap

## Summary

How to build the [[home-cluster]] from bare hardware. `task bootstrap:apps` does most of the work. The cluster comes back from the last daily [[volsync]] snapshot. Postgres needs one manual step first ([[complete-cluster-loss-runbook]]).

## Key points

- Get the Talos ISO from the Talos image factory. Use the version in `kubernetes/apps/system-upgrade/tuppr/upgrades/talos.yaml` and the schematic `talos/schematic.yaml` (Secure Boot image).
- [[ms-01]] Secure Boot setup:
  1. Boot to the BIOS.
  2. Set `Security` > `Secure Boot` to `custom`.
  3. Open `Key Management`.
  4. Set `Factory Key Provision` to `disabled`.
  5. Click `Reset To Setup Mode`. Click `cancel` when it asks to save without exit.
  6. Save and reset.
  7. Mount the Talos image, reboot, and select `Enroll secure boot keys: auto`.
- Key violation errors at boot mean the factory keys were not wiped (step 4).
- Components installed before [[flux]] takes over, in order: [[cilium]] (Talos CNI disabled with `cluster.network.cni.name: none`), CoreDNS (Talos CoreDNS disabled with `cluster.coreDNS.disabled: true`), cert-manager, [[external-secrets]], kubelet-csr-approver, spegel (in-cluster OCI mirror), Flux.
- `task bootstrap:apps` applies `bootstrap/resources.yaml` (1Password and [[cloudflare-tunnel]]) and installs everything with helmfile.

## Data and quotes

> "If all goes well the cluster should come up based on the last available Volsync snapshot, which runs daily."

## Connections

- [[talos-linux]], [[gitops]], [[complete-cluster-loss-runbook]].

## Open questions

- None.
