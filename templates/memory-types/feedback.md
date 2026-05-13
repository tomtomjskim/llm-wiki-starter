---
name: feedback-example-no-foo-pattern
description: foo 패턴을 사용하지 말 것 — 예시 피드백 메모리
metadata:
  type: rule
  updated: 2026-05-13
  confidence: high
  status: active
  llm_priority: medium
---

# foo 패턴 사용 금지

**foo 함수를 직접 호출하지 말 것.**

## Why

{이유 — 과거 어떤 문제가 있었는가, 사용자가 피드백한 내용}

## How to apply

{언제, 어디서, 어떻게 적용하는가}

예시:
```javascript
// 금지
foo();

// 권장
bar(); // foo를 내부에서 안전하게 래핑
```

## 관련

- [[feedback-use-bar-instead]]

---

> 이 파일은 `feedback_` 타입 메모리 예시입니다.
> 실제 사용 시 파일명: `feedback_{주제}.md`
> 저장 위치: `~/.claude/projects/{project}/memory/`
