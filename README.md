# LLM Wiki Starter

> LLM과 함께 운영하는 개인 지식 베이스(wiki)를 즉시 시작할 수 있는 starter kit.

Karpathy의 "Obsidian is the IDE; the LLM is the programmer; the wiki is the codebase" 패턴을 누구나 fork/clone해서 바로 적용할 수 있도록 구성한 레포지토리다.

## 누구를 위한 것인가

- 개인 지식 관리(PKM)에 LLM을 적극 활용하고 싶은 개발자
- 코드베이스를 LLM-friendly wiki로 문서화하고 싶은 팀
- Obsidian + Claude Code 조합으로 지식 시스템을 구축하려는 사람

## Quick Start (5단계)

```bash
# 1. 이 레포를 fork하거나 clone
git clone https://github.com/your-username/llm-wiki-starter.git ~/wiki-starter
cd ~/wiki-starter

# 2. wiki 디렉토리 초기화
bash scripts/init-wiki.sh

# 3. Obsidian에서 ~/wiki 폴더를 vault로 열기
#    (Obsidian 앱 → Open folder as vault → ~/wiki 선택)

# 4. frontmatter 검사 실행 (선택)
python3 scripts/lint-frontmatter.py ~/wiki

# 5. docs/ 가이드 읽기 → docs/01-concept/01-llm-wiki-pattern.md 부터
```

## 디렉토리 트리

```
llm-wiki-starter/
├── README.md
├── LICENSE
├── .gitignore
│
├── docs/
│   ├── 01-concept/       # 핵심 개념 학습 (Karpathy 패턴, 7원칙)
│   ├── 02-setup/         # 초기 설치 가이드
│   ├── 03-workflow/      # 4단계 파이프라인 (Collect→Compile→View→Ask)
│   ├── 04-patterns/      # 검증된 실전 패턴
│   ├── 05-sync/          # 멀티 디바이스 동기화
│   └── 06-advanced/      # MCP, 자동화 (선택)
│
├── templates/
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
