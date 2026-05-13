---
name: moc-pattern
description: Map of Content(_index.md) 작성법과 구조 가이드
type: guide
updated: 2026-05-13
status: active
---

# MOC (Map of Content) 패턴

## MOC란

Map of Content. wiki 내 관련 페이지들을 연결하는 허브 페이지.

각 도메인의 `_index.md`가 MOC 역할을 한다. wiki에 처음 접근하는 사람이 어디서 시작해야 하는지 즉시 파악할 수 있게 한다.

## 언제 MOC를 만드는가

- 도메인 compile 완료 시 (7개 파일의 진입점으로)
- 관련 학습 노트가 5개 이상 쌓였을 때
- 한 주제에 대해 여러 관점의 파일이 생겼을 때

## 표준 구조

```markdown
---
name: <domain>-index
description: <도메인 이름> 도메인 MOC
type: index
domain: <your-domain>
compiled_at: YYYY-MM-DD
status: active
confidence: high
---

# <도메인 이름> — Map of Content

<도메인 한 줄 설명>

## 페이지

| 페이지 | 줄 수 | confidence | 한 줄 요약 |
|--------|-------|------------|-----------|
| [overview](./overview.md) | 85 | high | 도메인 정의와 핵심 개념 |
| [domain-rules](./domain-rules.md) | 150 | high | 비즈니스 규칙 |
| [db-schema](./db-schema.md) | 200 | high | 테이블 구조 |
| [api-contracts](./api-contracts.md) | 180 | high | API 엔드포인트 명세 |
| [code-map](./code-map.md) | 100 | high | 파일별 책임 매핑 |
| [known-issues](./known-issues.md) | 120 | medium | 알려진 이슈 |

## 빠른 진입

| 작업 | 파일 |
|------|------|
| "이 도메인 처음 봐요" | [overview](./overview.md) |
| "비즈니스 규칙이 뭐죠?" | [domain-rules](./domain-rules.md) |
| "어떤 테이블 쓰나요?" | [db-schema](./db-schema.md) |
| "특정 이슈 원인은?" | [known-issues](./known-issues.md) |

## 출처

- 소스 파일 N개
- 비즈니스 문서: docs/requirements/<domain>.md

## 보완 필요

compile 결과에서 발견된 "확인 필요" 항목 목록.
INPUT에 추가하면 해결 가능한 파일 명시.

## 부수 발견

compile 중 발견한 코드 품질 이슈나 주목할 만한 사항.
```

## MOC 작성 원칙

### 1. 빠른 진입 표는 필수

단순히 모든 파일을 나열하는 것이 아니라, **질문 기반 진입**을 제공한다.

좋은 예:
```
| "주문 취소 시 재고가 복원되나요?" | [domain-rules §재고 관리](./domain-rules.md#재고-관리) |
```

나쁜 예:
```
| domain-rules | [domain-rules](./domain-rules.md) |
```

### 2. 줄 수와 confidence는 유지보수 신호

페이지 목록에 줄 수와 confidence를 표시해두면, MOC를 보는 것만으로 어떤 파일이 오래되었거나 불확실한지 파악할 수 있다.

### 3. 보완 필요 섹션은 열린 TODO

compile이 완벽하지 않음을 솔직하게 기록한다. "다음 compile 시 이 INPUT을 추가하면 X개 항목이 해결된다"는 정보가 담겨야 한다.

### 4. 부수 발견은 별도 섹션

compile 중 우연히 발견한 코드 이슈, 규칙 위반 등은 `known-issues.md`에 적는 것과 별도로, MOC에도 요약한다. 의도된 부산물 캡처.

## MOC vs 일반 페이지

| 구분 | MOC (_index.md) | 일반 페이지 |
|------|-----------------|------------|
| type | index | compiled / learn / ... |
| 내용 | 링크 + 표 + 요약 | 실제 내용 |
| 작성자 | 메인 에이전트 직접 | LLM compile |
| 갱신 주기 | compile 때마다 | 내용 변경 시 |
| 줄 수 | ~50줄 | 50-200줄 |

## 예시

전체 예시는 [examples/compiled-codebase/sample-domain/_index.md](../../examples/compiled-codebase/sample-domain/_index.md) 참조.

## 다음

멀티 티어 메모리: [04-multi-tier-memory.md](./04-multi-tier-memory.md)
