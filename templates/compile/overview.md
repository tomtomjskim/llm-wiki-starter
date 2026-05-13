---
name: <domain>-overview
description: <도메인> 도메인 정의, 핵심 개념, 경계, 진입점
type: compiled
domain: <your-domain>
source_files:
  - src/<domain>/
compiled_at: YYYY-MM-DD
compiled_by: claude-developer
confidence: high
status: draft
updated: YYYY-MM-DD
---

# <도메인> — 개요

## 도메인 한 줄 정의

{이 도메인이 무엇을 하는가. 한 문장.}

## 핵심 개념

### {개념 1}

{정의와 설명}

### {개념 2}

{정의와 설명}

## 도메인 경계

| 범위 내 | 범위 외 |
|--------|--------|
| {이 도메인이 담당하는 것} | {다른 도메인이 담당하는 것} |

## 진입점

| 시나리오 | URL 또는 진입 위치 |
|---------|------------------|
| {사용자 시나리오 1} | `/path/to/endpoint` |
| {사용자 시나리오 2} | `/path/to/endpoint` |

## 관련 페이지

- [domain-rules.md](./domain-rules.md) — 비즈니스 규칙 상세
- [db-schema.md](./db-schema.md) — 테이블 스키마
- [api-contracts.md](./api-contracts.md) — API 엔드포인트 명세
- [code-map.md](./code-map.md) — 파일 책임 매핑
- [known-issues.md](./known-issues.md) — 알려진 이슈
