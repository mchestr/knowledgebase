# Incident: a Plex user cannot sign in to Seerr

Date: 2026-10-22
Systems: home-cluster, Seerr (media/jellyseerr, requests.chestr.dev, image ghcr.io/seerr-team/seerr v3.5.1), Plex (media/plex), plex-manager (media/subs, subs.chestr.dev)

## Symptom

A shared Plex user signed in to requests.chestr.dev with Plex. Seerr showed the sign-in page again.

## Evidence

The Seerr log had these lines for each attempt:

- `[error]: Error checking user access: This user does not exist on the main Plex account's shared list`
- `[warn][API]: Failed sign-in attempt by Plex user without access to the media server` with the fields `ip`, `email`, `plexId` and `plexUsername`.

The same day, Seerr also logged `[Plex Refresh Token]: Failed to ping token` with status code 401.

## Cause

The email of the user in the owner's Plex share (Plex Settings → Manage → Users & Sharing) was wrong. Seerr compares the Plex account that signs in with the share list of the owner account. The account did not match, so Seerr refused it.

The 401 token error was a separate fault. It did not cause this sign-in failure.

## Fix

The owner shared the Plex server again with the correct email.

## Lessons

- The `email` and `plexUsername` fields in the Seerr log show the account that tried to sign in.
- plex-manager (Admin → Users) shows each Plex user's real email, Plex username and server access. Use it to compare with the Seerr log.
- Seerr's Plex hostname setting `plex.media.svc.cluster.local`, port 32400, no SSL, is correct. The hostname does not affect the access check, because Seerr asks plex.tv for the share list.
- Do not record user names, emails or IDs in Git or the wiki.
