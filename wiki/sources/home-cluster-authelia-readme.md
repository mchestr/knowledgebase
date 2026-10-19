---
title: home-cluster Authelia OAuth2 secrets README
type: source
source: raw/2026-10-18-home-cluster-authelia-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/default/authelia/app/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, auth, secrets]
---

# home-cluster Authelia OAuth2 secrets README

## Summary

How to make an OIDC client for a new app in [[authelia]] and store it in 1Password without the values reaching the screen.

## Key points

1. Set `APP` (upper-case prefix) and the Authelia image of the cluster (`authelia/authelia:4.39.28`).
2. Generate the client id with `authelia crypto rand --length 72 --charset rfc3986`.
3. Generate the secret and its argon2 hash with `authelia crypto hash generate argon2 --random --random.length 64`.
4. Stop if the hash does not start with `$argon2id$`.
5. Write `<APP>_OAUTH_CLIENT_ID`, `<APP>_OAUTH_CLIENT_SECRET` and `<APP>_OAUTH_CLIENT_SECRET_HASH` to the `authelia` item in the `kubernetes` vault with `op item edit`.
6. Add the three keys to `externalsecret.yaml`, the client to `resources/configuration.yaml` (Authelia gets the hash, the app gets the plain secret), and an access rule or `authorization_policies` entry.

## Data and quotes

The waitlist README is the full worked example ([[home-cluster-waitlist-readme]]).

## Connections

- [[authelia]], [[external-secrets]], [[security-posture]].

## Open questions

- None.
