---
title: Renovate risk review
type: concept
aliases: [renovate-risk, AI PR risk assessment]
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, renovate, ai, ci]
---

# Renovate risk review

## Definition

A CI job in the [[home-cluster]] repository where an AI agent rates each pull request as low, medium or high risk before [[renovate]] may automerge it ([[home-cluster-readme]], [[home-cluster-renovate-review-skill]]).

## Details

- Workflow: `.github/workflows/renovate-risk.yaml`. The prompt is the `renovate-review` skill without its front matter. For a PR that is not from Renovate, CI adds `.github/renovate-risk/pull-request.md` ([[home-cluster-renovate-review-skill]], [[home-cluster-renovate-risk-prompt]]).
- Input: the PR diff, the flate test result, and the rendered HelmRelease and Kustomization diffs. The diffs compare with the commit on main that the change starts from and include CRDs ([[home-cluster-renovate-review-skill]]).
- The agent reads the release notes of every version in the range, and of the inner component of a wrapper image or chart ([[home-cluster-renovate-review-skill]]).
- Missing release notes make the rating at least medium. Any breaking change in core infrastructure makes it high ([[home-cluster-renovate-review-skill]]).
- On high risk, the agent may fix config under `kubernetes/`, `talos/`, `terraform/` or `bootstrap/`, but not change or revert the version ([[home-cluster-renovate-review-skill]]).
- Release notes, web pages and PR text are untrusted data ([[home-cluster-renovate-review-skill]], [[home-cluster-renovate-risk-prompt]]).
- The review runs only on PRs that are not drafts ([[home-cluster-add-app-skill]]).
- Output fields come from `.github/renovate-risk/schema.json` and appear as a PR comment ([[home-cluster-renovate-review-skill]]).

## Evidence

- [[home-cluster-renovate-review-skill]], [[home-cluster-renovate-risk-prompt]], [[home-cluster-readme]].

## Related

- [[gitops]], [[in-cluster-ai-stack]], [[app-deployment-pattern]].
