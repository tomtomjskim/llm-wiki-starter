---
name: YYYY-MM-DD-profile-context-pack
description: AI context pack handoff
type: meta
date: YYYY-MM-DD
status: generated
source: compiled
confidence: medium
profile: quick
related: []
---

# AI Context Pack — {Profile}

## Handoff Rule

```text
이 context pack은 Life OS wiki의 reviewed/canonical 문서를 묶은 자료다.
Git과 Markdown 원본이 최종 진실 소스다.
raw, inbox, generated는 기본적으로 미검토 자료로 취급한다.
secret, token, private key, production log 원문은 저장하거나 재출력하지 마라.
충돌하는 정보가 있으면 canonical 문서를 우선하고, 오래된 내용은 확인 필요로 표시하라.
```

## Included Files

| Path | Trust Level | Reason |
|---|---|---|
| `{path}` | canonical | {포함 이유} |
| `{path}` | reviewed | {포함 이유} |

## Excluded Sources

| Path or Alias | Reason |
|---|---|
| `{raw-source}` | raw source, index only |

## Bundle

{canonical/reviewed 문서 내용을 목적에 맞게 요약 또는 연결한다.}

## Safety Check

- [ ] raw 전문을 포함하지 않았다.
- [ ] secret, token, private key가 없다.
- [ ] generated/inbox 자료가 포함된 경우 미검토 자료라고 표시했다.
- [ ] 오래된 내용은 `확인 필요`로 표시했다.
