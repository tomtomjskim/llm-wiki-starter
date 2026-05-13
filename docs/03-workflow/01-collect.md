---
name: collect
description: 4단계 파이프라인 1단계 — raw/ 수집 방법과 원칙
type: guide
updated: 2026-05-13
status: active
---

# 1단계: Collect (수집)

## 핵심 원칙

> raw/에 던져라. 정리하지 마라.

수집 단계의 유일한 목표는 **마찰 없이 쌓는 것**이다. 분류, 이름 정리, 내용 편집은 Compile 단계에서 LLM이 한다.

## 수집 방법

### Obsidian Web Clipper (웹 아티클)

Chrome/Firefox 확장 프로그램을 설치하면 웹 페이지를 `raw/` 폴더로 직접 저장할 수 있다.

1. [Obsidian Web Clipper 설치](https://obsidian.md/clipper)
2. 확장 프로그램 설정에서 저장 폴더를 `raw/` 로 지정
3. 웹에서 아티클 클립 → `raw/2026-05-article-title.md` 자동 저장

### 직접 파일 복사

```bash
# 코드 파일을 raw로 복사
cp src/users/*.php ~/wiki/raw/users-domain-code/

# 로그 파일
cp /var/log/app.log ~/wiki/raw/2026-05-app-error.log
```

### 빠른 메모 (Obsidian)

Obsidian 모바일 앱 → Quick note 버튼 → `raw/` 폴더에 즉시 저장.

### 드래그 앤 드롭

Obsidian 파일 탐색기에 PDF, 이미지를 드래그하면 `raw/` 폴더에 저장된다.

## 수집 대상 예시

| 소스 | 예시 | 저장 위치 |
|------|------|----------|
| 웹 아티클 | 기술 블로그, 공식 문서 | `raw/articles/` |
| 코드 파일 | 리팩토링할 레거시 모듈 | `raw/<domain>-code/` |
| PDF/논문 | arXiv 논문, 사양서 | `raw/papers/` |
| 오류 로그 | 재현 어려운 버그 스택 | `raw/bugs/` |
| 회의/메모 | 슬랙 스레드, 회의록 | `raw/notes/` |
| 스크린샷 | UI 참고, 차트 | `raw/images/` |

## raw/ 파일명 관리

엄격한 규칙은 없지만, 이 수준의 패턴은 권장한다:

```
YYYY-MM-DD-{간단한 제목}.{확장자}
2026-05-13-karpathy-llm-wiki-gist.md
2026-05-15-users-domain-legacy-code.php
```

날짜 접두사가 있으면 Compile 시 "언제 수집된 정보인가"를 LLM이 판단할 수 있다.

## 하지 말아야 할 것

- raw 파일 내용을 직접 편집하지 않는다 (Compile input이 오염됨)
- raw에서 frontmatter를 추가하려 하지 않는다
- "나중에 정리하자"는 생각으로 수집을 미루지 않는다

## Compile 트리거 시점

raw가 어느 정도 쌓이면 Compile을 돌린다. 반드시 많이 쌓여야 하는 것은 아니다.

권장 시점:
- 특정 주제/도메인 관련 raw가 5개 이상 쌓였을 때
- "이걸 LLM에 물어보고 싶다"는 생각이 들 때
- 코드 도메인을 처음 파악해야 할 때

## 다음

Compile 단계: [02-compile.md](./02-compile.md)
