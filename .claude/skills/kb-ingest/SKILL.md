---
name: kb-ingest
description: Ingest a new source into the knowledge base wiki. Use when the user adds a file to raw/, gives a URL or pasted text to add, or says "ingest", "add this source", or "process raw/".
---

# kb-ingest

The knowledge base is the current repository. If the current folder is not the knowledge base, use `/Users/mchestr/code/knowledgebase`. All paths in this skill start at that folder.

Turn one source into wiki pages. One source can change 10 to 15 pages. Follow the rules in `CLAUDE.md`.

## Get the source

1. Find the source file in `raw/`.
2. If the user gives a URL or pasted text, save it as `raw/YYYY-MM-DD-<slug>.md`. Put the URL on the first line.
3. If the user names no source, run `python3 scripts/lint.py` and use the files that have `uningested` warnings.

WARNING: Do not edit, rename or delete files in `raw/`. Raw sources are the record of truth.

## Read

1. Read `wiki/index.md` and `wiki/overview.md`.
2. Read the full source. Read the images in `raw/assets/` that the source refers to.
3. Find the existing entity and concept pages that the source mentions. Read them.

## Discuss

1. Tell the user the 3 to 5 most important points of the source.
2. Tell the user which points agree with or contradict the wiki.
3. Ask the user what to emphasize. Wait for the answer.

Skip the "Discuss" steps when the user asks for a batch ingest or the run is unattended.

## Write

1. Create the source page `wiki/sources/<slug>.md` from `templates/source.md`.
2. Set `source` to the raw file path.
3. Update each existing entity and concept page that the source adds facts to. Cite the source page.
4. Create a page for each important new entity or concept. Use `templates/entity.md` or `templates/concept.md`.
5. Add a contradiction callout where the source conflicts with an existing claim.
6. Update `wiki/overview.md` if the source changes the main themes or open questions.
7. Add an entry to `wiki/index.md` for each new page. Update the summary of each changed page if it changed.
8. Set `updated` to today on each page you changed.
9. Add an entry at the bottom of `wiki/log.md`: `## [YYYY-MM-DD] ingest | <source title>`. List the changed pages.

## Check

1. Run `python3 scripts/lint.py`.
2. Fix all errors. Fix the `orphan` and `uncited` warnings on pages you created.
3. Tell the user the pages you created and changed.
4. Commit the changes only when the user asks. Use the message `ingest: <source title>`.

## Batch ingest

1. Ingest the sources one at a time, in date order.
2. Do all steps for one source before you start the next source.
3. Run the lint once at the end of the batch.

## Ingest a new version of a source

Do these steps when a source page already exists for the document.

1. Find what changed since the old version, for example with a git diff of the two commits.
2. If nothing changed, tell the user and stop.
3. Save the new version as a new raw file. Add the commit or version to the name, for example `raw/2026-10-18-<slug>-<commit>.md`.
4. On the source page, set `source` to the new file. Add the old path at the top of the `previous_sources` list.
5. Update the source page for the changes. Note the new version in its "Data and quotes" section.
6. Update the entity and concept pages that the changes affect. Remove contradiction and `Unverified` callouts that the new version settles.
7. Do the "Write" steps 6 to 9 and the "Check" steps.

If the document was deleted upstream, keep its raw file and source page. Set `removed_upstream` in the frontmatter to the commit or date. Add a `[!note] Removed upstream` callout that says where the old content is.
