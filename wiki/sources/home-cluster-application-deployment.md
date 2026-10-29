---
title: home-cluster docs — Application Deployment
type: source
source: raw/2026-10-28-home-cluster-application-deployment-2d78212.md
previous_sources:
  - raw/2026-10-18-home-cluster-application-deployment-fa79b82.md
  - raw/2026-10-18-home-cluster-application-deployment-eff692f.md
  - raw/2026-10-18-home-cluster-application-deployment.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/docs/src/notes/application-deployment.md
commit: 2d78212
created: 2026-10-18
updated: 2026-10-28
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
- Pull request CI builds every Kustomization with flate, renders the Helm diff and posts a risk assessment.
- Put an app on `envoy-external` only when it has its own login. Give it a NetworkPolicy that admits only that gateway and a CiliumNetworkPolicy that admits the `kube-apiserver` entity. Copy both from `kubernetes/apps/default/radicale/app/helmrelease.yaml`. See [[internal-vs-external-gateway]].
- Manage: `task kubernetes:reconcile`, `flux get hr|ks`, `flux suspend|resume`.

## Data and quotes

> "Renovate automerges minor, patch and digest updates once the risk assessment passes and, where the registry gives a release date, once they are 2 days old"

Version `eff692f` added the 2-day condition to this sentence. Version `fa79b82` changed the policy example from `home-assistant` to `radicale` and added the CiliumNetworkPolicy.

Version `2d78212` changed only the CI tool name, from flux-local to flate.

## Connections

- [[app-deployment-pattern]], [[renovate]], [[external-secrets]], [[envoy-gateway]], [[authelia]].

## Open questions

- None. Version `eff692f` settled the automerge conflict with [[home-cluster-upgrade-procedures]].
