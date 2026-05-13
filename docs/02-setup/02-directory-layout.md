---
name: directory-layout
description: T1/T2/T3 3-tier wiki 디렉토리 구조 설명과 각 tier 사용 시점
type: guide
updated: 2026-05-13
status: active
---

# 디렉토리 레이아웃

## 3-Tier 구조 개요

```
~/wiki/
├── raw/                    # T1: 원본 수집 (정리 금지)
├── personal/               # T2: 개인 지식 (인간 작성)
│   ├── learn/              #   학습 노트
│   ├── decision/           #   결정 기록
│   └── journal/            #   일일 메모 (선택)
└── compiled/               # T3: LLM 컴파일 결과
    └── codebase/           #   코드베이스 도메인 wiki
        └── <your-domain>/  #   도메인당 폴더
```

LLM Memory 파일은 Claude Code 기준 `~/.claude/projects/{project}/memory/`에 별도 위치한다. `CLAUDE.md`, `AGENTS.md`, memory, wiki의 관계는 [00-mental-model.md](./00-mental-model.md)를 먼저 본다.

## Tier 상세

### T1: raw/ (수집 전용)

**역할**: 정리 없이 원본 그대로 쌓는 임시 수집함.

**특징:**
- 형식 제한 없음 (PDF, 이미지, HTML, 텍스트 모두)
- frontmatter 불필요
- 파일명 그대로 유지
- Git 추적 선택 사항 (개인 취향)

**언제 사용:**
- 웹 아티클 클립
- 로그, 오류 메시지, 스크린샷
- 회의록, 슬랙 링크
- 코드 스니펫, 참고 자료

**규칙: raw에서 직접 편집하지 않는다.** 컴파일 input으로만 사용.

### T2: personal/ (인간 작성)

**역할**: 인간이 직접 작성하는 개인 지식. LLM 보조는 가능하지만 인간이 책임진다.

**특징:**
- frontmatter 필수 (type: learn | decision | journal)
- 인간이 직접 작성·검토
- 개인적 관점, 의사결정 이력 포함

**서브 디렉토리:**

| 폴더 | 내용 | 예시 |
|------|------|------|
| `learn/` | 학습 노트, 패턴 이해 | `karpathy-llm-wiki-pattern.md` |
| `decision/` | 아키텍처·기술 결정 기록 | `2026-05-choose-obsidian.md` |
| `journal/` | 일일 메모, 진행 상황 | `2026-05-13.md` |

**언제 사용:**
- 새 기술/개념을 공부하고 내 말로 정리할 때
- 중요한 기술 결정을 기록할 때
- raw를 읽은 후 핵심만 뽑아 정리할 때

### T3: compiled/ (LLM 컴파일)

**역할**: LLM이 raw와 코드베이스를 읽고 생성한 구조화된 wiki.

**특징:**
- frontmatter 필수 (type: compiled)
- LLM이 작성, 인간은 spot check만
- `source_files:`, `confidence:`, `compiled_at:` 필수
- 도메인별 폴더로 구성

**도메인당 표준 산출물 7개:**

```
compiled/codebase/<your-domain>/
├── _index.md          # MOC (Map of Content) — 진입점
├── overview.md        # 도메인 정의·경계·핵심 개념
├── domain-rules.md    # 비즈니스 규칙
├── db-schema.md       # 테이블·컬럼·인덱스
├── api-contracts.md   # API 엔드포인트 명세
├── code-map.md        # 파일 → 책임 매핑
└── known-issues.md    # 알려진 이슈·위험 요소
```

**언제 사용:**
- 코드베이스 특정 도메인을 LLM-friendly wiki로 만들 때
- 새 팀원 온보딩 자료 생성 시
- 복잡한 비즈니스 로직을 문서화할 때

## 티어별 비교

| 구분 | raw/ | personal/ | compiled/ |
|------|------|-----------|-----------|
| 작성자 | 외부 소스 | 인간 | LLM |
| frontmatter | 불필요 | 필수 | 필수 |
| 갱신 방식 | 추가 전용 | 인간 직접 | LLM 재실행 |
| Git 추적 | 선택 | 필수 | 필수 |
| Obsidian 탐색 | 최소화 | 주요 사용 | 주요 사용 |

## 실제 경로 예시

```
~/wiki/
├── raw/
│   ├── 2026-05-karpathy-tweet.md
│   └── a-mem-paper.pdf
├── personal/
│   ├── learn/
│   │   └── llm-wiki-pattern.md
│   └── decision/
│       └── 2026-05-chose-git-sync.md
└── compiled/
    └── codebase/
        └── users/
            ├── _index.md
            ├── overview.md
            └── ...
```

## 다음

Claude Code 연동: [03-claude-code-integration.md](./03-claude-code-integration.md)
