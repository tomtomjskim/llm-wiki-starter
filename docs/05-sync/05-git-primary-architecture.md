---
name: git-primary-architecture
description: Git을 LLM Wiki, 장기기억, 개발환경 동기화의 기준 원본으로 쓰는 운영 아키텍처
type: guide
updated: 2026-05-18
status: active
---

# Git Primary Architecture

## 목적

이 문서는 Git을 단순 파일 동기화 도구가 아니라 LLM Wiki, 장기기억,
프로젝트 문서, 운영 runbook의 기준 원본으로 쓰는 구조를 설명한다.

Obsidian은 선택적 Markdown 편집기다. 기준점은 Git repo다.

## 최종 권장안

```text
GitHub Private repo = primary source of truth
개인/팀 서버 = mirror + Wiki Web + indexer + agent runner + backup
업무/회사 서버 = 회사 전용 문서 배포와 운영 자동화
개인 노트북 = 주 개발 단말
회사 장비 = 승인된 업무 repo만 접근
Obsidian = 선택적 클라이언트
```

## 왜 GitHub Private + Mirror인가

| 기준 | GitHub Private primary | Self-hosted Git primary | Local primary |
| --- | --- | --- | --- |
| 초기 구축 | 쉬움 | 보통 | 쉬움 |
| 장기 운영 | 낮음 | 높음 | 낮음 |
| 권한 분리 | 좋음 | 좋음 | 약함 |
| Agent 연동 | 좋음 | 보통 | 약함 |
| 백업/복구 | 좋음 | 직접 구성 필요 | 약함 |
| 장비 추가 | 쉬움 | 보통 | 어려움 |

Self-hosted Forgejo/Gitea는 좋은 예비안이지만, 처음부터 primary로 쓰면
패치, 백업, 장애대응, 인증, 메일, 스토리지 운영 책임이 생긴다. MVP 단계는
GitHub primary로 시작하고, 개인/팀 서버는 read-only mirror와 web/indexer
역할부터 맡기는 편이 현실적이다.

## 적대적 비교

| 후보 | 장점 | 리스크 | 판단 |
| --- | --- | --- | --- |
| GitHub Private primary | 권한/PR/보호규칙/협업 UX가 안정적 | 외부 서비스 의존 | 기본 선택 |
| GitHub primary + 서버 mirror | 기준 원본과 복구성이 모두 좋음 | mirror 운영 필요 | 최종 권장 |
| Forgejo/Gitea primary | 데이터 주권, 내부망 운영 가능 | self-hosting 부담, 장애대응 부담 | 예비안 |
| 회사 서버 primary | 회사 문서에는 가능 | 개인/회사 경계 오염 | 회사 repo에만 제한 |
| 개인 노트북 primary | 단순 | 분실/고장/충돌 위험 | 부적합 |
| Obsidian sync 중심 | 편집 경험 좋음 | LLM/PR/권한 모델 약함 | 보조 클라이언트 |

## 저장소 분리 원칙

Repo를 너무 많이 나누면 관리 피로도가 커지고, 너무 적게 나누면 권한과
검색 context가 오염된다. 기본은 3계층이다.

```text
개인 영역
├─ personal-llm-wiki
├─ personal-prompts
└─ personal-dev-templates

회사/팀 영역
├─ company-ops-wiki
├─ company-project-docs
├─ company-runbooks
└─ company-dev-templates

프로젝트 영역
└─ project-code-repo
   ├─ src/
   ├─ docs/
   ├─ prompts/
   └─ runbooks/
```

처음부터 `agent-memory`를 별도 repo로 분리하지 않는다. 먼저
`personal-llm-wiki/60-memory/`로 운영하고, 접근 권한이나 크기 문제가 생기면
분리한다.

## 권한 경계

금지:

- 회사 장비에 개인 전체 GitHub SSH key 등록
- 개인 repo와 회사 repo를 같은 SSH key 또는 같은 Git identity로 관리
- `.env`, API token, SSH key, DB password, 고객 개인정보를 Git에 저장
- Agent가 `main` branch에 직접 push
- Agent가 회사/개인 영역을 무분별하게 교차 참조

권장:

- 장비별 SSH key 분리
- 개인/회사 Git identity 분리
- 디렉토리별 `.gitconfig includeIf`
- `main` branch 보호
- Agent 작업은 `work/agent-*` branch 또는 PR 기반
- Secret은 1Password, Bitwarden, Vault, 환경변수로 관리

## Git 설정 예시

