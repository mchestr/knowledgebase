# Knowledge base schema

This repository is an LLM-maintained wiki. It follows Andrej Karpathy's "LLM wiki" pattern:
https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f

The human curates sources and asks questions. The LLM writes and maintains every page in `wiki/`.
The human and the LLM change this file together when a convention changes.

## Layers

| Layer | Path | Owner | Rule |
| --- | --- | --- | --- |
| Raw sources | `raw/` | Human | Read only. Never edit, rename or delete a file in `raw/`. |
| Wiki | `wiki/` | LLM | The LLM creates and updates all pages. |
| Schema | `CLAUDE.md` | Both | Conventions and workflows. |

## Directory layout

```
raw/                  Immutable source documents (articles, papers, notes, data).
raw/assets/           Images and attachments that sources refer to.
wiki/index.md         Catalog of every page. Read it first for every task.
wiki/log.md           Append-only record of operations.
wiki/overview.md      Top-level synthesis of the whole knowledge base.
wiki/sources/         One summary page for each file in raw/.
wiki/entities/        People, organizations, products, projects, places.
wiki/concepts/        Ideas, methods, terms, theories.
wiki/syntheses/       Comparisons, analyses and filed answers to queries.
templates/            Page templates for each page type.
scripts/lint.py       Structural lint. CI runs it.
.claude/skills/       The kb-ingest, kb-query and kb-lint skills.
```

## Page rules

1. Name each file in lowercase kebab-case, for example `wiki/concepts/scaling-laws.md`.
2. Use a unique file name across all of `wiki/`. Links resolve by file name only.
3. Start each page (except `index.md` and `log.md`) with the frontmatter from its template in `templates/`.
4. Set `type` to `overview`, `source`, `entity`, `concept` or `synthesis`. Put the page in the matching directory.
5. Write dates as `YYYY-MM-DD`. Set `updated` to today each time you change the page.
6. On a source page, set `source` to the path of the raw file, for example `raw/2026-10-18-article.md`.
7. Make one page for one thing. Update the existing page before you create a new page.
8. Use one name for one thing. Record other names in an `aliases` frontmatter list.

## Links and citations

1. Link pages with Obsidian wikilinks: `[[page-name]]` or `[[page-name|shown text]]`.
2. Link each important entity or concept the first time a page mentions it.
3. Cite a claim with a link to its source page, for example `... grew 40% in 2025 ([[acme-annual-report-2025]]).`
4. Link every entity, concept and synthesis page to at least one source page.
5. Do not link to a page that does not exist. Create the page or remove the link.
6. Embed images from `raw/assets/` with `![[file-name.png]]`.

## Contradictions and uncertainty

1. Do not delete a claim because a newer source disagrees. Record both claims with their sources.
2. Mark a conflict with this callout on each page that it affects:

   ```
   > [!warning] Contradiction
   > [[source-a]] says X. [[source-b]] says Y.
   ```

3. Mark a claim that a source does not support with `> [!question] Unverified`.

## index.md

1. List every page except `index.md` and `log.md`.
2. Put each page under its section: Overview, Sources, Entities, Concepts or Syntheses.
3. Write one entry for each page: `- [[page-name]] — one-line summary`.
4. Keep entries in alphabetical order inside each section.

## log.md

1. Add entries only at the bottom. Do not edit or delete old entries.
2. Start each entry with `## [YYYY-MM-DD] <op> | <title>`. Use the op `ingest`, `query`, `lint` or `update`.
3. Under the heading, list the pages you created or changed as bullets.

## Workflows

Use the skill for each operation. Each skill has its full procedure.

| Operation | Skill | Use |
| --- | --- | --- |
| Ingest | `kb-ingest` | Add a new source to the wiki. |
| Query | `kb-query` | Answer a question from the wiki. Optionally file the answer as a page. |
| Lint | `kb-lint` | Find and fix structural and content problems. |

## Lint

1. Run `python3 scripts/lint.py` after each change to `wiki/`.
2. Fix all errors before you finish a task. Errors fail CI.
3. The `lint` workflow runs the script on each push, each pull request, and each day.
4. The `llm-lint` workflow runs the `kb-lint` skill each week and opens a pull request.
