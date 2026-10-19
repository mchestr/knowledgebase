---
title: home-cluster Waitlist README
type: source
source: raw/2026-10-18-home-cluster-waitlist-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/waitlist/waitlist/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, waitlist, runbook, security]
---

# home-cluster Waitlist README

## Summary

Operations guide for [[waitlist]], a reservation-watcher app (formerly Ferry Watch) for BC Ferries and Buntzen Lake day passes. It covers the parts, the secrets, the fetcher, key rotation, a security warning, and the runbook that replaced Ferry Watch.

## Key points

- Parts: `waitlist-web` (sign-in with Authelia OIDC, API, dashboard, on `envoy-external` at `waitlist.chestr.dev`), `waitlist-control` (hub, browser pods, Buntzen check loop), `waitlist-fetcher` (only caller of `api.yodelpass.com`), `vnc-edge` (checkout page at `waitlist-checkout.chestr.dev`), `waitlist-db` (Helm hook Job for migrations), one browser pod for each watched trip in `waitlist-browsers`.
- Guard rails in the HelmRelease: quotas, network policies, RBAC, and three ValidatingAdmissionPolicies (`wl-browser-pod`, `wl-browser-pod-lock`, `wl-ns-objects`). Only the exact pod that waitlist-control builds is admitted, and nobody can change or exec into it. Nothing tests these policies against a real API server.
- Outside its folder: an Authelia OIDC client and `waitlist` authorization policy, CNPG login roles `waitlist_web` and `waitlist_control`, an smtp-relay ingress rule, Cilium `dnsProxy.dnsRejectResponseCode`, a Silence, Fluent Bit and descheduler exclusions, a Cloudflare rule that turns off Rocket Loader and email obfuscation (`terraform/cloudflare/rulesets.tf`), and the lldap group `waitlist`.
- The fetcher has no database login, no Secret, no ServiceAccount token and no RBAC. Ingress only from waitlist-control on 8767. Egress only to kube-dns and `api.yodelpass.com:443`, never to private, CGNAT, link-local or loopback addresses (`egressDeny`). One replica with its own rate cap.
- The render fails until the image digests and the public key are set, so flux-local blocks an early merge. A red flux-local also holds back every Renovate automerge.
- Checkout key rotation: add the new public key next to the old one, wait 26 hours (the longest browser pod life), move the new private key into place, then drop the old public key. VAPID key rotation is not covered, because every push subscription depends on it.
- The Ferry Watch replacement runbook has phases 0 (prepare), 1 (merge), S (smoke test), 2 (delete leftovers), and a rollback. `kubernetes/components/common/namespace.yaml` has `kustomize.toolkit.fluxcd.io/prune: disabled`, so Flux leaves namespaces behind.

## Data and quotes

> "An invitee's lldap account is also an account for every other Authelia OIDC client: those want `two_factor`, and anyone with a password can enrol a second factor. Before adding anyone but yourself to lldap, give Autobrr, Grafana, Immich, Paperless and Windmill their own `authorization_policies` limited to the groups that use them"

The old Postgres dumps are on `nebula.chestr.dev:/var/nfs/shared/cluster/apps/postgres-backup-local` ([[home-nas]]).

Authelia image in the runbook: `ghcr.io/authelia/authelia:4.39.28`.

## Connections

- [[waitlist]], [[authelia]], [[lldap]], [[security-posture]], [[cloudnative-pg]], [[cloudflare-terraform]].

## Open questions

- Has the Phase 2 step 8 follow-up (drop the `ensure: absent` Ferry Watch roles) landed?
