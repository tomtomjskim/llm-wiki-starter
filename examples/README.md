---
name: examples-readme
description: examples/ 디렉토리 사용 안내
type: guide
updated: 2026-05-13
status: active
---

# examples/ 사용 안내

실제 wiki 페이지가 어떻게 보여야 하는지 참고할 수 있는 예시 모음.

모든 예시는 **완전히 가상의 데이터**를 사용한다. 도메인명 `users`는 일반적인 예시로만 사용되며, 특정 프로젝트와 무관하다.

## 구조

```
examples/
├── README.md                          # 이 파일
└── compiled-codebase/
    └── sample-domain/
        └── _index.md                  # users 도메인 MOC 예시
```

## 어떻게 활용하는가

### MOC 작성 시 참고

`sample-domain/_index.md`를 열어 MOC의 구조와 "빠른 진입" 표 작성 방법을 확인한다.

### compile 프롬프트 작성 시 참고

LLM에 compile을 요청할 때 예시 파일을 컨텍스트로 주면 원하는 형식으로 출력된다.

```
examples/compiled-codebase/sample-domain/_index.md 의 형식과 동일하게
~/wiki/compiled/codebase/orders/_index.md 를 작성해줘.
```

### 팀에 wiki 소개 시

실제 코드베이스 정보가 없는 예시 파일이므로 팀에 "이런 형태가 됩니다"를 보여주기에 적합하다.

## 더 많은 예시 기여

이 레포에 PR을 열어 다양한 도메인 예시를 추가할 수 있다.

기여 규칙:
- 실제 회사/프로젝트 정보 포함 금지
- 가상의 도메인명 사용 (`users`, `orders`, `products`, `payments` 등)
- frontmatter 필수
- 각 파일 200줄 이하
