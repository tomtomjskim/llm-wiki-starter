#!/usr/bin/env python3
"""
lint-frontmatter.py — wiki 파일의 YAML frontmatter 필수 필드 검사

사용법:
  python3 scripts/lint-frontmatter.py ~/wiki
  python3 scripts/lint-frontmatter.py ~/wiki/compiled
  python3 scripts/lint-frontmatter.py ~/wiki --verbose
  python3 scripts/lint-frontmatter.py ~/wiki --error-only

종료 코드:
  0 — 오류 없음
  1 — 오류 1건 이상 발견
"""

import sys
import os
import re
import argparse
from pathlib import Path
from datetime import datetime, date
from typing import Dict, List, Optional


REQUIRED_FIELDS = ["name", "description", "type"]
STALE_THRESHOLD_DAYS = 90
CONFIDENCE_LOW_THRESHOLD_DAYS = 30

VALID_TYPES = {
    "compiled", "learn", "decision", "rule", "pattern",
    "guide", "index", "meta", "project", "journal"
}

DATE_PLACEHOLDERS = {"YYYY-MM-DD", "<YYYY-MM-DD>"}


def extract_frontmatter(content: str) -> Optional[Dict[str, str]]:
    """YAML frontmatter 블록을 파싱해서 딕셔너리로 반환. 없으면 None."""
    lines = content.splitlines()
    if not lines or lines[0].strip() != "---":
        return None

    end_idx = None
    for i, line in enumerate(lines[1:], start=1):
        if line.strip() == "---":
            end_idx = i
            break

    if end_idx is None:
        return None

    fm_lines = lines[1:end_idx]
    result = {}

    for line in fm_lines:
        # 주석 제거
        if line.strip().startswith("#"):
            continue
        # 단순 key: value 파싱 (중첩 없이)
        match = re.match(r'^(\w+):\s*(.*)', line)
        if match:
            key = match.group(1)
            value = re.split(r'\s+#', match.group(2), maxsplit=1)[0].strip().strip('"').strip("'")
            if value and not value.startswith("#"):
                result[key] = value

    return result


def check_file(filepath: Path, verbose: bool = False) -> List[Dict[str, str]]:
    """파일 하나를 검사해서 이슈 목록을 반환."""
    issues = []

    try:
        content = filepath.read_text(encoding="utf-8")
    except Exception as e:
        issues.append({
            "level": "ERROR",
            "file": str(filepath),
            "message": f"파일 읽기 실패: {e}"
        })
        return issues

    # frontmatter 없는 파일
    if not content.startswith("---"):
        if filepath.name == "README.md":
            return issues
        # raw/ 폴더는 frontmatter 불필요
        if "/raw/" in str(filepath):
            return issues
        issues.append({
            "level": "WARNING",
            "file": str(filepath),
            "message": "frontmatter 없음 (--- 로 시작하지 않음)"
        })
        return issues

    fm = extract_frontmatter(content)
    if fm is None:
        issues.append({
            "level": "WARNING",
            "file": str(filepath),
            "message": "frontmatter 파싱 실패 (--- 블록 형식 오류)"
        })
        return issues

    # 필수 필드 검사
    for field in REQUIRED_FIELDS:
        if field not in fm or not fm[field]:
            issues.append({
                "level": "ERROR",
                "file": str(filepath),
                "message": f"필수 필드 누락: '{field}'"
            })

    # type 값 유효성
    if "type" in fm and fm["type"] and fm["type"] not in VALID_TYPES:
        issues.append({
            "level": "WARNING",
            "file": str(filepath),
            "message": f"알 수 없는 type 값: '{fm['type']}' (유효값: {', '.join(sorted(VALID_TYPES))})"
        })

    # updated 날짜 검사
    if "updated" in fm and fm["updated"]:
        if fm["updated"] in DATE_PLACEHOLDERS:
            return issues

        try:
            updated_date = datetime.strptime(fm["updated"], "%Y-%m-%d").date()
            delta = (date.today() - updated_date).days

            if delta > STALE_THRESHOLD_DAYS:
                issues.append({
                    "level": "WARNING",
                    "file": str(filepath),
                    "message": f"stale: {delta}일 미갱신 (updated: {fm['updated']})"
                })

            # confidence: low + 30일 초과
            if fm.get("confidence") == "low" and delta > CONFIDENCE_LOW_THRESHOLD_DAYS:
                issues.append({
                    "level": "WARNING",
                    "file": str(filepath),
                    "message": f"confidence: low 이고 {delta}일 경과 — 검증 또는 삭제 결정 필요"
                })
        except ValueError:
            issues.append({
                "level": "WARNING",
                "file": str(filepath),
                "message": f"updated 날짜 형식 오류: '{fm['updated']}' (YYYY-MM-DD 필요)"
            })
    else:
        if verbose:
            issues.append({
                "level": "INFO",
                "file": str(filepath),
                "message": "updated 필드 없음"
            })

    # status: deprecated 알림
    if fm.get("status") == "deprecated":
        issues.append({
            "level": "INFO",
            "file": str(filepath),
            "message": "status: deprecated — 정리 후보"
        })

    return issues


