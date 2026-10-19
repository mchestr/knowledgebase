---
title: home-cluster Terraform README
type: source
source: raw/2026-10-18-home-cluster-terraform-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/terraform/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, terraform, cloudflare]
---

# home-cluster Terraform README

## Summary

The Cloudflare Terraform workspace. See [[cloudflare-terraform]].

## Key points

- Workspace `terraform/cloudflare`. State in Terraform Cloud, organization `mchestr`, workspace `cloudflare`.
- Cloudflare and 1Password Connect credentials come from workspace variables.
- Run `task terraform:cf:init`, `task terraform:cf:plan`, `task terraform:cf:apply`.

## Data and quotes

None.

## Connections

- [[cloudflare-terraform]], [[cloudflare-tunnel]].

## Open questions

- None.
