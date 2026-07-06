---
name: life-os-trust-boundary-and-promotion
description: Life OS profile의 신뢰 경계와 승격 정책
type: guide
updated: 2026-07-06
status: active
---

# 신뢰 경계와 승격

Life OS의 핵심은 기록을 많이 모으는 것이 아니라, 신뢰도가 다른 자료를 섞지
않는 것이다. 특히 AI가 만든 정리본은 편리하지만 검토 전에는 확정 사실이
아니다.

## Trust Flow

```text
raw/inbox -> generated -> reviewed -> canonical
```

| 단계 | 의미 | 사용 방식 |
|---|---|---|
| raw | 원본 source, export, 로그, 첨부 | 기본 답변 컨텍스트에서 제외 |
| inbox | 세션 요약, 빠른 메모, 미정리 기록 | 최근 맥락 확인용 |
| generated | AI가 구조화한 후보 | 검토 후보, authority 아님 |
| reviewed | 사람이 읽고 확인한 지식 | 일반 AI 세션 컨텍스트로 사용 가능 |
| canonical | 장기 기준, 반복 정책 | 충돌 시 최우선 |

## 승격 기준

### raw/inbox -> generated

- 원본에서 민감정보를 제거했다.
- 나중에 다시 볼 가치가 있다.
- 출처 날짜와 source alias를 남겼다.
- AI가 추론한 내용은 `confidence: low` 또는 `medium`으로 표시했다.

### generated -> reviewed

- 사람이 읽고 오류를 확인했다.
- source가 남아 있다.
- 비밀값, PII, 회사 내부 원문이 없다.
- 기존 reviewed 문서와 중복되거나 충돌하지 않는다.
- 재사용 가치가 있다.

### reviewed -> canonical

- 반복 적용할 기준이다.
- 틀렸을 때 영향이 크다.
- 다른 세션에서도 기본값으로 써도 된다.
- 사람이 명시적으로 승인했다.

## Agent Write Policy

| Path | Agent write | Human review |
|---|---|---|
| `personal/life-os/inbox/**` | allowed | optional |
| `compiled/life-os/generated/**` | allowed | recommended |
| `personal/life-os/reviewed/**` | proposal only | required |
| `personal/life-os/canonical/**` | proposal only | required |

agent는 session summary, generated 후보, review 후보를 만들 수 있다. 그러나
reviewed/canonical 승격, archive/delete, 기존 정책 변경은 사용자의 명시 승인을
받아야 한다.

## 민감 정보 규칙

저장 금지:

- password
- API token
- private key
- production `.env` 실제 값
- DB dump
- 원본 민감 로그
- 주민번호, 결제정보 등 PII
- 회사/고객 내부 비밀 원문

민감한 영역은 원문 대신 요약만 남긴다.

| 영역 | 권장 저장 방식 |
|---|---|
| 건강 | 진단/처방 원문이 아니라 루틴, 질문, 검토 날짜 |
| 재무 | 계좌/금액 원문이 아니라 원칙, 세금 질문, 리스크 기준 |
| 커리어 | 외부 공개 가능한 포트폴리오 증거와 결정 기록 |
| 회사 업무 | 익명화된 운영 패턴과 개인 학습만 |

## 보류와 폐기

보류는 영구 상태가 아니다. 승격하지 않을 항목은 다음 중 하나로 처리한다.

| Disposition | 의미 |
|---|---|
| `revise` | 보강 후 재검토 |
| `merge` | 기존 reviewed/canonical 문서에 병합 |
| `keep-generated` | 히스토리 산출물로 유지 |
| `archive-candidate` | 별도 승인 후 archive 후보 |
| `delete-candidate` | 별도 승인 후 삭제 후보 |
| `needs-human-source-check` | 원문 확인 전 승격 불가 |

삭제보다 archive를 우선하되, secret이나 오염 데이터는 별도 승인 후 삭제한다.
