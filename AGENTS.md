# LLM Wiki Starter Agent Instructions

## Project

- 이 repo는 Obsidian + LLM/Codex/Claude 조합으로 wiki를 시작하기 위한 starter kit다.
- 사용자의 실제 개인 wiki, 서버 운영 wiki, 프로젝트별 compiled 지식은 이 repo가 아니라 각 설치 대상 wiki에 둔다.
- 템플릿과 문서는 fork/clone 후 재사용 가능한 형태로 유지한다.

## Working Rules

- 기본 응답 언어는 한국어다.
- 문서 변경 시 starter 사용자와 실제 운영 wiki 사용자를 구분한다.
- `templates/agents/`는 다른 프로젝트에 복사되는 지침이므로, secret 경로와 자동화 권한을 보수적으로 작성한다.
- LLM wiki 내용은 raw -> compiled -> reviewed/canonical 같은 승격 단계를 명확히 분리한다.

## Commands

```bash
# initialize sample wiki structure
bash scripts/init-wiki.sh

# frontmatter validation
python3 scripts/lint-frontmatter.py ~/wiki
```

## Documentation

- First path: `docs/00-start-here.md`
- Agent integration: `docs/02-setup/`
- Workflow: `docs/03-workflow/`
- Templates: `templates/`
- Examples: `examples/`

## Quality Gates

- 문서는 “자동으로 되는 일”과 “사용자가 수동 검토해야 하는 일”을 분리해야 한다.
- 에이전트가 쓸 수 있는 경로와 사람이 review/canonical로 승격하는 경로를 혼동하지 않는다.
- 새 템플릿은 frontmatter 예시와 실제 사용 위치가 맞아야 한다.

## Security

- 실제 개인 메모, credential, `.env`, token, private key, 원본 민감 로그를 예시로 넣지 않는다.
- wiki 예시는 가명/샘플 데이터만 사용한다.

## Completion Format

- 변경 요약
- 확인한 문서/명령
- 생략한 검증과 이유
- 남은 리스크 또는 사용자 적용 시 주의점
