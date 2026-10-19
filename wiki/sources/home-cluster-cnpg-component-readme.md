---
title: home-cluster cnpg component README
type: source
source: raw/2026-10-18-home-cluster-cnpg-component-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/components/cnpg/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, database, secrets]
---

# home-cluster cnpg component README

## Summary

How to make the database credentials for an app that uses the `cnpg` component ([[cloudnative-pg]]).

## Key points

1. Set `APP`, for example `sonarr`.
2. Generate a 20-character password with `op item create --category password --generate-password=letters,digits,20 --dry-run`.
3. Write `<APP>_postgres_username` (= the app name) and `<APP>_postgres_password` to the `cloudnative-pg` 1Password item.

## Data and quotes

Unlike [[home-cluster-authelia-readme]], this script holds the password in a shell variable.

## Connections

- [[cloudnative-pg]], [[external-secrets]], [[app-deployment-pattern]].

## Open questions

- None.
