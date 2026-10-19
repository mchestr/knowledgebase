---
title: LiteLLM
type: entity
kind: software
aliases: [litellm-operator, LiteLLMModel]
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, ai]
---

# LiteLLM

## Summary

An OpenAI-compatible LLM proxy in the `ai` namespace. It routes to hosted models on OpenRouter. The cluster has no local GPU inference ([[home-cluster-agents-md]], [[home-cluster-readme]]).

## Facts

- `litellm-operator` from home-operations manages it ([[home-cluster-readme]]).
- Models are `LiteLLMModel` resources in `kubernetes/apps/ai/litellm/app/models/` ([[home-cluster-agents-md]]).
- It uses the `dragonfly` component and sits on `envoy-internal` ([[home-cluster-app-inventory]]).
- [[memini]] uses it for chat ([[home-cluster-agents-md]]).

## Related

- [[in-cluster-ai-stack]].
