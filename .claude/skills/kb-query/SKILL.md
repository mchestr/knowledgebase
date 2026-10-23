---
name: kb-query
description: Answer a question from the knowledge base wiki with citations, and optionally file the answer as a synthesis page. Use when the user asks a question about topics in the wiki, or says "query", "what does the wiki say", or "file this answer".
---

# kb-query

The knowledge base is the current repository. If the current folder is not the knowledge base, use `/Users/mchestr/code/knowledgebase`. All paths in this skill start at that folder.

Answer from the wiki, not from memory. Follow the rules in `CLAUDE.md`.

## Find

1. Read `wiki/index.md`.
2. Select the pages whose summaries match the question.
3. Search `wiki/` with Grep for the key terms. Add the pages that match.
4. Read the selected pages. Follow links to related pages when they are relevant.
5. Read a raw source in `raw/` only when the wiki pages do not have enough detail.

## Answer

1. Answer the question. Use the form that fits it: text, a table, a list or a chart.
2. Cite each claim with a link to the wiki page it comes from, for example `[[scaling-laws]]`.
3. Tell the user about contradictions between pages.
4. Tell the user when the wiki does not have the answer. Do not fill gaps from memory without saying so.
5. Suggest sources that can fill the gaps.

## File the answer

Do these steps when the user asks, or when the answer has lasting value and the user agrees.

1. Create `wiki/syntheses/<slug>.md` from `templates/synthesis.md`. If the answer is the cause and fix of a problem, use `templates/issue.md` in `wiki/issues/`. If it is a fixed procedure, use `templates/sop.md` in `wiki/sops/`.
2. Set `question` to the user's question.
3. Write the answer and the citations into the page.
4. Add a link to the new page from each main page it uses.
5. Add an entry to `wiki/index.md` under "Syntheses", "Issues" or "SOPs".
6. Add an entry at the bottom of `wiki/log.md`: `## [YYYY-MM-DD] query | <question>`.
7. Run `python3 scripts/lint.py`. Fix all errors.
