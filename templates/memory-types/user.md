---
name: user-preference-diagram-theme
description: 다이어그램 기본 테마 설정 — 예시 사용자 선호 메모리
type: rule
updated: 2026-05-13
confidence: high
status: active
llm_priority: medium
---

# 다이어그램 기본 테마: 화이트

다이어그램 생성 시 항상 화이트 배경 테마를 사용한다.

## Why

다크 테마 다이어그램은 밝은 배경의 문서나 슬라이드에 삽입 시 가독성이 떨어진다. 사용자가 명시적으로 선호를 표현함.

## How to apply

Mermaid 다이어그램:
```markdown
%%{init: {'theme': 'default'}}%%
graph TD
  ...
```

별도 요청이 없는 한 화이트(default) 테마 사용. 사용자가 "다크", "forest" 등을 명시 요청한 경우에만 변경.

---

> 이 파일은 사용자 선호(user preference) 타입 메모리 예시입니다.
> 사용자가 명시적으로 요청한 행동 규칙을 기록.
> 저장 위치: `~/.claude/projects/{project}/memory/`
