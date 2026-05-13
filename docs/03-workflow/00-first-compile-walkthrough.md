---
name: first-compile-walkthrough
description: 첫 코드베이스 도메인을 LLM Wiki로 compile하는 실습 절차
type: guide
updated: 2026-05-13
status: active
---

# 첫 Compile 실습

이 문서는 `orders` 도메인을 예시로 사용한다. 실제 프로젝트에서는 `orders`를 `users`, `payments`, `products` 같은 도메인명으로 바꾼다.

## 전제

- `~/wiki-starter`에 이 레포가 clone되어 있다.
- `bash ~/wiki-starter/scripts/init-wiki.sh`를 실행해 `~/wiki`가 있다.
- Agent가 프로젝트 코드와 `~/wiki`에 접근할 수 있다.
- 프로젝트 루트에 `AGENTS.md` 또는 `CLAUDE.md`가 있고 wiki root가 적혀 있다.

## 1. 프로젝트 루트에서 Agent 실행

```bash
cd /path/to/your-project
```

Claude Code나 Codex를 여기서 실행한다. Agent가 프로젝트 코드를 읽고, 동시에 `~/wiki`에 문서를 쓸 수 있어야 한다.

## 2. 입력 범위 정하기

작게 시작한다. 첫 compile은 전체 코드베이스가 아니라 한 도메인만 대상으로 한다.

좋은 입력:
- `src/orders/`
- `routes/orders.*` 또는 라우팅 설정
- `docs/requirements/orders.md`가 있으면 포함
- 도메인이 사용하는 공통 유틸리티 일부

나쁜 입력:
- 저장소 전체
- 오래된 기억만 기반으로 한 요청
- DB/API/비즈니스 요구사항을 “알아서 추측”하라는 요청

## 3. Agent에게 요청

```
src/orders/ 도메인을 읽고
~/wiki/compiled/codebase/orders/ 에 LLM wiki를 작성해줘.

입력:
- src/orders/
- routes/orders.*
- docs/requirements/orders.md 가 있으면 함께 참고

출력:
- _index.md
- overview.md
- domain-rules.md
- db-schema.md
- api-contracts.md
- code-map.md
- known-issues.md

규칙:
- 코드 수정 금지. 문서만 작성.
- 추측 금지. 확인되지 않는 내용은 "확인 필요"로 표시.
- templates/compile/ 의 파일 구조와 docs/04-patterns/02-frontmatter-spec.md 를 따른다.
- 모든 파일에 name, description, type, updated 필수.
- source_files, compiled_at, compiled_by, confidence, status를 포함한다.
- 각 파일은 가능하면 200줄 이하로 작성한다.

완료 보고:
- 작성한 파일 목록
- 각 파일 줄 수
- 확인 필요 항목
- 다음 compile 때 추가하면 좋은 input
```

## 4. 결과 확인

```bash
ls ~/wiki/compiled/codebase/orders/
wc -l ~/wiki/compiled/codebase/orders/*.md
python3 ~/wiki-starter/scripts/lint-frontmatter.py ~/wiki/compiled/codebase/orders --verbose
```

기대 파일:

```
_index.md
overview.md
domain-rules.md
db-schema.md
api-contracts.md
code-map.md
known-issues.md
```

## 5. Spot Check

모든 내용을 사람이 정독할 필요는 없다. 처음에는 다음만 확인한다.

| 파일 | 확인할 것 |
|------|-----------|
| `_index.md` | 7개 파일 링크가 모두 맞는가 |
| `overview.md` | 도메인 한 줄 정의가 코드와 맞는가 |
| `domain-rules.md` | 코드 근거 없이 단정한 규칙이 없는가 |
| `known-issues.md` | 추론 항목이 `confidence: medium` 또는 확인 필요로 표시됐는가 |

코드와 wiki가 충돌하면 코드를 기준으로 한다.

## 6. 실패했을 때

| 증상 | 조치 |
|------|------|
| 파일이 일부만 생성됨 | 같은 프롬프트에서 누락 파일만 이어서 요청 |
| frontmatter 오류 | `templates/frontmatter/compiled.md`를 보여주고 수정 요청 |
| 내용이 추측 위주 | 입력 파일을 늘리고 "확인 필요" 기준을 강화 |
| 파일이 너무 김 | `api-contracts-admin.md`처럼 분할 요청 |
| DB 스키마가 불확실 | 실제 migration/schema 파일 또는 DB dump를 input에 추가 |

## 7. Ask로 사용

```
~/wiki/compiled/codebase/orders/ 를 읽고
주문 취소 기능을 바꿀 때 영향을 받는 파일과 테스트를 정리해줘.
```

수정 작업이 끝난 뒤 wiki 업데이트가 필요하면 통합 후에 반영한다. 병렬 Agent 작업 중에는 compiled wiki를 임시 메모장처럼 쓰지 않는다.

## 다음

일반 compile 패턴: [02-compile.md](./02-compile.md)
