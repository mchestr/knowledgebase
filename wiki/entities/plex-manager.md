---
title: plex-manager
type: entity
kind: application
aliases: [subs, plex wrapped]
created: 2026-10-22
updated: 2026-10-22
tags: [home-cluster, media, plex]
---

# plex-manager

## Summary

The owner's Plex companion app (`github.com/mchestr/plex-manager`). It runs as the `subs` app in the `media` namespace of [[home-cluster]] at `subs.chestr.dev` and `wrapped.chestr.dev` ([[incident-2026-10-22-seerr-plex-signin]]).

## Facts

- Image: `ghcr.io/mchestr/plex-manager`.
- Admin → Users lists each Plex user with email, Plex username and Plex access. "Import Plex Users" reads the list from the Plex server.
- It is the place to look up the real details of a Plex user. See [[look-up-a-plex-user]].
- It also handles onboarding, Plex Wrapped, subscriptions and the Plex watchlist sync to [[seerr]].

## Timeline

- 2026-10-22: Made the standard tool to look up Plex users.

## Related

- [[seerr]]
- [[seerr-plex-user-cannot-sign-in]]
