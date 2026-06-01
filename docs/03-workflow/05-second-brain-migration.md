---
name: second-brain-migration
description: 개인 자료를 한 번에 옮기지 않고 단계별 SecondBrain으로 전환하는 버전별 실행 계획
type: guide
updated: 2026-06-01
status: active
---

# SecondBrain Migration Stages

개인 자료를 모두 한 번에 wiki에 넣으면 정리 비용과 민감정보 위험이 커진다. 이 문서는 Obsidian vault 하나를 SecondBrain으로 키울 때의 단계별 버전 계획이다.

## Version Ladder

| Version | Goal | Minimum Output | Stop Condition |
|---|---|---|---|
| v0 Capture | 안전한 수집 구조 만들기 | `sources/`, `notes/`, `Home.md` | 원본과 해석본이 분리됨 |
| v1 Hub | 주요 영역을 탐색 가능하게 만들기 | Home, area hubs, source index | Obsidian에서 3분 안에 원하는 영역 진입 |
| v2 Bridge | 클러스터 간 연결 시작 | bridge note 3-5개 | 새로운 질문이 생김 |
| v3 Graph | 그래프로 구조 관찰 | graph review checklist | orphan과 bridge를 구분 가능 |
| v4 Automation | 링크 품질 자동 점검 | graph JSON, broken-link/orphan report | 수동 리뷰 부담 감소 |
| v5 Emergence | 반복 연결을 장기 지식으로 승격 | monthly synthesis, reviewed decisions | 행동/전략이 바뀜 |

각 버전은 독립적으로 멈춰도 된다. 모든 사용자가 v5까지 갈 필요는 없다.

## v0 Capture

목표는 "많이 정리하기"가 아니라 "잘못 섞이지 않게 받기"다.

작업:

1. [SecondBrain Profile](../02-setup/06-second-brain-profile.md)의 폴더를 만든다.
2. `sources/`는 import 원본만 둔다.
3. `notes/`에는 직접 해석한 노트만 둔다.
4. Home에는 hub 링크만 둔다.

처음부터 Notion, email, PDF 전체를 넣지 않는다. 가장 자주 쓰는 source 1-2개만 pilot으로 넣는다.

완료 기준:

- source 원본을 수정하지 않는다.
- notes가 source를 복사한 것이 아니라 해석한 내용이다.
- Home에서 주요 영역으로 이동할 수 있다.

## v1 Hub

목표는 탐색 가능한 최소 지도다.

필수 hub:

- `[[Career Hub]]`
- `[[Projects Hub]]`
- `[[Learning Hub]]`
- `[[Journal Hub]]`
- `[[Decisions Hub]]`
- `[[Sources Index]]`
- `[[Bridge Notes]]`

각 hub는 다음 3가지만 갖는다.

```markdown
## Active Questions
## Notes
## Bridges
```

hub가 너무 길어지면 index가 아니라 archive가 된 것이다. 최신 질문과 핵심 링크만 남긴다.

## v2 Bridge

목표는 inter-cluster association을 실제 노트로 만드는 것이다.

처음 만들 bridge 예시:

| Bridge | Connects | Question |
|---|---|---|
| `Journal to Career Patterns` | journal, career | 에너지/몰입 패턴이 취업 전략에 주는 신호는 무엇인가 |
| `Projects to Career Evidence` | projects, career | 어떤 프로젝트가 이력서의 증거가 되는가 |
| `Learning to Projects` | learning, projects | 학습한 개념이 어떤 구현으로 이어지는가 |
| `Sources to Decisions` | sources, decisions | 원본 기록에서 반복 결정으로 승격할 내용은 무엇인가 |

bridge note는 5개 이하로 시작한다. 너무 많으면 연결의 질보다 관리 비용이 커진다.

## v3 Graph

목표는 그래프를 예쁘게 만드는 것이 아니라 구조 문제를 찾는 것이다.

Obsidian graph에서 확인할 것:

- Home에 모든 노드가 직접 붙어 있지 않은가
- hub 없이 고립된 중요한 노트가 있는가
- `sources/` 원본이 해석 없이 중심 노드가 되고 있지 않은가
- bridge note가 서로 다른 cluster를 실제로 잇고 있는가

권장 필터:

```text
path:notes/
path:notes/bridges/
path:sources/
tag:#career
tag:#projects
```

## v4 Automation

노트가 30-50개 이상 쌓인 뒤에만 자동화를 붙인다.

자동화 후보:

- `[[wikilink]]`와 Markdown link를 파싱해 `meta/graph/graph.json` 생성
- broken link report
- orphan note report
- frontmatter `cluster`별 노드 수 집계
- bridge note가 최소 2개 cluster를 참조하는지 검사

자동화는 source 원본을 수정하지 않는다. 파생 report만 생성한다.

## v5 Emergence

창발성은 그래프의 모양이 아니라 새 결정과 행동 변화로 확인한다.

월간 synthesis 질문:

- 이번 달 가장 반복된 연결은 무엇인가
- 예상 못한 cluster 조합은 무엇인가
- 어떤 bridge가 실제 프로젝트/취업/학습 행동을 바꿨는가
- reviewed decision 또는 policy로 승격할 내용은 무엇인가
- 삭제하거나 archive할 연결은 무엇인가

산출물:

```text
notes/decisions/YYYY-MM-monthly-synthesis.md
notes/bridges/<stable-bridge>.md
```

## Choosing Your Starting Version

| Situation | Start At |
|---|---|
| 자료가 흩어져 있고 구조가 없다 | v0 |
| 이미 Obsidian을 쓰지만 그래프가 의미 없다 | v1 |
| 노트는 많은데 새로운 질문이 안 나온다 | v2 |
| 노트가 50개 이상이고 유지보수가 어렵다 | v3 |
| broken link와 orphan이 반복된다 | v4 |
| 전략/행동 변화까지 기록하고 싶다 | v5 |

## Next

- 구조 만들기: [SecondBrain Profile](../02-setup/06-second-brain-profile.md)
- 연결 원리: [Inter-Cluster Association](../04-patterns/07-inter-cluster-association.md)
- 보기 단계: [View](./03-view.md)
