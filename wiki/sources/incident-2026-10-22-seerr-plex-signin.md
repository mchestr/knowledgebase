---
title: Incident 2026-10-22 — Plex user cannot sign in to Seerr
type: source
source: raw/2026-10-22-incident-seerr-plex-signin.md
author: Mike Chester
published: 2026-10-22
url:
created: 2026-10-22
updated: 2026-10-22
tags: [home-cluster, incident, seerr, plex]
---

# Incident 2026-10-22 — Plex user cannot sign in to Seerr

## Summary

A shared Plex user could not sign in to [[seerr]]. The email in the owner's Plex share was wrong. The fix was to share the server again with the correct email. See [[seerr-plex-user-cannot-sign-in]].

## Key points

- Seerr checks each Plex sign-in against the owner's Plex share list.
- The Seerr log line `Failed sign-in attempt by Plex user without access to the media server` names the account that tried to sign in.
- [[plex-manager]] shows the real email and access of each Plex user. See [[look-up-a-plex-user]].
- A `Failed to ping token` 401 error on the same day was a separate fault.

## Data and quotes

- "Error checking user access: This user does not exist on the main Plex account's shared list"
- Seerr Plex settings: hostname `plex.media.svc.cluster.local`, port 32400, no SSL.

## Connections

- [[home-cluster]] runs Seerr, Plex and plex-manager in the `media` namespace.
- Seerr is on the external gateway ([[internal-vs-external-gateway]]) and does its own sign-in.

## Open questions

- What made the Seerr Plex admin token fail with 401 on 2026-10-22?
