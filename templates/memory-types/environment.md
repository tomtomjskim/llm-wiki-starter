---
name: <environment-name>
description: 개발 단말 또는 서버 환경 프로필
type: memory
scope: environment
updated: YYYY-MM-DD
status: draft
confidence: medium
---

# <Environment Name>

## Role

예: personal local dev, company workstation, personal OCI, company staging.

## Machine

- OS:
- Architecture:
- Package managers:
- Shell:

## Project Roots

| Path | Purpose | Access |
| --- | --- | --- |
| `/path/to/projects` | project workspace | personal/company/public |

## Git Identity

| Scope | SSH host alias | Git user/email |
| --- | --- | --- |
| personal | `github-personal` | `<personal-email>` |
| company | `github-company` | `<company-email>` |

## Runtime Tools

| Tool | Version | Notes |
| --- | --- | --- |
| Git | | |
| Node.js | | |
| Python | | |
| Docker | | |

## Services

| Service | How it runs | Port/domain | Health check |
| --- | --- | --- | --- |
| `<service>` | Docker Compose | `<service>.example.com` | `/health` |

## Secrets

Do not record values.

| Name | Location | Rotation/verification |
| --- | --- | --- |
| `<SECRET_NAME>` | Password manager or `.env` path | How to verify without exposing value |

## Allowed Repositories

- `<repo>`

## Forbidden Repositories

- `<repo-or-scope>`

## Workflows

- Start dev:
- Run tests:
- Deploy:
- Check health:

## Known Issues

- <issue>

## Open Questions

- <question>
