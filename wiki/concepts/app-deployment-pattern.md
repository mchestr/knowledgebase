---
title: App deployment pattern
type: concept
aliases: [new app checklist, app-template]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, flux, runbook]
---

# App deployment pattern

## Definition

The standard files and rules for an app in the [[home-cluster]]. Each app has a [[flux]] Kustomization, a HelmRelease on the shared `app-template` chart, and optional components for storage, backups and databases ([[home-cluster-application-deployment]]).

## Details

Files in `kubernetes/apps/<namespace>/<app>/`:

```
ks.yaml                    Flux Kustomization: dependsOn, components, postBuild vars
app/kustomization.yaml     Lists the files below
app/helmrelease.yaml
app/externalsecret.yaml    If needed
app/resources/             Config files mounted from ConfigMaps
```

`dependsOn` values: `onepassword-store` (ExternalSecret), `rook-ceph-cluster` (PVC), `cloudnative-pg-cluster` (database).

Components: `volsync` ([[volsync]]), `cnpg` ([[cloudnative-pg]]), `dragonfly` (Redis-compatible store, with a NetworkPolicy and a PodMonitor; use `DRAGONFLY_REPLICAS: 3` to survive a node reboot) ([[home-cluster-agents-md]]).

## Add an app

1. Write `ks.yaml`. Set `targetNamespace`, `dependsOn`, `components` and `postBuild.substitute` (`APP`, and `VOLSYNC_CAPACITY` if needed).
2. Write `helmrelease.yaml` with `chartRef` `OCIRepository/app-template`.
3. Add liveness and readiness probes on a real health endpoint. Helm rollback works only when probes fail.
4. Set `runAsNonRoot` with a fixed UID/GID. Set `allowPrivilegeEscalation: false`, `readOnlyRootFilesystem: true`, `capabilities.drop: [ALL]`.
5. Set a CPU request and a memory limit.
6. Load secrets with `envFrom.secretRef`. Add `reloader.stakater.com/auto: "true"` on the controller.
7. Add a `route`. Use `envoy-internal` unless [[internal-vs-external-gateway]] says otherwise.
8. If the app runs database migrations, set `upgrade.strategy.name: RetryOnFailure`.
9. Make the 1Password item and the `ExternalSecret` ([[external-secrets]]).
10. List the files in `app/kustomization.yaml`.
11. Add `./<app>/ks.yaml` to `kubernetes/apps/<namespace>/kustomization.yaml`.
12. Build it as Flux does: `flux build kustomization <app> --namespace <ns> --path ./kubernetes/apps/<ns>/<app>/app --kustomization-file ./kubernetes/apps/<ns>/<app>/ks.yaml --dry-run` ([[home-cluster-add-app-skill]]).
13. Commit as `feat(<app>): add <app>` and open a PR. CI builds it with flate (Flate Test), posts the Flux Diff comment, and runs the [[renovate-risk-review]] when the PR is not a draft ([[home-cluster-add-app-skill]]).
14. After the merge, run `task kubernetes:reconcile` to apply it sooner.

The `add-app` skill does these steps for an agent. Its reference app is `kubernetes/apps/media/tautulli` ([[home-cluster-add-app-skill]]).

Source: [[home-cluster-application-deployment]].

## Evidence

- [[home-cluster-application-deployment]], [[home-cluster-upgrade-procedures]].

## Related

- [[gitops]], [[renovate]].
