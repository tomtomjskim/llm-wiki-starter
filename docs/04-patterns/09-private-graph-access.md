---
name: private-graph-access
description: 개인 wiki의 visual graph/link graph를 안전하게 보는 Tailscale, Wiki.js, MFA 접근 패턴
type: guide
updated: 2026-06-01
status: active
---

# Private Graph Access

개인 wiki의 graph view는 문서 내용보다 더 민감할 수 있다. 프로젝트명, 관계, 우선순위, 운영 흔적이 한눈에 드러나기 때문이다. 따라서 visual graph는 기본적으로 private surface로 취급한다.

## Recommended Shape

먼저 Git/Markdown wiki에서 graph artifact를 생성한다.

```text
wiki/generated/meta/wiki-manifest.json
wiki/generated/meta/wiki-graph.json
wiki/generated/meta/wiki-graph-viewer.html
```

역할:

- `wiki-manifest.json`: Hermes/LLM agent가 신뢰도, project, tag, related를 읽는 routing manifest.
- `wiki-graph.json`: 시각화 도구가 쓰는 node/edge 데이터.
- `wiki-graph-viewer.html`: 사람이 브라우저에서 보는 standalone graph viewer.

CI에서는 generator를 다시 실행하고 generated artifact diff가 있으면 실패시킨다.

```yaml
- name: Generate wiki graph artifacts
  run: python3 scripts/generate_wiki_graph.py

- name: Check generated graph artifacts
  run: git diff --exit-code wiki/generated/meta scripts/generate_wiki_graph.py
```

## Access Options

### Option A: Local Only

Obsidian graph view와 standalone HTML viewer를 로컬에서만 연다.

장점:

- 가장 안전하다.
- 서버 운영 비용이 없다.
- 초기 graph 품질 조정에 적합하다.

단점:

- 다른 기기에서 보기 불편하다.

### Option B: Tailscale-Only Static Viewer

개인 기본 추천안이다.

```text
127.0.0.1:8088 static server
  -> Tailscale Serve
  -> owner devices inside tailnet
```

운영 규칙:

- local server는 `127.0.0.1`에만 bind한다.
- private graph에는 Tailscale Serve를 쓰고, Funnel은 쓰지 않는다.
- Tailnet access control은 owner 또는 매우 작은 admin group만 허용한다.
- raw `sources/` 전체가 아니라 generated graph artifact만 serve한다.

Tailscale Serve는 tailnet 내부 공유용이고 access controls가 적용된다. Funnel은 public internet 노출용이므로 private graph에는 맞지 않다.

## Public/Private Wiki Split

`wiki.example.com` 같은 공개 wiki를 만들고 싶다면 public/private를 처음부터 분리한다.

권장:

```text
wiki.example.com          public wiki
private-wiki.example.com  private wiki behind auth/MFA
```

더 안전한 권장:

```text
public wiki app + public repo/database
private wiki app + private repo/database
```

Wiki.js는 public/private 혼합, groups, permissions, page rules를 지원하지만, 초기에 하나의 instance에서 둘을 섞으면 page rule 실수 하나가 private 문서를 노출할 수 있다. 개인 wiki는 별도 app/storage로 분리하는 쪽이 blast radius가 작다.

## MFA

MFA는 직접 구현하지 말고 검증된 identity layer를 쓴다.

개인 기본안:

- Tailscale로 network reachability 제한.
- Wiki.js를 쓴다면 global 2FA를 켠다.
- Wiki.js 2.5+는 OTP/TOTP 기반 2FA를 지원한다.

공개 도메인 private wiki가 필요할 때:

- Cloudflare Access, Authelia, Authentik, Keycloak/OIDC 같은 reverse-proxy 또는 identity provider를 앞단에 둔다.
- self-registration은 끈다.
- private wiki app 자체에도 별도 계정/2FA를 둔다.

직접 MFA를 구현하는 것은 recovery code, lockout, replay, clock skew, session fixation, phishing resistance까지 책임져야 하므로 personal wiki에는 과하다.

## Public Graph Rule

공개 graph가 필요하면 private graph를 필터링해서 공개하지 않는다. 별도의 curated public manifest에서 새로 생성한다.

```text
private wiki -> private graph
public wiki  -> public graph
```

## Source Links

- Tailscale Serve: https://tailscale.com/docs/features/tailscale-serve
- Tailscale Funnel: https://tailscale.com/docs/features/tailscale-funnel
- Tailscale Grants: https://tailscale.com/docs/features/access-control/grants
- Wiki.js Auth / 2FA: https://docs.requarks.io/auth
- Wiki.js feature overview: https://js.wiki/

## Next

- Wiki health guardrails: [08-wiki-health-guardrails.md](./08-wiki-health-guardrails.md)
- Inter-cluster association: [07-inter-cluster-association.md](./07-inter-cluster-association.md)
