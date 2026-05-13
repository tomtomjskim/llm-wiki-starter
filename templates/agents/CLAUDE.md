# CLAUDE.md

## LLM Wiki

- Wiki root: `~/wiki`
- Codebase wiki: `~/wiki/compiled/codebase`
- Personal wiki: `~/wiki/personal`
- Raw inputs: `~/wiki/raw`

Use wiki pages as context, not authority. Code, tests, schemas, and source documents are the final source of truth.

## Domain Map

| Domain | Wiki path | Source path |
|--------|-----------|-------------|
| `<your-domain>` | `~/wiki/compiled/codebase/<your-domain>/` | `src/<your-domain>/` |

## Memory Boundary

Claude memory stores recurring behavior rules and feedback. It should not contain long API contracts, DB schemas, or domain facts. Put those in `~/wiki/compiled/codebase/<domain>/` and link to them here when needed.

## Working Rules

- Before domain work, read the matching `_index.md` if it exists.
- Reading relevant wiki context is expected when it exists; writing or updating wiki requires an explicit user request or an approved final update step.
- If `~/wiki` or a referenced wiki page does not exist, continue from repository files and report that wiki context was unavailable. Do not fail the task only because wiki is missing.
- If wiki and code disagree, trust code and report the wiki update needed.
- Do not use `~/wiki/compiled/` as a scratchpad during implementation.
- Update wiki after implementation, tests, and review are complete.
- Run `python3 ~/wiki-starter/scripts/lint-frontmatter.py ~/wiki --error-only` after wiki edits when the starter repo and wiki are available.

## Claude Code + Codex

When Codex is also used:

- Prefer one implementer and one reviewer.
- Review findings should include severity, evidence, and minimal fix direction.
- Parallel work requires explicit owned file globs and forbidden paths.
- Do not revert or overwrite changes made by the other Agent.

Full protocol: `~/wiki-starter/docs/06-advanced/03-dual-agent-workflow.md`

## Project Commands

```bash
# TODO: replace with project commands
<test-command>
<lint-command>
<build-command>
```
