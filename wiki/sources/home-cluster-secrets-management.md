---
title: home-cluster docs — Secrets Management
type: source
source: raw/2026-10-18-home-cluster-secrets-management.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/secrets-management.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, secrets, runbook]
---

# home-cluster docs — Secrets Management

## Summary

How secrets flow from 1Password into the cluster with [[external-secrets]], and how to add, sync, rotate and debug them.

## Key points

- Flow: 1Password, then 1Password Connect, then the External Secrets Operator, then Kubernetes Secrets. All secrets are in the `kubernetes` vault.
- Two exceptions: `op inject` renders the Talos machine secrets and bootstrap secrets (`op://kubernetes/...` references). `CLOUDFLARE_ACCOUNT_ID` and `CLOUDFLARE_TUNNEL_ID` come from the `cluster-secrets` Secret as Flux `${VAR}` substitutions.
- Generated credentials have their own scripts: `kubernetes/apps/default/authelia/app/README.md` (OIDC clients) and `kubernetes/components/cnpg/README.md` (database users).
- Add a secret: make a 1Password item, add an `ExternalSecret` with `ClusterSecretStore` `onepassword`, commit.
- Sync all: `task kubernetes:sync-secrets`. Sync one: annotate the ExternalSecret with `force-sync="$(date +%s)"`.
- Rotate: change the value in 1Password, force a sync, restart the deployment.
- Errors: `item not found`, `field not found`, `connect error` (1Password Connect pod is down).
- Emergency: `kubectl create secret generic` works, but External Secrets overwrites it when it recovers.

## Data and quotes

None.

## Connections

- [[external-secrets]], [[authelia]], [[cloudnative-pg]], [[app-deployment-pattern]].

## Open questions

- None.
