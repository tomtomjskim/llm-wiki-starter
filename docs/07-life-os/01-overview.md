---
name: life-os-overview
description: LLM Wiki를 개인 Life OS profile로 확장하는 개요
type: guide
updated: 2026-07-06
status: active
---

# Life OS Profile 개요

Life OS Profile은 LLM Wiki를 개인 장기 기억, 루틴, 결정 기록, 작업 세션,
AI context pack 운영에 맞게 확장하는 선택형 구조다. 기본 starter의
`raw/`, `personal/`, `compiled/` 구조를 대체하지 않고 그 위에 얹는다.

## 목적

Life OS의 목적은 모든 기록을 한곳에 쌓는 것이 아니다. 원본, AI 정리 후보,
사람이 검토한 지식, 장기 기준을 분리해서 AI가 검토되지 않은 내용을 확정
사실처럼 사용하지 않게 하는 것이다.

```text
raw/inbox -> generated -> reviewed -> canonical
```

핵심 원칙:

- raw는 증거다. 기본 답변 컨텍스트로 직접 쓰지 않는다.
- generated는 AI가 만든 후보이며 authority가 아니다.
- reviewed는 사람이 읽고 확인한 지식이다.
- canonical은 반복 적용할 장기 기준이다.
- AI는 generated까지만 자동 작성하고, reviewed/canonical 승격은 사람 승인으로 한다.

## 기본 LLM Wiki와의 관계

| 기본 LLM Wiki | Life OS Profile |
|---|---|
| raw 수집 | raw와 inbox를 분리해 오염을 줄임 |
| personal 노트 | reviewed/canonical 기준으로 장기 기억 관리 |
| compiled 문서 | generated 후보, hub, context pack 생성 |
| Ask 단계 | 검토된 context pack을 AI 세션에 주입 |

Life OS는 코드베이스 wiki보다 개인 운영 지식에 가깝다. 건강, 재무, 커리어,
학습처럼 민감하거나 시점 의존적인 영역은 원문을 넣지 않고 요약, 루틴,
결정 기준만 남긴다.

## 언제 쓰는가

- AI 세션마다 같은 개인 선호와 작업 맥락을 반복 설명하고 싶지 않을 때
- 프로젝트, 학습, 루틴, 회고를 Obsidian에서 연결하고 싶을 때
- Claude/Codex/ChatGPT에 넘길 context pack을 안전하게 만들고 싶을 때
- Notion, Claude export, Telegram 기록 같은 raw source를 정제하고 싶을 때

## 하지 않는 것

- secret, token, private key, production `.env` 값을 저장하지 않는다.
- raw 대화 전문을 장기 기억으로 자동 승격하지 않는다.
- generated 문서를 reviewed/canonical처럼 취급하지 않는다.
- Life OS를 처음부터 별도 제품이나 복잡한 자동화 시스템으로 만들지 않는다.

## 다음

- 디렉토리 구조: [02-directory-layout.md](./02-directory-layout.md)
- 신뢰 경계와 승격: [03-trust-boundary-and-promotion.md](./03-trust-boundary-and-promotion.md)
- AI context pack: [04-ai-context-pack.md](./04-ai-context-pack.md)
- Codex/Claude 사용법: [05-codex-claude-session-usage.md](./05-codex-claude-session-usage.md)
