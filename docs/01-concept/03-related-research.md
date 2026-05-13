---
name: related-research
description: LLM Wiki 패턴과 관련된 학술/실용 연구 — Evergreen Notes, A-MEM, Zettelkasten 비교
type: guide
updated: 2026-05-13
status: active
---

# 관련 연구 및 비교

## Andy Matuschak — Evergreen Notes

Andy Matuschak이 정립한 노트 작성 방법론. [공식 사이트](https://notes.andymatuschak.org/)

### 핵심 개념

- **Evergreen Notes**: 시간이 지나도 가치를 유지하도록 지속적으로 갱신되는 노트
- **Atomic**: 하나의 노트는 하나의 아이디어만 다룬다
- **Concept-oriented**: 저자·날짜 기준이 아닌 개념 기준으로 조직
- **Link-centric**: 노트는 링크를 통해 맥락을 드러낸다

### Karpathy 패턴과의 차이

| 구분 | Evergreen Notes | Karpathy LLM Wiki |
|------|-----------------|-------------------|
| 작성 주체 | 인간 | LLM |
| 갱신 트리거 | 인간이 인식 시 | 새 raw 추가 시 자동 |
| 링크 생성 | 인간이 판단 | LLM이 자동 생성 |
| 컨텍스트 활용 | 인간의 기억 | 200K window |
| 확장 속도 | 인간의 쓰기 속도 | LLM 처리 속도 |

**공통점:** Atomic 원칙, 개념 중심 구성, 지속적 갱신

## Zettelkasten

Niklas Luhmann이 60년간 90,000개의 index card로 71권의 책을 쓴 방법론.

### 핵심 요소

- **Zettel(메모)**: 하나의 아이디어, 고유 ID 부여
- **Luhmann ID**: 계층적 번호 체계 (1a2b...)
- **Folgezettel**: 연속 아이디어 링크
- **Permanent Notes**: 임시 메모 → 정제된 영구 메모

### LLM 적용의 시사점

Zettelkasten의 "모든 메모가 연결되어야 한다"는 원칙은 LLM Wiki에서 자동 링크 생성으로 구현된다. 인간이 ID 체계를 관리하는 부담 없이 LLM이 의미론적 연결을 만든다.

### 도구 구현체

- Obsidian (이 starter kit의 기반)
- Roam Research
- Logseq

## A-MEM: Agentic Memory

**논문**: [A-MEM: Agentic Memory for LLM Agents (arxiv 2502.12110)](https://arxiv.org/abs/2502.12110)

### 핵심 아이디어

LLM Agent가 Zettelkasten 원칙을 따르는 메모리 시스템. 새로운 경험이 들어올 때 기존 메모리와 자동으로 연결·갱신·인덱싱한다.

### 구조

```
새 경험 입력
    ↓
Note Creator → 구조화된 메모 생성 (관련 키워드, 컨텍스트, 링크)
    ↓
Memory Linker → 기존 메모와 연결 업데이트
    ↓
Persistent Store → 검색 가능한 형태로 저장
```

### Karpathy 패턴과의 비교

| 구분 | A-MEM | Karpathy LLM Wiki |
|------|-------|-------------------|
| 목적 | Agent 메모리 | 인간 지식 베이스 |
| 갱신 주기 | 대화마다 실시간 | 새 raw 추가 시 배치 |
| 저장 형식 | 벡터 DB + JSON | 마크다운 파일 |
| 탐색 방식 | 임베딩 검색 | 전체 컨텍스트 로드 |
| 인간 접근 | 제한적 | Obsidian으로 직접 탐색 |

A-MEM은 Agent 내부 메모리에 가깝고, Karpathy 패턴은 인간과 LLM이 공유하는 외부화된 지식 베이스에 가깝다.

## 비교 요약

| 방법론 | 작성자 | 갱신 | 링크 | LLM 친화성 |
|--------|--------|------|------|------------|
| Zettelkasten | 인간 | 인간 | 인간 | 낮음 (ID 체계 복잡) |
| Evergreen Notes | 인간 | 인간 | 인간 | 중간 (구조 좋음) |
| A-MEM | LLM Agent | 자동 | 자동 | 높음 (Agent 전용) |
| Karpathy LLM Wiki | LLM | 배치 | 자동 | 최고 (인간+LLM 공용) |

## 참고 링크

- [Andy Matuschak Notes](https://notes.andymatuschak.org/About_these_notes)
- [A-MEM Paper (arXiv:2502.12110)](https://arxiv.org/abs/2502.12110)
- [Zettelkasten.de](https://zettelkasten.de/introduction/)
- [Karpathy Gist](https://gist.github.com/karpathy/442a6bf555914893e9891c11519de94f)
