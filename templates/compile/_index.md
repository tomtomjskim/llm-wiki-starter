---
name: <domain>-index
description: <도메인 이름> 도메인 MOC
type: index
domain: <your-domain>
compiled_at: YYYY-MM-DD
status: active
confidence: high
updated: YYYY-MM-DD
---

# <도메인 이름> — Map of Content

{도메인 한 줄 정의. 무엇을 하는 도메인인가.}

## 페이지

| 페이지 | 줄 수 | confidence | 한 줄 요약 |
|--------|-------|------------|-----------|
| [overview](./overview.md) | - | high | 도메인 정의, 핵심 개념, 진입점 |
| [domain-rules](./domain-rules.md) | - | high | 비즈니스 규칙 |
| [db-schema](./db-schema.md) | - | high | 테이블/컬럼/인덱스 |
| [api-contracts](./api-contracts.md) | - | high | API 엔드포인트 명세 |
| [code-map](./code-map.md) | - | high | 파일 → 책임 매핑 |
| [known-issues](./known-issues.md) | - | medium | 알려진 이슈·위험 요소 |

## 빠른 진입

| 작업 또는 질문 | 파일 |
|--------------|------|
| "이 도메인 처음 봐요" | [overview](./overview.md) |
| "비즈니스 규칙이 뭐죠?" | [domain-rules](./domain-rules.md) |
| "어떤 테이블 쓰나요?" | [db-schema](./db-schema.md) |
| "API 명세 주세요" | [api-contracts](./api-contracts.md) |
| "X 이슈 원인이 뭐죠?" | [known-issues](./known-issues.md) |

## 출처

- 소스 파일 N개: `src/<your-domain>/`
- 비즈니스 문서: `docs/requirements/<your-domain>.md` (있으면)
- compile 일시: YYYY-MM-DD

## 보완 필요

{compile 결과에서 "확인 필요"로 표시된 항목 목록.}
{INPUT에 추가하면 해결 가능한 파일 명시.}

예:
- `config/app-config.js` — 전역 설정값 확인 필요 (N건)
- `src/common/utils.js` — 공통 유틸리티 함수 시그니처 확인

## 부수 발견

{compile 중 우연히 발견한 코드 품질 이슈나 주목할 사항.}
{없으면 이 섹션 삭제.}
