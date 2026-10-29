---
title: home-cluster claude-code agent instructions
type: source
source: raw/2026-10-28-home-cluster-claude-code-agent-instructions-2d78212.md
previous_sources:
  - raw/2026-10-18-home-cluster-claude-code-agent-instructions.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/2d78212a4670e1ee96dd9d496cc41aa59f9c9d9b/kubernetes/apps/ai/claude-code/app/resources/CLAUDE.md
commit: 2d78212
created: 2026-10-18
updated: 2026-10-28
tags: [home-cluster, ai, claude-code]
---

# home-cluster claude-code agent instructions

## Summary

The `CLAUDE.md` mounted into the in-cluster Claude Code server ([[claude-code-remote-control]]). It sets two rule sets: write in ASD-STE100 Simplified Technical English, and use this knowledge base.

## Key points

- Instructions as numbered lists in command form, one instruction for each step.
- At most 20 words in an instruction and 25 words in a description.
- Active voice, one name for one thing, simple words (not: utilize, ensure, facilitate, leverage, commence, terminate).
- Warnings before the step, starting with "WARNING:".
- No introduction, praise or summary. At most 6 sentences in a paragraph.
- Keep every fact, value and safety step.
- Knowledge base: read `~/knowledgebase/wiki/index.md` before troubleshooting. Use `wiki/issues/` and `wiki/sops/` first. Offer to record a new fix as an issue or SOP under this wiki's `CLAUDE.md` rules. Record no personal information.

## Data and quotes

The same rules explain the style of the repository's newer docs and skills, for example [[home-cluster-volsync-restore-skill]] and the node failure steps in [[home-cluster-disaster-recovery]].

Version `2d78212` added the knowledge base rules.

## Connections

- [[claude-code-remote-control]].

## Open questions

- None.
