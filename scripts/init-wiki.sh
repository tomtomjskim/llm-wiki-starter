#!/usr/bin/env bash
# =============================================================================
# init-wiki.sh — wiki 디렉토리 구조 초기화
# 사용법: bash scripts/init-wiki.sh [--life-os] [wiki-root]
# 기본값: ~/wiki
# =============================================================================

set -euo pipefail

INCLUDE_LIFE_OS=0
WIKI_ROOT="$HOME/wiki"

usage() {
  cat <<'USAGE'
사용법: bash scripts/init-wiki.sh [--life-os] [wiki-root]

옵션:
  --life-os   Life OS 선택 profile 디렉토리도 함께 생성
  -h, --help  도움말 출력
USAGE
}

while [ "$#" -gt 0 ]; do
  case "$1" in
    --life-os)
      INCLUDE_LIFE_OS=1
      shift
      ;;
    -h|--help)
      usage
      exit 0
      ;;
    --*)
      echo "알 수 없는 옵션: $1" >&2
      usage >&2
      exit 64
      ;;
    *)
      WIKI_ROOT="$1"
      shift
      ;;
  esac
done

echo "wiki 디렉토리를 초기화합니다: $WIKI_ROOT"
if [ "$INCLUDE_LIFE_OS" -eq 1 ]; then
  echo "Life OS profile 디렉토리도 함께 생성합니다."
fi
echo ""

# --- 디렉토리 생성 -----------------------------------------------------------

dirs=(
  "$WIKI_ROOT/raw"
  "$WIKI_ROOT/personal/learn"
  "$WIKI_ROOT/personal/decision"
  "$WIKI_ROOT/personal/journal"
  "$WIKI_ROOT/compiled/codebase"
)

if [ "$INCLUDE_LIFE_OS" -eq 1 ]; then
  dirs+=(
    "$WIKI_ROOT/raw/life-os"
    "$WIKI_ROOT/personal/life-os/inbox"
    "$WIKI_ROOT/personal/life-os/reviewed"
    "$WIKI_ROOT/personal/life-os/canonical"
    "$WIKI_ROOT/compiled/life-os/generated"
    "$WIKI_ROOT/compiled/life-os/hubs"
    "$WIKI_ROOT/compiled/life-os/context-packs"
  )
fi

for dir in "${dirs[@]}"; do
  if [ -d "$dir" ]; then
    echo "  (이미 존재) $dir"
  else
    mkdir -p "$dir"
    echo "  생성: $dir"
  fi
done

echo ""

# --- .gitkeep 생성 (빈 디렉토리 Git 추적용) ----------------------------------

gitkeep_dirs=(
  "$WIKI_ROOT/raw"
  "$WIKI_ROOT/personal/learn"
  "$WIKI_ROOT/personal/decision"
  "$WIKI_ROOT/personal/journal"
  "$WIKI_ROOT/compiled/codebase"
)

if [ "$INCLUDE_LIFE_OS" -eq 1 ]; then
  gitkeep_dirs+=(
    "$WIKI_ROOT/raw/life-os"
    "$WIKI_ROOT/personal/life-os/inbox"
    "$WIKI_ROOT/personal/life-os/reviewed"
    "$WIKI_ROOT/personal/life-os/canonical"
    "$WIKI_ROOT/compiled/life-os/generated"
    "$WIKI_ROOT/compiled/life-os/hubs"
    "$WIKI_ROOT/compiled/life-os/context-packs"
  )
fi

for dir in "${gitkeep_dirs[@]}"; do
  touch "$dir/.gitkeep"
done

echo "  .gitkeep 생성 완료"
echo ""

# --- .gitignore 생성 ---------------------------------------------------------

GITIGNORE="$WIKI_ROOT/.gitignore"

if [ -f "$GITIGNORE" ]; then
  echo "  (이미 존재) $GITIGNORE — 건너뜀"
else
  cat > "$GITIGNORE" << 'GITIGNORE_EOF'
# macOS
.DS_Store

# Obsidian
.obsidian/workspace
.obsidian/workspace.json
.obsidian/workspaces.json
.obsidian/cache

# 개인 민감 정보 (공개 repo에서 제외 권장)
personal/

# Python
__pycache__/
*.pyc
GITIGNORE_EOF
  echo "  생성: $GITIGNORE"
fi

echo ""

# --- 완료 메시지 -------------------------------------------------------------

echo "초기화 완료!"
echo ""
echo "다음 단계:"
echo "  1. Obsidian에서 '$WIKI_ROOT' 폴더를 vault로 열기"
echo "     (Obsidian → Open folder as vault → $WIKI_ROOT)"
echo ""
echo "  2. (선택) Git 초기화 및 remote 연결:"
echo "     cd $WIKI_ROOT"
echo "     git init"
echo "     git remote add origin https://github.com/your-username/my-wiki-private.git"
echo ""
echo "  3. docs/02-setup/ 가이드 읽기"
echo ""

echo "디렉토리 구조:"
if command -v tree &>/dev/null; then
  tree -a --noreport "$WIKI_ROOT" -I ".git"
else
  find "$WIKI_ROOT" -not -path '*/.git/*' | sort | sed 's|'"$WIKI_ROOT"'||' | sed 's|^/||' | awk '{print "  " $0}'
fi
