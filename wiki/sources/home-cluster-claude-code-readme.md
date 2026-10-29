---
title: home-cluster claude-code README
type: source
source: raw/2026-10-28-home-cluster-claude-code-readme-2d78212.md
previous_sources:
  - raw/2026-10-18-home-cluster-claude-code-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/kubernetes/apps/ai/claude-code/README.md
commit: 2d78212
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, ai, claude-code]
---

# home-cluster claude-code README

## Summary

How Claude Code runs in the cluster as a Remote Control server, so the owner can fix the cluster from claude.ai/code or the Claude app. See [[claude-code-remote-control]].

## Key points

- Reach: `cluster-admin`, talosctl, gh with push access, and the kubernetes and flux-operator MCP servers. The guard is the permission mode: tools outside the repo's `.claude/settings.json` allowlist wait for approval in the app.
- 1Password item `claude-code`: `GITHUB_TOKEN` (fine-grained PAT on `mchestr/home-cluster`, contents and PRs read/write), `TALOSCONFIG` (admin talosconfig), `HASS_TOKEN` (non-admin Home Assistant user for the `/api/mcp/assist` MCP server). Without `HASS_TOKEN` the ExternalSecret does not sync and the pod cannot start. An empty value skips the server.
- Remote Control needs a full claude.ai login. A `claude setup-token` token is rejected. The first run is interactive. The pod only sleeps until `~/.remote-control-ready` exists.
- Bootstrap: exec into `deploy/claude-code` in `ai`, `claude auth login`, `claude remote-control` in `~/home-cluster` (answer y twice, then Ctrl-C), `touch ~/.remote-control-ready`, restart the deployment.
- Each new session gets its own git worktree. The session name is `home-cluster`.
- `~/.claude` is on the `claude-code` PVC, which VolSync does not back up on purpose. If it is lost, repeat the bootstrap.
- Remote Control does not start if `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `DISABLE_GROWTHBOOK` is set.
- The pod has `terraform`. The ExternalSecret also copies `CLOUDFLARE_TERRAFORM_TOKEN` (item `cloudflare`), `OP_CONNECT_TOKEN` (item `1password`) and `TERRAFORM_TOKEN` (item `terraform`, as `TF_TOKEN_app_terraform_io`), so `task terraform:cf:*` needs no `op`.
- There is no `op` CLI, so `talos:apply-node` (`op inject`) still needs the Mac.

## Data and quotes

The app has an outbound-only NetworkPolicy (`app/networkpolicy.yaml`, "Remote Control is outbound-only") ([[home-cluster-app-inventory]]).

Version `2d78212` added Terraform to the pod. Before it, Terraform also needed the Mac.

## Connections

- [[claude-code-remote-control]], [[security-posture]], [[in-cluster-ai-stack]].

## Open questions

- None.
