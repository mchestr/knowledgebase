---
title: memini
type: entity
kind: software
aliases: []
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, ai]
---

# memini

## Summary

Persistent memory for AI agents (eleboucher/memini), at `memini.chestr.dev` in the `ai` namespace ([[home-cluster-readme]], [[home-cluster-agents-md]]).

## Facts

- Vectors come from the in-cluster text-embeddings service. Chat goes through [[litellm]] ([[home-cluster-agents-md]]).
- The `/v1` and `/mcp` paths bypass [[authelia]], because memini's own API key protects them ([[home-cluster-agents-md]]).
- It is on `envoy-internal`, with the `volsync` component ([[home-cluster-app-inventory]]).

## Related

- [[in-cluster-ai-stack]], [[security-posture]].
