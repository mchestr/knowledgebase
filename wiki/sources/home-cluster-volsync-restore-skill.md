---
title: home-cluster volsync-restore skill
type: source
source: raw/2026-10-18-home-cluster-volsync-restore-skill.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/.claude/skills/volsync-restore/SKILL.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, backup, agents, runbook]
---

# home-cluster volsync-restore skill

## Summary

A Claude Code skill that restores an app PVC from a [[volsync]] snapshot and checks the data. It adds safety checks to the restore in [[home-cluster-disaster-recovery]].

## Key points

- Retention: 7 daily, 4 weekly and 3 monthly snapshots. Tasks are in `.taskfiles/volsync/Taskfile.yml`.
- Pre-checks: the four VolSync assumptions; the ReplicationSource exists; the `volsync` deployment in `volsync-system` has replicas; `flux`, `kubectl` and `minijinja-cli` are installed; `KUBECONFIG` is set.
- `volsync:list` shows the oldest snapshot first. Count `PREVIOUS` back from the last line.
- Run the restore as a background command. It waits up to 2 hours.
- To start an app after a failed restore: `flux resume ks`, `flux resume hr`, then `flux reconcile hr --force`.
- Check: Flux objects ready, pods ready, logs show no "no data" start, files present at the mount path, the owner confirms the data.

## Data and quotes

> "WARNING: Do not run `task volsync:snapshot` before the restore. A new snapshot changes the `PREVIOUS` count. The retention keeps one snapshot for each day, so it can remove a good snapshot from the same day."

> "WARNING: The restore replaces the data on the PVC. It deletes the files that are not in the snapshot."

> "WARNING: Do not start the app while a restore Job still writes to the PVC."

## Connections

- [[volsync]], [[backup-strategy]].

## Open questions

- None.
