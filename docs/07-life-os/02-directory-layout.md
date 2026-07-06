---
name: life-os-directory-layout
description: Life OS profile의 starter-compatible 디렉토리 구조
type: guide
updated: 2026-07-06
status: active
---

# Life OS 디렉토리 레이아웃

Life OS는 starter의 3-tier 구조를 유지하면서 하위 profile로 추가한다.
처음부터 별도 repository를 만들 필요는 없다.

생성 명령:

```bash
bash scripts/init-wiki.sh --life-os ~/wiki
```

## 권장 구조

```text
~/wiki/
├── raw/
│   └── life-os/                  # 원본 수집, export, import 후보
│
├── personal/
│   └── life-os/
│       ├── inbox/                # 세션 요약, 빠른 메모, 미검토 기록
│       ├── reviewed/             # 사람이 확인한 개인 지식
│       └── canonical/            # 장기 기준, 반복 정책, 운영 루틴
│
└── compiled/
    └── life-os/
        ├── generated/            # AI 정리 후보
        ├── hubs/                 # Home, area hub, bridge hub
        └── context-packs/        # AI 세션 전달용 bundle 후보
```

## 경로별 역할

| Path | 역할 | 기본 신뢰도 | Agent write |
|---|---|---:|---|
| `raw/life-os/` | 원본 source, import 후보 | 낮음 | 제한 |
| `personal/life-os/inbox/` | 세션 요약, 빠른 기록 | 낮음 | 허용 |
| `compiled/life-os/generated/` | AI 정리 후보 | 낮음-중간 | 허용 |
| `personal/life-os/reviewed/` | 사람이 검토한 지식 | 중간-높음 | 제안만 |
| `personal/life-os/canonical/` | 장기 기준 | 높음 | 제안만 |
| `compiled/life-os/hubs/` | 탐색 허브와 MOC | 중간 | 제안 또는 허용 |
| `compiled/life-os/context-packs/` | AI 전달용 파생 bundle | 중간 | 허용 |

## Hub 예시

```text
compiled/life-os/hubs/
├── home.md
├── projects-hub.md
├── learning-hub.md
├── career-hub.md
├── health-hub.md
├── finance-hub.md
├── operations-hub.md
└── bridges-hub.md
```

처음부터 모든 hub를 만들 필요는 없다. `home.md`, `projects-hub.md`,
`learning-hub.md`, `operations-hub.md` 정도로 시작하고 실제 기록이 쌓일 때
확장한다.

## 기존 personal-wiki가 있는 경우

이미 `wiki/inbox`, `wiki/generated`, `wiki/reviewed`, `wiki/canonical`처럼
엄격한 trust flow를 쓰는 개인 wiki가 있다면 그 구조를 유지해도 된다. 이
starter의 Life OS profile은 범용 설명이며, 기존 wiki를 강제로
`raw/personal/compiled`로 옮기라는 뜻이 아니다.

대응 관계:

| Starter Life OS | Strict personal wiki |
|---|---|
| `personal/life-os/inbox/` | `wiki/inbox/` |
| `compiled/life-os/generated/` | `wiki/generated/life-os/` |
| `personal/life-os/reviewed/` | `wiki/reviewed/life-os/` |
| `personal/life-os/canonical/` | `wiki/canonical/life-os/` |

## 별도 repo 옵션

Life OS가 독립 제품 수준으로 커지거나, 민감도가 높아서 starter wiki와 물리적으로
분리해야 한다면 별도 repo를 사용할 수 있다.

```text
~/life-os-wiki/
~/llm-wiki-starter/
```

장점:

- 권한, remote, sync 정책을 분리할 수 있다.
- Telegram, 자동 review, context export 같은 고급 자동화를 독립적으로 붙일 수 있다.
- 공개 starter와 개인 지식이 섞일 위험이 줄어든다.

단점:

- 초기 학습 비용이 올라간다.
- starter의 기본 스크립트와 문서 흐름을 따로 맞춰야 한다.
- 사용자가 "별도 제품"처럼 느낄 수 있다.

초기에는 같은 wiki 안의 선택 profile로 시작하고, 자동화와 민감도가 커질 때
별도 repo를 검토한다.
