---
name: <repo-boundary-name>
description: 저장소 권한, 포함/제외 파일, Agent 접근 정책
type: memory
scope: security
updated: YYYY-MM-DD
status: draft
confidence: medium
---

# <Repo Boundary Name>

## Purpose

이 repo가 어떤 지식과 산출물을 담는지 설명한다.

## Access

| Actor | Access | Notes |
| --- | --- | --- |
| Personal laptop | read/write | |
| Company workstation | none/read/write | |
| Personal server | read-only mirror | |
| Agent runner | work branch only | |

## Include

- <allowed content>

## Exclude

- `.env`
- API token
- SSH private key
- DB password
- customer data
- unrelated personal/company memory

## Agent Policy

Writable:

- `80-raw/**`
- `60-memory/agent-notes/**`
- assigned project folder

Read-only:

- ADR
- runbooks
- architecture docs

Forbidden:

- secret files
- unrelated private memory
- repos outside assigned scope

## Branch Policy

- Main branch is protected.
- Agent works only on `work/agent-*`.
- Human review is required before merge.
