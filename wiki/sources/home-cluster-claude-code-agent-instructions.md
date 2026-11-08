---
title: home-cluster claude-code agent instructions
type: source
source: raw/2026-11-08-home-cluster-claude-code-agent-instructions-924c31d.md
previous_sources:
  - raw/2026-10-18-home-cluster-claude-code-agent-instructions.md
author: Mike Chester
url: https://github.com/mchestr/home-cluster/blob/924c31d581b9010658ac58e4022448e7d6bf5ba9/kubernetes/apps/ai/claude-code/app/resources/CLAUDE.md
commit: 924c31d
created: 2026-10-18
updated: 2026-11-08
tags: [home-cluster, ai, claude-code]
---

# home-cluster claude-code agent instructions

## Summary

The `CLAUDE.md` mounted into the in-cluster Claude Code server ([[claude-code-remote-control]]). It sets two rule sets: write in ASD-STE100 Simplified Technical English, and use the knowledge base (this wiki) when you troubleshoot.

## Key points

- Instructions as numbered lists in command form, one instruction for each step.
- At most 20 words in an instruction and 25 words in a description.
- Active voice, one name for one thing, simple words (not: utilize, ensure, facilitate, leverage, commence, terminate).
- Warnings before the step, starting with "WARNING:".
- No introduction, praise or summary. At most 6 sentences in a paragraph.
- Keep every fact, value and safety step.
- Knowledge base: the wiki is cloned at `~/knowledgebase`. Read `wiki/index.md` before you troubleshoot or answer a question about the systems. Use the pages in `wiki/issues/` and `wiki/sops/` before you investigate from the start. After a new fix, offer to record it as an issue or SOP under the rules in the wiki's `CLAUDE.md`. Do not record personal information of users, because the repository is public.

## Data and quotes

The same rules explain the style of the repository's newer docs and skills, for example [[home-cluster-volsync-restore-skill]] and the node failure steps in [[home-cluster-disaster-recovery]].

Version `924c31d` added the "Knowledge base" section. Version `e36a8c8` had only the writing rules.

## Connections

- [[claude-code-remote-control]].

## Open questions

- None.
