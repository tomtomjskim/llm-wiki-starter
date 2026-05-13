---
name: conflict-resolution
description: 멀티 디바이스 동시 편집 충돌 처리 가이드
type: guide
updated: 2026-05-13
status: active
---

# 충돌 처리 가이드

## 충돌이 발생하는 상황

Git 기반 동기화에서 두 기기가 같은 파일을 동시에 편집하고 모두 커밋하면 충돌이 발생한다.

```
기기 A: overview.md 편집 → 커밋 → 푸시 (성공)
기기 B: overview.md 편집 → 커밋 → 푸시 → ERROR (충돌)
```

## 충돌 예방

### 1. Pull before you write 습관

파일을 편집하기 전에 항상 최신 상태로 풀한다.

```bash
cd ~/wiki
git pull
# 이후 편집 시작
```

Obsidian Git의 "Pull updates on startup" 옵션을 ON으로 설정하면 앱 시작 시 자동 풀.

### 2. 작업 기기를 명확히 구분

가능하면 기기별 역할을 나눈다.

- **메인 PC:** compile 작업, 긴 편집
- **노트북/모바일:** 읽기, 짧은 메모 추가

### 3. 자동 커밋 간격 조정

Obsidian Git의 자동 커밋 간격을 짧게 설정할수록 동기화가 빨라져 충돌 가능성 감소.

```
Auto push interval: 5분 (기본 10분보다 짧게)
```

## 충돌 해결 (Git 기반)

### 충돌 발생 확인

```bash
cd ~/wiki
git status
# 충돌 파일이 "both modified" 로 표시됨
```

### 충돌 파일 열기

```
<<<<<<< HEAD (현재 기기 내용)
현재 기기에서 편집한 내용
=======
다른 기기에서 편집한 내용
>>>>>>> origin/main
```

### 해결 방법 3가지

**방법 1: 내 변경 유지**

```bash
git checkout --ours wiki/compiled/codebase/orders/overview.md
git add wiki/compiled/codebase/orders/overview.md
```

**방법 2: 상대 변경 유지**

```bash
git checkout --theirs wiki/compiled/codebase/orders/overview.md
git add wiki/compiled/codebase/orders/overview.md
```

**방법 3: 두 변경 합치기 (권장)**

충돌 마커(`<<<`, `===`, `>>>`)를 제거하고 두 내용을 수동으로 합친다. Obsidian에서 해당 파일을 열면 충돌 마커가 표시됨.

```bash
# 편집 완료 후
git add wiki/compiled/codebase/orders/overview.md
git commit -m "resolve: overview.md 충돌 해결"
git push
```

## LLM compile 파일의 충돌 처리

`compiled/` 폴더의 파일은 LLM이 생성한 것이므로, 충돌 시 더 최신 compile 결과를 선택하는 것이 일반적으로 맞다.

```bash
# 최신 compile이 기기 B에서 실행된 경우
git checkout --theirs compiled/codebase/orders/
git add compiled/codebase/orders/
git commit -m "resolve: orders compile 최신본 선택"
```

## Obsidian Sync의 충돌 처리

Obsidian Sync는 자동으로 충돌을 처리한다. 충돌 발생 시:

1. 두 버전 모두 보존 (`파일명 (conflict 1).md` 형태)
2. 사용자가 직접 두 파일을 비교하고 합침
3. 중복 파일 삭제

## 예방이 최선

LLM wiki의 특성상, `compiled/` 파일은 LLM이 재생성하면 그만이다. 충돌이 자주 발생하는 경우:

1. compile 완료 즉시 푸시
2. 다른 기기에서 풀 후 읽기

`personal/` 폴더의 파일은 인간이 직접 작성하므로 충돌 해결에 더 신중해야 한다. 두 버전을 LLM에게 보여주고 합치도록 요청하는 것도 방법이다.
