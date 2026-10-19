# knowledgebase

A personal knowledge base that an LLM maintains as a markdown wiki. It follows Andrej Karpathy's
[LLM wiki pattern](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f).
You add sources and ask questions. The LLM writes the summaries, links and syntheses.

## Layout

| Path | Contents |
| --- | --- |
| `raw/` | Source documents. You add them. The LLM never changes them. |
| `raw/assets/` | Images and attachments. |
| `wiki/` | LLM-written pages: `index.md`, `log.md`, `overview.md`, `sources/`, `entities/`, `concepts/`, `syntheses/`. |
| `templates/` | Frontmatter and section templates for each page type. |
| `CLAUDE.md` | The schema: conventions and workflows. `AGENTS.md` links to it. |
| `.claude/skills/` | The `kb-ingest`, `kb-query` and `kb-lint` skills for Claude Code. |
| `scripts/lint.py` | Structural lint. Python 3.10 or later, standard library only. |

## Use

1. Add a source file to `raw/`. The Obsidian Web Clipper is a good tool for this.
2. Open Claude Code in this directory.
3. Type `/kb-ingest raw/<file>` to add the source to the wiki.
4. Type `/kb-query <question>` to ask a question.
5. Type `/kb-lint` to run a health check.
6. Open the repository root as an Obsidian vault to read the wiki and see the graph view.

## Lint

Run the structural lint locally:

```sh
python3 scripts/lint.py                    # text output, exit 1 on errors
python3 scripts/lint.py --strict           # exit 1 on warnings too
python3 scripts/lint.py --format markdown  # also: json
```

| Severity | Code | Meaning |
| --- | --- | --- |
| error | `frontmatter-missing`, `frontmatter-invalid`, `missing-field`, `bad-field` | Page frontmatter is absent, incomplete or has the wrong value type. |
| error | `bad-type`, `wrong-dir` | `type` is not valid, or the page is in the wrong directory. |
| error | `bad-date` | Date is not `YYYY-MM-DD`, is in the future, or `updated` is before `created`. |
| error | `duplicate-name` | Two pages have the same file name, so links are ambiguous. |
| error | `broken-link` | A wikilink or embed points to nothing. |
| error | `missing-source` | A source page `source` or `previous_sources` path is not in `raw/`. |
| error | `not-in-index` | A page is not listed in `wiki/index.md`. |
| error | `log-format`, `log-order` | A `wiki/log.md` heading has the wrong format or date order. |
| warning | `orphan` | No page links to this page. |
| warning | `uncited` | An entity, concept or synthesis page links to no source page. |
| warning | `stale` | The page was not updated for 180 days. |
| warning | `uningested` | A file in `raw/` has no source page. |

## GitHub workflows

| Workflow | Schedule | Action |
| --- | --- | --- |
| `lint` | Each push to `main`, each PR, each day at 06:00 UTC | Runs `scripts/lint.py`. A failed daily run opens or updates an issue with the `kb-lint` label. The next passing daily run closes it. |
| `llm-lint` | Each Monday at 07:00 UTC, or manual | Runs the `kb-lint` skill with Claude Code. Fixes safe problems and opens a PR with the report. |

### Set up `llm-lint`

The workflow uses a Claude Pro or Max subscription token. Each run counts against the subscription usage limits.

1. Run `claude setup-token` and copy the token.
2. Run `pbpaste | gh secret set CLAUDE_CODE_OAUTH_TOKEN -R mchestr/knowledgebase`.
3. Go to Settings > Actions > General. Select "Allow GitHub Actions to create and approve pull requests".
4. Run the workflow once from the Actions tab to test it.

To use an API key instead, store it as `ANTHROPIC_API_KEY`. In `llm-lint.yml`, replace `claude_code_oauth_token` with `anthropic_api_key`.

A PR that the workflow opens with `GITHUB_TOKEN` does not trigger the `lint` workflow.
The `llm-lint` job runs the structural lint itself before it opens the PR.
