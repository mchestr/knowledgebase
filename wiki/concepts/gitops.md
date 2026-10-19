---
title: GitOps
type: concept
aliases: []
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, gitops]
---

# GitOps

## Definition

A way to run a system where Git holds the desired state and a controller in the system makes the live state match it. In the [[home-cluster]], [[flux]] is the controller and the `kubernetes/` folder is the desired state ([[home-cluster-readme]]).

## Details

- A change is a commit. Pull request CI builds each Kustomization with flux-local and posts a risk assessment of the rendered diff ([[home-cluster-application-deployment]]).
- An AI agent rates each PR before automerge ([[renovate-risk-review]]).
- A version bump is a [[renovate]] PR. Merging a [[tuppr]] version PR is the Talos or Kubernetes upgrade ([[home-cluster-upgrade-procedures]]).
- Recovery from a deleted resource is a reconcile: `task kubernetes:reconcile` ([[home-cluster-disaster-recovery]]).
- Rollback is `git revert`, except for apps with database migrations ([[home-cluster-upgrade-procedures]]).
- Git does not hold everything. Secrets are in 1Password ([[external-secrets]]). PVC data is in R2 ([[volsync]]). Postgres data is in R2 and needs manual recovery steps ([[cloudnative-pg]]). UDM firewall rules are outside the repository ([[home-cluster-networking]]).

## Evidence

- [[home-cluster-readme]], [[home-cluster-application-deployment]], [[home-cluster-disaster-recovery]].

## Related

- [[app-deployment-pattern]], [[backup-strategy]].
