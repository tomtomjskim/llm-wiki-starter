---
name: prerequisites
description: LLM Wiki 시스템 시작에 필요한 도구 설치 목록
type: guide
updated: 2026-05-13
status: active
---

# 사전 준비 (Prerequisites)

## 필수 도구

### 1. Obsidian

wiki를 탐색하고 편집하는 주 인터페이스. 무료.

- 다운로드: [https://obsidian.md](https://obsidian.md)
- 설치 후 `~/wiki` 폴더를 vault로 열기 (아직 생성 전이면 `scripts/init-wiki.sh` 먼저 실행)

```bash
# macOS Homebrew 설치 (선택)
brew install --cask obsidian
```

### 2. LLM Agent CLI

wiki compile 및 관리를 수행하는 LLM Agent.

Claude Code, Codex, 또는 둘 다 사용할 수 있다. 둘을 함께 쓰는 경우 한쪽은 구현자, 다른 한쪽은 리뷰어/검수자로 역할을 나누는 구성이 권장된다.

Claude Code 설치:

```bash
npm install -g @anthropic-ai/claude-code
```

- Claude Code 연동: [03-claude-code-integration.md](./03-claude-code-integration.md)
- Codex 연동: [05-codex-integration.md](./05-codex-integration.md)
- 병행 운영: [docs/06-advanced/03-dual-agent-workflow.md](../06-advanced/03-dual-agent-workflow.md)

### 3. Git

wiki 버전 관리 및 멀티 디바이스 동기화에 사용.

```bash
# macOS
brew install git

# 확인
git --version
```

## 권장 도구

### Obsidian 플러그인 (Community Plugins)

Obsidian 설치 후 Settings → Community plugins에서 활성화.

| 플러그인 | 용도 | 필요성 |
|---------|------|--------|
| **Dataview** | frontmatter 기반 동적 쿼리 | 강력 권장 |
| **Templater** | 파일 생성 시 frontmatter 자동 삽입 | 권장 |
| **Obsidian Git** | Git 자동 커밋/동기화 | 멀티 디바이스 사용 시 필수 |
| **Calendar** | 일일 노트 기반 raw 수집 | 선택 |
| **Advanced Tables** | 마크다운 테이블 편집 | 선택 |

### Obsidian Web Clipper

브라우저에서 웹 페이지를 `raw/` 폴더로 직접 저장하는 확장 프로그램.

- Chrome/Firefox: [Obsidian Web Clipper](https://obsidian.md/clipper)

## 선택 도구

### MCP 서버 (고급 사용자)

wiki를 LLM Agent API로 노출하려는 경우.

- 개념: [docs/06-advanced/01-mcp-integration.md](../06-advanced/01-mcp-integration.md)
- Model Context Protocol: [https://modelcontextprotocol.io](https://modelcontextprotocol.io)

### Python 3 (스크립트 실행)

`scripts/lint-frontmatter.py` 실행에 필요.

```bash
# 확인
python3 --version

# macOS (없으면)
brew install python3
```

## 확인 체크리스트

```
[ ] Obsidian 설치 완료
[ ] Claude Code 또는 Codex 사용 환경 준비 완료
[ ] Git 설치 완료 (git --version 확인)
[ ] Python 3 설치 완료 (python3 --version 확인)
[ ] scripts/init-wiki.sh 실행 완료 (~/wiki/ 디렉토리 생성)
```

## 다음

디렉토리 구조 이해: [02-directory-layout.md](./02-directory-layout.md)
