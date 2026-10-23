---
title: Seerr
type: entity
kind: application
aliases: [jellyseerr, overseerr, requests]
created: 2026-10-22
updated: 2026-10-22
tags: [home-cluster, media, plex]
---

# Seerr

## Summary

Media request app at `requests.chestr.dev`. It runs as the `jellyseerr` HelmRelease in the `media` namespace of [[home-cluster]] ([[incident-2026-10-22-seerr-plex-signin]]).

## Facts

- Image: `ghcr.io/seerr-team/seerr`, v3.5.1 on 2026-10-22.
- Gateway: `envoy-external`. Seerr does its own sign-in with Plex ([[internal-vs-external-gateway]]).
- Plex connection: hostname `plex.media.svc.cluster.local`, port 32400, no SSL.
- A Plex user can sign in only when the user is on the owner's Plex share list. See [[seerr-plex-user-cannot-sign-in]].
- [[plex-manager]] calls the Seerr (Overseerr) API.

## Timeline

- 2026-10-22: Upgrade from v3.5.0 to v3.5.1. A shared user could not sign in because of a wrong share email.

## Related

- [[plex-manager]]
- [[look-up-a-plex-user]]
