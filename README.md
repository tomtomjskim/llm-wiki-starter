# LLM Wiki Starter

> LLM과 함께 운영하는 개인 지식 베이스(wiki)를 즉시 시작할 수 있는 starter kit.

Version: 0.4.1

Karpathy의 "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase" 패턴을 누구나 fork/clone해서 바로 적용할 수 있도록 구성한 레포지토리다.

## 누구를 위한 것인가

- 개인 지식 관리(PKM)에 LLM을 적극 활용하고 싶은 개발자
- 코드베이스를 LLM-friendly wiki로 문서화하고 싶은 팀
- Obsidian + Claude Code 또는 Codex 조합으로 지식 시스템을 구축하려는 사람

## Quick Start (5단계)

```bash
# 1. 이 레포를 fork하거나 clone
git clone https://github.com/your-username/llm-wiki-starter.git ~/wiki-starter
cd ~/wiki-starter

# 2. wiki 디렉토리 초기화
bash scripts/init-wiki.sh

# 3. Obsidian에서 ~/wiki 폴더를 vault로 열기
#    (Obsidian 앱 → Open folder as vault → ~/wiki 선택)

# 4. 프로젝트에 Agent 지침 템플릿 복사 (필요한 것만)
cp templates/agents/AGENTS.md /path/to/your-project/AGENTS.md
cp templates/agents/CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. frontmatter 검사 실행 (선택)
python3 scripts/lint-frontmatter.py ~/wiki
```

처음이면 [docs/00-start-here.md](./docs/00-start-here.md)부터 읽는다. 이 문서는 무엇이 자동이고 무엇이 수동인지, 첫 도메인 compile을 어떻게 시작하는지까지 안내한다.

개인 SecondBrain을 먼저 만들고 싶다면 [docs/02-setup/06-second-brain-profile.md](./docs/02-setup/06-second-brain-profile.md)에서 `Home.md`, `notes/`, `sources/` 기반 profile로 시작할 수 있다.

## Agent 연동

| Agent | 시작 문서 | 용도 |
|-------|----------|------|
| 공통 원리 | [docs/02-setup/00-mental-model.md](./docs/02-setup/00-mental-model.md) | 자동/수동 경계, `CLAUDE.md`/`AGENTS.md`/wiki 관계 |
| Claude Code | [docs/02-setup/03-claude-code-integration.md](./docs/02-setup/03-claude-code-integration.md) | Claude Code memory와 wiki 연결 |
| Codex | [docs/02-setup/05-codex-integration.md](./docs/02-setup/05-codex-integration.md) | `AGENTS.md`와 wiki 컨텍스트 연결 |
| Claude Code + Codex | [docs/06-advanced/03-dual-agent-workflow.md](./docs/06-advanced/03-dual-agent-workflow.md) | 상호 적대적 리뷰, 병렬 구현, 통합 검수 |
| Git primary architecture | [docs/05-sync/05-git-primary-architecture.md](./docs/05-sync/05-git-primary-architecture.md) | GitHub private primary, 서버 mirror, Agent update policy |
| AI Ops + Hermes | [docs/06-advanced/04-ai-ops-hermes-workflow.md](./docs/06-advanced/04-ai-ops-hermes-workflow.md) | 여러 wiki/project repo를 중앙 Hermes로 점검하고 report하는 선택 운영 방식 |

## 시작 Profile

| Profile | 시작 문서 | 적합한 경우 |
|---|---|---|
| Codebase Wiki | [Start Here](./docs/00-start-here.md) | 특정 코드베이스/도메인을 LLM-friendly wiki로 compile |
| SecondBrain | [SecondBrain Profile](./docs/02-setup/06-second-brain-profile.md) | Obsidian vault 하나에 일기, 취업, 프로젝트, source 원본을 통합 |
| Wiki Health | [Wiki Health Guardrails](./docs/04-patterns/08-wiki-health-guardrails.md) | 문서가 늘어난 뒤 validator, health report, hub layer로 품질 유지 |
| Advanced Ops | [AI Ops + Hermes](./docs/06-advanced/04-ai-ops-hermes-workflow.md) | 여러 wiki/project repo를 중앙 서버에서 점검/요약 |

## 디렉토리 트리

```
llm-wiki-starter/
├── README.md
├── VERSION
├── CHANGELOG.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── 00-start-here.md # 첫 실행 경로
│   ├── 01-concept/       # 핵심 개념 학습 (Karpathy 패턴, 7원칙)
│   ├── 02-setup/         # 초기 설치 가이드
│   ├── 03-workflow/      # 4단계 파이프라인 (Collect→Compile→View→Ask)
│   ├── 04-patterns/      # 검증된 실전 패턴
│   ├── 05-sync/          # 멀티 디바이스 동기화와 Git primary architecture
│   └── 06-advanced/      # MCP, 자동화 (선택)
│
├── templates/
│   ├── agents/           # AGENTS.md, CLAUDE.md 템플릿
│   ├── frontmatter/      # 파일 타입별 frontmatter 템플릿
│   ├── compile/          # 도메인 compile 산출물 7종 템플릿
│   └── memory-types/     # LLM Memory 4가지 타입 예시
│
├── scripts/
│   ├── init-wiki.sh      # wiki 디렉토리 구조 생성
│   ├── lint-frontmatter.py
│   └── README.md
│
└── examples/
    ├── README.md
    └── compiled-codebase/
        └── sample-domain/ # 가상 'users' 도메인 예시 MOC
```

## 라이선스

MIT — 자세한 내용은 [LICENSE](./LICENSE) 참조.
