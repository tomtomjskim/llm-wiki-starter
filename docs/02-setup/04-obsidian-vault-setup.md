---
name: obsidian-vault-setup
description: Obsidian vault 위치 설정, 권장 플러그인, 초기 구성 가이드
type: guide
updated: 2026-05-13
status: active
---

# Obsidian Vault 설정

## Vault 위치

`~/wiki/` 폴더를 Obsidian vault로 설정한다.

```bash
# 1. 디렉토리 초기화 (아직 안 했다면)
bash scripts/init-wiki.sh

# 2. Obsidian 열기 → "Open folder as vault" → ~/wiki 선택
```

하나의 vault에 `raw/`, `personal/`, `compiled/` 모두 포함시키는 것이 권장 구성이다. 그래프 뷰에서 전체 연결을 한눈에 볼 수 있고, 검색도 단일 vault에서 이루어진다.

## 핵심 설정

### Editor 설정

```
Settings → Editor
- Default editing mode: Source mode (LLM 작성 파일 편집 시 마크다운 직접 보기)
- Show line numbers: ON
- Fold heading: ON
```

### Files & Links 설정

```
Settings → Files & Links
- New link format: Relative path to file
- Use [[Wikilinks]]: ON (Obsidian 내 링크)
- Detect all file extensions: ON (PDF, 이미지 인식)
```

## 권장 플러그인

### Dataview (강력 권장)

frontmatter 기반으로 파일을 동적 쿼리할 수 있는 플러그인.

```dataview
table description, updated
from "compiled/codebase"
where type = "compiled"
sort updated desc
```

위 코드블록을 노트에 삽입하면 모든 compiled 파일의 목록이 자동으로 렌더링된다.

**설치:** Settings → Community plugins → Search "Dataview"

### Templater (권장)

새 파일 생성 시 frontmatter를 자동으로 삽입하는 플러그인.

```
templates/frontmatter/compiled.md 를 Templater 템플릿 폴더로 지정하면,
새 파일 생성 시 Ctrl+Shift+T 로 템플릿 선택 가능.
```

**설치:** Settings → Community plugins → Search "Templater"

### Obsidian Git (멀티 디바이스 사용 시 필수)

일정 간격으로 자동 커밋·푸시·풀을 수행한다. Git 기반 동기화의 핵심.

```
Settings → Obsidian Git
- Vault backup interval: 10 (분)
- Auto pull interval: 10 (분)
- Commit message: {{date}} auto-backup
```

**설치:** Settings → Community plugins → Search "Obsidian Git"

상세 설정: [docs/05-sync/02-git-based-sync.md](../05-sync/02-git-based-sync.md)

### Calendar (선택)

일일 노트를 생성하고 탐색하는 플러그인. `raw/journal/` 수집에 유용.

## Vault 초기 구조 확인

Obsidian을 열었을 때 왼쪽 파일 탐색기에서 다음 구조가 보여야 한다:

```
wiki/
├── raw/
├── personal/
│   ├── learn/
│   └── decision/
└── compiled/
    └── codebase/
```

## 그래프 뷰 활용

`Ctrl+G` (macOS: `Cmd+G`) 로 그래프 뷰를 열면 모든 페이지와 링크가 시각화된다.

**필터 팁:**
- `path:compiled/` — compiled 페이지만 표시
- `tag:#active` — 활성 페이지만 표시

## 모바일 설정 (선택)

Obsidian 모바일 앱을 사용하면 스마트폰에서도 wiki 탐색이 가능하다.

- iPhone/Android: Obsidian 앱 설치
- Obsidian Git 또는 iCloud로 동기화

상세: [docs/05-sync/01-comparison.md](../05-sync/01-comparison.md)

## 다음

Collect 단계 시작: [docs/03-workflow/01-collect.md](../03-workflow/01-collect.md)
