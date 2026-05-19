---
name: sync-comparison
description: wiki 멀티 디바이스 동기화 4가지 방식 비교표와 추천
type: guide
updated: 2026-05-13
status: active
---

# 동기화 방식 비교

## 배경: Obsidian 로그인으로 공통 관리가 가능한가?

**결론: 가능하다. 단 유료다.**

Obsidian 계정으로 로그인하면 **Obsidian Sync** 서비스를 통해 여러 디바이스 (PC, Mac, iPhone, Android) 간에 vault를 동기화할 수 있다. 별도 설정 없이 Obsidian 앱 내에서 완결된다.

단, 가격이 $4-10/월(플랜에 따라 다름)이다.

**무료 대안이 있는가?** 있다. **Git 기반 + Obsidian Git 플러그인**이 가장 일관성 있는 무료 대안이다. 이 starter kit도 이 방식을 기본 권장한다.

## 4가지 동기화 방식 비교

| 방식 | 가격 | PC↔PC | PC↔모바일 | 충돌 처리 | 설정 난이도 |
|------|------|-------|-----------|----------|------------|
| Obsidian Sync | $4-10/월 | | | 자동 | 쉬움 |
| iCloud | 무료 (5GB) | Mac 전용 | Mac↔iPhone | 자동 | 쉬움 |
| Git 기반 | 무료 | | | 수동 | 보통 |
| Remotely Save (S3/WebDAV) | 스토리지 비용 | | | 보통 | 어려움 |

### Obsidian Sync (유료)

**장점:**
- Obsidian 앱 내 완결, 별도 설정 없음
- 실시간 동기화
- 버전 히스토리 제공 (1년)
- 선택적 파일 암호화 지원

**단점:**
- 유료 ($4/월 기본, $10/월 Plus)
- 저장 용량 제한 (기본 1GB)

**권장 대상:** 설정 복잡도를 피하고 싶고, 월 $4-10를 지불할 의향이 있는 경우.

상세: [03-obsidian-sync-paid.md](./03-obsidian-sync-paid.md)

### iCloud (무료, Mac/iPhone 전용)

**장점:**
- macOS/iOS에서 추가 설정 없이 동기화
- Obsidian의 iCloud 드라이브 지원

**단점:**
- Mac ↔ iPhone 만 가능 (Android, Windows, Linux 지원 안 됨)
- 간헐적 동기화 지연 보고

**권장 대상:** Mac + iPhone 조합으로만 사용하는 경우.

### Git 기반 + Obsidian Git 플러그인 (권장)

**장점:**
- 무료 (private GitHub/GitLab repo)
- 버전 관리 + 히스토리
- 플랫폼 무관 (Windows, Mac, Linux, Android)
- wiki와 코드베이스를 같은 방식으로 관리

**단점:**
- 초기 설정 필요 (Git 지식 필요)
- 모바일에서 자동 동기화를 위해 Obsidian Git 플러그인 설정 필요
- 동시 편집 시 수동 충돌 해결

**이 starter kit 권장 방식.** 상세: [02-git-based-sync.md](./02-git-based-sync.md)

### Remotely Save (S3/WebDAV)

**장점:**
- 플랫폼 무관
- 자체 S3 버킷 사용 가능 (데이터 소유권)

**단점:**
- 설정 복잡 (AWS S3 또는 WebDAV 서버 필요)
- 스토리지 비용 발생
- 충돌 처리 불안정 보고

**권장 대상:** 이미 S3/WebDAV 인프라가 있는 경우.

## 결론 및 권장

| 상황 | 권장 방식 |
|------|----------|
| 간단하게 시작, 비용 OK | Obsidian Sync |
| Mac + iPhone만 | iCloud |
| 무료, Git 익숙 | Git 기반 (이 starter kit 기본) |
| 기존 S3 인프라 있음 | Remotely Save |
| 팀 공유 wiki | Git 기반 (private repo) |
| Git을 운영 기준점으로 쓰고 Agent/서버 mirror까지 연결 | Git primary architecture |

## 다음

Git 기반 동기화 설정: [02-git-based-sync.md](./02-git-based-sync.md)

Git을 단순 동기화가 아니라 운영 기준점으로 쓰는 구조:
[05-git-primary-architecture.md](./05-git-primary-architecture.md)
