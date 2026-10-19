---
name: kb-lint
description: Health-check the knowledge base wiki for structural and content problems, then fix them. Use when the user says "lint", "health check", "clean up the wiki", or when the weekly llm-lint workflow runs.
---

# kb-lint

Find problems in the wiki and fix the safe ones. Follow the rules in `CLAUDE.md`.

## Structural pass

1. Run `python3 scripts/lint.py`.
2. Fix each error:
   - `broken-link`: Create the missing page if two or more pages need it. Else remove the link.
   - `not-in-index`: Add the page to `wiki/index.md`.
   - `missing-field`, `bad-type`, `wrong-dir`, `bad-date`: Correct the frontmatter or move the page.
   - `duplicate-name`: Rename one page. Update all links to it.
   - `log-format`, `log-order`: Correct only the heading format. Do not reorder or delete entries.
3. Fix each warning:
   - `orphan`: Add a link to the page from the most related page.
   - `uncited`: Add a citation to a source page. If no source supports the page, add an `Unverified` callout.
   - `uningested`: Do not ingest. List the file in the report.
   - `stale`: Check the page in the content pass.

## Content pass

Read `wiki/index.md`, `wiki/overview.md`, and then each page. Look for these problems:

1. Contradictions: two pages make claims that conflict.
2. Stale claims: a newer source replaces a claim, but the page still shows the old claim as current.
3. Missing pages: two or more pages mention an entity or concept that has no page.
4. Missing links: a page names another page but does not link to it.
5. Duplicates: two pages describe the same thing.
6. Gaps: important questions that no source answers.
7. Weak pages: pages with only one or two sentences.

## Fix

1. Add the missing links.
2. Create the missing pages. Use only facts from existing pages and sources. Cite them.
3. Add a contradiction callout on each page in a conflict.
4. Mark a stale claim with its date and add the newer claim with its citation.
5. Update `wiki/index.md` and set `updated` to today on each page you changed.

WARNING: Do not delete pages or merge duplicates without approval. Do not resolve a contradiction by removing a claim.

6. List duplicates, gaps and weak pages in the report. Suggest sources or questions for each gap.

## Finish

1. Run `python3 scripts/lint.py` again. Fix all errors.
2. Add an entry at the bottom of `wiki/log.md`: `## [YYYY-MM-DD] lint | <short title>`. List the changes.
3. Give the report to the user. Use these sections: Fixed, Needs decision, Gaps, Suggested sources.

## Unattended mode

The `llm-lint` workflow runs this skill with no user.

1. Do not ask questions.
2. Write the report to `.lint-report.md` in the repository root.
3. Do not commit. The workflow commits the changes and opens a pull request.
