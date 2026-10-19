---
title: home-cluster docs — Workstation Setup
type: source
source: raw/2026-10-18-home-cluster-workstation-setup.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/workstation-setup.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, tooling]
---

# home-cluster docs — Workstation Setup

## Summary

The tools and configuration needed to manage the [[home-cluster]] from a Mac. Homebrew installs all tools. Krew installs the kubectl plugins.

## Key points

- Install: `task workstation:brew` (Homebrew packages) and `task workstation:krew` (kubectl plugins).
- Core tools: `kubernetes-cli`, `talosctl`, `flux`, `helm`, `helmfile`, `kustomize`. Others: `go-task`, `jq`, `yq`, `k9s`, `kubecolor`, `stern`, `viddy`, `cloudflared`, `gh`, `minijinja-cli`, `1password`, `1password-cli`.
- kubectl plugins: `browse-pvc`, `node-shell`, `rook-ceph`, `view-secret`, `cert-manager`, `cnpg`. The `rook-ceph` plugin replaces the Ceph toolbox pod ([[rook-ceph]]).
- The kubeconfig is `kubernetes/kubeconfig`. `task` sets `KUBECONFIG` for each task. `.mise.toml` exports `KUBECONFIG` and `TALOSCONFIG` to the shell.
- `TALOSCONFIG` is `talos/talosconfig` (git-ignored). `task talos:regen-certs` makes it again from the machine CA in 1Password. `task talos:kubeconfig` makes the kubeconfig again.
- 1Password login: `eval $(op signin)`. Check: `op user get --me`.
- Check the setup: `kubectl get nodes`, `talosctl version`, `flux check`, `op user get --me`.

## Data and quotes

Suggested aliases: `k=kubectl`, `kc=kubecolor`, `f=flux`, `watch=viddy`, `logs=stern`.

## Connections

- [[talos-linux]], [[flux]], [[rook-ceph]], [[cloudnative-pg]], [[external-secrets]].

## Open questions

- None.
