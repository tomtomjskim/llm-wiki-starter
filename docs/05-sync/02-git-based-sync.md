---
name: git-based-sync
description: Git + Obsidian Git 플러그인으로 wiki를 멀티 디바이스 동기화하는 권장 방법
type: guide
updated: 2026-05-13
status: active
---

# Git 기반 동기화 (권장)

## 개요

private GitHub/GitLab 레포지토리를 remote로 사용하고, Obsidian Git 플러그인이 자동으로 커밋·푸시·풀을 수행한다.

**이 방식이 권장되는 이유:**
- 무료
- wiki 버전 히스토리가 Git으로 관리됨
- 코드베이스와 동일한 방식으로 wiki를 관리
- 팀 협업 가능 (private repo)

## 초기 설정

### 1. Private 레포지토리 생성

GitHub에서 private repo를 생성한다.

```bash
# 이미 ~/wiki가 있다면
cd ~/wiki
git init
git remote add origin https://github.com/your-username/my-wiki-private.git
git add .
git commit -m "initial wiki"
git push -u origin main
```

### 2. Obsidian Git 플러그인 설치

```
Obsidian → Settings → Community plugins → Search "Obsidian Git" → Install → Enable
```

### 3. Obsidian Git 설정

```
Settings → Obsidian Git
- Vault backup interval (minutes): 10      # 10분마다 자동 커밋
- Auto pull interval (minutes): 10         # 10분마다 자동 풀
- Commit message: {{date}} auto-backup     # 커밋 메시지 형식
- Pull updates on startup: ON              # 앱 시작 시 최신화
- Push on commit: ON                       # 커밋 즉시 푸시
```

### 4. 두 번째 기기에서 클론

```bash
# PC 2 또는 다른 Mac
git clone https://github.com/your-username/my-wiki-private.git ~/wiki

# Obsidian에서 ~/wiki 폴더를 vault로 열기
# Obsidian Git 플러그인 설치 후 위와 동일하게 설정
```

## 모바일 설정 (iOS/Android)

### iOS (iPhone/iPad)

1. GitHub mobile 앱에서 SSH 키 또는 토큰 설정
2. Obsidian 앱 설치 후 ~/wiki를 iCloud에 복사하거나 Working Copy 앱 활용
3. Obsidian Git 플러그인 → iOS에서도 동일하게 동작 (Working Copy와 연동)

**팁:** iOS에서 Obsidian Git은 Working Copy 앱이 있으면 더 안정적으로 동작한다.

### Android

1. Obsidian 앱 설치
2. Obsidian Git 플러그인 → 직접 Git 동작 지원 (별도 앱 불필요)

## 일상적인 사용 흐름

```
[기기 A에서 작업]
1. Obsidian 열기 → 자동으로 최신 풀
2. wiki 편집 또는 compile 실행
3. Obsidian Git이 10분마다 자동 커밋·푸시

[기기 B에서 확인]
1. Obsidian 열기 → 자동으로 최신 풀
2. 기기 A의 변경 내용 즉시 반영
```

## 수동 커밋 (Compile 완료 시)

큰 compile이 완료된 후에는 수동으로 커밋하는 것이 권장된다.

```
Obsidian → Cmd+P → "Obsidian Git: Commit all changes"
메시지: "compile: orders 도메인 7개 파일 (2026-05-13)"
```

또는 터미널에서:

```bash
cd ~/wiki
git add compiled/codebase/orders/
git commit -m "compile: orders 도메인 초기 compile"
git push
```

## .gitignore 설정

`~/wiki/.gitignore` 권장 내용:

```
# 개인 민감 정보 (공개 repo라면 반드시)
personal/

# Obsidian 설정 (개인화된 파일)
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspaces.json
.obsidian/cache

# macOS
.DS_Store
```

**주의:** `personal/` 폴더는 개인 판단, 결정 기록 등이 포함될 수 있으므로 공개 repo에서는 `.gitignore`에 추가한다.

## 다음

동기화 충돌 처리: [04-conflict-resolution.md](./04-conflict-resolution.md)
