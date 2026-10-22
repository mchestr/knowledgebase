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
wiki/issues/          Common issues: symptom, cause, check and fix.
wiki/sops/            Standard operating procedures: numbered steps for one task.
templates/            Page templates for each page type.
scripts/lint.py       Structural lint. CI runs it.
scripts/sources.py    Finds new versions of tracked sources and saves them to raw/.
scripts/inventory.py  Generates the home-cluster app inventory (needs yq).
sources.json          Tracked sources and the last ingested version of each.
.claude/skills/       The kb-ingest, kb-query and kb-lint skills.
```

## Page rules

1. Name each file in lowercase kebab-case, for example `wiki/concepts/scaling-laws.md`.
2. Use a unique file name across all of `wiki/`. Links resolve by file name only.
3. Start each page (except `index.md` and `log.md`) with the frontmatter from its template in `templates/`.
4. Set `type` to `overview`, `source`, `entity`, `concept`, `synthesis`, `issue` or `sop`. Put the page in the matching directory.
5. Write dates as `YYYY-MM-DD`. Set `updated` to today each time you change the page.
6. On a source page, set `source` to the path of the raw file, for example `raw/2026-10-18-article.md`.
7. Keep one source page for each document. When a new version of the document arrives, save it as a new raw file.
   Set `source` to the new file. Move the old path to the `previous_sources` list, newest first.
   When a document is deleted upstream, keep its raw file and source page. Set `removed_upstream` to the commit or date.
8. Make one page for one thing. Update the existing page before you create a new page.
9. Use one name for one thing. Record other names in an `aliases` frontmatter list.

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

## Issues and SOPs

1. Write an issue page for each problem that can happen again. Name it for the symptom, for example `seerr-plex-user-cannot-sign-in`.
2. Give each issue page these sections: Symptom, Cause, Check, Fix, Prevention, Related.
3. Write an SOP page for each task that has fixed steps. Name it with a verb, for example `look-up-a-plex-user`.
4. Give each SOP page these sections: Purpose, When to use, Before you start, Procedure, Verify, Related.
5. Write the Check, Fix and Procedure sections as numbered steps. Put a command in a code block.
6. Link an issue to the SOPs that its Check and Fix steps use.
7. Record each incident as a raw file `raw/YYYY-MM-DD-incident-<slug>.md`, then ingest it. Cite the incident source page from the issue page.

WARNING: Do not write personal information on any page or raw file. This includes names, emails, usernames, account IDs and IP addresses of users. Write "the user" instead. Tell the reader where to look up the real value.

## index.md

1. List every page except `index.md` and `log.md`.
2. Put each page under its section: Overview, Sources, Entities, Concepts, Syntheses, Issues or SOPs.
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

## Tracked sources

1. List each source to re-ingest in `sources.json`. The `reingest` workflow checks them each Sunday.
2. The workflow runs `scripts/sources.py fetch`, then `kb-ingest` in unattended mode, then the lint.
3. It merges the result without review. Check `wiki/log.md` and the merged pull requests.
4. Run `python3 scripts/sources.py check` to see pending changes without a change to any file.
