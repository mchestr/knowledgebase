# Log

Append-only record of wiki operations. Add new entries at the bottom.
Heading format: `## [YYYY-MM-DD] <op> | <title>`. Ops: `ingest`, `query`, `lint`, `update`.
Find recent entries with `grep '^## \[' wiki/log.md | tail -5`.

## [2026-10-18] update | Initialize knowledge base

- Created the repository structure, schema, skills and lint workflows.
