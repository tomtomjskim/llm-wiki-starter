---
name: claude-code-integration
description: Claude Code memory 시스템과 wiki 연동 방법
type: guide
updated: 2026-05-13
status: active
---

# Claude Code 연동

## Claude Code Memory 시스템

Claude Code는 프로젝트별 memory 폴더를 통해 지속적인 컨텍스트를 유지한다.

### 구조

```
~/.claude/
├── CLAUDE.md                    # 전역 개인 규칙
└── projects/
    └── -Users-yourname-dev-myproject/
        └── memory/
            ├── MEMORY.md        # 메모리 인덱스 (자동 로드)
            └── *.md             # 개별 메모리 파일
```

경로 규칙: 프로젝트 절대 경로에서 `/`를 `-`로 치환한 폴더명. 예를 들어 `/Users/yourname/dev/myproject`는 `-Users-yourname-dev-myproject`가 된다.

### MEMORY.md 역할

세션 시작마다 자동으로 로드되는 인덱스 파일. 개별 메모리 파일을 목록화하고, 중요 규칙을 요약한다.

```markdown
## 활성 규칙

- [규칙명](file.md) — 한 줄 설명

## 프로젝트 컨텍스트

- [도메인 아키텍처](project_domain_arch.md)
```

## wiki와 Memory의 관계

| 위치 | 목적 | 로드 방식 |
|------|------|----------|
| `~/wiki/compiled/` | 코드베이스 wiki (탐색용) | 수동 (필요 시 컨텍스트 주입) |
| `~/.claude/projects/*/memory/` | LLM 행동 규칙·패턴 | 자동 (세션마다) |

두 시스템은 보완적이다. memory는 "LLM이 어떻게 행동해야 하는가"를, wiki는 "이 도메인의 사실이 무엇인가"를 저장한다.

## Memory 파일 작성 패턴

### 파일 명명 규칙

```
feedback_{주제}.md       # Claude에 대한 피드백/교정
project_{도메인}.md      # 프로젝트 컨텍스트 스냅샷
_frontmatter-spec.md     # _ 접두사: 메타 문서
MEMORY.md                # 대문자: 인덱스 파일
```

### frontmatter 표준

```yaml
---
name: kebab-case-slug
description: 한 줄 요약
metadata:
  type: rule | pattern | decision | guide | project | meta
  updated: YYYY-MM-DD
  confidence: high | medium | low
  status: active | deprecated | draft
---
```

상세: [docs/04-patterns/02-frontmatter-spec.md](../04-patterns/02-frontmatter-spec.md)

## 실제 사용 시나리오

### 시나리오 1: 새 코딩 규칙 기록

어떤 패턴을 써서 안 된다는 것을 배웠을 때:

```bash
# 파일 생성
touch ~/.claude/projects/YOUR-PROJECT/memory/feedback_no_foo_pattern.md

# 내용 작성 후 MEMORY.md 인덱스에 추가
```

### 시나리오 2: 도메인 wiki를 컨텍스트에 주입

특정 도메인 관련 질문 시:

```
# Claude Code에서 wiki 폴더를 context에 추가
/add ~/wiki/compiled/codebase/users/

# 또는 특정 파일만
/add ~/wiki/compiled/codebase/users/domain-rules.md
```

### 시나리오 3: 새 도메인 compile 의뢰

```
~/wiki/compiled/codebase/orders/ 디렉토리에
아래 파일들을 작성해줘:
- 소스: src/orders/ 디렉토리 전체
- 산출물: _index.md, overview.md, domain-rules.md, db-schema.md, api-contracts.md, code-map.md, known-issues.md
- 기준: 각 파일 200줄 이하, frontmatter 필수
```

## CLAUDE.md 설정

프로젝트별 `CLAUDE.md`에 wiki 위치를 명시해두면 모든 세션에서 참조 가능하다.

```markdown
# CLAUDE.md

## Wiki 위치

- 코드베이스 wiki: ~/wiki/compiled/codebase/
- 학습 노트: ~/wiki/personal/learn/

## 도메인 목록

| 도메인 | wiki 경로 |
|--------|----------|
| users  | ~/wiki/compiled/codebase/users/ |
| orders | ~/wiki/compiled/codebase/orders/ |
```

## 다음

Obsidian vault 설정: [04-obsidian-vault-setup.md](./04-obsidian-vault-setup.md)
