---
name: life-os-codex-claude-session-usage
description: Life OS profile을 Codex와 Claude Code 세션에서 사용하는 방법
type: guide
updated: 2026-07-06
status: active
---

# Codex / Claude 세션 사용법

Life OS는 AI 세션의 자동 기억을 대체하지 않는다. 대신 검토된 Markdown을
source of truth로 두고, 필요한 범위만 세션에 주입한다.

## 세션 시작 패턴

새 AI 세션에서 전체 wiki를 읽히지 않는다. 먼저 entry point만 읽힌다.

```text
Life OS context:
- compiled/life-os/hubs/home.md
- personal/life-os/canonical/<relevant-policy>.md
- personal/life-os/reviewed/<relevant-topic>.md

규칙:
- canonical을 우선한다.
- generated/inbox는 미검토 자료로 취급한다.
- secret, token, private key를 저장하거나 출력하지 않는다.
```

## 작업 전 읽을 문서 고르기

| 작업 | 읽을 문서 |
|---|---|
| 프로젝트 작업 | `projects-hub.md`, 관련 project note |
| 학습 정리 | `learning-hub.md`, 관련 learning note |
| 회고 | 최근 session summary, promotion review |
| 운영 문제 | `operations-hub.md`, 관련 runbook |
| 장기 정책 변경 | canonical policy, 관련 reviewed decision |

## 세션 종료 패턴

작업이 끝나면 session summary를 남긴다.

```text
personal/life-os/inbox/sessions/YYYY-MM-DD-topic.md
```

최소 항목:

- 오늘 무엇을 했는가
- 어떤 파일/repo/document가 바뀌었는가
- 어떤 결정을 했는가
- 다음에 이어서 할 일은 무엇인가
- secret/PII가 없는가

템플릿: [session-summary.md](../../templates/life-os/session-summary.md)

## Promotion Review

주 1회 generated와 inbox를 검토한다.

```text
compiled/life-os/generated/reviews/YYYY-MM-DD-promotion-review.md
```

검토 결과:

- reviewed 승격 후보
- canonical 승격 후보
- revise
- merge
- keep-generated
- archive-candidate
- delete-candidate
- needs-human-source-check

템플릿: [promotion-review.md](../../templates/life-os/promotion-review.md)

## Codex/Claude에 요청하는 예시

```text
compiled/life-os/hubs/projects-hub.md 와
personal/life-os/reviewed/projects/<project>.md 를 읽고,
이번 작업의 전제와 확인해야 할 위험을 요약해줘.

규칙:
- generated 문서는 확정 사실로 쓰지 마라.
- code/repo와 wiki가 충돌하면 code/repo를 우선하고 wiki update 후보를 남겨라.
```

```text
personal/life-os/inbox/sessions/ 의 최근 7일 세션을 보고
weekly promotion review 후보를 만들어줘.

출력은 compiled/life-os/generated/reviews/YYYY-MM-DD-promotion-review.md 형식으로.
reviewed/canonical 파일은 직접 수정하지 마라.
```

## 반복 개선 루프

```text
1. 작업 전 relevant Life OS docs 읽기
2. 작업 수행
3. session summary 작성
4. weekly promotion review 생성
5. 사람이 reviewed/canonical 승격 결정
6. 다음 AI session에서 더 적은 설명으로 시작
```

이 루프가 반복될수록 Life OS는 단순 기록 저장소가 아니라 AI와 함께 쓰는
개인 운영 컨텍스트가 된다.
