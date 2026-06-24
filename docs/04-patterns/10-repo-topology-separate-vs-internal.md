---
name: repo-topology-separate-vs-internal
description: LLM wiki를 별도 repo로 둘지 personal wiki 내부 namespace로 둘지 결정하는 운영 패턴
type: guide
updated: 2026-06-24
status: active
---

# Repo Topology: Separate Repo vs Internal Namespace

LLM wiki 운영에서 가장 먼저 결정할 것은 “지식을 어디에 둘 것인가”다. 정답은 항상 별도 repo가 아니다. 핵심은 repo 분리보다 **신뢰 경계와 운영 비용**을 함께 설계하는 것이다.

## 두 가지 선택지

### A. Separate `llm-wiki` repo

```text
personal-wiki/        # 개인 장기 기억, 일지, 선호, private context
llm-wiki/             # codebase, server, operations, runbooks
project-repo/         # source code
```

적합한 경우:

- 팀/회사/고객 권한 경계가 있다.
- 개인 메모와 운영 문서를 repo 권한으로 분리해야 한다.
- wiki 크기가 커서 index/build/deploy 주기가 달라졌다.
- agent runner가 personal vault를 볼 필요가 없어야 한다.
- 여러 사람이 `llm-wiki`를 공동 관리한다.

장점:

- 권한·보안 경계가 명확하다.
- project/ops agent에 필요한 repo만 붙일 수 있다.
- 팀 협업과 branch protection을 걸기 쉽다.

단점:

- 서버/agent 수가 늘면 clone, pull, push, validation, credential, dirty-state 확인이 `2n` 이상으로 증가한다.
- personal context와 llm context의 cross-reference가 끊기기 쉽다.
- “어느 wiki가 최신인가”를 판단하는 운영 비용이 생긴다.

### B. Internal `llm` namespace inside personal wiki

```text
personal-wiki/
└── wiki/
    ├── inbox/
    ├── generated/
    │   └── llm/
    │       ├── codebase/
    │       ├── environments/
    │       ├── operations/
    │       └── agents/
    ├── reviewed/
    │   └── llm/
    └── canonical/
```

적합한 경우:

- 1인 또는 소수 운영 환경이다.
- 이미 여러 서버/agent가 personal wiki를 공통 장기기억 backbone으로 사용한다.
- 별도 `llm-wiki`를 모든 서버에 붙이면 sync/검증/credential 관리가 2배가 된다.
- 개인 context와 project/ops context의 연결을 유지하고 싶다.
- repo 권한 분리보다 lifecycle/trust 분리가 더 중요하다.

장점:

- 하나의 Git repo, 하나의 sync/validation/reporting 루프만 관리한다.
- agent가 개인 환경과 운영 환경의 관계를 더 잘 파악할 수 있다.
- 기존 `inbox -> generated -> reviewed -> canonical` 승격 정책을 재사용한다.
- context pack/export 정책을 한곳에서 유지한다.

단점:

- path/trust policy가 약하면 agent가 개인 메모를 과하게 읽을 수 있다.
- 팀 협업이나 회사 권한 경계에는 부적합할 수 있다.
- repo가 커질수록 health report와 index/hub 설계가 중요해진다.

## Decision Matrix

| 질문 | Separate repo 쪽 | Internal namespace 쪽 |
|---|---|---|
| 팀/회사/고객 권한 경계가 필요한가? | 예 | 아니오 |
| 이미 personal wiki가 모든 서버에 붙어 있는가? | 아니오 | 예 |
| 서버마다 두 repo를 관리해도 괜찮은가? | 예 | 아니오 |
| 개인 맥락과 ops/code 맥락 연결이 중요한가? | 보통 | 예 |
| agent가 personal vault 접근을 최소화해야 하는가? | 예 | 정책으로 제한 가능 |
| wiki 수명주기/validator를 하나로 유지하고 싶은가? | 아니오 | 예 |

## Recommended Rule

- 조직/팀/회사 경계: separate repo.
- 개인 multi-server/multi-agent 환경: internal `llm` namespace.
- 처음에는 internal namespace로 시작하고, 권한·크기·협업 문제가 실제로 생기면 separate repo로 분리한다.

## Trust Boundary For Internal Namespace

Internal namespace를 선택해도 agent가 personal wiki 전체를 bulk-load하면 안 된다.

권장 규칙:

```text
- canonical: 안정 정책과 agent entry point
- reviewed/llm: 검토된 codebase/ops 지식
- generated/llm: 미검토 compiled context
- inbox/llm: 빠른 원천 메모
- generated/inbox 일반 영역: 미검토 개인 자료, 기본 bulk-load 금지
```

Agent는 가장 작은 entry point만 읽는다:

1. `AGENTS.md`
2. `wiki/canonical/agent-context.md` 또는 equivalent
3. 관련 `wiki/reviewed/llm/**` index
4. 없으면 관련 `wiki/generated/llm/**` page를 낮은 신뢰도로 확인

## Migration Pattern

Standalone `llm-wiki`를 이미 만들었다가 internal namespace로 바꿀 때:

1. standalone repo를 즉시 삭제하지 말고 compatibility shim으로 표시한다.
2. source of truth를 `personal-wiki/wiki/{generated,reviewed}/llm/**`로 선언한다.
3. agent instruction에서 `/path/to/llm-wiki` 참조를 internal namespace로 바꾼다.
4. 기존 standalone 내용은 검토 후 `generated/llm` 또는 `reviewed/llm`로 이동한다.
5. validation/health report가 internal namespace를 포함하는지 확인한다.

## Template

Internal namespace starter:

```text
wiki/generated/llm/
├── index.md
├── agents/
├── codebase/
│   └── <project>/
├── environments/
├── operations/
├── raw/
└── reference/
```

Separate repo starter:

```text
llm-wiki/
├── AGENTS.md
├── SCHEMA.md
├── index.md
├── log.md
├── raw/
├── compiled/
│   ├── codebase/
│   ├── environments/
│   └── operations/
├── reviewed/
└── canonical/
```

## Pitfall

Do not confuse “same repo” with “same trust level.” Internal namespace works only when path policy, frontmatter status, review flow, and context loading rules remain strict.
