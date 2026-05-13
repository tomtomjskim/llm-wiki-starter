---
name: scripts-readme
description: scripts/ 디렉토리 스크립트 사용법
type: guide
updated: 2026-05-13
status: active
---

# scripts/ 사용법

## init-wiki.sh — wiki 디렉토리 초기화

```bash
# 기본 (~/wiki 에 생성)
bash scripts/init-wiki.sh

# 경로 지정
bash scripts/init-wiki.sh /path/to/my-wiki
```

생성되는 구조:

```
~/wiki/
├── raw/                 # T1: 수집 원본
├── personal/
│   ├── learn/           # T2: 학습 노트
│   ├── decision/        # T2: 결정 기록
│   └── journal/         # T2: 일일 메모
└── compiled/
    └── codebase/        # T3: 코드베이스 wiki
```

각 폴더에 `.gitkeep` 파일이 생성되어 Git이 빈 폴더를 추적할 수 있다.

`.gitignore`도 자동 생성된다 (이미 있으면 건너뜀).

## lint-frontmatter.py — frontmatter 검사

Python 3.6 이상 필요. 외부 라이브러리 없음 (표준 라이브러리만 사용).

```bash
# wiki 전체 검사
python3 scripts/lint-frontmatter.py ~/wiki

# 특정 폴더만
python3 scripts/lint-frontmatter.py ~/wiki/compiled

# 특정 파일
python3 scripts/lint-frontmatter.py ~/wiki/compiled/codebase/orders/overview.md

# 상세 모드 (INFO 레벨도 출력)
python3 scripts/lint-frontmatter.py ~/wiki --verbose

# ERROR만 출력 (CI/pre-commit 용)
python3 scripts/lint-frontmatter.py ~/wiki --error-only
```

### 검사 항목

| 레벨 | 항목 |
|------|------|
| ERROR | `name`, `description`, `type` 필수 필드 누락 |
| WARNING | `updated` 날짜가 90일 초과 (stale) |
| WARNING | `confidence: low` + 30일 초과 |
| WARNING | `type` 값이 유효하지 않음 |
| WARNING | frontmatter 형식 오류 |
| INFO | `updated` 필드 없음 (`--verbose` 시에만) |
| INFO | `status: deprecated` 파일 (`--verbose` 시에만) |

`README.md` 중 frontmatter가 없는 파일은 안내 문서로 보고 검사 대상에서 제외한다.

### 종료 코드

- `0`: ERROR 0건 (정상)
- `1`: ERROR 1건 이상

### pre-commit hook으로 등록

```bash
# ~/wiki/.git/hooks/pre-commit
#!/bin/bash
python3 /path/to/llm-wiki-starter/scripts/lint-frontmatter.py ~/wiki --error-only
```

```bash
chmod +x ~/wiki/.git/hooks/pre-commit
```

### 주간 자동 실행 (cron)

```bash
# crontab -e
0 9 * * 1 python3 /path/to/llm-wiki-starter/scripts/lint-frontmatter.py ~/wiki >> ~/wiki-lint.log 2>&1
```
