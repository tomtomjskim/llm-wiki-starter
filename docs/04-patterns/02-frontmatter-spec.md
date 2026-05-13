---
name: frontmatter-spec
description: LLM-friendly wiki 파일의 YAML frontmatter 표준 스펙
type: guide
updated: 2026-05-13
status: active
---

# Frontmatter 표준 스펙

모든 wiki 파일의 최상단에 붙이는 YAML frontmatter 규칙.

## 필수 필드

```yaml
---
name: kebab-case-slug        # 필수, 파일명과 일치
description: 한 줄 요약        # 필수, 검색·인덱스에 사용
type: <타입>                  # 필수 (아래 타입 목록 참조)
updated: YYYY-MM-DD          # 필수, 마지막 수정일
---
```

## 전체 필드 목록

```yaml
---
# 필수
name: kebab-case-slug
description: 한 줄 요약
type: compiled | learn | decision | journal | rule | pattern | guide | index | meta | project
updated: YYYY-MM-DD

# 권장
status: active | draft | deprecated | needs-update
confidence: high | medium | low

# compiled 타입 전용
domain: <your-domain>
source_files:
  - src/<domain>/file.js
compiled_at: YYYY-MM-DD
compiled_by: claude-developer
ground_truth_refs:
  - docs/requirements/<domain>.md

# 선택
tags: [tag1, tag2]
llm_priority: high | medium | low
source: url | file-path | session-id
---
```

## Type 목록

| type | 의미 | 예시 |
|------|------|------|
| `compiled` | LLM이 코드/raw를 읽고 생성한 wiki | `overview.md`, `domain-rules.md` |
| `learn` | 개인 학습 노트 | `karpathy-llm-wiki-pattern.md` |
| `decision` | 기술/아키텍처 결정 기록 | `2026-05-chose-git-sync.md` |
| `journal` | 일일 진행 메모 | `2026-05-13.md` |
| `rule` | 코딩·작업 규칙 | `no-inline-sql.md` |
| `pattern` | 코드/작업 패턴 | `api-response-format.md` |
| `guide` | 가이드라인 (이 파일처럼) | `frontmatter-spec.md` |
| `index` | 다른 파일들의 MOC | `_index.md` |
| `meta` | wiki 시스템 자체 메타 문서 | `_frontmatter-spec.md` |
| `project` | 프로젝트 컨텍스트 스냅샷 | `project-arch.md` |

## Status 필드

| 값 | 의미 |
|----|------|
| `active` | 현재 유효, 신뢰 가능 |
| `draft` | 초안, 검증 전 |
| `deprecated` | 더 이상 유효하지 않음 |
| `needs-update` | Ask 단계에서 보완 필요 발견 |

## Confidence 필드

| 값 | 의미 | 언제 사용 |
|----|------|----------|
| `high` | 코드/DB/문서로 검증 완료 | 사실 확인된 정보 |
| `medium` | 1-2회 적용, 추론 포함 | 코드 의도를 추론한 경우 |
| `low` | 최근 생성, 미검증 | 처음 compile한 초안 |

compiled 파일의 `known-issues.md`는 거의 항상 `confidence: medium`이다. 알려진 이슈 자체는 사실이지만, 원인 분석과 영향 범위는 추론을 포함하기 때문이다.

## LLM Priority 필드

Claude Code memory 시스템에서 자동 로드 우선순위를 결정한다.

| 값 | 의미 |
|----|------|
| `high` | 모든 세션에서 사전 로드 권장 |
| `medium` | 도메인 매치 시 로드 |
| `low` | 명시 요청 시만 로드 |

일반 wiki 페이지에는 생략해도 된다. memory 파일에서 주로 사용.

## Linting 자동 점검 항목

`scripts/lint-frontmatter.py`가 검사하는 항목:

- `name` 필드 없음 → ERROR
- `description` 필드 없음 → ERROR
- `type` 필드 없음 → ERROR
- `updated` 누락 또는 90일 초과 → WARNING (stale)
- 템플릿의 `updated: YYYY-MM-DD` placeholder → 검사 제외
- `confidence: low` + 30일 초과 → WARNING
- `status: deprecated` → INFO (정리 후보)

## 예시: compiled 파일

```yaml
---
name: orders-overview
description: 주문 도메인 정의, 핵심 개념, 진입점
type: compiled
domain: orders
source_files:
  - src/orders/OrderHandler.js
  - src/orders/OrderRepository.js
compiled_at: 2026-05-13
compiled_by: claude-developer
confidence: high
status: active
updated: 2026-05-13
---
```

## 예시: 학습 노트

```yaml
---
name: a-mem-summary
description: A-MEM 논문 핵심 정리 (arXiv 2502.12110)
type: learn
tags: [llm, memory, agent]
updated: 2026-05-13
status: active
confidence: medium
source: https://arxiv.org/abs/2502.12110
---
```

## 예시: 결정 기록

```yaml
---
name: 2026-05-chose-git-sync
description: wiki 동기화 방식으로 Git 기반 선택한 이유
type: decision
updated: 2026-05-13
status: active
---
```

## 다음

MOC 패턴: [03-moc-pattern.md](./03-moc-pattern.md)
