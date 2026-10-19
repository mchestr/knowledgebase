---
title: Cloudflare Terraform workspace
type: entity
kind: config
aliases: [terraform/cloudflare]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, terraform, cloudflare]
---

# Cloudflare Terraform workspace

## Summary

Terraform in `terraform/cloudflare` that manages the Cloudflare tunnel, rulesets, zone settings and the tunnel's 1Password item. external-dns makes the DNS records, not Terraform ([[home-cluster-agents-md]]).

## Facts

- State: Terraform Cloud, organization `mchestr`, workspace `cloudflare`. Credentials from workspace variables ([[home-cluster-terraform-readme]]).
- Commands: `task terraform:cf:init`, `task terraform:cf:plan`, `task terraform:cf:apply` ([[home-cluster-terraform-readme]]).
- `rulesets.tf` turns off Rocket Loader and email obfuscation on the Waitlist hosts, because they break its CSP hashes ([[home-cluster-waitlist-readme]]).
- The in-cluster Claude Code server cannot run it, because it has no `op` CLI ([[home-cluster-claude-code-readme]]).

## Related

- [[cloudflare-tunnel]], [[split-horizon-dns]].
