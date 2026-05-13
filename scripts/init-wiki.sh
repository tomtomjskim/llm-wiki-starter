#!/usr/bin/env bash
# =============================================================================
# init-wiki.sh — wiki 디렉토리 구조 초기화
# 사용법: bash scripts/init-wiki.sh [wiki-root]
# 기본값: ~/wiki
# =============================================================================

set -euo pipefail

WIKI_ROOT="${1:-$HOME/wiki}"

echo "wiki 디렉토리를 초기화합니다: $WIKI_ROOT"
echo ""

# --- 디렉토리 생성 -----------------------------------------------------------

dirs=(
  "$WIKI_ROOT/raw"
  "$WIKI_ROOT/personal/learn"
  "$WIKI_ROOT/personal/decision"
  "$WIKI_ROOT/personal/journal"
  "$WIKI_ROOT/compiled/codebase"
)

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
