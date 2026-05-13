---
# ============================================================
# compiled/ 페이지 frontmatter 템플릿
# LLM이 코드베이스/raw를 읽고 생성하는 wiki 페이지에 사용
# ============================================================

name: <domain>-<purpose>           # 예: orders-overview, orders-domain-rules
description: 한 줄 요약              # 검색·MOC에 사용됨

type: compiled
domain: <your-domain>              # 예: orders, users, products

source_files:                      # compile에 사용한 소스 파일 목록
  - src/<domain>/Handler.js
  - src/<domain>/Repository.js

# ground_truth_refs:               # 비즈니스 요구사항 문서 (있으면)
#   - docs/requirements/<domain>.md

compiled_at: YYYY-MM-DD
compiled_by: claude-developer
updated: YYYY-MM-DD

confidence: high                   # high | medium | low
status: draft                      # draft → active (검증 후 변경)
---

# {도메인} — {페이지 목적}

{페이지 내용}
