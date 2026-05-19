---
name: environment-profile-pattern
description: 여러 개발 단말과 서버 환경을 LLM Wiki 지식으로 정리하는 패턴
type: guide
updated: 2026-05-18
status: active
---

# Environment Profile Pattern

## 목적

개인 노트북, 회사 장비, OCI/VPS 서버, staging/production 서버가 섞이면
프로젝트 지식만으로는 부족하다. 환경별 toolchain, repo 접근권한, 배포
경로, secret 위치, 운영 제약을 별도 문서로 정리해야 한다.

## 저장 위치

```text
compiled/environments/
├─ index.md
├─ personal-laptop.md
├─ company-workstation.md
├─ personal-oci.md
└─ company-oci.md
```

환경 문서는 코드베이스 문서가 아니다. 특정 기기나 서버에서 무엇이 가능하고
무엇이 금지되는지를 기록한다.

## 수집해야 할 정보

| 범주 | 예시 |
| --- | --- |
| 역할 | 개인 개발, 회사 작업, staging, production |
| OS/아키텍처 | macOS, Ubuntu, arm64, x86_64 |
| 프로젝트 루트 | `~/projects`, `/srv/apps` |
| Git identity | 개인/회사 email, SSH host alias |
| 런타임 | Node, Python, Docker, pnpm, uv |
| 서비스 | compose service, local DB, reverse proxy |
| Secret 위치 | 1Password item, Vault path, `.env` path |
| 금지 영역 | 접근 금지 repo, 고객 데이터, 개인 memory |
| 검증 명령 | health check, build, test, deploy |

## 보내면 안 되는 정보

- `.env` 값
- API token
- SSH private key
- DB password
- session cookie
- password manager export
- raw production database dump
- 고객 개인정보

Secret은 값이 아니라 이름과 위치만 기록한다.

```text
ANTHROPIC_API_KEY: 1Password item "<item>", value not shared.
DATABASE_URL: stored in server .env, value not shared.
```

## Mac 수집 명령

```bash
sw_vers
uname -m
git --version
node --version 2>/dev/null || true
npm --version 2>/dev/null || true
pnpm --version 2>/dev/null || true
python3 --version 2>/dev/null || true
docker --version 2>/dev/null || true
docker context ls 2>/dev/null || true
docker ps --format 'table {{.Names}}\t{{.Image}}\t{{.Status}}\t{{.Ports}}' 2>/dev/null || true
```

프로젝트 목록:

```bash
find ~/projects ~/workspace ~/dev -maxdepth 2 -type d -name .git 2>/dev/null \
  | sed 's#/.git$##' \
  | sort
```

## Linux/OCI 수집 명령

```bash
hostnamectl
uname -a
df -h
free -h
docker --version
docker compose version
docker compose -f /path/to/docker-compose.yml ps
```

Nginx나 reverse proxy를 쓰는 경우 실제 domain/IP는 공개 문서에서 치환한다.

```text
<service>.example.com -> http://<internal-service>:<port>
```

## 공개 문서 치환 규칙

| 실제 값 | 공개 예시 |
| --- | --- |
| 개인 이름 | `<developer>` |
| 회사명 | `<company>` |
| 실제 도메인 | `<service>.example.com` |
| 공인 IP | `203.0.113.10` |
| 내부 IP | `10.0.0.10` |
| 홈 경로 | `/home/<user>` 또는 `/Users/<user>` |
| 저장소명 | `<project>` |
| 토큰/키 | `<redacted>` |

## 컴파일 절차

1. 수집 결과를 `raw/environment-<name>.md`에 저장한다.
2. 민감정보가 없는지 확인한다.
3. `templates/memory-types/environment.md` 기준으로
   `compiled/environments/<name>.md`를 작성한다.
4. `compiled/environments/index.md`에 링크를 추가한다.
5. 환경별 접근 가능 repo와 접근 금지 repo를 명시한다.
6. `log.md`에 변경 이유를 기록한다.

## 완료 기준

- 이 환경에서 작업 가능한 repo가 명확하다.
- 이 환경에서 접근하면 안 되는 repo가 명확하다.
- Secret 값이 없다.
- build/test/deploy/health check 명령이 최소 1개 이상 있다.
- Agent가 이 환경에서 수행 가능한 작업과 금지 작업이 구분되어 있다.
