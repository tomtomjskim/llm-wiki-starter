---
name: reference-api-response-format
description: API 응답 형식 표준 — 예시 reference 메모리
metadata:
  type: pattern
  updated: 2026-05-13
  confidence: high
  status: active
  llm_priority: high
---

# API 응답 형식 표준

모든 API 응답은 다음 형식을 따른다:

```json
{
  "result": "success | fail",
  "payload": {
    "data": {},
    "pagination": {},
    "message": ""
  }
}
```

## Why

일관된 응답 형식은 프론트엔드에서 공통 에러 핸들러를 사용할 수 있게 한다. 응답 형식이 다르면 각 API마다 개별 파싱 코드가 필요해진다.

## How to apply

- `result`: 항상 `"success"` 또는 `"fail"` 문자열
- `payload.data`: 실제 응답 데이터 (객체 또는 배열)
- `payload.pagination`: 목록 API에서만 사용 (total, page, per_page)
- `payload.message`: 에러 메시지 또는 성공 메시지

## 예시

성공:
```json
{"result": "success", "payload": {"data": {"id": 1}}}
```

실패:
```json
{"result": "fail", "payload": {"message": "항목을 찾을 수 없습니다."}}
```

---

> 이 파일은 `reference` (pattern) 타입 메모리 예시입니다.
> API 표준, 코딩 규칙, 아키텍처 패턴 등에 사용.
> 저장 위치: `~/.claude/projects/{project}/memory/`
