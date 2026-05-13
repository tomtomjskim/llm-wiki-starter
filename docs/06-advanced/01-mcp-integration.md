---
name: mcp-integration
description: wiki를 LLM Agent API로 노출하는 MCP 서버 패턴
type: guide
updated: 2026-05-13
status: active
---

# MCP 연동 (고급)

## MCP란

Model Context Protocol. LLM이 외부 도구와 데이터 소스에 접근할 수 있는 표준 프로토콜.

- 공식 사이트: [modelcontextprotocol.io](https://modelcontextprotocol.io)
- GitHub: [github.com/modelcontextprotocol](https://github.com/modelcontextprotocol)

## wiki를 MCP 서버로 노출하는 이유

기본 방식 (파일 직접 로드):
```
Claude Code → /add ~/wiki/compiled/... → 수동
```

MCP 방식:
```
Claude Code → MCP Server → wiki 파일 시스템 → 자동
```

MCP 서버가 있으면:
- "orders 도메인 overview를 읽어줘" → LLM이 자동으로 파일 찾아 읽기
- wiki 전체 검색 → LLM이 검색 결과를 컨텍스트에 자동 주입
- 세션마다 수동으로 `/add` 하지 않아도 됨

## 핵심 도구 3개

### search_wiki(query)

wiki 전체에서 키워드 검색. 관련 파일 경로와 매칭 텍스트 반환.

```json
{
  "name": "search_wiki",
  "description": "wiki에서 키워드로 페이지 검색",
  "inputSchema": {
    "query": {"type": "string"},
    "path": {"type": "string", "description": "검색 범위 (선택)"}
  }
}
```

### read_page(path)

특정 파일을 읽어 컨텍스트에 주입.

```json
{
  "name": "read_page",
  "description": "wiki 페이지 읽기",
  "inputSchema": {
    "path": {"type": "string", "description": "~/wiki/... 상대 경로"}
  }
}
```

### list_pages(domain)

특정 도메인의 파일 목록 반환.

```json
{
  "name": "list_pages",
  "description": "도메인의 파일 목록",
  "inputSchema": {
    "domain": {"type": "string"}
  }
}
```

## MCP 서버 구현 개요

Node.js/Python으로 구현 가능. `@modelcontextprotocol/sdk` 사용 권장.

```javascript
// 개념 코드 (실제 구현은 MCP SDK 문서 참조)
import { Server } from "@modelcontextprotocol/sdk/server/index.js";

const server = new Server({
  name: "wiki-server",
  version: "0.1.0"
});

server.setRequestHandler("tools/call", async (request) => {
  if (request.params.name === "search_wiki") {
    const results = await searchFiles(
      "~/wiki",
      request.params.arguments.query
    );
    return { content: [{ type: "text", text: JSON.stringify(results) }] };
  }
});
```

## Claude Code 연동 설정

MCP 서버 구현 후 `~/.claude/settings.json` 에 등록:

```json
{
  "mcpServers": {
    "wiki": {
      "command": "node",
      "args": ["/path/to/wiki-mcp-server/index.js"],
      "env": {
        "WIKI_ROOT": "/Users/yourname/wiki"
      }
    }
  }
}
```

## 참고 자료

- [MCP 공식 문서](https://modelcontextprotocol.io/docs)
- [MCP TypeScript SDK](https://github.com/modelcontextprotocol/typescript-sdk)
- [MCP Python SDK](https://github.com/modelcontextprotocol/python-sdk)
- [Claude Code MCP 설정 가이드](https://docs.anthropic.com/claude-code/mcp)

## 이 starter kit의 MCP 지원 로드맵

현재: 개념 문서만 제공.

향후 계획:
- `scripts/wiki-mcp-server.js`: 기본 MCP 서버 구현 추가
- `search_wiki`, `read_page`, `list_pages` 세 도구 구현
- Claude Code 자동 설정 스크립트

관심 있다면 이 레포에 이슈/PR을 열어달라.

## 다음

자동화: [02-automation.md](./02-automation.md)
