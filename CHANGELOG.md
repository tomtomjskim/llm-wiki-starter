---
name: changelog
description: LLM Wiki Starter 릴리스 변경 이력
type: meta
updated: 2026-07-06
status: active
---

# Changelog

## Unreleased

## 0.6.0 - 2026-07-06

- Life OS 선택 profile 추가: `docs/07-life-os/`에 개인 장기 기억, trust boundary,
  AI context pack, Codex/Claude 세션 사용법을 문서화.
- `templates/life-os/` 추가: session summary, promotion review, decision,
  learning note, canonical policy, AI context pack 템플릿 제공.
- `scripts/init-wiki.sh --life-os` 옵션 추가: 기본 wiki 구조와 함께
  `raw/life-os`, `personal/life-os`, `compiled/life-os` 디렉토리를 생성.
- `scripts/export-life-os-context.py` 추가: Life OS reviewed/canonical 문서를
  AI context pack으로 내보내고 raw/inbox/generated는 index로만 기록.
- `lint-frontmatter.py`의 Python 3.9 호환성과 template placeholder 처리를
  회귀 테스트로 고정.

## 0.5.0 - 2026-06-24

- `docs/04-patterns/10-repo-topology-separate-vs-internal.md` 추가: 별도 `llm-wiki` repo와 personal-wiki 내부 `llm` namespace 운영을 비교하고, 개인 multi-server/multi-agent 환경에서는 내부 namespace가 관리 비용을 줄인다는 판단 기준을 문서화.
- `templates/wiki-topology/internal-llm-namespace-index.md` 추가: personal wiki 내부에서 agent/codebase/ops 지식을 관리하는 index 템플릿 제공.
- `templates/agents/AGENTS.md`에 Separate Wiki Repo와 Internal LLM Namespace 선택지를 추가.
- Start Here, Directory Layout, SecondBrain Profile, README에서 repo topology 선택 경로를 연결.

- Wiki promotion review를 proposal-only trust-boundary 패턴으로 강화: unattended agent는 `generated -> reviewed`/canonical 승격, archive/delete를 직접 수행하지 않고 numbered approval shortlist와 cleanup disposition을 제안하도록 문서화.
- AI Ops/Hermes 자동화 문서와 AGENTS template에 chat/issue 기반 승인, deferred cleanup queue, `revise`/`merge`/`keep-generated`/`archive-candidate`/`delete-candidate`/`needs-human-source-check` lifecycle을 추가.

## 0.4.4 - 2026-06-01

- `docs/04-patterns/09-private-graph-access.md` 추가: wiki manifest, graph JSON, standalone HTML viewer를 만들고 Tailscale Serve / Wiki.js / MFA로 안전하게 보는 private graph 접근 패턴 문서화.
- README 시작 profile 표에 Private Graph 경로 추가.

## 0.4.3 - 2026-06-01

- Wiki Health Guardrails에 Action Review Queue 패턴 추가: digest/inbox에
  흩어진 open checkbox를 source note에는 action candidate로 보존하고,
  `wiki/generated/action-queue/YYYY-MM-DD-open-action-review.md`에서 주간
  검토 queue로 묶는 방식을 문서화.
- health target 예시를 `open checkbox actions`, `zero inbound`,
  `oversized reviewed`, `reviewed draft residue`가 모두 0인 상태로 명시.

## 0.4.2 - 2026-06-01

- Wiki Health Guardrails에 reviewed/reference split 패턴 추가: 긴 구현 spec과
  troubleshooting transcript는 `wiki/generated/reference/*-full.md`로 보존하고,
  `wiki/reviewed`에는 durable summary만 남기는 운영 원칙을 명시.
- health report 권장 지표에 oversized reviewed docs, reviewed draft residue,
  open checkbox actions by top-level을 추가.

## 0.4.1 - 2026-06-01

- `docs/04-patterns/08-wiki-health-guardrails.md` 추가: 실제 personal wiki
  적대적 감사에서 나온 validator 강화, health report, generated hub layer,
  reviewed anti-bloat, export boundary, CI parity 패턴을 일반화.
- README 시작 profile 표에 Wiki Health guardrails 경로 추가.
- LLM Linting 문서에서 health guardrails로 연결.

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
