---
name: codex-integration
description: Codex에서 LLM Wiki를 컨텍스트와 작업 규칙으로 활용하는 방법
type: guide
updated: 2026-05-13
status: active
---

# Codex 연동

먼저 자동/수동 경계와 `CLAUDE.md`, `AGENTS.md`, memory, wiki의 역할을 확인한다: [00-mental-model.md](./00-mental-model.md)

## 목적

Codex에서 이 wiki를 쓰는 목표는 두 가지다.

1. 프로젝트별 `AGENTS.md`에 wiki 위치와 운영 규칙을 고정한다.
2. 작업 중 필요한 compiled wiki만 읽게 해서 컨텍스트 낭비와 오래된 정보 사용을 줄인다.

Claude Code의 memory가 세션 시작 시 자동 로드되는 규칙 저장소에 가깝다면, Codex에서는 `AGENTS.md`와 명시적인 파일 참조를 중심으로 운용하는 편이 안정적이다.

## 권장 배치

```
~/wiki/
├── raw/
├── personal/
└── compiled/
    └── codebase/
        └── <domain>/

<your-project>/
├── AGENTS.md
└── src/
```

wiki는 프로젝트 바깥에 두고, 프로젝트 루트의 `AGENTS.md`에서 wiki 경로만 참조한다. 이렇게 하면 코드 저장소에 개인 지식이나 민감한 compiled 결과가 섞이지 않는다.

## AGENTS.md 예시

프로젝트 루트에 다음 블록을 추가한다.

기본 템플릿: [templates/agents/AGENTS.md](../../templates/agents/AGENTS.md)

```markdown
## LLM Wiki

- Wiki root: `~/wiki`
- Codebase wiki: `~/wiki/compiled/codebase`
- Before changing a domain, inspect the matching wiki folder when it exists.
- Treat wiki pages as context, not authority. If code and wiki conflict, trust code and update the wiki.
- After discovering missing or stale knowledge, report the wiki update needed. In dual-agent workflows, update compiled wiki after implementation and review are complete.

## Domain Map

| Domain | Wiki path |
|--------|-----------|
| orders | `~/wiki/compiled/codebase/orders/` |
| users | `~/wiki/compiled/codebase/users/` |
```

도메인이 많아지면 `Domain Map`만 유지해도 Codex가 필요한 wiki 폴더를 빠르게 찾을 수 있다.

## Codex에 요청하는 패턴

### 도메인 작업 전 컨텍스트 로드

```
주문 취소 로직을 수정하기 전에
~/wiki/compiled/codebase/orders/ 를 먼저 읽고,
code-map.md와 domain-rules.md 기준으로 영향 범위를 정리한 뒤 수정해줘.
```

### wiki와 코드 불일치 점검

```
src/orders/ 와 ~/wiki/compiled/codebase/orders/ 를 비교해서
wiki가 코드와 어긋난 부분을 찾아줘.
수정이 필요한 wiki 파일과 근거 코드 경로를 함께 정리해줘.
```

### 작업 후 wiki 업데이트

```
이번 변경으로 orders 도메인의 API 계약이 바뀌었는지 확인하고,
필요하면 ~/wiki/compiled/codebase/orders/api-contracts.md 와
known-issues.md 를 업데이트해줘.
```

## Codex 작업 루프

1. `AGENTS.md`에서 wiki root와 도메인 맵을 확인한다.
2. 작업 도메인의 `_index.md`를 먼저 읽고 필요한 파일만 추가로 읽는다.
3. 코드가 기준이고 wiki는 검증 가능한 보조 컨텍스트로 취급한다.
4. 변경 후 wiki에 반영할 사실, 추론, 미해결 위험을 분리해서 기록한다.
5. `python3 scripts/lint-frontmatter.py ~/wiki --error-only`로 문서 기본 형식을 확인한다.

## Codex용 메모리 파일로 옮길 것과 옮기지 않을 것

Codex에 항상 적용해야 하는 행동 규칙은 프로젝트 `AGENTS.md`나 Codex 전역 지침에 둔다.

| 둘 곳 | 넣을 내용 | 예시 |
|------|----------|------|
| `AGENTS.md` | 프로젝트 작업 규칙, wiki 위치, 테스트 명령 | "DB 변경 전 migration 확인" |
| `~/wiki/compiled/` | 코드베이스 사실, API, DB, known issue | "orders.cancel은 재고 복원을 호출" |
| `~/wiki/personal/` | 개인 학습, 결정 기록 | "Git sync를 선택한 이유" |
| `~/wiki/raw/` | 검증 전 원본 자료 | 로그, 스크린샷, 회의 메모 |

wiki의 모든 내용을 Codex 지침으로 옮기면 컨텍스트가 무거워지고 오래된 정보가 규칙처럼 굳어진다. 반복 적용해야 하는 행동 규칙만 지침으로 승격한다.

## 적대적 리뷰 체크리스트

Codex에게 wiki 품질 점검을 맡길 때는 다음처럼 요청한다.

```
~/wiki/compiled/codebase/orders/ 를 적대적으로 리뷰해줘.
아래 관점으로 severity를 붙여줘:
- 코드와 충돌하는 설명
- 출처 없이 단정한 비즈니스 규칙
- 오래된 updated 날짜 또는 low confidence
- broken link / orphan page
- 테스트나 API 계약에 반영되지 않은 known issue
```

리뷰 결과는 바로 고치지 말고, 먼저 `known-issues.md`에 기록한 뒤 코드 근거를 확인한다.

## Claude Code와 함께 쓸 때

Claude Code와 Codex를 함께 쓰는 경우 Codex를 항상 구현자로 둘 필요는 없다. 구현은 Claude Code가 맡고 Codex는 적대적 리뷰와 통합 검수를 맡기는 방식이 특히 안정적이다.

```
Claude Code가 만든 diff를 검수해줘.
~/wiki/compiled/codebase/orders/ 도 함께 읽고,
코드와 wiki가 충돌하는 부분, 누락 테스트, edge case를 severity별로 정리해줘.
직접 수정하지 말고 리뷰만 해줘.
```

병렬 구현을 할 때는 파일 소유권을 먼저 나눈다. 같은 파일, migration, 공통 타입, API 계약을 두 에이전트가 동시에 수정하게 두지 않는다.

상세: [docs/06-advanced/03-dual-agent-workflow.md](../06-advanced/03-dual-agent-workflow.md)

## 다음

Obsidian vault 설정을 마쳤다면 워크플로우로 이동: [docs/03-workflow/01-collect.md](../03-workflow/01-collect.md)
