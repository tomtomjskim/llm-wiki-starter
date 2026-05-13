---
name: dual-agent-workflow
description: Claude Code와 Codex를 함께 사용할 때의 역할 분리, 적대적 리뷰, 병렬 구현 검수 패턴
type: guide
updated: 2026-05-13
status: active
---

# Claude Code + Codex 병행 운영

## 핵심 원칙

Claude Code와 Codex를 함께 쓸 때는 두 에이전트를 같은 사람처럼 다루지 않는다. 한쪽은 구현자, 다른 한쪽은 리뷰어 또는 검수자로 두고, 작업 단위와 파일 소유권을 분리한다.

| 원칙 | 이유 |
|------|------|
| 코드가 최종 기준 | wiki, memory, `AGENTS.md`가 코드와 충돌하면 코드를 먼저 믿고 문서를 고친다. |
| 한 파일 한 작성자 | 두 에이전트가 같은 파일을 동시에 수정하면 merge 품질이 급격히 떨어진다. |
| 리뷰어는 바로 고치지 않음 | 적대적 리뷰의 목적은 결함 발견이다. 수정은 별도 단계로 넘긴다. |
| 규칙은 중복보다 링크 | Claude memory와 Codex `AGENTS.md`에 같은 규칙을 복붙하면 drift가 생긴다. |
| wiki 업데이트는 마지막 | 구현 중간에 wiki를 고치면 리뷰어가 아직 확정되지 않은 사실을 기준으로 삼을 수 있다. |

## 권장 역할 분리

| 상황 | Claude Code | Codex |
|------|-------------|-------|
| 코드 구현 | 도메인 구현 또는 리팩터링 | 영향 범위 점검, 테스트/리뷰 |
| 적대적 리뷰 | 구현 결과에 대한 반대 관점 리뷰 | 구현자 또는 2차 리뷰 |
| 병렬 구현 | 모듈 A 담당 | 모듈 B 담당 |
| wiki compile | 초안 생성 | 코드 대조 검수 |
| 규칙 정리 | memory 후보 추출 | `AGENTS.md` 반영 여부 검토 |

역할은 고정이 아니다. 중요한 것은 한 작업 안에서 “작성자”와 “검수자”를 분리하는 것이다.

## 병렬 구현 프로토콜

병렬 구현은 파일 소유권이 분명할 때만 한다.

```
목표: 주문 취소 기능 개선

Claude Code 담당:
- src/orders/cancel/*
- tests/orders/cancel/*

Codex 담당:
- src/inventory/reservation/*
- tests/inventory/reservation/*

공통 금지:
- migration 파일 수정 금지
- API 응답 형식 변경 금지
- 상대 에이전트 담당 파일 revert 금지
```

병렬 구현 전 체크:

1. 같은 파일을 수정하지 않는가?
2. DB migration, OpenAPI spec, 공통 타입처럼 공유 계약을 건드리지 않는가?
3. 두 작업을 합친 뒤 실행할 단일 테스트 명령이 있는가?
4. 충돌 시 누가 최종 통합자인가?

이 네 가지가 불명확하면 병렬 구현 대신 한쪽 구현, 다른 한쪽 리뷰로 운영한다.

## 적대적 리뷰 프로토콜

리뷰어에게는 구현 의도를 설명하되, 방어적으로 검토하도록 요청한다.

```
아래 변경을 적대적으로 리뷰해줘.
목표는 칭찬이 아니라 결함 발견이다.

검토 관점:
- 요구사항을 잘못 해석한 부분
- 코드와 wiki/문서가 충돌하는 부분
- edge case 누락
- 테스트가 통과해도 운영에서 깨질 수 있는 부분
- 보안, 데이터 정합성, migration 위험
- 과한 추상화 또는 불필요한 변경

출력 형식:
- severity: critical | high | medium | low
- 파일/라인 또는 근거 경로
- 왜 문제인지
- 최소 수정 방향

직접 수정하지 말고 리뷰 결과만 작성해줘.
```

리뷰 결과를 받은 뒤에는 구현 에이전트가 수정하고, 리뷰어가 재검수한다. 리뷰어가 곧바로 수정하면 원래 구현 의도와 리뷰 관점이 섞인다.

