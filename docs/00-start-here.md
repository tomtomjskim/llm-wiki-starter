---
name: start-here
description: LLM Wiki Starter를 처음 사용하는 사용자를 위한 최소 실행 경로
type: guide
updated: 2026-06-01
status: active
---

# Start Here

이 문서는 처음 30분 안에 “쓸 수 있는 wiki”를 만드는 최소 경로다. 개념 문서를 모두 읽기 전에 이 순서대로 한 번 실행한다.

## 0. 이 레포가 해주는 것과 안 해주는 것

이 레포는 wiki 운영 구조와 템플릿, 검증 스크립트, Agent 지침 예시를 제공한다.

자동으로 되는 것:
- `scripts/init-wiki.sh`가 `~/wiki` 폴더 구조를 만든다.
- `lint-frontmatter.py`가 markdown frontmatter 기본 형식을 검사한다.
- 템플릿과 예시 문서가 compile 결과의 표준 모양을 제공한다.

자동이 아닌 것:
- `CLAUDE.md`나 `AGENTS.md`를 만든다고 wiki 내용이 자동 생성되지는 않는다.
- `~/wiki/compiled/`는 자동 로드되지 않는다. 필요한 도메인을 Agent에게 읽으라고 요청해야 한다.
- 프로젝트 코드 분석과 wiki 작성은 Claude Code, Codex 같은 Agent에게 명시적으로 요청해야 한다.
- Skill은 아직 자동 설치 대상이 아니다. 반복 작업을 안정화할 때 별도로 만들거나 설치한다.

팀원이 wiki를 쓰지 않는 경우:
- 프로젝트 작업은 계속 가능하다.
- Agent는 repository 파일과 프로젝트 문서를 기준으로 작업한다.
- `~/wiki` 또는 도메인 wiki가 없으면 “wiki context unavailable”로 보고하고 넘어간다.
- wiki 기반 문서화가 필요할 때만 이 starter kit를 clone하고 `scripts/init-wiki.sh`를 실행한다.

상세 원리: [docs/02-setup/00-mental-model.md](./02-setup/00-mental-model.md)

## 0.5. 시작 profile 고르기

처음부터 모든 기능을 쓸 필요는 없다. 목적에 맞는 profile 하나로 시작한다.

| Profile | 시작점 | 선택 기준 |
|---|---|---|
| Codebase Wiki | 이 문서의 1-7단계 | 코드베이스 도메인을 LLM-friendly wiki로 만들고 싶다 |
| SecondBrain | [SecondBrain Profile](./02-setup/06-second-brain-profile.md) | Obsidian vault 하나에 `notes/`, `sources/`, `Home.md`를 두고 개인 자료를 연결하고 싶다 |
| Advanced Ops | [AI Ops + Hermes](./06-advanced/04-ai-ops-hermes-workflow.md) | 여러 wiki/project repo를 중앙 서버에서 점검하고 요약하고 싶다 |
| Repo Topology | [Separate Repo vs Internal Namespace](./04-patterns/10-repo-topology-separate-vs-internal.md) | 별도 `llm-wiki` repo와 personal-wiki 내부 `llm` namespace 중 어떤 구조가 맞는지 먼저 정하고 싶다 |

개인 일기, 취업, 프로젝트, Notion/email/PDF 원본을 한 vault에 넣고 싶다면 Codebase Wiki 단계를 건너뛰고 SecondBrain profile부터 시작해도 된다. 이미 여러 서버/agent가 personal wiki를 공유한다면, 별도 `llm-wiki` repo를 추가하기 전에 Repo Topology 문서의 internal `llm` namespace 방식을 검토한다.

## 1. wiki 폴더 만들기

```bash
git clone https://github.com/your-username/llm-wiki-starter.git ~/wiki-starter
cd ~/wiki-starter
bash scripts/init-wiki.sh
```

결과:

```
~/wiki/
├── raw/
├── personal/
│   ├── learn/
│   ├── decision/
│   └── journal/
└── compiled/
    └── codebase/
```

`raw/`는 원본 수집, `personal/`은 인간이 책임지는 개인 지식, `compiled/`는 Agent가 코드나 raw를 읽고 생성한 구조화 문서다.

## 2. Obsidian에서 바로 보기

Obsidian은 wiki를 탐색하고 편집하는 기본 UI다.

설치:

```bash
# macOS Homebrew 사용 시
brew install --cask obsidian
```

