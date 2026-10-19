---
title: Authelia
type: entity
kind: software
aliases: []
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, auth]
---

# Authelia

## Summary

SSO and two-factor authentication for the [[home-cluster]]. It guards every app on the internal gateway and is an OIDC provider for apps on the external gateway. lldap is its user directory ([[home-cluster-readme]]).

## Facts

- [[envoy-gateway]] asks Authelia about each request on `envoy-internal` through the `internal-secure` SecurityPolicy ([[home-cluster-networking]]).
- It fails closed. If Authelia is down, internal apps are unreachable. The `AutheliaDown` alert reports this ([[home-cluster-networking]]).
- Access rules are in `kubernetes/apps/default/authelia/app/resources/configuration.yaml` ([[home-cluster-networking]]):
  - two-factor for the `admin` group;
  - one-factor for the `media` group on the *arr apps;
  - `bypass` for apps with their own login;
  - deny for all other requests.
- Authelia itself is on the external gateway ([[home-cluster-networking]]).
- OIDC client secrets are generated with the script in `kubernetes/apps/default/authelia/app/README.md` ([[home-cluster-secrets-management]]).

## Related

- [[internal-vs-external-gateway]].