## wiki와 규칙 동기화

Claude Code memory와 Codex `AGENTS.md`는 역할이 다르다.

| 위치 | 넣을 것 | 넣지 말 것 |
|------|---------|-------------|
| Claude memory | 반복적으로 지켜야 하는 행동 교정, 개인 피드백 | 도메인별 상세 API/DB 사실 |
| Codex `AGENTS.md` | 프로젝트 작업 규칙, 테스트 명령, wiki root | 긴 도메인 문서 전문 |
| `~/wiki/compiled/` | 코드에서 검증 가능한 도메인 사실 | 에이전트 행동 규칙 |
| `~/wiki/personal/decision/` | 왜 그렇게 운영하기로 했는지 | 매 세션 자동 주입해야 하는 명령 |

중복이 필요한 경우에는 원문을 복사하지 말고 링크한다.

```markdown
## LLM Wiki

- Shared wiki root: `~/wiki`
- Detailed domain facts live in `~/wiki/compiled/codebase/`.
- Shared agent operating rules are summarized here; longer rationale lives in `~/wiki/personal/decision/`.
```

## 충돌 방지

### 코드 충돌

두 에이전트를 같은 브랜치에서 동시에 쓰면 작업이 섞이기 쉽다. 병렬 구현은 가능한 한 별도 브랜치 또는 별도 worktree에서 진행한다.

```bash
git worktree add -b codex/orders-cancel ../project-codex
git worktree add -b claude/inventory-reservation ../project-claude
```

통합자는 각 브랜치의 diff를 확인하고 하나씩 merge한다. 자동 병합이 되더라도 테스트와 wiki 대조는 별도로 수행한다.

### wiki 충돌

wiki 파일은 구현이 확정된 뒤 한 번만 업데이트한다. 병렬 작업 중에는 각 에이전트가 발견한 내용을 `known-issues.md`에 바로 쓰기보다 리뷰 노트로 남기고, 통합자가 최종 반영한다.

권장 순서:

1. 구현 완료
2. 테스트 실행
3. 상대 에이전트 리뷰
4. 수정 및 재검수
5. wiki 업데이트
6. `lint-frontmatter.py` 실행

## 상호 검수 프롬프트

### Claude Code가 구현하고 Codex가 검수

```
Claude Code가 만든 diff를 기준으로 Codex가 검수해줘.
~/wiki/compiled/codebase/orders/ 도 함께 읽고,
코드와 wiki가 충돌하는 부분, 누락 테스트, edge case를 severity별로 정리해줘.
직접 파일 수정은 하지 마.
```

### Codex가 구현하고 Claude Code가 검수

```
Codex가 만든 diff를 기준으로 Claude Code가 적대적으로 리뷰해줘.
구현 의도와 다른 해석 가능성, 프로젝트 memory 규칙 위반,
테스트 누락, wiki 업데이트 필요 항목을 분리해서 정리해줘.
```

### 병렬 구현 후 통합 검수

```
두 브랜치의 변경을 통합하기 전에 검수해줘.
검토 대상:
- 서로 같은 파일 또는 같은 책임을 중복 수정했는가
- API/DB/타입 계약이 한쪽 변경만 반영된 상태인가
- 테스트가 각 브랜치 단독뿐 아니라 통합 상태에서도 충분한가
- wiki 업데이트가 필요한 파일은 무엇인가
```

## 문제가 없는지 확인하는 체크리스트

두 에이전트를 같이 쓰기 전 다음 항목을 만족해야 한다.

- `AGENTS.md`와 Claude memory가 서로 반대되는 규칙을 말하지 않는다.
- wiki root가 두 에이전트에서 같은 경로를 가리킨다.
- 구현자와 리뷰어 역할이 명시되어 있다.
- 병렬 구현이면 파일 소유권이 분리되어 있다.
- 공유 계약 파일은 한쪽만 수정하거나 통합자가 직접 수정한다.
- 리뷰어는 허락 없이 구현 파일을 수정하지 않는다.
- 최종 통합 후 코드 기준으로 wiki를 업데이트한다.

## 다음

자동화와 CI로 검수 루프를 고정하려면: [02-automation.md](./02-automation.md)
