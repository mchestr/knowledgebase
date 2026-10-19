---
title: Overview
type: overview
created: 2026-10-18
updated: 2026-10-18
tags: []
---

# Overview

The knowledge base has one subject so far: the [[home-cluster]], a three-node Kubernetes cluster at home. The sources are its README, its operations docs, `AGENTS.md`, its component READMEs, its Claude agent files, and a generated app inventory ([[app-inventory]]), up to commit `e36a8c8`.

## Main themes

- **GitOps for everything that can be in Git.** [[flux]] applies the repository. [[renovate]] and [[tuppr]] turn upgrades into merged PRs. See [[gitops]].
- **Two trust zones for apps.** `envoy-internal` with [[authelia]] for LAN apps, `envoy-external` through the [[cloudflare-tunnel]] for apps with their own login. See [[internal-vs-external-gateway]].
- **Layered backups.** Git, 1Password, [[volsync]] to R2, and [[cloudnative-pg]] to R2 and the NAS. Postgres is the only state that needs manual recovery. See [[backup-strategy]].
- **Safe automation gates.** tuppr waits for Ceph health and idle backups. Helm rolls back on failed probes. Renovate merges only low-risk updates.
- **AI as an operator.** An AI agent rates each PR before automerge ([[renovate-risk-review]]). An in-cluster Claude Code server can fix the cluster from claude.ai/code or the Claude app ([[claude-code-remote-control]]). See [[in-cluster-ai-stack]].
- **Security posture.** Gateway choice plus a NetworkPolicy for each external app. Coverage is not complete. See [[security-posture]].
- **Runbooks.** [[triage-runbook]], [[node-failure-runbook]], [[complete-cluster-loss-runbook]], [[app-deployment-pattern]].

## Open questions

- When will the CNPG Clusters move from `barmanObjectStore` to the Barman Cloud Plugin? See [[cloudnative-pg]].
- Six external apps have no NetworkPolicy, and `home-assistant` lacks the `kube-apiserver` rule. Are these planned? See [[security-posture]].
- Which page is right about the reference policy: the docs (`home-assistant`) or AGENTS.md (`radicale`)? The code agrees with AGENTS.md. See [[internal-vs-external-gateway]].
- Do Autobrr, Grafana, Immich, Paperless and Windmill have group-limited `authorization_policies` yet? See [[lldap]].