또는 [obsidian.md](https://obsidian.md)에서 앱을 설치한다.

열기:

```
Obsidian → Open folder as vault → ~/wiki 선택
```

이 단계 이후 `raw/`, `personal/`, `compiled/` 폴더를 왼쪽 파일 탐색기에서 바로 볼 수 있다. Agent가 작성한 `~/wiki/compiled/codebase/<domain>/` 문서도 Obsidian에서 즉시 확인한다.

상세 설정: [docs/02-setup/04-obsidian-vault-setup.md](./02-setup/04-obsidian-vault-setup.md)

## 3. Agent에 wiki 위치 알려주기

Codex를 쓰면 프로젝트 루트에 `AGENTS.md`를 둔다.

```bash
cp templates/agents/AGENTS.md /path/to/your-project/AGENTS.md
```

Claude Code를 쓰면 프로젝트 루트에 `CLAUDE.md`를 둔다.

```bash
cp templates/agents/CLAUDE.md /path/to/your-project/CLAUDE.md
```

템플릿 안의 `<your-domain>`과 도메인 표는 실제 프로젝트에 맞게 줄인다. 이 파일들은 wiki를 생성하지 않는다. Agent가 `~/wiki`를 어디서 찾아야 하는지, 어떤 규칙으로 읽고 업데이트해야 하는지 알려준다.

## 4. 첫 도메인 compile 하기

프로젝트 루트에서 Agent를 실행하고 다음처럼 요청한다.

```
src/orders/ 디렉토리를 읽고
~/wiki/compiled/codebase/orders/ 에 LLM wiki를 작성해줘.

규칙:
- 코드 수정 금지. 문서만 작성.
- 추측 금지. 코드에서 확인되지 않는 내용은 "확인 필요"로 표시.
- templates/compile/ 의 7개 표준 파일 구조를 따른다.
- 모든 파일은 frontmatter 필수.
- 완료 후 작성 파일 목록, 줄 수, 확인 필요 항목을 보고해줘.
```

더 자세한 실습: [docs/03-workflow/00-first-compile-walkthrough.md](./03-workflow/00-first-compile-walkthrough.md)

## 5. 검증하기

```bash
python3 ~/wiki-starter/scripts/lint-frontmatter.py ~/wiki --verbose
ls ~/wiki/compiled/codebase/orders/
wc -l ~/wiki/compiled/codebase/orders/*.md
```

확인 기준:
- ERROR가 없어야 한다.
- 도메인 폴더에 `_index.md`, `overview.md`, `domain-rules.md`, `db-schema.md`, `api-contracts.md`, `code-map.md`, `known-issues.md`가 있어야 한다.
- 너무 긴 파일은 분할하거나 다음 compile 때 범위를 줄인다.

## 6. Ask 단계로 사용하기

Claude Code:

```
/add ~/wiki/compiled/codebase/orders/
주문 취소 시 재고 복원 로직이 어디 있는지 찾아줘.
```

Codex:

```
~/wiki/compiled/codebase/orders/ 를 먼저 읽고
주문 취소 로직 변경의 영향 범위를 정리한 뒤 수정해줘.
코드와 wiki가 충돌하면 코드를 기준으로 보고, wiki 업데이트 필요 항목을 마지막에 알려줘.
```

## 7. 이후 작업할 때 기본 요청

프로젝트에 `AGENTS.md` 또는 `CLAUDE.md`가 있어도 wiki가 자동으로 계속 작성되지는 않는다. 관련 wiki를 읽는 것은 기대 동작이고, wiki에 쓰는 것은 명시 요청 또는 승인된 최종 업데이트 단계다.

일반 작업 기본형:

```text
<작업 내용>을 진행해줘.

시작 전에:
- AGENTS.md / CLAUDE.md 확인
- 관련 도메인 wiki가 있으면 먼저 읽기

작업 후:
- 코드 변경 검증
- wiki 업데이트 필요 항목 보고
- 내가 승인하기 전에는 ~/wiki/compiled/ 문서를 수정하지 않기
```

wiki까지 바로 반영할 때:

```text
작업 완료 후 코드와 wiki가 달라진 부분이 있으면
~/wiki/compiled/codebase/<domain>/ 문서도 업데이트해줘.
업데이트 후 lint도 실행해줘.
```

## 다음

- 디렉토리 원리: [docs/02-setup/02-directory-layout.md](./02-setup/02-directory-layout.md)
- 개인 SecondBrain profile: [docs/02-setup/06-second-brain-profile.md](./02-setup/06-second-brain-profile.md)
- SecondBrain 단계별 전환: [docs/03-workflow/05-second-brain-migration.md](./03-workflow/05-second-brain-migration.md)
- Inter-cluster association: [docs/04-patterns/07-inter-cluster-association.md](./04-patterns/07-inter-cluster-association.md)
- Wiki health guardrails: [docs/04-patterns/08-wiki-health-guardrails.md](./04-patterns/08-wiki-health-guardrails.md)
- Private graph access: [docs/04-patterns/09-private-graph-access.md](./04-patterns/09-private-graph-access.md)
- Obsidian 설정: [docs/02-setup/04-obsidian-vault-setup.md](./02-setup/04-obsidian-vault-setup.md)
- Claude Code 연동: [docs/02-setup/03-claude-code-integration.md](./02-setup/03-claude-code-integration.md)
- Codex 연동: [docs/02-setup/05-codex-integration.md](./02-setup/05-codex-integration.md)
- Claude Code + Codex 병행 운영: [docs/06-advanced/03-dual-agent-workflow.md](./06-advanced/03-dual-agent-workflow.md)
- 여러 wiki/project repo를 Hermes로 통합 관리: [docs/06-advanced/04-ai-ops-hermes-workflow.md](./06-advanced/04-ai-ops-hermes-workflow.md)
