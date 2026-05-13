---
name: <domain>-code-map
description: <도메인> 파일별 책임 매핑과 의존 관계
type: compiled
domain: <your-domain>
source_files:
  - src/<domain>/
compiled_at: YYYY-MM-DD
compiled_by: claude-developer
confidence: high
status: draft
updated: YYYY-MM-DD
---

# <도메인> — 코드 맵

## 파일 목록

| 파일 | 레이어 | 책임 |
|------|--------|------|
| `src/<domain>/Handler.js` | API | 요청 수신, 유효성 검사, 응답 포맷 |
| `src/<domain>/Service.js` | 비즈니스 | 비즈니스 로직, 트랜잭션 조율 |
| `src/<domain>/Repository.js` | 데이터 | DB 쿼리 실행, 데이터 매핑 |
| `src/<domain>/Validator.js` | 공통 | 입력값 유효성 검사 규칙 |
| `src/views/<domain>/` | UI | 프론트엔드 뷰, API 호출 |

## 파일별 상세

### `src/<domain>/Handler.js`

**책임:** {한 줄 요약}

**주요 함수:**
- `create(req, res)`: {설명}
- `getById(req, res)`: {설명}

**의존:** `Service.js`, `Validator.js`

---

### `src/<domain>/Service.js`

**책임:** {한 줄 요약}

**주요 함수:**
- `createItem(data)`: {설명}
- `findById(id)`: {설명}

**의존:** `Repository.js`

---

### `src/<domain>/Repository.js`

**책임:** {한 줄 요약}

**사용 테이블:** `<table_1>`, `<table_2>`

**주요 함수:**
- `insert(data)`: {설명}
- `findById(id)`: {설명}

---

## 의존 관계 다이어그램 (텍스트)

```
Handler → Service → Repository → DB
   ↓
Validator
```

## 마이그레이션/리팩토링 상태

| 파일 | 상태 | 비고 |
|------|------|------|
| `Handler.js` | 완료 | DDD 구조로 분리됨 |
| `Service.js` | 진행 중 | 레거시 함수 혼재 |
| `Repository.js` | 미시작 | 레거시 직접 DB 접근 |
