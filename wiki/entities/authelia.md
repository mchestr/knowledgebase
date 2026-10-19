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
- Authelia itself is on the external gateway, with no NetworkPolicy in its app path ([[home-cluster-networking]], [[home-cluster-app-inventory]]).
- Image `authelia/authelia:4.39.28`. It uses the `cnpg` and `dragonfly` components and depends on [[lldap]] and smtp-relay ([[home-cluster-app-inventory]]).
- [[memini]] `/v1` and `/mcp` bypass Authelia ([[home-cluster-agents-md]]).
- Authelia enables an OIDC client only when its fields reach `authelia-secret`. A missing field disables sign-in to that app, not Authelia ([[home-cluster-waitlist-readme]]).
- OIDC client secrets are generated with the script in `kubernetes/apps/default/authelia/app/README.md` ([[home-cluster-secrets-management]]). See [[home-cluster-authelia-readme]] for the steps.

WARNING: Any [[lldap]] account can use every OIDC client that has no group-limited `authorization_policies`. Limit Autobrr, Grafana, Immich, Paperless and Windmill before you add a second user ([[home-cluster-waitlist-readme]]).

## Related

- [[internal-vs-external-gateway]], [[security-posture]].
