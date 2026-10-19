---
title: home-cluster claude-code README
type: source
source: raw/2026-10-18-home-cluster-claude-code-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/ai/claude-code/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
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
- There is no `op` CLI, so 1Password tasks (terraform, `talos:apply-node`) still need the Mac.

## Data and quotes

The app has an outbound-only NetworkPolicy (`app/networkpolicy.yaml`, "Remote Control is outbound-only") ([[home-cluster-app-inventory]]).

## Connections

- [[claude-code-remote-control]], [[security-posture]], [[in-cluster-ai-stack]].

## Open questions

- None.
