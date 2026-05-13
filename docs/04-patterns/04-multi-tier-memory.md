---
name: multi-tier-memory
description: T1/T2/T3 3-tier 메모리 분리 운영 패턴과 각 티어의 역할
type: guide
updated: 2026-05-13
status: active
---

# 멀티 티어 메모리 패턴

## 왜 티어를 나누는가

단일 폴더에 모든 파일을 쌓으면:
- 원본(raw)과 정제본(compiled)이 섞여서 LLM이 혼동
- 개인 노트와 코드베이스 문서가 같이 컨텍스트에 주입됨
- 갱신 주기와 신뢰도가 다른 파일이 뒤섞임

티어 분리로 "무엇을 언제 컨텍스트에 넣을지"를 명확히 제어할 수 있다.

## 3-Tier 구조

```
T1: ~/wiki/raw/                    ← 수집 (정리 없음)
T2: ~/wiki/personal/               ← 인간 작성 지식
T3: ~/wiki/compiled/               ← LLM 생성 지식
    + ~/.claude/projects/*/memory/ ← LLM 행동 규칙
```

## Tier 1: Raw (수집 원본)

**목적:** 마찰 없는 수집. 정리는 나중에.

**특징:**
- 형식 자유 (PDF, 이미지, 웹 클립, 코드 파일)
- frontmatter 없음
- LLM이 compile input으로만 읽음
- 컨텍스트에 직접 주입하지 않음

**갱신:** 추가 전용. 삭제나 편집 없음.

## Tier 2: Personal (인간 지식)

**목적:** 인간이 책임지는 개인 지식·결정·학습.

**특징:**
- frontmatter 필수
- 인간이 직접 작성하거나 LLM 보조 후 인간이 검토
- 개인적 관점, 의사결정 이력, 팀 내 비공개 정보 포함 가능
- Git에 커밋하되 공개 레포에는 포함 안 할 수 있음

**서브 티어:**

| 폴더 | type | 내용 |
|------|------|------|
| `personal/learn/` | learn | 기술 학습 노트 |
| `personal/decision/` | decision | 아키텍처·기술 결정 |
| `personal/journal/` | - | 일일 메모 (선택) |

## Tier 3: Compiled + LLM Memory

**T3a: compiled wiki (탐색용)**

`~/wiki/compiled/`

- LLM이 raw/코드베이스를 읽고 생성
- 도메인별 폴더 구조
- 수동 컨텍스트 주입 ("이 파일들을 읽어줘")
- 공개 레포에 포함 가능 (개인 정보 없음)

**T3b: LLM Memory (자동 로드)**

`~/.claude/projects/{project}/memory/`

- Claude Code가 세션마다 자동 로드
- 코딩 규칙, 패턴, 결정 기록
- `MEMORY.md`가 인덱스 역할
- 프로젝트별 분리 (다른 프로젝트 메모리 오염 방지)

## 어떤 정보를 어디에 넣는가

| 정보 | 위치 | 이유 |
|------|------|------|
| 웹 아티클 클립 | T1 raw/ | 원본 그대로 보존 |
| 아티클 요약/인사이트 | T2 personal/learn/ | 인간이 검토한 정제본 |
| 코드 도메인 문서 | T3 compiled/ | LLM 생성, 수동 주입 |
| 코딩 규칙/피드백 | T3b memory/ | 자동 로드 필요 |
| 비즈니스 결정 | T2 personal/decision/ | 개인 판단 포함 |
| DB 스키마 wiki | T3 compiled/ | LLM 생성, 코드베이스 기반 |

## 컨텍스트 주입 전략

### 세션 시작 시 자동 로드

```
T3b memory/*.md → MEMORY.md 인덱스 → 세션 시작마다 자동
```

### 필요 시 수동 주입

```
T3a compiled/codebase/<domain>/ → 특정 도메인 질문 시
T2 personal/learn/ → 학습한 내용 참조 시
```

### 전체 wiki 로드 (드물게)

```
~/wiki/compiled/ 전체 → 도메인 간 관계 질문 시
```

## 티어 간 이동

raw → compiled:
```
LLM이 raw를 읽고 compiled를 생성 (Compile 단계)
```

compiled → memory:
```
compile 결과에서 행동 규칙을 추출해 memory에 추가 (메인이 직접)
```

personal → compiled:
```
개인 결정 기록이 팀 공통 문서가 될 때 (승격)
```

## 다음

LLM Linting: [05-llm-linting.md](./05-llm-linting.md)
