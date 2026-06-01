---
name: changelog
description: LLM Wiki Starter 릴리스 변경 이력
type: meta
updated: 2026-05-13
status: active
---

# Changelog

## Unreleased

## 0.4.0 - 2026-06-01

- `docs/02-setup/06-second-brain-profile.md` 추가: Obsidian vault 하나를
  `Home.md`, `notes/`, `sources/`, `meta/graph` 구조로 운영하는 개인
  SecondBrain profile 정리.
- `docs/03-workflow/05-second-brain-migration.md` 추가: v0 Capture부터 v5
  Emergence까지 사용자가 원하는 성숙도에서 시작할 수 있는 단계별 전환 계획
  추가.
- `docs/04-patterns/07-inter-cluster-association.md` 추가: 서로 다른 지식
  클러스터를 bridge note로 연결해 창발성을 높이는 패턴, graph signal, LLM
  prompt 정리.
- README에 Codebase Wiki, SecondBrain, Advanced Ops 시작 profile 표 추가.
- Start Here, directory layout, Obsidian setup, View, frontmatter spec에서
  SecondBrain profile과 graph/bridge note 문서로 연결.

- `docs/06-advanced/04-ai-ops-hermes-workflow.md` 추가: 여러 wiki/project
  repo를 중앙 Hermes 또는 AI Ops workspace로 pull/check/report 하는 고급
  운영 방식, 샘플 작업, write policy, skill 승격 기준을 정리.
- `docs/06-advanced/02-automation.md`에 중앙 Agent 운영 서버와 연결하는
  선택 흐름 추가.
- README와 Start Here에서 AI Ops + Hermes 운영 문서로 연결.
- `docs/05-sync/05-git-primary-architecture.md` 추가: GitHub private primary,
  개인/팀 서버 mirror, Wiki Web, LLM indexer, Agent runner, 백업/복구까지
  포함한 운영형 Git 기반 LLM Wiki 아키텍처.
- `docs/04-patterns/06-environment-profile.md` 추가: 개인 노트북, 회사 장비,
  OCI/VPS 서버 등 개발환경을 안전하게 수집하고 지식화하는 패턴.
- `templates/memory-types/environment.md` 추가: 환경 프로필 템플릿.
- `templates/memory-types/repo-boundary.md` 추가: repo 권한 경계와 Agent 접근
  정책 템플릿.
- Git 기반 동기화 문서와 README에서 운영형 Git primary architecture로 연결.

## 0.3.0 - 2026-05-13

- 처음 사용하는 사람을 위한 `docs/00-start-here.md` 추가.
- 자동/수동 경계와 `CLAUDE.md`, `AGENTS.md`, wiki, memory, Skill 관계를 설명하는 mental model 문서 추가.
- 첫 코드베이스 도메인 compile walkthrough 추가.
- `templates/agents/AGENTS.md`, `templates/agents/CLAUDE.md` 추가.
- README Quick Start를 Agent 지침 템플릿 사용 흐름에 맞게 정리.
- Start Here에 Obsidian 설치와 `~/wiki` vault 열기 단계를 명시.
- 일반 작업 세션에서 wiki 읽기와 쓰기 경계를 명시.
- `~/wiki`가 없는 사용자도 프로젝트 작업을 계속할 수 있는 fallback 원칙 추가.
- agent 지침 템플릿은 실제 프로젝트 복사용 파일이므로 frontmatter lint 대상에서 제외.
- codebase compile frontmatter 예시를 실제 linter 규칙과 일치하도록 수정.
- 아직 구현되지 않은 orphan check 명령 예시를 future work 설명으로 정정.

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
