---
name: ai-ops-hermes-workflow
description: 여러 wiki/project repo를 중앙 Hermes 또는 AI Ops workspace로 관리하는 고급 운영 방식
type: guide
updated: 2026-05-20
status: active
---

# AI Ops + Hermes 운영 방식

이 문서는 `llm-wiki-starter`로 만든 개인 wiki나 프로젝트 wiki를 중앙 운영 repo와 Hermes 같은 Agent runner로 관리하는 선택 방식이다.

처음 사용하는 사람에게 필수는 아니다. wiki가 1개뿐이면 `scripts/init-wiki.sh`, Obsidian, Git, 수동 lint만으로 충분하다.

## 언제 필요한가

도입할 만한 경우:

- 개인 wiki, 프로젝트 wiki, 프로젝트 docs repo가 여러 개다.
- 여러 개발 장비에서 같은 wiki 상태를 확인해야 한다.
- 매일/매주 문서 점검 report가 필요하다.
- Agent 세션 요약, 운영 report, promotion review를 누락 없이 남기고 싶다.
- Telegram 같은 모바일 채널로 read-only 상태를 받고 싶다.

아직 과한 경우:

- wiki가 1개뿐이다.
- Obsidian과 GitHub viewer만으로 충분하다.
- 자동화 유지보수에 시간을 쓰기 어렵다.
- secret, production, DB 권한 경계가 정리되지 않았다.

## 역할 분리

```text
llm-wiki-starter
  └─ wiki 구조, frontmatter 규칙, 템플릿, 예시 제공

wiki repo
  └─ 개인 기억, 프로젝트 지식, compiled docs 저장

ai-ops workspace
  └─ source registry, schedule, 권한 정책, report 기준 저장

Hermes 또는 Agent runner
  └─ repo pull, lint, audit, report, notification 실행
```

중요한 기준:

- Git과 Markdown이 최종 진실 소스다.
- Agent memory는 최종 진실 소스가 아니다.
- `raw`, `inbox`, `generated`는 확정 정보가 아니다.
- `reviewed`, `canonical`, 프로젝트 docs는 사람 검토 후 반영한다.

## Source Registry 예시

중앙 운영 repo에는 관리할 wiki source를 registry로 둔다.

```yaml
version: 1

defaults:
  clone_base: /srv/ai-ops/repos
  branch: main
  viewer: github
  write_policy: generated_only
  canonical_policy: human_review_required

sources:
  - id: personal-wiki
    kind: personal_wiki
    repo: https://github.com/your-name/personal-wiki.git
    branch: main
    purpose: Personal long-term memory and session summaries.
    enabled: true
    write_policy: generated_only
    canonical_policy: human_review_required
    paths:
      inbox: wiki/inbox
      generated: wiki/generated
      reviewed: wiki/reviewed
      canonical: wiki/canonical

  - id: project-docs
    kind: project_repo
    repo: https://github.com/your-name/project.git
    branch: main
    purpose: Project docs and agent rules.
    enabled: true
    write_policy: generated_only
    paths:
      docs: docs
      agent_rules: AGENTS.md
      decisions: docs/DECISIONS.md
      runbook: docs/RUNBOOK.md
```

이 파일에는 token, private key, `.env` 값을 넣지 않는다.

## 샘플 작업

### 1. Source 상태 점검

```text
registry에 enabled로 등록된 wiki/project repo를 점검한다.

확인:
- clone 또는 pull 가능 여부
- branch 상태
- dirty worktree 여부
- 필수 wiki/docs 경로 존재 여부
```

권한: read-only

### 2. Frontmatter Lint Report

```text
각 wiki repo에서 markdown frontmatter lint를 실행하고 report를 생성한다.

허용:
- report 파일 생성

금지:
- 자동 수정 commit
- canonical 이동
```

권한: generated/report only

### 3. Session Capture

```text
Agent 작업 후 세션 요약을 wiki inbox에 저장한다.

포함:
- 작업 목표
- 변경 파일
- 검증 결과
- 결정사항
- 남은 작업
- 보안상 주의점
```

권한: inbox write

### 4. Promotion Review

```text
inbox/generated 문서를 검토해 승격 후보를 분류한다.

분류:
- 삭제 후보
- 보류 후보
- reviewed 승격 후보
- canonical 승격 후보
```

권한: report only

### 5. Project Docs Audit

```text
프로젝트 repo의 AGENTS.md, PROJECT.md, RUNBOOK.md, DECISIONS.md 존재 여부와 최신성을 점검한다.
```

권한: report only

## 안전한 Write Policy

| 정책 | 의미 | 권장 사용처 |
|---|---|---|
| `read_only` | 조회와 report만 허용 | 외부/민감 repo |
| `generated_only` | inbox/generated/report 작성 허용 | 개인 wiki, 프로젝트 wiki 기본값 |
| `direct_commit_allowed` | 제한된 문서 경로 직접 commit 허용 | 1인 운영 repo |
| `pr_required` | 변경 후보를 PR로 제출 | 팀 repo, 충돌이 잦은 repo |

초기 기본값은 `generated_only`다. 직접 commit은 편하지만 wiki 오염과 충돌이 반복되면 `pr_required`로 낮춘다.

## Skill로 만들기 전 기준

처음부터 skill로 만들지 않는다.

순서:

```text
prompt template -> no-agent script -> scheduled prompt -> reviewed workflow -> skill
```

skill 후보 조건:

- 같은 작업을 3회 이상 반복했다.
- 입력과 출력 형식이 안정적이다.
- 실패해도 production write가 없다.
- secret 접근이 없다.
- audit log나 report가 남는다.
- 사람이 검토했을 때 오탐이 적다.

초기 skill 후보:

- `project-doc-audit`
- `wiki-promotion-review`
- `security-permission-audit`
- `tailscale-access-review`

MVP에서 skill로 만들지 않을 작업:

- deploy 실행
- DB migration 적용
- DB write
- firewall 변경
- production secret rotation
- 운영 서버 restart

## 다른 Agent 세션에 줄 시작 프롬프트

```text
Read AGENTS.md, README.md, docs/00-start-here.md, and docs/06-advanced/04-ai-ops-hermes-workflow.md first.
Git and Markdown are the source of truth.
Do not store secrets in memory or docs.
Write only to inbox/generated/report paths unless explicitly approved.
If code and wiki disagree, trust code and report the wiki update needed.
```

## 도입 순서

1. `llm-wiki-starter`로 wiki 구조를 만든다.
2. wiki repo를 private GitHub repo로 push한다.
3. 중앙 운영 repo에 source registry를 만든다.
4. Agent runner는 read-only pull/check부터 시작한다.
5. frontmatter lint와 stale report를 자동화한다.
6. session capture를 `inbox`에 저장한다.
7. promotion review를 주간으로 실행한다.
8. 3회 이상 안정적으로 반복된 작업만 skill 후보로 올린다.

## 체크리스트

- [ ] wiki repo에 secret이 없는가
- [ ] registry에 token 값이 없는가
- [ ] write policy가 `generated_only`인가
- [ ] canonical 반영에 사람 검토가 있는가
- [ ] report 위치가 정해져 있는가
- [ ] 실패 시 자동 write를 멈출 수 있는가
- [ ] 다른 Agent 세션이 읽을 시작 문서가 명확한가
