---
title: External Secrets Operator
type: entity
kind: software
aliases: [ESO, ExternalSecret, 1Password Connect, onepassword]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, secrets]
---

# External Secrets Operator

## Summary

Copies secrets from 1Password into Kubernetes Secrets through 1Password Connect. All secrets are in the 1Password `kubernetes` vault ([[home-cluster-secrets-management]]).

## Facts

- `ClusterSecretStore` name: `onepassword`. Apps with an ExternalSecret depend on the `onepassword-store` Kustomization in `external-secrets` ([[home-cluster-application-deployment]]).
- Bootstrap installs it before [[flux]] ([[home-cluster-bootstrap]]).
- Outside this flow: Talos and bootstrap secrets (`op inject`), and `cluster-secrets` substitutions ([[home-cluster-secrets-management]]).
- Pods restart on a secret change through `reloader.stakater.com/auto: "true"` ([[app-deployment-pattern]]).

## Procedures

Add a secret ([[home-cluster-secrets-management]]):

1. Make a 1Password item with the needed fields.
2. Add an `ExternalSecret` with `secretStoreRef` `ClusterSecretStore/onepassword`. Use `dataFrom.extract` for all fields or `data.remoteRef.property` for one field.
3. Commit. Check with `kubectl get externalsecret -n <ns> <name>`.

Rotate a secret ([[home-cluster-secrets-management]]):

1. Change the value in 1Password.
2. Force a sync: `kubectl -n <ns> annotate externalsecret <name> force-sync="$(date +%s)" --overwrite`.
3. Restart the app: `kubectl rollout restart deployment -n <ns> <deployment>`.

Sync all secrets: `task kubernetes:sync-secrets`.

## Errors

| Error | Cause | Fix |
| --- | --- | --- |
| `item not found` | No item in 1Password | Make the item |
| `field not found` | No such field | Add the field |
| `connect error` | 1Password Connect is down | Check the `onepassword` pod in `external-secrets` |

## Related

- [[app-deployment-pattern]].
