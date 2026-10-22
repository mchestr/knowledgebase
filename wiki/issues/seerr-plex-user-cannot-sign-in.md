---
title: Seerr — Plex user cannot sign in
type: issue
aliases: [requests sign-in fails, seerr login loop]
systems: [seerr, plex, plex-manager]
created: 2026-10-22
updated: 2026-10-22
tags: [home-cluster, media, auth]
---

# Seerr — Plex user cannot sign in

## Symptom

A user signs in to `requests.chestr.dev` with Plex. [[seerr]] shows the sign-in page again, or shows an access error ([[incident-2026-10-22-seerr-plex-signin]]).

## Cause

Seerr checks each Plex sign-in against the Plex share list of the owner account. Seerr refuses the user when:

| Cause | Log line |
| --- | --- |
| The email in the Plex share is wrong | `This user does not exist on the main Plex account's shared list` |
| The user is not on the share list | `This user does not exist on the main Plex account's shared list` |
| The Seerr Plex admin token is bad, so Seerr cannot read the list | `[Plex Refresh Token]: Failed to ping token` with status 401 |

## Check

1. Read the Seerr log for sign-in errors:

   ```bash
   kubectl -n media logs deploy/jellyseerr --since=24h | grep -i "sign-in\|user access\|refresh token"
   ```

2. Find the line `Failed sign-in attempt by Plex user without access to the media server`.
3. Note its `plexUsername` and `email` fields. Do not copy them into Git, an issue or the wiki.
4. Look up the user in plex-manager. Do the steps in [[look-up-a-plex-user]].
5. Compare the email in plex-manager with the `email` in the Seerr log.
6. Check that plex-manager shows Plex access for the user.
7. Look for a `Failed to ping token` line with status 401.

## Fix

| Result of the check | Fix |
| --- | --- |
| The emails are different | Share the Plex server again with the email of the user's Plex account. |
| The user has no Plex access | Share the Plex server with the user. |
| The token error is in the log | Sign in to Plex again in Seerr Settings → Plex. |

1. Tell the user to accept the Plex invite.
2. In Seerr, open Settings → Users and select "Import Plex Users".
3. Tell the user to sign in again.
4. Read the Seerr log again. Make sure that there is no new failed attempt.

## Prevention

- Share the Plex server with the email of the user's Plex account, not another email of the user.
- Watch the Seerr log for `Failed to ping token` errors.

## Related

- [[look-up-a-plex-user]]
- [[plex-manager]]
- [[seerr]]
