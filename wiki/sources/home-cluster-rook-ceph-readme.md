---
title: home-cluster Rook Ceph README
type: source
source: raw/2026-10-18-home-cluster-rook-ceph-readme.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/rook-ceph/rook-ceph/README.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, storage, runbook]
---

# home-cluster Rook Ceph README

## Summary

Rook-Ceph procedures next to the manifests. It says that the same procedures are in [[home-cluster-storage-operations]].

## Key points

- The toolbox pod is disabled. Use `kubectl rook-ceph ceph ...`.
- Remove a dead OSD, clean the Rook directory on a disk, and fix an OSD that fails to join after a disk move. The steps match [[rook-ceph]].
- The disk-clean pod manifest here has no `namespace`. The docs version uses `namespace: rook-ceph`.

## Data and quotes

None.

## Connections

- [[rook-ceph]].

## Open questions

- None.
