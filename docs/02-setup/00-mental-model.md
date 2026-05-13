---
name: mental-model
description: LLM Wiki의 자동/수동 경계와 CLAUDE.md, AGENTS.md, memory, skill의 역할
type: guide
updated: 2026-05-13
status: active
---

# Mental Model

LLM Wiki Starter는 자동 지식 생성 시스템이 아니라, Agent가 정확하게 읽고 쓰도록 돕는 운영 구조다. 어떤 파일은 Agent에게 항상 지침으로 읽히고, 어떤 파일은 필요할 때만 컨텍스트로 넣는다.

## 자동과 수동의 경계

| 대상 | 생성 방식 | 로드 방식 | 목적 |
|------|-----------|-----------|------|
| `~/wiki/raw/` | 사용자가 수집 | 수동 | 원본 자료 보관 |
| `~/wiki/personal/` | 사용자가 작성, Agent 보조 가능 | 수동 | 학습, 결정, 일지 |
| `~/wiki/compiled/` | Agent에게 요청해서 생성 | 수동 | 코드베이스/도메인 사실 |
| `CLAUDE.md` | 사용자가 프로젝트에 생성 | Claude Code가 지침으로 참조 | 프로젝트 규칙과 wiki 위치 |
| `AGENTS.md` | 사용자가 프로젝트에 생성 | Codex가 지침으로 참조 | 프로젝트 규칙과 wiki 위치 |
| Claude memory | 사용자가 `~/.claude/projects/*/memory/`에 생성 | Claude Code가 세션마다 자동 로드 | 반복 행동 규칙, 피드백 |
| Codex Skill | 사용자가 설치/작성 | 관련 작업에서 명시 또는 자동 선택 | 반복 가능한 전문 작업 절차 |
| Obsidian Git | 사용자가 설정 | 주기적 자동 sync 가능 | wiki 버전 관리와 동기화 |
| `lint-frontmatter.py` | 이 레포가 제공 | 사용자가 실행, hook/CI로 자동화 가능 | 문서 형식 검사 |

핵심 규칙: Agent 지침 파일은 “어디를 볼지와 어떻게 일할지”를 담고, wiki는 “무엇이 사실인지”를 담는다.

## 일반 작업 세션의 기본 동작

프로젝트에 `CLAUDE.md` 또는 `AGENTS.md`가 있으면 Agent는 관련 wiki 경로를 찾을 수 있다. 그렇다고 wiki가 자동으로 계속 쌓이는 것은 아니다.

기본 기대 동작:
- 작업 전 관련 도메인 wiki가 있으면 읽는다.
- 작업 중 코드와 wiki가 충돌하면 코드를 기준으로 판단한다.
- 작업 후 wiki와 달라진 사실이 있으면 업데이트 필요 항목을 보고한다.

명시 요청이 필요한 동작:
- 새 도메인 wiki compile
- 기존 `~/wiki/compiled/` 문서 수정
- `~/wiki/personal/`에 결정/학습 노트 추가
- wiki 변경 후 lint 실행

권장 요청 문구:

```text
관련 도메인 wiki가 있으면 먼저 읽고 작업해줘.
작업 후 wiki 업데이트가 필요한 항목은 보고만 해줘.
내가 승인하면 그때 ~/wiki/compiled/codebase/<domain>/ 문서를 업데이트하고 lint를 실행해줘.
```

wiki까지 바로 반영하고 싶을 때만 이렇게 요청한다.

```text
작업 완료 후 코드와 wiki가 달라진 부분이 있으면
~/wiki/compiled/codebase/<domain>/ 문서도 업데이트하고 lint를 실행해줘.
```

## CLAUDE.md, AGENTS.md, wiki의 관계

```
<your-project>/
├── CLAUDE.md     # Claude Code용 프로젝트 지침
├── AGENTS.md     # Codex용 프로젝트 지침
└── src/          # 실제 코드, 최종 기준

~/wiki/
├── personal/     # 인간이 책임지는 개인 지식
└── compiled/     # Agent가 코드/raw를 읽고 만든 도메인 wiki

~/.claude/projects/*/memory/
└── MEMORY.md     # Claude Code가 반복 로드하는 행동 규칙 인덱스
```

`CLAUDE.md`와 `AGENTS.md`에는 긴 도메인 설명을 복사하지 않는다. 대신 `~/wiki/compiled/codebase/<domain>/` 경로를 적는다.

## 무엇을 어디에 넣을까

| 내용 | 넣을 곳 | 이유 |
|------|---------|------|
| 테스트 명령, 빌드 명령 | `CLAUDE.md`, `AGENTS.md` | Agent가 작업 전후 반복 사용 |
| wiki root, 도메인 맵 | `CLAUDE.md`, `AGENTS.md` | Agent가 필요한 문서를 찾도록 안내 |
| 반복 실수에 대한 교정 | Claude memory 또는 `AGENTS.md` | 세션마다 적용해야 함 |
| API 계약, DB 스키마, 도메인 규칙 | `~/wiki/compiled/` | 코드에서 검증 가능한 사실 |
| 학습 요약, 개인 결정 | `~/wiki/personal/` | 인간 판단과 맥락 포함 |
| 검증 전 로그, 스크린샷, PDF | `~/wiki/raw/` | 원본 보존 |
| 반복 가능한 전문 절차 | Skill | 작업 절차 자체를 재사용 |

## 중복 금지 원칙

같은 규칙을 `CLAUDE.md`, `AGENTS.md`, memory, wiki에 모두 복사하면 시간이 지나며 서로 달라진다.

권장 방식:
- 프로젝트 운영 규칙은 `CLAUDE.md`/`AGENTS.md`에 짧게 둔다.
- 긴 설명과 근거는 `~/wiki/personal/decision/`에 둔다.
- 도메인 사실은 `~/wiki/compiled/`에 둔다.
- Claude Code만 반복 적용해야 하는 피드백은 Claude memory에 둔다.
- 여러 곳에서 필요하면 본문 복사 대신 링크한다.

## Skill은 어디에 들어가나

Skill은 지식 저장소가 아니라 절차 저장소다.

Skill로 승격할 후보:
- 도메인 compile을 매번 같은 형식으로 수행한다.
- 브라우저 검증, 문서 렌더링, GitHub PR 처리처럼 도구 사용 순서가 중요하다.
- 결과 검증 절차가 반복된다.

Skill로 만들지 말아야 할 것:
- 특정 도메인의 API/DB 사실
- 한 번만 쓰는 프로젝트 메모
- 아직 검증되지 않은 개인 선호

Skill 결과도 최종 기준은 아니다. 코드, 테스트, 렌더 결과, 원본 문서로 검증한다.

## 운영 흐름

1. `init-wiki.sh`로 `~/wiki` 구조를 만든다.
2. 프로젝트에 `CLAUDE.md` 또는 `AGENTS.md`를 둔다.
3. Agent에게 특정 도메인을 compile하라고 요청한다.
4. Agent가 `~/wiki/compiled/codebase/<domain>/`에 문서를 작성한다.
5. 사람이 spot check하고 linter를 실행한다.
6. 이후 작업 때 Agent에게 해당 wiki 폴더를 읽게 한다.
7. 코드 변경 후 wiki가 달라져야 하면 업데이트 필요 항목을 먼저 보고받는다.
8. 승인 후 통합된 코드 기준으로 wiki를 업데이트한다.

## 다음

첫 실행 경로: [docs/00-start-here.md](../00-start-here.md)
