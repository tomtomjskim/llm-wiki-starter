---
name: seven-principles
description: LLM-friendly wiki를 만드는 7원칙 상세 설명
type: guide
updated: 2026-05-13
status: active
---

# LLM-Friendly Wiki 7원칙

Karpathy 패턴에서 도출한 7원칙. LLM이 wiki를 효과적으로 읽고, 작성하고, 갱신할 수 있게 하는 설계 규칙이다.

## 원칙 1: YAML Frontmatter 필수

모든 페이지 최상단에 YAML frontmatter를 붙인다.

```yaml
---
name: page-slug
description: 한 줄 요약
type: compiled | learn | decision | rule | pattern | guide
updated: YYYY-MM-DD
status: active | draft | deprecated
---
```

**왜 필요한가:** LLM이 파일을 읽을 때 frontmatter가 "이 파일이 무엇인가"를 즉시 알려준다. 인간이 파일을 열지 않아도 메타데이터만으로 관련성을 판단할 수 있다. Linting 자동화의 기반이기도 하다.

**상세 스펙:** [docs/04-patterns/02-frontmatter-spec.md](../04-patterns/02-frontmatter-spec.md)

## 원칙 2: Atomic Page — 한 페이지 = 한 개념, 200줄 이하

각 페이지는 하나의 개념만 다루고, 200줄(마크다운 기준)을 넘지 않는다.

**왜 필요한가:**
- LLM 컨텍스트 효율: 200K window에 더 많은 페이지를 담을 수 있다
- 검색 정확도: 작은 파일은 관련성 판단이 쉽다
- 갱신 용이성: 개념 하나가 바뀌면 파일 하나만 갱신하면 된다

200줄 초과 시 강제 압축보다 **자연스러운 분할**이 낫다. 예: API 명세가 400줄이면 `api-contracts-admin.md`와 `api-contracts-user.md`로 분할.

## 원칙 3: RAG 없는 전체 로딩 (200K Window 활용)

wiki를 RAG로 쪼개서 검색하지 않고, 전체를 컨텍스트에 직접 로드한다.

**언제 전체 로드가 가능한가:**
- 컴파일된 도메인 wiki (도메인당 80-120K 토큰)
- 특정 카테고리만 선택 로드 (예: `compiled/codebase/` 전체)
- LLM 메모리 파일 전체

**실용 팁:** 200K window 기준 약 150만 자. atomic 페이지 평균 3천 자라면 약 500페이지가 한 컨텍스트에 들어간다.

## 원칙 4: LLM이 작성·유지 (인간은 raw만)

wiki의 실제 내용은 LLM이 작성한다. 인간의 역할은 raw 소스 공급과 방향 결정.

**인간이 하는 것:**
- raw 파일 수집·공급
- "이 도메인을 compile해줘" 지시
- 결과물 검증 (spot check)
- 보완이 필요한 항목 피드백

**LLM이 하는 것:**
- raw 읽기 및 구조화
- frontmatter 작성
- 내부 링크 생성
- 모순·이슈 식별

## 원칙 5: 지식 누적 (Compounding)

새 raw 소스를 추가할 때 기존 페이지를 **자동 갱신·충돌 감지**한다.

```
새 raw 추가 → LLM이 기존 wiki 전체 참조 → 관련 페이지 갱신
                                          → 모순 발견 시 known-issues에 기록
                                          → 새 링크 자동 생성
```

wiki가 쌓일수록 새로운 정보의 통합 품질이 올라간다. 이것이 단순 문서화와 다른 핵심 차이다.

## 원칙 6: 인용 추적 가능성

모든 claim(주장, 사실)은 `.md` 파일로 역추적이 가능해야 한다.

**구체적으로:**
- `source_files:` frontmatter에 원본 파일 경로 명시
- `ground_truth_refs:` 에 근거 문서 링크
- `compiled_by: claude-developer` 로 작성 주체 명시
- `confidence: high | medium | low` 로 불확실성 표시

LLM이 추론으로 작성한 내용은 `confidence: medium` 또는 `low`로 표시해서 구분한다.

## 원칙 7: MCP/Agent 연동

wiki를 LLM Agent가 직접 접근할 수 있는 인터페이스로 노출한다.

```
LLM Agent → MCP Server → wiki 파일 시스템
                       → search_wiki(query)
                       → read_page(path)
                       → list_pages(domain)
```

Claude Code의 경우 `~/.claude/projects/{project}/memory/` 구조를 통해 자동 로드된다. MCP 서버를 별도 구축하면 다른 LLM tool에서도 wiki에 접근할 수 있다.

**상세:** [docs/06-advanced/01-mcp-integration.md](../06-advanced/01-mcp-integration.md)

## 원칙 요약표

| 번호 | 원칙 | 핵심 한 줄 |
|------|------|-----------|
| 1 | YAML Frontmatter | 기계가 파싱할 수 있는 메타데이터 |
| 2 | Atomic Page | 한 개념, 200줄 이하 |
| 3 | 전체 로딩 | RAG 없이 컨텍스트에 직접 주입 |
| 4 | LLM 작성 | 인간은 raw만, LLM이 구조화 |
| 5 | Compounding | 새 정보가 기존 wiki를 강화 |
| 6 | 인용 추적 | 모든 사실이 역추적 가능 |
| 7 | MCP 연동 | Agent가 wiki를 직접 읽고 쓰기 |
