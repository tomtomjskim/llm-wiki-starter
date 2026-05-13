---
name: compile
description: 4단계 파이프라인 2단계 — LLM compile 프롬프트 패턴과 4슬롯 구조
type: guide
updated: 2026-05-13
status: active
---

# 2단계: Compile (컴파일)

## 개요

LLM이 `raw/` 또는 코드베이스를 읽고 구조화된 `compiled/` markdown을 생성하는 단계.

인간의 역할: LLM에 **무엇을 읽을지**와 **어디에 출력할지**를 지시하는 것뿐.

처음이라면 실습 문서부터 진행: [00-first-compile-walkthrough.md](./00-first-compile-walkthrough.md)

## 4슬롯 프롬프트 패턴

검증된 Compile 프롬프트 구조. 4개 슬롯으로 구성된다.

```
[SCOPE]
무엇을 compile하는가, 출력 위치는 어디인가.

[RULES]
LLM이 따라야 할 제약 조건.

[TASK]
입력 자산 목록과 각 출력 파일의 사양.

[RETURN]
완료 후 메인에 보고할 내용.
```

## 코드베이스 Compile 예시

```
[SCOPE]
`src/orders/` 디렉토리의 코드를 읽고
`~/wiki/compiled/codebase/orders/` 에 wiki를 생성해줘.

[RULES]
- 추측 금지. 코드에서 확인 불가한 내용은 "확인 필요"로 표시
- 각 파일 200줄 이하 (초과 시 자연스럽게 분할)
- 모든 파일에 frontmatter 필수 (name, description, type: compiled, updated, confidence)
- frontmatter는 `templates/frontmatter/compiled.md`와 [docs/04-patterns/02-frontmatter-spec.md](../04-patterns/02-frontmatter-spec.md)를 따른다.
- DB 스키마는 실제 DESCRIBE/SHOW COLUMNS로 검증
- 코드 수정 금지 — 읽기와 문서화만

[TASK]
입력:
- src/orders/ 전체
- docs/requirements/orders.md (비즈니스 요구사항, 있으면)

출력 7개 파일:
- _index.md: MOC (맵), 빠른 진입 표 포함 (~50줄)
- overview.md: 도메인 정의, 핵심 개념, 도메인 경계, 진입점 (50-100줄)
- domain-rules.md: 비즈니스 규칙 — Why + How (100-200줄)
- db-schema.md: 테이블/컬럼/인덱스/외래키 (100-250줄)
- api-contracts.md: 엔드포인트 목록, 요청/응답 스키마 (100-200줄)
- code-map.md: 파일별 책임 매핑 (50-150줄)
- known-issues.md: 알려진 이슈, 주의 사항, 기술 부채 (50-150줄)

[RETURN]
- 작성 파일 목록 + 실제 줄 수
- 검증한 DB 테이블 목록
- "확인 필요" 항목 목록 (보완 필요 내용)
- 다음 compile 시 추가하면 좋을 input 파일
```

## 학습 노트 Compile 예시

```
[SCOPE]
~/wiki/raw/papers/ 의 A-MEM 논문 PDF를 읽고
~/wiki/personal/learn/a-mem-summary.md 를 작성해줘.

[RULES]
- frontmatter: type: learn, updated: 오늘 날짜
- 200줄 이하
- 인용 가능한 핵심 주장만 (저자 원문 표현 그대로)
- 내 의견은 "## 내 생각" 섹션에 별도로

[TASK]
1. 논문의 핵심 contribution 3개 추출
2. 아키텍처 다이어그램 텍스트로 재현
3. 기존 방법론과 비교 표
4. 이 wiki 시스템에 적용 가능한 아이디어

[RETURN]
작성 파일 경로 + 줄 수
```

## 도메인당 예상 비용

코드베이스 compile 기준 (실전 측정치):

| 항목 | 수치 |
|------|------|
| 입력 토큰 | 50-80K (소스 코드) |
| 출력 토큰 | 30-50K (7개 파일) |
| 총 처리 | 80-120K 토큰 |
| 소요 시간 | 5-10분 |

소규모 도메인 (파일 10개 이하)은 더 빠르다.

## 메인 검증 절차

LLM이 compile을 완료하면 다음 3단계를 인간이 검증한다.

### 1. 구조 검증

```bash
ls ~/wiki/compiled/codebase/orders/
# _index.md, overview.md, domain-rules.md, db-schema.md,
# api-contracts.md, code-map.md, known-issues.md 확인

wc -l ~/wiki/compiled/codebase/orders/*.md
# 각 파일 200줄 이하 확인
```

### 2. Spot Check

- `overview.md`: 도메인 정의가 실제 코드와 일치하는가?
- `known-issues.md`: 추론으로 작성된 내용이 `confidence: medium` 으로 표시되었는가?

### 3. MOC 작성 또는 확인

`_index.md`가 모든 산출물을 올바르게 링크하고, "빠른 진입" 표가 있는지 확인.

## 안티패턴

- raw 없이 기억에 의존해서 compile 요청 (사실 오류 위험)
- 200줄 제한을 강제로 지키다 정보를 압축 (분할이 낫다)
- compile 결과를 검증 없이 바로 신뢰 (spot check 필수)
- 도메인 전체를 한 파일에 몰아넣기

## 다음

View 단계: [03-view.md](./03-view.md)
