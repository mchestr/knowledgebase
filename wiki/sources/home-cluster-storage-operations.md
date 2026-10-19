---
title: home-cluster docs — Storage Operations
type: source
source: raw/2026-10-18-home-cluster-storage-operations.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2ce9069c102d7eda4c430078c05a2c400befe730/docs/src/notes/storage-operations.md
commit: 2ce9069
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, storage, runbook]
---

# home-cluster docs — Storage Operations

## Summary

Procedures for [[rook-ceph]]: health checks, dead OSD removal, disk cleaning, OSD keyring repair, PVC browsing and maintenance mode.

## Key points

- The Rook toolbox pod is disabled. Run `ceph` through the `rook-ceph` kubectl plugin: `kubectl rook-ceph ceph status`.
- Remove a dead OSD: scale `rook-ceph-osd-<ID>` to 0, `ceph osd purge <ID> --yes-i-really-mean-it`, `ceph auth del osd.<ID>`, and `ceph osd crush remove <nodename>` when you retire the node.
- Clean a used disk with a privileged busybox pod that deletes `/var/lib/rook` on the node.
- An OSD that does not join after a disk moves to another node: get the keyring with `kubectl rook-ceph debug start`, write an `osd.export` file with the OSD caps, and import it with `ceph auth import`.
- Browse a PVC: `task kubernetes:browse-pvc NS=media CLAIM=plex`. Volume names match the app name. Cache volumes are `<app>-cache`.
- Maintenance mode: `ceph osd set noout`, then `ceph osd unset noout` after the work.

## Data and quotes

The OSD removal procedure comes from the Mirantis docs. The keyring fix comes from rook/rook issue 4238.

## Connections

- [[rook-ceph]], [[volsync]], [[node-failure-runbook]].

## Open questions

- None.
