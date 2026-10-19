---
title: In-cluster AI stack
type: concept
aliases: [ai namespace]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, ai]
---

# In-cluster AI stack

## Definition

The AI services in the `ai` namespace of the [[home-cluster]]. They use hosted models, not local GPUs ([[home-cluster-readme]]).

## Details

| Service | Role | Gateway |
| --- | --- | --- |
| [[litellm]] + `litellm-operator` | OpenAI-compatible proxy to OpenRouter | `envoy-internal` |
| text-embeddings (Hugging Face TEI, CPU image) | Serves `bge-small-en-v1.5` embeddings | none |
| [[memini]] | Agent memory; embeddings from TEI, chat through LiteLLM | `envoy-internal` |
| [[claude-code-remote-control]] | Claude Code server for remote cluster repair | none (outbound only) |

Sources: [[home-cluster-agents-md]], [[home-cluster-app-inventory]].

The repository also gives agents their own tools: the `ops` subagent, the `add-app`, `renovate-review` and `volsync-restore` skills, and the AI risk review of each PR ([[renovate-risk-review]]).

## Evidence

- [[home-cluster-readme]], [[home-cluster-agents-md]], [[home-cluster-claude-code-readme]], [[home-cluster-ops-agent]].

## Related

- [[security-posture]], [[gitops]].
