---
# ============================================================
# T3 LLM Memory frontmatter 템플릿
# Claude Code ~/.claude/projects/{project}/memory/ 에 사용
# ============================================================

name: kebab-case-slug              # 필수. 파일명과 일치 (확장자 제외)
description: 한 줄 요약              # 필수. MEMORY.md 인덱스에 사용
# type 값 (7종 중 하나 선택):
#   rule      - Agent 행동 규칙 (반드시 따라야 함)
#   pattern   - 코드/작업 패턴 (권장 방식)
#   decision  - 의사결정 기록 (배경 + 결정 + 근거)
#   guide     - 가이드라인 (참조용)
#   index     - 다른 메모리 묶는 인덱스
#   meta      - 메모리 시스템 자체 메타 문서
#   project   - 프로젝트 컨텍스트 스냅샷
type: rule
updated: YYYY-MM-DD              # 필수. 마지막 수정일
confidence: high                 # high | medium | low
status: active                   # active | deprecated | draft
llm_priority: medium             # high | medium | low (자동 주입 우선순위)

# 선택 필드
# domain: your-domain            # 도메인 한정 시
# source: session-id | file-path # 출처 추적
---

# {제목}

{핵심 규칙 또는 내용 한 줄}

## Why

{이 규칙/패턴이 필요한 근거 — 과거 실수, 강한 선호, incident}

## How to apply

{언제, 어디서, 어떻게 적용하는가}

## 예시

```
(선택) 코드 또는 사용 예시
```

## 관련

- [[관련-메모리-파일-slug]]
