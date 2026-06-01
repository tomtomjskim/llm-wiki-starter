---
name: wiki-health-guardrails
description: 개인 wiki가 커질 때 CI, validator, health report, hub layer로 품질을 유지하는 운영 패턴
type: guide
updated: 2026-06-01
status: active
---

# Wiki Health Guardrails

wiki가 30-50개 문서를 넘기기 시작하면 frontmatter lint만으로는 부족하다. 이 문서는 personal wiki를 실제 운영하면서 발견한 guardrail 패턴을 starter kit에 일반화한 것이다.

## 핵심 문제

잘못된 wiki는 보통 다음 순서로 망가진다.

1. CI는 통과하지만 `related` 링크가 깨진다.
2. `review_after`가 필드로만 존재하고 실제 review queue가 되지 않는다.
3. `reviewed` 문서가 generated draft 문구를 그대로 가진다.
4. 긴 구현 spec이 reviewed memory에 들어와 검색과 AI context를 오염시킨다.
5. Home/index는 정책만 담고, 실제 project/environment/operation hub가 없다.
6. context export가 generated/inbox까지 섞어 외부 AI에 넘긴다.

## Minimum Guardrails

### 1. Stronger Validator

기본 frontmatter 검사에 다음을 추가한다.

- `date`와 `review_after` 형식 검사
- generated/reviewed/canonical 문서의 non-empty `review_after`
- `source`, `status`, `confidence` enum 검사
- `tags`, `related` list type 검사
- `related` 내부 Markdown path 존재 여부 검사
- `archive/` 경로는 `status: archived`로 강제
- bearer token, GitHub token, Slack token, AWS access key 등 obvious secret pattern 검사

### 2. Health Report

validator는 fail/pass 용도다. 운영 판단은 read-only health report가 맡는다.

권장 지표:

```text
files by status
files by confidence
files by source
blank review_after count
due review count
open checkbox action count
largest documents
zero inbound non-index docs
markdown link count
wikilink count
```

health report는 CI에서 실행해도 실패시키지 않는 것이 좋다. 실패는 validator가 담당하고, health report는 추세와 운영 품질을 보여준다.

### 3. CI Parity

CI와 local autopush가 서로 다른 검사를 하면 한쪽에서만 실패하는 일이 생긴다.

권장 CI 단계:

```yaml
- uses: actions/checkout@v4
  with:
    fetch-depth: 2

- name: Check committed whitespace
  run: git diff --check HEAD^ HEAD

- name: Validate wiki
  run: python3 scripts/validate_wiki.py

- name: Wiki health report
  run: python3 scripts/wiki_health_report.py
```

`fetch-depth: 1`에서는 부모 commit이 없어 whitespace check가 전체 tree 검사처럼 동작할 수 있다. commit-range 검사를 하려면 parent를 가져와야 한다.

### 4. Generated Hub Layer

reviewed/canonical hub를 바로 만들지 않는다. 먼저 generated hub draft를 둔다.

```text
wiki/generated/hubs/projects-hub.md
wiki/generated/hubs/environments-hub.md
wiki/generated/hubs/operations-hub.md
wiki/generated/hubs/digests-hub.md
wiki/generated/hubs/bridges-hub.md
```

Home/index에는 이 hub들이 draft임을 명시하고 링크한다. 실제로 한두 주 사용한 뒤 reviewed hub로 승격한다.

### 5. Reviewed Anti-Bloat Rule

reviewed 문서는 durable memory여야 한다.

권장 shape:

```text
# Title

## Verified Facts
## Durable Takeaways
## Source Links
## Open Questions
## Next Review
```

피해야 할 것:

- 1,000줄 이상의 구현 spec
- generated draft 문구
- “not reviewed yet” 문구가 남은 reviewed 문서
- source 없이 “current state”라고 말하는 portfolio claim

긴 spec은 project repo나 generated 문서에 두고, reviewed에는 1-2 page summary와 링크만 둔다.

### 6. Export Boundary

AI context export는 기본적으로 canonical/reviewed만 포함한다.

Project profile은 다음처럼 동작해야 한다.

```text
core canonical docs
+ canonical/reviewed files whose frontmatter project matches the requested project
```

Generated/inbox를 포함하려면 `--include-generated` 또는 `--include-inbox`처럼 명시 flag를 요구한다. Manifest에도 unreviewed material이 포함됐다고 표시한다.

## Remediation Order

| Priority | Fix | Why |
|---|---|---|
| P0 | validator: `related`, `review_after`, obvious secret patterns | CI가 구조 오염을 즉시 잡음 |
| P1 | generated hub drafts | graph view를 실제 탐색 구조로 바꿈 |
| P2 | health report | 운영 품질을 수치로 봄 |
| P3 | reviewed cleanup | AI가 over-trust하지 않게 함 |
| P4 | export boundary | 외부 AI에 미검토 자료가 섞이지 않게 함 |

## LLM Audit Prompt

```text
이 wiki를 다섯 관점에서 적대적으로 검수해줘.

1. sync/push/CI reliability
2. schema/validation/privacy
3. content quality/promotion discipline
4. graph/MOC/SecondBrain architecture
5. operational usage cadence

각 관점은 findings를 severity, evidence path, concrete fix로 정리해줘.
파일 수정은 하지 말고 audit report 후보만 작성해줘.
```

## Next

- Linting 기본: [LLM Linting](./05-llm-linting.md)
- Hub/bridge 전략: [Inter-Cluster Association](./07-inter-cluster-association.md)
- 단계별 도입: [SecondBrain Migration Stages](../03-workflow/05-second-brain-migration.md)
