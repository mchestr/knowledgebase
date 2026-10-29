---
title: Claude Code Remote Control (in-cluster)
type: entity
kind: software
aliases: [claude-code, in-cluster Claude Code]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, ai, claude-code, security]
---

# Claude Code Remote Control (in-cluster)

## Summary

A Claude Code server in the `ai` namespace of the [[home-cluster]]. The owner connects to it from claude.ai/code or the Claude app to fix the cluster without the Mac ([[home-cluster-claude-code-readme]]).

## Facts

- Reach: `cluster-admin`, talosctl, gh with push access to `mchestr/home-cluster`, and the kubernetes and flux-operator MCP servers ([[home-cluster-claude-code-readme]]).
- Guard: the permission mode. Tools outside the repo's `.claude/settings.json` allowlist wait for approval in the app ([[home-cluster-claude-code-readme]]).
- Optional Home Assistant MCP server through a non-admin user's `HASS_TOKEN` (`/api/mcp/assist`, Assist-exposed entities only) ([[home-cluster-claude-code-readme]]).
- Network: an outbound-only NetworkPolicy. No HTTPRoute ([[home-cluster-claude-code-readme]], [[home-cluster-app-inventory]]).
- Login: a full claude.ai login, stored in `~/.claude` on the `claude-code` PVC. VolSync does not back up this PVC on purpose. `claude setup-token` tokens are rejected ([[home-cluster-claude-code-readme]]).
- Terraform runs in the pod: the ExternalSecret supplies the Cloudflare, 1Password Connect and Terraform Cloud tokens. There is no `op` CLI, so `talos:apply-node` still needs the Mac ([[home-cluster-claude-code-readme]]).
- Its `CLAUDE.md` sets the ASD-STE100 writing style and tells it to read this knowledge base at `~/knowledgebase` before it troubleshoots ([[home-cluster-claude-code-agent-instructions]]).
- The repository also defines the `ops` subagent ([[home-cluster-ops-agent]]) and the `add-app`, `renovate-review` and `volsync-restore` skills.

## Bootstrap

1. Exec into the pod: `kubectl exec -it -n ai deploy/claude-code -- bash`.
2. Log in: `claude auth login`.
3. Run `cd ~/home-cluster && claude remote-control`. Answer y and y, then press Ctrl-C.
4. Run `touch ~/.remote-control-ready`, then exit.
5. Restart: `kubectl rollout restart -n ai deploy/claude-code`.

If the login expires, sessions stop. Run `claude auth login` again ([[home-cluster-claude-code-readme]]).

WARNING: Remote Control does not start if `ANTHROPIC_API_KEY`, `ANTHROPIC_AUTH_TOKEN`, `CLAUDE_CODE_DISABLE_NONESSENTIAL_TRAFFIC` or `DISABLE_GROWTHBOOK` is set.

## Related

- [[in-cluster-ai-stack]], [[security-posture]], [[renovate-risk-review]].
