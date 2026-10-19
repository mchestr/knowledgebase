---
title: Overview
type: overview
created: 2026-10-18
updated: 2026-10-18
tags: []
---

# Overview

The knowledge base has one subject so far: the [[home-cluster]], a three-node Kubernetes cluster at home. The sources are its README and its operations docs at commit `2ce9069`.

## Main themes

- **GitOps for everything that can be in Git.** [[flux]] applies the repository. [[renovate]] and [[tuppr]] turn upgrades into merged PRs. See [[gitops]].
- **Two trust zones for apps.** `envoy-internal` with [[authelia]] for LAN apps, `envoy-external` through the [[cloudflare-tunnel]] for apps with their own login. See [[internal-vs-external-gateway]].
- **Layered backups.** Git, 1Password, [[volsync]] to R2, and [[cloudnative-pg]] to R2 and the NAS. Postgres is the only state that needs manual recovery. See [[backup-strategy]].
- **Safe automation gates.** tuppr waits for Ceph health and idle backups. Helm rolls back on failed probes. Renovate merges only low-risk updates.
- **Runbooks.** [[triage-runbook]], [[node-failure-runbook]], [[complete-cluster-loss-runbook]], [[app-deployment-pattern]].

## Open questions

- When will the CNPG Clusters move from `barmanObjectStore` to the Barman Cloud Plugin? See [[cloudnative-pg]].
- Which external apps still need the gateway NetworkPolicy? See [[internal-vs-external-gateway]].
