# AGENTS.md

## LLM Wiki

- Wiki root: `~/wiki`
- Codebase wiki: `~/wiki/compiled/codebase`
- Personal wiki: `~/wiki/personal`
- Raw inputs: `~/wiki/raw`

Before changing a domain, inspect the matching wiki folder when it exists. Treat wiki pages as context, not authority. If code and wiki conflict, trust code and update the wiki after implementation is verified.

## Domain Map

| Domain | Wiki path | Source path |
|--------|-----------|-------------|
| `<your-domain>` | `~/wiki/compiled/codebase/<your-domain>/` | `src/<your-domain>/` |

## Operating Rules

- Keep code as the final source of truth.
- Do not copy long domain facts into this file; link to wiki paths instead.
- Reading relevant wiki context is expected when it exists; writing or updating wiki requires an explicit user request or an approved final update step.
- If `~/wiki` or a referenced wiki page does not exist, continue from repository files and report that wiki context was unavailable. Do not fail the task only because wiki is missing.
- Update compiled wiki only after code changes are implemented, tested, and reviewed.
- Treat `reviewed`/`canonical` wiki areas as trust-elevated. Do not move generated/inbox notes into reviewed/canonical, set `status: reviewed`/`canonical`, or archive/delete wiki pages unless the user explicitly approves that exact action.
- If you produce a promotion review, make it proposal-only: include a numbered approval shortlist (`approve 1-3`, `hold 2`) and assign non-promoted candidates a disposition (`revise`, `merge`, `keep-generated`, `archive-candidate`, `delete-candidate`, `needs-human-source-check`) with next action/revisit date.
- If you discover stale or missing wiki knowledge during implementation, record it in the final report unless the user explicitly asks you to update wiki files immediately.
- Run the project test command before finalizing code changes.
- Run `python3 ~/wiki-starter/scripts/lint-frontmatter.py ~/wiki --error-only` after wiki edits when the starter repo and wiki are available.

## Claude Code + Codex

When working with Claude Code in parallel:

- Use implementer/reviewer mode by default.
- Parallel implementation requires separate file ownership and preferably separate worktrees.
- Shared contracts such as migrations, API schemas, common types, and public interfaces are owned by the integrator unless explicitly assigned.
- Reviewers should report findings before editing implementation files.

Full protocol: `~/wiki-starter/docs/06-advanced/03-dual-agent-workflow.md`

## Project Commands

```bash
# TODO: replace with project commands
<test-command>
<lint-command>
<build-command>
```
