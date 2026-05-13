---
name: codebase-compile
description: 코드베이스 도메인을 LLM-friendly wiki로 compile하는 검증된 패턴
type: guide
updated: 2026-05-13
status: active
---

# 코드베이스 Compile 패턴

실전에서 검증된 코드베이스 → wiki 변환 패턴. 도메인당 7개 표준 산출물을 생성한다.

## 표준 산출물 7개

| 파일 | 목적 | 권장 줄 수 | confidence 기준 |
|------|------|----------|----------------|
| `_index.md` | MOC, 진입점 | ~50 | 직접 작성 |
| `overview.md` | 도메인 정의, 경계, 진입점 | 50-100 | high |
| `domain-rules.md` | 비즈니스 규칙 (Why + How) | 100-200 | high |
| `db-schema.md` | 테이블/컬럼/인덱스 | 100-250 | high |
| `api-contracts.md` | 엔드포인트 명세 | 100-200 | high |
| `code-map.md` | 파일 → 책임 매핑 | 50-150 | high |
| `known-issues.md` | 이슈·위험·기술 부채 | 50-150 | medium (추론 포함) |

## Frontmatter 표준

```yaml
---
title: <domain> - <파일 목적>
type: compiled
domain: <your-domain>
source_files:
  - src/<domain>/handler.js
  - src/<domain>/repository.js
compiled_at: YYYY-MM-DD
compiled_by: claude-developer
confidence: high | medium | low
status: draft | active
---
```

## INPUT 사전 준비

### 필수 (정확도 직결)

- 도메인 소스 파일 전수
- 비즈니스 요구사항 문서 (있으면)
- 기존 메모리/패턴 파일에서 도메인 관련 항목

### 권장 (포함 시 "확인 필요" 항목 50% 감소)

- 전역 설정 파일 (config, defineConfig 등)
- 공통 유틸리티 클래스 (해당 도메인에서 사용하는 것)
- 라우팅 설정 (도메인 진입점 확인)
- 스케줄러/크론 설정

### 선택 (도메인 특수)

- 결제 연동: 결제 게이트웨이 클라이언트 코드
- 실시간: 웹소켓 핸들러
- 인증: 권한 체크 미들웨어

## LLM Compile 프롬프트 (4슬롯)

```
[SCOPE]
<your-domain> 도메인 코드베이스를 compile.
출력: ~/wiki/compiled/codebase/<your-domain>/

[RULES]
- 추측 금지. 코드 미확인 내용 → "확인 필요" 표시
- 각 파일 200줄 이하 (초과 시 분할, 예: api-admin.md / api-user.md)
- 모든 파일에 위 표준 frontmatter 필수
- DB 스키마: DESCRIBE/SHOW COLUMNS로 실제 검증 (코드 추정 금지)
- 코드 수정 금지 — 읽기와 문서화만

[TASK]
INPUT:
- src/<your-domain>/ 전체
- docs/requirements/<your-domain>.md (있으면)

OUTPUT 7개 파일:
- _index.md: MOC + 빠른 진입 표 (~50줄)
- overview.md: 도메인 정의, 핵심 개념, 경계, 진입점 5개 이상 (50-100줄)
- domain-rules.md: 비즈니스 규칙 — 이유(Why) + 적용 방법(How) (100-200줄)
- db-schema.md: 테이블별 컬럼/타입/인덱스/제약 (100-250줄)
- api-contracts.md: 엔드포인트별 메서드/경로/요청/응답 (100-200줄)
- code-map.md: 파일별 책임 한 줄 + 의존 관계 (50-150줄)
- known-issues.md: 알려진 이슈 + 잠재 위험 + 기술 부채 (50-150줄)

[RETURN]
- 작성 파일 목록 + 실제 줄 수
- 검증한 DB 테이블 목록
- "확인 필요" 항목 목록 (INPUT에 추가 시 해결 가능한 것 명시)
- 다음 compile 시 추가 INPUT 추천
```

## 메인 검증 절차 (3단계)

### 1. 구조 검증

```bash
ls ~/wiki/compiled/codebase/<your-domain>/
# 7개 파일 존재 확인

wc -l ~/wiki/compiled/codebase/<your-domain>/*.md
# 각 파일 200줄 이하 확인
```

### 2. Spot Check (2개 파일만)

- `overview.md`: 도메인 정의가 실제와 일치하는가?
- `known-issues.md`: 추론 내용이 `confidence: medium`으로 명시되었는가?

### 3. MOC 확인

`_index.md`의 "빠른 진입" 표가 실제 파일을 올바르게 링크하는지 확인.

## 실전에서 배운 5가지

### 1. INPUT 범위가 정확도를 결정한다

전역 설정 파일과 공통 유틸리티가 빠지면 "확인 필요" 항목이 급증한다. compile 전에 반드시 전역 설정과 도메인이 사용하는 유틸리티 클래스를 INPUT에 포함시킨다.

### 2. View 레이어의 JavaScript도 중요한 자산이다

프론트엔드 코드에서 `fetch()`, `apiPost()` 등의 호출 위치가 `api-contracts.md`의 "호출 위치" 필드를 채운다. View 레이어를 단순 템플릿으로 취급하면 API-View 연결 추적이 불가능해진다.

### 3. 200줄 초과 시 강제 압축보다 분할이 낫다

API 명세가 400줄이면 `api-contracts-admin.md`와 `api-contracts-user.md`로 분할한다. `_index.md`에서 두 파일을 묶어 표시하면 된다.

### 4. 비즈니스 문서 비교 표가 효과적이다

"항목 / 요구사항 문서 / 코드 실제 / 판정" 4컬럼 표로 모순을 한눈에 파악한다. compile 결과 신뢰도 검증의 핵심 도구.

### 5. 부수 발견을 캡처한다

compile 중 발견한 코드 품질 이슈 (로깅 정책 위반, 미사용 컬럼 등)를 `known-issues.md`의 별도 섹션에 기록한다. 도메인 정리와 코드 품질 개선이 자연스럽게 묶인다.

## 안티패턴

- 비즈니스 문서 없이 코드만으로 compile (의도 누락, 비즈니스 규칙 추론 오류)
- DB 스키마 코드 추정값 그대로 기록 (반드시 실제 DB 검증)
- 200줄 강제 압축 (정보 손실)
- compile 결과 무비판 적용 (spot check 없이 통과)
- 1회성 compile 후 갱신 없이 방치

## 다음

Frontmatter 스펙: [02-frontmatter-spec.md](./02-frontmatter-spec.md)