def lint_directory(root: Path, verbose: bool = False, error_only: bool = False) -> List[Dict[str, str]]:
    """디렉토리 내 모든 .md 파일을 재귀적으로 검사."""
    all_issues = []

    md_files = sorted(root.rglob("*.md"))
    # .git, .obsidian 제외
    md_files = [f for f in md_files if "/.git/" not in str(f) and "/.obsidian/" not in str(f)]

    for filepath in md_files:
        issues = check_file(filepath, verbose=verbose)
        if error_only:
            issues = [i for i in issues if i["level"] == "ERROR"]
        all_issues.extend(issues)

    return all_issues


def main():
    parser = argparse.ArgumentParser(
        description="wiki 파일의 YAML frontmatter 필수 필드 검사"
    )
    parser.add_argument("path", help="검사할 디렉토리 또는 파일 경로")
    parser.add_argument("--verbose", "-v", action="store_true", help="INFO 레벨도 출력")
    parser.add_argument("--error-only", action="store_true", help="ERROR만 출력")
    args = parser.parse_args()

    target = Path(args.path).expanduser().resolve()

    if not target.exists():
        print(f"오류: 경로가 존재하지 않습니다: {target}", file=sys.stderr)
        sys.exit(1)

    if target.is_file():
        issues = check_file(target, verbose=args.verbose)
        if args.error_only:
            issues = [i for i in issues if i["level"] == "ERROR"]
        files_checked = 1
    else:
        issues = lint_directory(target, verbose=args.verbose, error_only=args.error_only)
        files_checked = len(list(target.rglob("*.md")))

    # 결과 출력
    level_order = {"ERROR": 0, "WARNING": 1, "INFO": 2}
    issues.sort(key=lambda x: (level_order.get(x["level"], 9), x["file"]))

    error_count = sum(1 for i in issues if i["level"] == "ERROR")
    warning_count = sum(1 for i in issues if i["level"] == "WARNING")
    info_count = sum(1 for i in issues if i["level"] == "INFO")

    for issue in issues:
        level = issue["level"]
        filepath = issue["file"]
        msg = issue["message"]

        # 경로 단축 (홈 디렉토리 ~로)
        short_path = filepath.replace(str(Path.home()), "~")

        print(f"[{level}] {short_path}")
        print(f"       {msg}")

    print("")
    print(f"검사 완료: {files_checked}개 파일")
    print(f"  ERROR:   {error_count}건")
    print(f"  WARNING: {warning_count}건")
    if args.verbose:
        print(f"  INFO:    {info_count}건")

    sys.exit(1 if error_count > 0 else 0)


if __name__ == "__main__":
    main()
