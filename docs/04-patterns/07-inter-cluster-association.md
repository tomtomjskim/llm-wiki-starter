---
name: inter-cluster-association
description: 서로 다른 지식 클러스터를 bridge note로 연결해 창발성을 높이는 패턴
type: guide
updated: 2026-06-01
status: active
---

# Inter-Cluster Association

Inter-cluster association은 서로 다른 지식 클러스터 사이에 명시적인 연결을 만드는 패턴이다. 목적은 그래프를 복잡하게 만드는 것이 아니라, 평소에는 따로 보던 자료 사이에서 새 질문과 결정을 끌어내는 것이다.

## Core Idea

일반 링크는 같은 주제 안에서 이동하게 해준다. Inter-cluster association은 다른 주제 사이를 건너가게 해준다.

예시:

| Cluster A | Cluster B | Association |
|---|---|---|
| journal | career | 반복 감정/몰입 패턴이 취업 전략에 주는 신호 |
| projects | career | 프로젝트 결과물이 이력서 증거가 되는 방식 |
| learning | projects | 학습한 개념이 실제 구현으로 바뀌는 지점 |
| sources | decisions | 원본 기록에서 반복 결정으로 승격할 내용 |
| school | projects | 수업/과제에서 제품화 가능한 아이디어 |

## Bridge Note

Bridge note는 두 개 이상의 cluster를 연결하는 작은 노트다.

```markdown
---
name: journal-to-career-patterns
description: 일기 패턴을 취업 전략과 연결하는 bridge note
type: pattern
updated: 2026-06-01
status: draft
confidence: medium
cluster: bridge
tags: [journal, career, bridge]
related:
  - [[Journal Hub]]
  - [[Career Hub]]
---

# Journal to Career Patterns

## Association

일기에서 반복되는 에너지, 회피, 몰입 패턴을 취업 준비 루틴과 연결한다.

## Evidence

- [[2026-06-weekly-review]]
- [[Career Hub]]

## Questions

- 반복적으로 미루는 작업은 무엇인가?
- 몰입이 높았던 프로젝트 유형은 무엇인가?
- 지원 전략에 반영할 제약은 무엇인가?

## Next Action

- 이력서/포트폴리오 작업 시간을 에너지가 높은 시간대로 옮긴다.
```

## Association Types

| Type | Use When | Example |
|---|---|---|
| evidence | 한 영역의 기록이 다른 영역의 주장을 증명함 | project commit -> resume claim |
| transfer | 한 영역의 원리를 다른 영역에 적용함 | paper concept -> product feature |
| tension | 두 영역이 충돌함 | career goal vs current routine |
| synthesis | 여러 영역에서 반복 패턴을 추출함 | journal + projects + learning |
| decision | 연결이 실제 선택으로 이어짐 | choose portfolio project |

Bridge note의 제목에는 연결 방향이 드러나야 한다. `Projects to Career Evidence`처럼 A와 B가 모두 보이면 graph에서도 역할이 명확하다.

## Graph Signals

좋은 graph signal:

- bridge note가 최소 2개 cluster hub를 연결한다.
- source 원본보다 interpreted note가 중심이 된다.
- Home은 입구이고, 모든 노드의 중심이 아니다.
- hub별로 active question이 유지된다.

나쁜 graph signal:

- 모든 노트가 Home에만 붙어 있다.
- `sources/` 원본이 graph 중심이 된다.
- bridge note가 너무 많아져 실제 질문이 사라진다.
- link가 많지만 next action이 없다.

## Weekly Review

주간 리뷰에서 bridge note를 10분만 점검한다.

질문:

1. 이번 주 새로 연결된 cluster는 무엇인가?
2. bridge가 실제 action이나 decision으로 이어졌는가?
3. 반복되는 bridge를 reviewed note로 승격할 가치가 있는가?
4. 끊어야 할 억지 연결은 무엇인가?

## LLM Prompt

```text
내 vault의 notes/ 하위 노트 목록과 최근 7일 노트를 보고
inter-cluster association 후보를 5개 이하로 제안해줘.

규칙:
- source 원본을 사실로 확정하지 말 것.
- 서로 다른 cluster를 잇는 후보만 제안할 것.
- 각 후보마다 bridge note 제목, 연결 cluster, 근거 노트, 다음 질문을 제시할 것.
- 민감 정보 원문은 포함하지 말 것.
```

## When Not To Use

- 노트가 20개 미만이면 Home과 area hub만으로 충분하다.
- source import가 아직 불안정하면 bridge보다 source hygiene을 먼저 한다.
- graph view를 외부 공개하려면 민감정보 제거와 metadata 축약이 먼저다.

## Next

- 단계별 도입: [SecondBrain Migration Stages](../03-workflow/05-second-brain-migration.md)
- MOC 구조: [MOC 패턴](./03-moc-pattern.md)
- View 단계: [View](../03-workflow/03-view.md)
