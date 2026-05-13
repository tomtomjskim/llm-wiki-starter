---
name: view
description: 4단계 파이프라인 3단계 — Obsidian 그래프/검색/MOC 활용법
type: guide
updated: 2026-05-13
status: active
---

# 3단계: View (탐색)

## 개요

Obsidian으로 compiled wiki를 탐색한다. 인간이 wiki를 소비하는 단계.

## 그래프 뷰

`Cmd+G` (macOS) 로 열리는 그래프 뷰는 페이지 간 링크를 시각화한다.

### 활용 방법

**도메인 클러스터 확인:**
- 같은 도메인의 7개 파일이 `_index.md`를 중심으로 클러스터를 형성하면 정상
- 고립된 노드(orphan)는 MOC에 링크가 빠진 것 — 보완 필요

**필터 사용:**
```
그래프 뷰 → 필터 패널 → Path 필터
path:compiled/codebase/orders  — orders 도메인만 표시
```

**링크 깊이 조정:**
- Depth 1: 선택 파일과 직접 연결된 파일만
- Depth 2-3: 간접 연결까지 — 도메인 간 의존성 파악에 유용

## 전문 검색

`Cmd+Shift+F` 로 vault 전체를 전문 검색한다.

### 검색 팁

```
# frontmatter 검색
type:compiled confidence:low

# 경로 한정
path:compiled/codebase/ users

# 태그 검색
tag:#needs-review

# 특정 내용 검색
"확인 필요"
```

LLM이 "확인 필요"로 표시한 항목을 한 번에 찾을 때 유용하다.

## MOC (Map of Content) 활용

`_index.md`는 도메인의 진입점이자 내비게이션 허브다.

```markdown
## 빠른 진입

| 작업 | 파일 |
|------|------|
| "이 도메인 처음 봐요" | [overview.md](./overview.md) |
| "DB 테이블이 뭐죠?" | [db-schema.md](./db-schema.md) |
| "API 명세 주세요" | [api-contracts.md](./api-contracts.md) |
```

MOC를 잘 작성해두면 "도메인에 처음 접근할 때 어디서 시작해야 하는가"를 즉시 알 수 있다.

## Dataview 플러그인 활용

Dataview가 설치되어 있으면 동적 쿼리로 wiki를 탐색할 수 있다.

### 예시: 최근 갱신된 파일

```dataview
table description, updated, confidence
from "compiled/codebase"
sort updated desc
limit 10
```

### 예시: 확인이 필요한 항목

```dataview
table description
from "compiled"
where confidence = "medium" or confidence = "low"
sort updated asc
```

### 예시: 특정 도메인 목록

```dataview
list
from "compiled/codebase/orders"
where type = "compiled"
```

## 백링크 패널

파일을 열면 우측 패널에 백링크가 표시된다. "어떤 파일이 이 파일을 참조하는가"를 즉시 확인할 수 있다.

코드베이스 compile의 경우, `domain-rules.md`가 `db-schema.md`와 `api-contracts.md` 모두에서 참조되어야 자연스러운 연결이다. 백링크가 없는 파일은 orphan일 가능성이 높다.

## Outline 패널

`Cmd+P` → "Outline" 으로 현재 파일의 헤딩 구조를 탐색 패널로 표시한다. 200줄 이하의 atomic 파일이라면 크게 필요하진 않지만, domain-rules.md 같이 구조가 복잡한 파일에서 유용하다.

## 다음

Ask 단계: [04-ask.md](./04-ask.md)
