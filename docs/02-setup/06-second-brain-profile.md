---
name: second-brain-profile
description: Obsidian vault 하나를 notes/sources/Home 구조로 운영하는 SecondBrain profile
type: guide
updated: 2026-06-01
status: active
---

# SecondBrain Profile

이 profile은 Obsidian vault 하나를 개인 SecondBrain으로 쓰고 싶은 사용자를 위한 선택 구조다. 기본 starter의 `raw/personal/compiled` 3-tier 구조를 대체하기보다, 개인 자료 중심 vault에 맞게 이름과 운영 흐름을 바꾼다.

## 언제 이 profile을 쓰는가

- 일기, 취업 준비, 프로젝트, 학교 자료, PDF, 이메일, Notion export를 한 vault에서 보고 싶다.
- 원본 자료와 사람이 해석한 노트를 분리하고 싶다.
- Obsidian graph view에서 지식 클러스터와 연결을 보고 싶다.
- 코드베이스 compile보다 개인 지식 관리가 주된 목적이다.

코드베이스 문서화가 주 목적이면 기본 `raw/personal/compiled` 구조를 먼저 쓴다.

## Vault Layout

```text
~/SecondBrain/
├── Home.md
├── notes/
│   ├── journal/
│   ├── career/
│   ├── projects/
│   ├── learning/
│   ├── decisions/
│   └── bridges/
├── sources/
│   ├── notion/
│   ├── email/
│   ├── github/
│   ├── gachon/
│   └── pdfs/
├── meta/
│   ├── templates/
│   └── graph/
└── assets/
```

## Directory Rules

| Path | Purpose | Write Rule |
|---|---|---|
| `Home.md` | 첫 화면, 허브 | 사람이 직접 관리 |
| `notes/` | 해석된 지식 | 사람 작성 또는 LLM 보조 후 검토 |
| `notes/bridges/` | 서로 다른 클러스터를 잇는 연결 노트 | 초안은 작게, 주간 리뷰 |
| `sources/` | sync/import 원본 | 편집 금지, 가능하면 local-only |
| `meta/templates/` | 노트 템플릿 | 안정화 후 수정 |
| `meta/graph/` | graph export, link report | 파생물, 공개 전 민감정보 제거 |
| `assets/` | 이미지/PDF 첨부 | 원본 정책에 맞게 관리 |

## Home Hub

처음 Home은 짧게 둔다.

```markdown
# Home

## Areas

- [[Career Hub]]
- [[Projects Hub]]
- [[Learning Hub]]
- [[Journal Hub]]
- [[Decisions Hub]]
- [[Sources Index]]
- [[Bridge Notes]]

## This Week

- [[2026-06-weekly-review]]

## Bridge Prompts

- Which journal pattern should affect career strategy?
- Which project proves a skill claimed in career notes?
- Which source deserves a reviewed note?
- Which repeated decision should become policy?
```

Home은 모든 링크를 넣는 페이지가 아니다. 자주 쓰는 hub와 주간 focus만 둔다.

## Frontmatter Extension

기본 frontmatter에 cluster와 related를 추가하면 graph와 Dataview에서 다루기 쉽다.

```yaml
---
name: portfolio-project-selection
description: 취업 포트폴리오에 넣을 프로젝트 선택 기준
type: decision
updated: 2026-06-01
status: active
confidence: medium
cluster: career
tags: [career, portfolio, projects]
related:
  - [[Projects Hub]]
  - [[Career Hub]]
source:
  - sources/github/
---
```

`sources/` 원본은 지식으로 취급하지 않는다. 해석된 내용은 `notes/`에 따로 적고 source만 연결한다.

## Minimal Templates

### Area Hub

```markdown
---
name: career-hub
description: 취업 준비 관련 노트의 진입점
type: index
updated: 2026-06-01
status: active
cluster: career
---

# Career Hub

## Active Questions

- 어떤 역할을 목표로 하는가?
- 어떤 프로젝트가 증거로 가장 강한가?

## Notes

- [[Portfolio Project Selection]]
- [[Resume Evidence Map]]

## Bridges

- [[Journal to Career Patterns]]
- [[Projects to Career Evidence]]
```

### Bridge Note

```markdown
---
name: projects-to-career-evidence
description: 프로젝트 경험을 취업 증거로 연결하는 bridge note
type: pattern
updated: 2026-06-01
status: draft
confidence: medium
cluster: bridge
related:
  - [[Projects Hub]]
  - [[Career Hub]]
---

# Projects to Career Evidence

## Association

프로젝트 기록과 취업 문서 사이에서 반복되는 증거를 연결한다.

## Links

- Project side: [[Projects Hub]]
- Career side: [[Career Hub]]

## Review Questions

- 실제 결과물 URL이나 commit이 있는가?
- 이 경험이 이력서 문장으로 바뀔 수 있는가?
- 부족한 증거는 무엇인가?
```

## Trust Rule

SecondBrain profile에서도 trust flow는 유지한다.

```text
sources -> notes draft -> reviewed note -> policy/decision
```

LLM이 source를 요약할 수는 있지만, 검토되지 않은 요약을 장기 정책처럼 쓰면 안 된다.

## Next

- 단계별 도입: [SecondBrain Migration Stages](../03-workflow/05-second-brain-migration.md)
- 연결 패턴: [Inter-Cluster Association](../04-patterns/07-inter-cluster-association.md)
- Obsidian 설정: [Obsidian Vault 설정](./04-obsidian-vault-setup.md)
