---
name: llm-wiki-pattern
description: Karpathy LLM Wiki 패턴 핵심 아이디어와 4단계 파이프라인
type: guide
updated: 2026-05-13
status: active
---

# LLM Wiki 패턴

## 핵심 인용

> Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase.
>
> — Andrej Karpathy, 2026-04-03

## 핵심 아이디어

LLM과 함께 운영하는 개인 지식 베이스. 인간은 **raw 소스**만 공급하고, LLM이 wiki 전체를 작성·유지·연결한다. RAG 없이 200K 컨텍스트에 wiki 전체를 직접 로드해서 추론한다.

Karpathy 본인은 이 방식으로 100개 아티클, 40만 단어 규모의 리서치 wiki를 운영하면서 단 한 줄도 직접 쓰지 않았다고 밝혔다.

기존 PKM(Personal Knowledge Management) 도구들이 "인간이 구조를 설계하고 정리하는" 방식이라면, LLM Wiki 패턴은 **인간이 raw를 던지면 LLM이 구조화**하는 역할 반전이 핵심이다.

## 4단계 파이프라인

```
raw/ → [LLM Compile] → compiled/ → [Obsidian View] → [Ask]
  ↑                                                      ↓
수집                                                    질문·추론
```

### 1단계: Collect (수집)

`raw/` 폴더에 아무 형식이나 그대로 쌓는다.

- Obsidian Web Clipper로 웹 아티클 클립
- PDF, 이미지 drag-drop
- 빠른 메모, 링크, 스크린샷
- 코드 파일, 로그, 오류 메시지

**규칙: 정리하지 않는다.** 수집 마찰을 0으로 낮추는 것이 목적.

### 2단계: Compile (컴파일)

LLM이 `raw/`를 읽고 구조화된 `compiled/` markdown으로 변환한다.

- 요약·백링크·연결
- 모순·충돌 식별
- 인용 추적 가능한 형태로 재작성
- YAML frontmatter 부착

**인간의 역할**: LLM에 raw 경로를 알려주고 출력 위치를 지정하는 것뿐.

### 3단계: View (탐색)

Obsidian으로 compiled wiki를 탐색한다.

- 그래프 뷰로 개념 간 연결 확인
- 전문 검색으로 특정 내용 위치 파악
- 모바일 앱으로 이동 중 조회
- Dataview 플러그인으로 동적 쿼리

### 4단계: Ask (질문)

wiki 전체 또는 관련 파일을 컨텍스트에 올려 LLM에 질문한다.

- RAG 없이 200K window에 직접 로드
- "이 도메인에서 X를 하려면 어떤 파일을 건드려야 해?"
- "이 개념과 저 개념의 차이점을 설명해줘"
- wiki가 쌓일수록 답변 품질이 올라간다 (Compounding 효과)

## 왜 RAG를 쓰지 않는가

RAG(Retrieval-Augmented Generation)는 관련 청크를 검색해서 컨텍스트에 주입하지만, 검색이 실패하면 정보가 누락된다. Karpathy 패턴은 wiki 전체를 컨텍스트에 올려 **LLM이 스스로 관련성을 판단**하게 한다.

wiki가 200K 토큰 이하로 유지되는 한 (약 300-500개 atomic 페이지) 이 접근이 더 신뢰성 있다.

## 출처

- [Karpathy X 포스트 (2026-04-03)](https://x.com/karpathy/status/2039805659525644595)
- [GitHub Gist: karpathy/llm-wiki](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
- [VentureBeat 분석](https://venturebeat.com/data/karpathy-shares-llm-knowledge-base-architecture-that-bypasses-rag-with-an)

## 다음

- 7원칙 상세: [02-seven-principles.md](./02-seven-principles.md)
- 관련 연구: [03-related-research.md](./03-related-research.md)
