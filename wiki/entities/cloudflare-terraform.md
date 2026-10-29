---
title: Cloudflare Terraform workspace
type: entity
kind: config
aliases: [terraform/cloudflare]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, terraform, cloudflare]
---

# Cloudflare Terraform workspace

## Summary

Terraform in `terraform/cloudflare` that manages the Cloudflare tunnel, rulesets, zone settings and the tunnel's 1Password item. external-dns makes the DNS records, not Terraform ([[home-cluster-agents-md]]).

## Facts

- State: Terraform Cloud, organization `mchestr`, workspace `cloudflare`. Credentials from workspace variables ([[home-cluster-terraform-readme]]).
- Commands: `task terraform:cf:init`, `task terraform:cf:plan`, `task terraform:cf:apply` ([[home-cluster-terraform-readme]]).
- `rulesets.tf` turns off Rocket Loader and email obfuscation on the Waitlist hosts, because they break its CSP hashes ([[home-cluster-waitlist-readme]]).

  > [!question] Unverified
  > Commit `3f55114` turns off Rocket Loader on every zone in `terraform/cloudflare/zone_settings.tf`, and the Waitlist rule keeps only email obfuscation off. No ingested source covers this yet.

- The in-cluster Claude Code server can run it: its ExternalSecret supplies the tokens, so `task terraform:cf:*` needs no `op` ([[home-cluster-claude-code-readme]]).

## Related

- [[cloudflare-tunnel]], [[split-horizon-dns]].
