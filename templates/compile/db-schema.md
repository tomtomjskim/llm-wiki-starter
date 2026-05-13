---
name: <domain>-db-schema
description: <도메인> DB 테이블 스키마 — 컬럼/인덱스/제약
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

# <도메인> — DB 스키마

## 테이블 목록

| 테이블 | 목적 |
|--------|------|
| `<table_1>` | {용도} |
| `<table_2>` | {용도} |

## <table_1>

**목적:** {이 테이블이 저장하는 것}

| 컬럼 | 타입 | NULL | 기본값 | 설명 |
|------|------|------|--------|------|
| `id` | BIGINT UNSIGNED | NO | AUTO_INCREMENT | PK |
| `{column}` | VARCHAR(255) | NO | | {설명} |
| `created_at` | DATETIME | NO | | 생성일시 |

**인덱스:**

| 이름 | 컬럼 | 타입 |
|------|------|------|
| PRIMARY | `id` | PRIMARY |
| `idx_{column}` | `{column}` | INDEX |

**외래키:** {없음 | 있으면 명시}

---

## <table_2>

**목적:** {이 테이블이 저장하는 것}

| 컬럼 | 타입 | NULL | 기본값 | 설명 |
|------|------|------|--------|------|
| `id` | BIGINT UNSIGNED | NO | AUTO_INCREMENT | PK |

**인덱스:**

| 이름 | 컬럼 | 타입 |
|------|------|------|
| PRIMARY | `id` | PRIMARY |

---

## 확인 필요

- [ ] {테이블명}: {확인이 필요한 항목}
