---
name: project-orders-architecture
description: Orders 도메인 아키텍처 현황 스냅샷 — 예시 프로젝트 메모리
type: project
updated: 2026-05-13
confidence: high
status: active
domain: orders
---

# Orders 도메인 아키텍처

{프로젝트 핵심 사실 1-3줄}

Orders 도메인은 주문 생성·조회·취소를 담당한다. Node.js Handler → Service → Repository 3-레이어 구조. MySQL 단일 DB.

## 상태

현재 진행 단계: {리팩토링 진행 중 | 안정화 | 마이그레이션 예정}

## 핵심 제약

기억해야 할 제약:
- {제약 1}: {이유}
- {제약 2}: {이유}

## 주요 테이블

- `orders`: 주문 기본 정보
- `order_items`: 주문 상품 목록

## 관련

- [compiled wiki](~/wiki/compiled/codebase/orders/_index.md)
- [[feedback-orders-no-direct-db]]

---

> 이 파일은 `project_` 타입 메모리 예시입니다.
> 실제 사용 시 파일명: `project_{도메인}_architecture.md`
> 저장 위치: `~/.claude/projects/{project}/memory/`