```ini
[user]
  useConfigOnly = true

[includeIf "gitdir:~/work/personal/"]
  path = ~/.gitconfig-personal

[includeIf "gitdir:~/work/company/"]
  path = ~/.gitconfig-company

[pull]
  rebase = true

[rebase]
  autoStash = true

[init]
  defaultBranch = main
```

```sshconfig
Host github-personal
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github_personal
  IdentitiesOnly yes

Host github-company
  HostName github.com
  User git
  IdentityFile ~/.ssh/id_ed25519_github_company
  IdentitiesOnly yes
```

Remote 예시:

```bash
git remote set-url origin git@github-personal:<user>/personal-llm-wiki.git
git remote set-url origin git@github-company:<org>/company-ops-wiki.git
```

## Branch 정책

```text
main
├─ stable 문서
├─ Agent가 읽는 기준 문서
└─ Wiki Web 배포 기준

work/*
├─ 작성 중인 문서
├─ LLM 초안
└─ 실험 prompt

archive/*
└─ 장기 보관 branch. 가능하면 99-archive/ 디렉토리를 우선 사용
```

Branch 이름:

```text
work/<user>/YYYYMMDD-topic
work/agent-<name>/YYYYMMDD-topic
experiment/<topic>-YYYYMM
```

Commit message:

```text
docs: update project wiki
memory: update active context
adr: choose git-based wiki
runbook: add backup restore
prompt: refine agent workflow
chore: update index
```

## Agent 업데이트 정책

Agent가 수정 가능한 파일:

- `80-raw/**`
- `10-projects/<assigned-project>/**`
- `60-memory/agent-notes/**`
- `70-logs/daily/**`
- 관련 index와 changelog

읽기만 가능한 파일:

- ADR
- runbook
- architecture 문서
- 다른 프로젝트의 `_index.md`

읽으면 안 되는 파일:

- `.env`, secret, key, dump, customer data
- 개인/회사 경계 밖 repo
- 권한이 배정되지 않은 private memory

Agent는 `main`에 직접 push하지 않는다. 항상 `work/agent-*` branch에서 diff
또는 PR을 만든다.

## 충돌 방지 구조

충돌이 잦은 단일 파일을 분해한다.

```text
60-memory/
├─ common.md
├─ constraints.md
├─ recurring-patterns.md
├─ active-projects/
│  ├─ project-a.md
│  └─ project-b.md
└─ agent-notes/
   ├─ 2026-05-18-project-a.md
   └─ 2026-05-18-git-wiki.md

70-logs/
├─ daily/
│  └─ 2026-05-18.md
└─ changelog.md
```

`active-context.md`를 하나만 두면 여러 장비와 Agent가 동시에 수정할 때
충돌이 잦다. 프로젝트별 active file과 날짜별 log로 분산한다.

## Mirror와 Backup

권장 흐름:

```text
Primary Git remote
→ 개인/팀 서버 read-only mirror
→ Wiki Web build
→ Indexer/vector DB build
→ 암호화 백업
→ Object Storage 또는 별도 storage
```

주기:

- mirror fetch: 15분 또는 1시간
- Wiki Web build: `main` merge 후
- encrypted object backup: 매일
- archive zip: 매주
- restore drill: 매월
- secret/key rotation review: 분기별

복구:

```bash
git revert <bad_commit>
git checkout <good_commit> -- path/to/file.md
```

## Wiki Web 도구 선택

1순위는 MkDocs Material이다.

- Markdown 중심
- 정적 배포가 단순함
- 검색 지원
- Python 기반이라 의존성이 작음
- LLM Agent가 파일을 직접 읽고 쓰기 좋음

보조 선택은 VitePress다. JS/TS 프로젝트와 프런트엔드 팀 중심 문서에는
VitePress가 더 자연스러울 수 있다.

## 단계별 실행 계획

| Phase | 산출물 | 완료 기준 |
| --- | --- | --- |
| 1. Repo 분리 | 개인/회사/wiki/template repo | README, AGENTS, branch 보호 |
| 2. Git identity 분리 | `.gitconfig`, `.ssh/config` | 장비별 key와 identity 분리 |
| 3. Server mirror | read-only mirror cron | primary 장애 시 clone 가능 |
| 4. Wiki Web | MkDocs Material site | `main` 기준 웹 문서 배포 |
| 5. Indexer | Markdown index/vector DB | project별 retrieval 가능 |
| 6. Agent policy | `work/agent-*` workflow | Agent PR만 허용 |
| 7. Backup/restore | 암호화 백업과 runbook | 월 1회 restore drill 통과 |

## 다음

- 환경별 지식 수집: [환경 프로필 패턴](../04-patterns/06-environment-profile.md)
- 충돌 처리: [conflict-resolution](./04-conflict-resolution.md)
