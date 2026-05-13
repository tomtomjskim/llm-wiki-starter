---
name: <domain>-known-issues
description: <도메인> 알려진 이슈, 위험 요소, 기술 부채
type: compiled
domain: <your-domain>
source_files:
  - src/<domain>/
compiled_at: YYYY-MM-DD
compiled_by: claude-developer
confidence: medium
status: draft
updated: YYYY-MM-DD
---

# <도메인> — 알려진 이슈

> confidence: medium — 이슈 존재는 사실이나, 영향 범위 및 원인 분석은 추론 포함

## 이슈 목록

| 번호 | 제목 | 심각도 | 상태 |
|------|------|--------|------|
| I1 | {이슈 이름} | HIGH | 미해결 |
| I2 | {이슈 이름} | MED | 모니터링 중 |
| I3 | {이슈 이름} | LOW | 기술 부채 |

---

## I1: {이슈 이름} — HIGH

**증상:** {어떤 문제가 발생하는가}

**재현 조건:** {언제 발생하는가}

**추정 원인:** {코드 분석 기반 추론. 추론임을 명시}

**영향 범위:** {어떤 기능·데이터에 영향을 주는가}

**임시 대응:** {현재 있다면}

**코드 위치:** `src/<domain>/Service.js:87`

---

## I2: {이슈 이름} — MED

**증상:** {설명}

**재현 조건:** {설명}

**추정 원인:** {설명}

**코드 위치:** `src/<domain>/`

---

## I3: {이슈 이름} — LOW (기술 부채)

**내용:** {무엇이 개선되어야 하는가}

**현재 방식:** {현재 코드가 하는 것}

**개선 방향:** {어떻게 바꾸어야 하는가}

---

## 잠재 위험 (아직 이슈 아님)

compile 중 발견했지만 현재 문제가 아닌 잠재적 위험:

- {위험 요소}: {왜 위험한가, 어떤 조건에서 문제가 될 수 있는가}

## 코드 품질 이슈 (부수 발견)

compile 중 발견한 코딩 규칙 위반이나 주의 사항:

- `src/<domain>/file.js:32` — {발견 내용}
