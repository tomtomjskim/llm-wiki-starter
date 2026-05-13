---
name: <domain>-domain-rules
description: <도메인> 비즈니스 규칙 — Why + How
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

# <도메인> — 비즈니스 규칙

## 규칙 목록

| 번호 | 규칙 이름 | 중요도 |
|------|----------|--------|
| R1 | {규칙 이름} | 높음 |
| R2 | {규칙 이름} | 중간 |

## R1: {규칙 이름}

**Why (왜):** {이 규칙이 존재하는 비즈니스적 이유}

**How (어떻게):** {코드에서 어떻게 구현되어 있는가}

**예외:** {예외 케이스가 있으면 명시}

**코드 위치:** `src/<domain>/Handler.js:42`

---

## R2: {규칙 이름}

**Why:** {이유}

**How:** {구현 방식}

**예외:** {없음 | 있으면 명시}

**코드 위치:** `src/<domain>/`

---

## 확인 필요

{코드에서 명확하지 않아 비즈니스 문서나 담당자 확인이 필요한 항목}

- [ ] {항목 1}: {왜 불명확한가}
