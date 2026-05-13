---
name: llm-linting
description: wiki 파일의 orphan/stale/broken-refs 감지 개념과 linting 전략
type: guide
updated: 2026-05-13
status: active
---

# LLM Linting

## 왜 Linting이 필요한가

wiki가 커지면 자연스럽게 발생하는 문제:

- **Orphan**: 아무 파일에서도 링크되지 않는 고립된 페이지
- **Stale**: `updated` 날짜가 오래되어 정보가 낡아진 페이지
- **Broken refs**: 삭제·이동된 파일을 참조하는 깨진 링크
- **Missing frontmatter**: frontmatter가 없거나 필수 필드가 누락된 파일

이런 문제를 주기적으로 찾아내는 것이 LLM Linting이다.

## 4가지 Lint 유형

### 1. Orphan 감지

어떤 파일에서도 참조되지 않는 파일.

```bash
# 현재는 개념 단계. 자동 orphan 검사는 향후 wiki-doctor 스크립트에서 제공 예정.
# 지금은 LLM에게 compiled 폴더를 읽게 해서 orphan 후보를 찾도록 요청한다.
```

**처리 방법:**
- 관련 MOC에 링크 추가
- 연관 파일에서 참조
- 삭제 (orphan이 맞다면)

### 2. Stale 감지

`updated` 날짜가 90일 이상 지난 파일.

```yaml
updated: 2025-12-01  # 90일 초과 → stale 경고
```

**처리 방법:**
- 내용이 여전히 유효한지 확인
- 여전히 유효하면 `updated` 날짜만 갱신
- 내용 변경 필요 시 재 compile

### 3. Broken refs 감지

`[[링크]]` 또는 `[텍스트](경로)` 가 존재하지 않는 파일을 가리킬 때.

```markdown
[overview](./overview.md)  # overview.md가 삭제되면 broken ref
```

**처리 방법:**
- 링크 수정 (이동된 경우 새 경로로)
- 파일 복원 (실수로 삭제된 경우)
- 링크 제거 (파일이 의도적으로 삭제된 경우)

### 4. Missing frontmatter

필수 필드(`name`, `description`, `type`)가 없는 파일.

```bash
python3 scripts/lint-frontmatter.py ~/wiki
# 누락된 필드를 파일별로 보고
```

**처리 방법:**
- frontmatter 추가 (신규 파일)
- 기존 파일에 필수 필드 보강

## 도구

### scripts/lint-frontmatter.py

이 starter kit에 포함된 기본 linter.

```bash
# 전체 wiki 검사
python3 scripts/lint-frontmatter.py ~/wiki

# 특정 폴더만
python3 scripts/lint-frontmatter.py ~/wiki/compiled

# 상세 모드
python3 scripts/lint-frontmatter.py ~/wiki --verbose
```

검사 항목: `name`, `description`, `type` 필수 필드 누락 여부.

### LLM에게 Linting 위임

```
~/wiki/compiled/ 를 전체 읽고 다음을 검사해줘:
1. _index.md에서 링크되지 않은 파일 (orphan)
2. updated가 2025년 이전인 파일 (stale 후보)
3. 다른 파일에서 참조하지만 실제 없는 경로 (broken refs)

결과를 severity별로 정리해줘:
ERROR: 즉시 수정 필요
WARNING: 검토 필요
INFO: 참고용
```

## Linting 주기

| 이벤트 | Lint 범위 |
|--------|----------|
| 새 compile 완료 시 | 해당 도메인 폴더 |
| 월 1회 | wiki 전체 |
| 파일 삭제·이동 시 | 전체 (broken refs 확인) |

## Phase별 도입 전략

**Phase 1 (지금):** `lint-frontmatter.py`로 필수 필드만 검사.

**Phase 2:** `wiki-doctor.py`로 orphan + broken refs 스크립트 추가.

**Phase 3:** `updated` 날짜 기반 stale 자동 감지 + 갱신 제안.

**Phase 4:** MCP 서버에 lint 엔드포인트 추가 → LLM Agent가 세션마다 자동 lint.

## 다음

멀티 디바이스 동기화: [docs/05-sync/01-comparison.md](../05-sync/01-comparison.md)
