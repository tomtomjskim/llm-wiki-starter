---
name: ask
description: 4단계 파이프라인 4단계 — wiki를 컨텍스트에 올려 질문하는 패턴
type: guide
updated: 2026-05-13
status: active
---

# 4단계: Ask (질문)

## 개요

wiki 전체 또는 관련 부분을 LLM 컨텍스트에 올려 질문한다. RAG 없이 직접 로드하는 것이 Karpathy 패턴의 핵심.

## 컨텍스트 주입 방법

### Claude Code에서 파일 추가

```bash
# 특정 도메인 전체
/add ~/wiki/compiled/codebase/orders/

# 특정 파일만
/add ~/wiki/compiled/codebase/orders/domain-rules.md

# 여러 도메인
/add ~/wiki/compiled/codebase/orders/
/add ~/wiki/compiled/codebase/users/
```

### Codex에서 경로를 직접 지정

Codex에서는 작업 요청에 wiki 경로와 기대 동작을 함께 적는다.

```
~/wiki/compiled/codebase/orders/ 를 먼저 읽고
주문 취소 로직 변경의 영향 범위를 정리한 뒤 수정해줘.
코드와 wiki가 충돌하면 코드를 기준으로 보고,
wiki 업데이트가 필요한 파일도 마지막에 알려줘.
```

프로젝트 루트의 `AGENTS.md`에 wiki root와 도메인 맵을 적어두면 매번 긴 경로를 설명하지 않아도 된다.

상세: [docs/02-setup/05-codex-integration.md](../02-setup/05-codex-integration.md)

### 프롬프트에 직접 경로 언급

```
~/wiki/compiled/codebase/orders/ 를 전부 읽고
주문 취소 시 재고 복원 로직이 어디 있는지 찾아줘.
```

## 효과적인 질문 패턴

### 패턴 1: 도메인 탐색

```
wiki/compiled/codebase/orders/ 를 컨텍스트로 갖고:

"주문 생성 API에서 재고 확인은 언제 일어나나요?"
"orders 도메인과 users 도메인의 연결 지점이 어디인가요?"
"DB 스키마에서 인덱스가 없는 쿼리 대상 컬럼이 있나요?"
```

### 패턴 2: 비교 분석

```
wiki/compiled/codebase/orders/ 와
wiki/compiled/codebase/returns/ 를 동시에 읽고:

"반품 처리 흐름이 주문 흐름과 어떻게 다른가요?"
"두 도메인이 공유하는 테이블이 있나요?"
```

### 패턴 3: 이슈 진단

```
wiki/compiled/codebase/orders/known-issues.md 를 읽고:

"이슈 #3 (결제 이중 처리 위험)에 대한 방어 코드가
 현재 api-contracts.md 명세에 반영되어 있나요?"
```

### 패턴 4: 신규 기능 설계

```
wiki/compiled/codebase/ 전체를 읽고:

"주문 도메인에 '선물하기' 기능을 추가한다면
 어떤 테이블과 API 엔드포인트가 영향을 받나요?"
```

## 컨텍스트 크기 관리

도메인당 compiled wiki는 약 80-120K 토큰. Claude의 200K window 기준:

| 구성 | 토큰 | 가능 여부 |
|------|------|----------|
| 도메인 1개 전체 | ~100K | |
| 도메인 2개 전체 | ~200K | 경계 |
| 특정 파일 3-4개 | ~30K | 여유 |

여러 도메인을 한 번에 비교하거나, 대화가 길어질 경우 특정 파일만 선택해서 주입하는 것이 효율적이다.

## wiki Compounding 효과 활용

wiki가 쌓일수록 Ask 단계의 질문 품질이 올라간다.

**초기 (도메인 1개):**
```
"orders 도메인 API 명세를 설명해줘" → 정확하지만 단일 도메인 한정
```

**성숙기 (도메인 5개 이상):**
```
"orders, users, products 도메인의 상호작용 지도를 그려줘"
→ 도메인 간 의존성을 LLM이 wiki에서 직접 추론
```

"새 raw 추가 → compile → ask"를 반복할수록 LLM의 답변이 더 정확해진다.

## Ask 후 발견한 것을 wiki에 반영

Ask 단계에서 wiki에 빠진 내용을 발견했다면:

1. `known-issues.md`에 항목 추가
2. 해당 파일을 `status: needs-update`로 변경
3. 다음 compile 주기에서 보완

wiki는 한 번 만들고 끝나는 문서가 아니라, Ask 단계의 피드백으로 지속 개선된다.

## 다음

실전 패턴: [docs/04-patterns/01-codebase-compile.md](../04-patterns/01-codebase-compile.md)
