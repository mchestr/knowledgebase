---
title: home-cluster docs — Application Deployment
type: source
source: raw/2026-10-18-home-cluster-application-deployment.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/application-deployment.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, flux, runbook]
---

# home-cluster docs — Application Deployment

## Summary

How to add an app to the [[home-cluster]] with [[flux]]: the repository layout, the Flux Kustomization, the reusable components, the HelmRelease rules, secrets, and gateway choice. See [[app-deployment-pattern]].

## Key points

- Layout: `kubernetes/flux/cluster/ks.yaml` is the entry point. `kubernetes/components/` has the `common`, `volsync`, `cnpg` and `dragonfly` components. `kubernetes/apps/<namespace>/<app>/` has `ks.yaml` and `app/`.
- `ks.yaml` lives in the app namespace and uses `targetNamespace`. `dependsOn` lists `onepassword-store` (for an ExternalSecret), `rook-ceph-cluster` (for a PVC) or `cloudnative-pg-cluster` (for a database).
- Components:
  - `volsync`: PVC `${APP}` and a restic backup to R2 ([[volsync]]). `APP_UID`/`APP_GID` must match the container user.
  - `cnpg`: a database on the [[cloudnative-pg]] cluster (`CNPG_NAME` default `postgres17`), user and initdb secrets, and a backup CronJob.
  - `dragonfly`: a Redis-compatible instance `${APP}-dragonfly`.
- HelmRelease rules (shared `app-template` chart): real health probes, non-root pod with fixed UID/GID, read-only root filesystem, all capabilities dropped, a CPU request and a memory limit, secrets with `envFrom` plus `reloader.stakater.com/auto: "true"`, routes on `envoy-internal` by default.
- `kubernetes/flux/cluster/ks.yaml` patches every HelmRelease to roll back a failed upgrade. Apps with database migrations set `upgrade.strategy.name: RetryOnFailure`.
- Add `./<app>/ks.yaml` to the namespace `kustomization.yaml`. New namespace folders are found automatically.
- Pull request CI builds every Kustomization with flux-local, renders the Helm diff and posts a risk assessment.
- Put an app on `envoy-external` only when it has its own login. Give it a NetworkPolicy that admits only that gateway. See [[internal-vs-external-gateway]].
- Manage: `task kubernetes:reconcile`, `flux get hr|ks`, `flux suspend|resume`.

## Data and quotes

> "Renovate automerges minor, patch and digest updates once the risk assessment passes"

## Connections

- [[app-deployment-pattern]], [[renovate]], [[external-secrets]], [[envoy-gateway]], [[authelia]].

## Open questions

- The automerge rule here does not mention the 2-day wait in [[home-cluster-upgrade-procedures]]. See [[renovate]].
