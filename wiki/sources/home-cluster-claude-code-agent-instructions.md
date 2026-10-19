---
title: home-cluster claude-code agent instructions
type: source
source: raw/2026-10-18-home-cluster-claude-code-agent-instructions.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/e36a8c83c6e8a21f1dfffbb167aee922365a2917/kubernetes/apps/ai/claude-code/app/resources/CLAUDE.md
commit: e36a8c8
created: 2026-10-18
updated: 2026-10-18
tags: [home-cluster, ai, claude-code]
---

# home-cluster claude-code agent instructions

## Summary

The `CLAUDE.md` mounted into the in-cluster Claude Code server ([[claude-code-remote-control]]). It sets one rule set: write in ASD-STE100 Simplified Technical English.

## Key points

- Instructions as numbered lists in command form, one instruction for each step.
- At most 20 words in an instruction and 25 words in a description.
- Active voice, one name for one thing, simple words (not: utilize, ensure, facilitate, leverage, commence, terminate).
- Warnings before the step, starting with "WARNING:".
- No introduction, praise or summary. At most 6 sentences in a paragraph.
- Keep every fact, value and safety step.

## Data and quotes

The same rules explain the style of the repository's newer docs and skills, for example [[home-cluster-volsync-restore-skill]] and the node failure steps in [[home-cluster-disaster-recovery]].

## Connections

- [[claude-code-remote-control]].

## Open questions

- None.
