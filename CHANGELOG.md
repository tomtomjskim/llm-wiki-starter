---
name: changelog
description: LLM Wiki Starter 릴리스 변경 이력
type: meta
updated: 2026-05-13
status: active
---

# Changelog

## 0.2.0 - 2026-05-13

- Codex에서 wiki를 컨텍스트와 작업 규칙으로 활용하는 가이드 추가.
- Claude Code와 Codex를 함께 쓰는 상호 적대적 리뷰, 병렬 구현, 통합 검수 프로토콜 추가.
- README와 Ask 워크플로우에 Codex 사용 경로 연결.
- memory 템플릿 frontmatter를 linter 규칙과 일치하도록 정리.
- `lint-frontmatter.py`가 템플릿 날짜 placeholder를 경고로 오탐하지 않도록 개선.
- `journal` 타입을 유효한 frontmatter 타입으로 추가.
- Python 3.6+ 안내와 맞도록 linter 타입 힌트 호환성 개선.

## 0.1.0 - 2026-05-13

- LLM-friendly wiki starter kit 최초 구성.
- docs, templates, examples, frontmatter linter, wiki 초기화 스크립트 추가.
