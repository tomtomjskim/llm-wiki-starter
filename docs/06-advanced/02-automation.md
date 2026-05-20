---
name: automation
description: wiki 자동 lint, compile dry-run 등 자동화 패턴
type: guide
updated: 2026-05-20
status: active
---

# 자동화 패턴 (고급)

## 자동화 대상

wiki 운영에서 반복되는 작업을 자동화할 수 있다.

| 작업 | 자동화 방식 | 복잡도 |
|------|-----------|--------|
| frontmatter 검사 | cron + lint 스크립트 | 낮음 |
| stale 파일 알림 | cron + 날짜 비교 | 낮음 |
| orphan 감지 | 링크 파싱 스크립트 | 중간 |
| compile dry-run | LLM API 호출 | 높음 |
| 자동 커밋 | Obsidian Git | 낮음 (이미 지원) |

## Cron 기반 Lint

### 주간 frontmatter 검사

```bash
# crontab -e
# 매주 월요일 오전 9시
0 9 * * 1 python3 /path/to/wiki-starter/scripts/lint-frontmatter.py ~/wiki >> ~/wiki-lint.log 2>&1
```

### 90일 stale 파일 알림

```bash
#!/bin/bash
# scripts/check-stale.sh
WIKI_DIR=~/wiki
THRESHOLD_DAYS=90

find "$WIKI_DIR" -name "*.md" | while read file; do
  updated=$(grep "^updated:" "$file" 2>/dev/null | cut -d' ' -f2)
  if [ -z "$updated" ]; then
    echo "MISSING updated: $file"
    continue
  fi
  
  file_date=$(date -d "$updated" +%s 2>/dev/null || date -j -f "%Y-%m-%d" "$updated" +%s)
  now=$(date +%s)
  diff_days=$(( (now - file_date) / 86400 ))
  
  if [ $diff_days -gt $THRESHOLD_DAYS ]; then
    echo "STALE ($diff_days days): $file"
  fi
done
```

## Compile Dry-Run 패턴

실제 compile 전에 "어떤 파일을 INPUT으로 줘야 하는가"를 LLM이 분석하는 단계.

```
[dry-run 프롬프트]
src/payments/ 디렉토리 구조를 ls -la로 확인하고:
1. compile에 필요한 INPUT 파일 목록 (우선순위 포함)
2. 예상 출력 파일 7개의 예상 줄 수
3. "확인 필요" 항목이 발생할 것으로 예상되는 부분
를 리포트해줘. 실제 파일은 작성하지 않아도 됨.
```

Dry-run을 먼저 실행하면 실제 compile에서 INPUT 누락으로 인한 "확인 필요" 항목을 크게 줄일 수 있다.

## Git Hook 활용

### pre-commit: frontmatter 검사

```bash
# ~/wiki/.git/hooks/pre-commit
#!/bin/bash
python3 /path/to/wiki-starter/scripts/lint-frontmatter.py ~/wiki --error-only
if [ $? -ne 0 ]; then
  echo "frontmatter 오류가 있습니다. 커밋을 중단합니다."
  exit 1
fi
```

```bash
chmod +x ~/wiki/.git/hooks/pre-commit
```

## GitHub Actions (팀 wiki)

팀이 공유하는 private wiki repo라면 GitHub Actions로 자동화.

```yaml
# .github/workflows/lint.yml
name: Wiki Lint

on:
  push:
    branches: [main]
  pull_request:

jobs:
  lint:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4
      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: '3.11'
      - name: Run frontmatter lint
        run: python3 scripts/lint-frontmatter.py .
```

## 자동화 도입 순서 (권장)

1. **지금:** `scripts/lint-frontmatter.py` 수동 실행
2. **1주 후:** cron으로 주간 자동 실행
3. **1달 후:** stale 감지 스크립트 추가
4. **필요 시:** Git hook으로 커밋 전 자동 검사
5. **팀 사용 시:** GitHub Actions 연동

## 중앙 Agent 운영 서버와 연결

개인 wiki나 프로젝트 wiki가 여러 개로 늘어나면 repo마다 자동화를 따로 설치하기보다 중앙 운영 repo와 Agent runner를 두는 방식이 더 단순할 수 있다.

권장 분리:

```text
llm-wiki-starter = wiki 구조, 템플릿, frontmatter lint
wiki repo = 개인/프로젝트 지식 원본
ai-ops workspace = source registry, schedule, 권한 정책, report
Hermes 또는 Agent runner = pull/check/report 실행
```

이 방식은 starter의 기본 사용법이 아니라 고급 운영 방식이다. 처음에는 이 문서의 수동 lint와 cron부터 시작하고, 여러 repo를 관리해야 할 때 [04-ai-ops-hermes-workflow.md](./04-ai-ops-hermes-workflow.md)를 검토한다.

초기 권장 자동화:

- enabled wiki repo pull 가능 여부 확인
- frontmatter lint report 생성
- stale 문서 후보 report 생성
- generated 문서 promotion 후보 report 생성

초기 금지 자동화:

- 검토 없는 canonical 반영
- secret이 포함된 raw log 인덱싱
- production 서버 write
- DB write
- deploy 실행

## 주의

자동화는 도구이지 목적이 아니다. wiki 내용을 좋게 만드는 것이 우선이다. 자동화 설정에 시간을 너무 많이 쏟기보다 실제 compile과 Ask 단계를 반복하는 것이 더 가치 있다.
