---
name: life-os-ai-context-pack
description: Life OS 문서를 AI 세션에 안전하게 전달하는 context pack 기준
type: guide
updated: 2026-07-06
status: active
---

# AI Context Pack

AI context pack은 Life OS 전체를 AI에 던지는 방식이 아니다. 목적에 맞는
reviewed/canonical 중심 bundle을 만들고, raw는 필요한 경우에만 source index로
제공한다.

## 기본 원칙

```text
canonical + reviewed 중심 bundle
  -> AI / Notion / 다른 개발환경

raw / inbox / generated
  -> 기본 제외
  -> 필요한 경우 미검토 자료로 표시
```

raw 전체 dump는 피한다. 오래된 기록, 추측, 민감정보가 섞여 AI 답변 품질과
보안 모두 나빠질 수 있다.

## 추천 산출물

```text
compiled/life-os/context-packs/YYYY-MM-DD-profile/
├── AI_HANDOFF.md
├── MANIFEST.md
├── CANONICAL_REVIEWED_BUNDLE.md
├── RAW_INDEX.md
└── SOURCE_FILES.txt
```

| 파일 | 역할 |
|---|---|
| `AI_HANDOFF.md` | AI에게 전달할 사용 규칙 |
| `MANIFEST.md` | 포함 파일 목록과 생성 목적 |
| `CANONICAL_REVIEWED_BUNDLE.md` | 실제 기본 컨텍스트 |
| `RAW_INDEX.md` | raw 파일 목록 또는 source alias |
| `SOURCE_FILES.txt` | 재생성 가능한 source file 목록 |

## Profile 예시

| Profile | 목적 | 포함 범위 |
|---|---|---|
| `quick` | 새 AI session 시작 | 핵심 canonical, 최근 reviewed hub |
| `project` | 특정 프로젝트 작업 | project hub, 결정 기록, 관련 runbook |
| `learning` | 학습 계획/정리 | learning hub, reviewed learning notes |
| `life-review` | 주간/월간 회고 | 최근 inbox index, generated 후보, reviewed routines |
| `notion` | Notion 보기용 | raw 제외, reviewed summary 중심 |

## AI Handoff 문구

```text
이 context pack은 Life OS wiki의 reviewed/canonical 문서를 묶은 자료다.
Git과 Markdown 원본이 최종 진실 소스다.
raw, inbox, generated는 기본적으로 미검토 자료로 취급한다.
secret, token, private key, production log 원문은 저장하거나 재출력하지 마라.
충돌하는 정보가 있으면 canonical 문서를 우선하고, 오래된 내용은 확인 필요로 표시하라.
```

## 생성 절차

1. 목적을 고른다. 예: quick, project, learning.
2. 포함할 canonical/reviewed 문서를 선택한다.
3. generated/inbox가 필요하면 "미검토 자료"로 표시한다.
4. raw는 본문이 아니라 `RAW_INDEX.md`로만 제공한다.
5. secret pattern과 민감 경로를 점검한다.
6. AI 답변 중 장기 기준이 될 내용은 다시 reviewed/canonical 승격 후보로 남긴다.

기본 스크립트:

```bash
python3 scripts/export-life-os-context.py --wiki-root ~/wiki --profile quick
```

스크립트는 `personal/life-os/canonical/`과 `personal/life-os/reviewed/` 본문만
bundle에 포함한다. raw, inbox, generated 파일은 `RAW_INDEX.md`에 경로만
기록한다.

## 자동화 경계

자동화 가능:

- bundle 생성
- source file 목록 작성
- obvious secret pattern scan
- Notion import용 Markdown 후보 생성

자동화 금지:

- raw 전체 외부 전송
- generated 내용을 canonical처럼 전달
- secret scan 실패 후 강행
- AI 답변을 reviewed/canonical로 자동 승격
