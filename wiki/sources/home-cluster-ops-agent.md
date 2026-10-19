---
title: home-cluster ops agent
type: source
source: raw/2026-10-18-home-cluster-ops-agent.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/.claude/agents/ops.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, agents, ai]
---

# home-cluster ops agent

## Summary

A Claude Code subagent definition (`ops`, model sonnet) for cluster operations: investigate state, debug workloads, read logs, reconcile Flux. See [[claude-code-remote-control]].

## Key points

- Tools: `Read`, the `kubernetes` MCP server (pods, events, nodes, resources: get, list, create, delete, scale, exec) and the `flux-operator` MCP server (reconcile, suspend, resume, apply, delete, search docs).
- The tool list includes write tools: `pods_delete`, `resources_delete`, `resources_create_or_update`, `apply_kubernetes_manifest`, `install_flux_instance`.
- Method: check pod status and events, read logs (`previous: true` for crashes), compare with `kubernetes/apps/`, check Flux conditions, prefer MCP tools over kubectl commands for the user.
- Stack summary: rook-ceph, openebs, volsync; cilium, multus, envoy-gateway, cloudflare tunnel, external-dns; external-secrets with 1Password.

## Data and quotes

None.

## Connections

- [[claude-code-remote-control]], [[flux]], [[security-posture]].

## Open questions

- None.
