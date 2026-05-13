---
name: users-index
description: Users 도메인 MOC — 사용자 계정 관리 시스템 (예시)
type: index
domain: users
compiled_at: 2026-05-13
status: active
confidence: high
updated: 2026-05-13
---

# Users Domain — Map of Content

사용자 계정 생성·인증·프로필 관리 도메인. 회원 가입부터 탈퇴까지의 전체 생명주기를 담당한다.

> 이 파일은 예시입니다. 실제 코드베이스 기반이 아닙니다.

## 페이지

| 페이지 | 줄 수 | confidence | 한 줄 요약 |
|--------|-------|------------|-----------|
| overview | 75 | high | 도메인 정의, 핵심 개념 (account/profile/session), 진입점 4개 |
| domain-rules | 140 | high | 비밀번호 정책, 이메일 인증 필수, 계정 잠금 규칙 |
| db-schema | 180 | high | 4개 테이블 (users, user_profiles, user_sessions, email_verifications) |
| api-contracts | 160 | high | 인증 API 6개, 프로필 API 3개 |
| code-map | 90 | high | 8개 파일 → 책임 매핑 |
| known-issues | 110 | medium | 이슈 3건 + 잠재 위험 2건 |

## 빠른 진입

| 작업 또는 질문 | 파일 |
|--------------|------|
| "이 도메인 처음 봐요" | [overview.md](./overview.md) |
| "비밀번호 정책이 뭐죠?" | [domain-rules.md §비밀번호 정책](./domain-rules.md) |
| "어떤 테이블 쓰나요?" | [db-schema.md](./db-schema.md) |
| "로그인 API 명세 주세요" | [api-contracts.md §POST /auth/login](./api-contracts.md) |
| "세션 만료 로직이 어디 있죠?" | [code-map.md §SessionService](./code-map.md) |
| "이메일 인증 안 되는 이슈" | [known-issues.md §I2](./known-issues.md) |

## 출처

- 소스 파일 8개: `src/users/`
- 비즈니스 문서: `docs/requirements/users.md`
- compile 일시: 2026-05-13

## 보완 필요

다음 파일을 INPUT에 추가하면 아래 "확인 필요" 항목이 해결된다:

- `config/auth-config.js` — JWT 만료 시간, 세션 최대 유지 시간 정의 (3건)
- `src/common/EmailService.js` — 이메일 전송 실패 처리 로직 확인 (1건)

## 부수 발견

compile 중 발견한 주의 사항:

- `src/users/AuthHandler.js:134` — 비밀번호 평문 로깅 위험 (console.log 내 password 필드)
- `user_sessions` 테이블 — `expires_at` 컬럼에 인덱스 없음, 만료 세션 정리 쿼리 성능 우려
