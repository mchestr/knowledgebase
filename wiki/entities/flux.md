---
title: Flux
type: entity
kind: software
aliases: [FluxCD, flux2]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, gitops]
---

# Flux

## Summary

The GitOps controller of the [[home-cluster]]. It watches the `kubernetes/` folder and applies it to the cluster ([[home-cluster-readme]], [[gitops]]).

## Facts

- Bootstrap installs Flux last, after [[cilium]], CoreDNS, cert-manager, [[external-secrets]], kubelet-csr-approver and spegel ([[home-cluster-bootstrap]]).
- Entry point: `kubernetes/flux/cluster/ks.yaml`. It loads `kubernetes/flux/meta/`, then each namespace under `kubernetes/apps/` ([[home-cluster-application-deployment]]).
- That entry point also patches every HelmRelease to roll back a failed upgrade and to replace chart CRDs on every upgrade. The Helm timeout is 5 minutes ([[home-cluster-application-deployment]], [[home-cluster-agents-md]]).
- `kubernetes/components/common/namespace.yaml` has `kustomize.toolkit.fluxcd.io/prune: disabled`, so Flux never deletes a namespace ([[home-cluster-waitlist-readme]]).
- CI: `flux-local` validates and `flux-diff` posts the diff on each PR that touches `kubernetes/**` ([[home-cluster-agents-md]]).
- `cluster-secrets` supplies `${VAR}` substitutions such as `CLOUDFLARE_ACCOUNT_ID` ([[home-cluster-secrets-management]]).
- Most apps use the shared `app-template` chart through `chartRef` ([[app-deployment-pattern]]).
- An `OCIRepository` whose registry denies the pull stays `Ready=False`, and CI fails to render its chart on every branch. See [[oci-chart-pull-denied]] ([[incident-2026-10-28-fluent-bit-chart-mirror-403]]).

## Commands

| Task | Command |
| --- | --- |
| Reconcile all | `task kubernetes:reconcile` |
| Status | `flux get hr -n <ns> <app>`, `flux get ks -n <ns> <app>` |
| Failed objects | `flux get all -A \| grep -i false` |
| Restart failed releases | `task kubernetes:hr:restart` |
| Pause | `flux suspend ks\|hr -n <ns> <app>` |
| Force a release | `flux reconcile hr -n <ns> <app> --force` |

## Related

- [[renovate]], [[app-deployment-pattern]].
