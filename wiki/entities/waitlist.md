---
title: Waitlist
type: entity
kind: software
aliases: [Ferry Watch, mchestr/waitlist]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, app, security]
---

# Waitlist

## Summary

The owner's reservation-watcher app (github.com/mchestr/waitlist, formerly Ferry Watch). One dashboard watches BC Ferries trips and Buntzen Lake day passes (alerts only) ([[home-cluster-waitlist-readme]]).

## Facts

- Hosts: `waitlist.chestr.dev` and `waitlist-checkout.chestr.dev`, both on `envoy-external`. Sign-in through [[authelia]] OIDC and the lldap group `waitlist` ([[home-cluster-waitlist-readme]]).
- One browser pod for each watched BC Ferries trip, in `waitlist-browsers`. Three ValidatingAdmissionPolicies admit only the exact pod that waitlist-control builds ([[home-cluster-waitlist-readme]]).
- `waitlist-fetcher` holds no secrets and can reach only `api.yodelpass.com` ([[home-cluster-waitlist-readme]]).
- It is a reference implementation of the external-gateway NetworkPolicy ([[home-cluster-agents-md]], [[home-cluster-networking]]).
- Database `waitlist` on `postgres17`, with login roles `waitlist_web` and `waitlist_control` ([[home-cluster-waitlist-readme]]).
- `app/helmrelease.yaml` is the only copy of its Kubernetes config. The app repository has none ([[home-cluster-waitlist-readme]]).
- Checkout key rotation needs a 26-hour wait between steps ([[home-cluster-waitlist-readme]]).
- Commit `470f9f8` removed the waitlist README from the repository. Its runbooks are in git history at `e36a8c8` ([[home-cluster-waitlist-readme]]).

## Related

- [[security-posture]], [[cloudnative-pg]], [[lldap]].
