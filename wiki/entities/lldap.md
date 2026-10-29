---
title: lldap
type: entity
kind: software
aliases: [LLDAP]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, auth]
---

# lldap

## Summary

A light LDAP server. It is the user directory for [[authelia]] in the [[home-cluster]] ([[home-cluster-readme]]).

## Facts

- Groups decide access: `admin`, `media`, `waitlist` and others ([[home-cluster-networking]], [[home-cluster-waitlist-readme]]).
- Groups are made in the lldap UI, not in Git ([[home-cluster-waitlist-readme]]).
- Authelia `dependsOn` lldap ([[home-cluster-app-inventory]]).

WARNING: An lldap account can sign in to every Authelia OIDC client that has no group-limited `authorization_policies`. Before you add another user, limit Autobrr, Grafana, Immich and Paperless ([[home-cluster-waitlist-readme]]). The source also named Windmill. The inventory at `2d78212` has no Windmill ([[home-cluster-app-inventory]]).

## Related

- [[security-posture]].
