---
name: <domain>-api-contracts
description: <도메인> API 엔드포인트 명세
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

# <도메인> — API 명세

## 엔드포인트 목록

| 메서드 | 경로 | 인증 | 설명 |
|--------|------|------|------|
| POST | `/api/<domain>/create` | 필요 | {설명} |
| GET | `/api/<domain>/:id` | 필요 | {설명} |
| DELETE | `/api/<domain>/:id` | 필요 | {설명} |

---

## POST /api/<domain>/create

**설명:** {무엇을 하는 API인가}

**요청 Body:**

```json
{
  "field1": "string",
  "field2": 0
}
```

| 필드 | 타입 | 필수 | 설명 |
|------|------|------|------|
| `field1` | string | 필수 | {설명} |
| `field2` | number | 선택 | {설명} |

**성공 응답 (200):**

```json
{
  "result": "success",
  "payload": {
    "id": 1,
    "created_at": "2026-05-13T09:00:00Z"
  }
}
```

**실패 응답:**

| HTTP | result | message | 원인 |
|------|--------|---------|------|
| 400 | fail | {메시지} | {원인} |
| 404 | fail | {메시지} | {원인} |

**호출 위치:** `src/views/<domain>/create.js`

---

## GET /api/<domain>/:id

**설명:** {설명}

**URL 파라미터:**

| 파라미터 | 타입 | 설명 |
|---------|------|------|
| `id` | number | {설명} |

**성공 응답 (200):**

```json
{
  "result": "success",
  "payload": {
    "id": 1,
    "field1": "value"
  }
}
```

**호출 위치:** `src/views/<domain>/detail.js`

---

## 확인 필요

- [ ] `DELETE /api/<domain>/:id`: 소프트 삭제인지 하드 삭제인지 코드 미확인
