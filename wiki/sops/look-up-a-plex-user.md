---
title: Look up a Plex user
type: sop
aliases: [find plex user email]
systems: [plex-manager, plex]
created: 2026-10-22
updated: 2026-10-22
tags: [home-cluster, media, plex]
---

# Look up a Plex user

## Purpose

Find the real email, Plex username and server access of a Plex user. Use [[plex-manager]] as the source of truth, not memory, chat or notes ([[incident-2026-10-22-seerr-plex-signin]]).

## When to use

- A user cannot sign in to an app that uses Plex sign-in, for example [[seerr]].
- You must compare a log entry with a real Plex account.
- You must find out if a user still has access to the Plex server.

## Before you start

- You need an admin account in plex-manager at `subs.chestr.dev`.

WARNING: Do not copy names, emails, usernames or account IDs into Git, issues, the wiki or agent memory. Write "the user" instead.

## Procedure

1. Open `subs.chestr.dev` and sign in as an admin.
2. Open Admin → Users.
3. Select "Import Plex Users". This reads the current user list from the Plex server.
4. Search for the user by name, email or Plex username.
5. Open the user.
6. Read the email, the Plex username and the Plex access status.

## Verify

1. Compare the values with the log entry or the report.
2. If the user is missing, open Plex Settings → Manage → Users & Sharing as the owner. Look for the user there.

## Related

- [[seerr-plex-user-cannot-sign-in]]
- [[plex-manager]]
