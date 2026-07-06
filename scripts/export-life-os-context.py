#!/usr/bin/env python3
"""Export a Life OS context pack from reviewed/canonical Markdown."""

import argparse
from datetime import date
from pathlib import Path
from typing import Iterable, List, Optional


HANDOFF_TEXT = """\
이 context pack은 Life OS wiki의 reviewed/canonical 문서를 묶은 자료다.
Git과 Markdown 원본이 최종 진실 소스다.
raw, inbox, generated는 기본적으로 미검토 자료로 취급한다.
secret, token, private key, production log 원문은 저장하거나 재출력하지 마라.
충돌하는 정보가 있으면 canonical 문서를 우선하고, 오래된 내용은 확인 필요로 표시하라.
"""


def markdown_files(root: Path) -> List[Path]:
    if not root.exists():
        return []
    return sorted(path for path in root.rglob("*.md") if path.is_file())


def relative(path: Path, root: Path) -> str:
    return path.relative_to(root).as_posix()


def write_file(path: Path, content: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content.rstrip() + "\n", encoding="utf-8")


def render_bundle(files: Iterable[Path], wiki_root: Path) -> str:
    sections = [
        "# Canonical / Reviewed Bundle",
        "",
        "이 파일은 Life OS context pack의 기본 컨텍스트다. raw, inbox, generated 본문은 포함하지 않는다.",
    ]
    for path in files:
        rel = relative(path, wiki_root)
        sections.extend(["", f"## {rel}", "", path.read_text(encoding="utf-8").rstrip()])
    return "\n".join(sections)


def render_manifest(profile: str, export_date: str, source_files: List[Path], raw_files: List[Path], wiki_root: Path) -> str:
    lines = [
        "# Life OS Context Pack Manifest",
        "",
        f"- profile: `{profile}`",
        f"- date: `{export_date}`",
        f"- included files: {len(source_files)}",
        f"- indexed unreviewed files: {len(raw_files)}",
        "",
        "## Included",
    ]
    lines.extend(f"- `{relative(path, wiki_root)}`" for path in source_files)
    lines.extend(["", "## Indexed Only"])
    lines.extend(f"- `{relative(path, wiki_root)}`" for path in raw_files)
    return "\n".join(lines)


def render_raw_index(raw_files: List[Path], wiki_root: Path) -> str:
    lines = [
        "# Raw / Unreviewed Index",
        "",
        "이 파일은 raw, inbox, generated 자료의 경로 index다. 본문은 포함하지 않는다.",
    ]
    if raw_files:
        lines.extend(["", "## Files"])
        lines.extend(f"- `{relative(path, wiki_root)}`" for path in raw_files)
    else:
        lines.extend(["", "No raw, inbox, or generated files found."])
    return "\n".join(lines)


def export_context_pack(wiki_root: Path, profile: str, export_date: str, output_dir: Optional[Path] = None) -> Path:
    canonical = markdown_files(wiki_root / "personal/life-os/canonical")
    reviewed = markdown_files(wiki_root / "personal/life-os/reviewed")
    source_files = canonical + reviewed

    raw_files = []
    for rel in [
        "raw/life-os",
        "personal/life-os/inbox",
        "compiled/life-os/generated",
    ]:
        raw_files.extend(markdown_files(wiki_root / rel))
    raw_files = sorted(raw_files)

    if output_dir is None:
        output_dir = wiki_root / "compiled/life-os/context-packs" / f"{export_date}-{profile}"

    write_file(output_dir / "AI_HANDOFF.md", "# AI Handoff\n\n```text\n" + HANDOFF_TEXT.rstrip() + "\n```")
    write_file(output_dir / "MANIFEST.md", render_manifest(profile, export_date, source_files, raw_files, wiki_root))
    write_file(output_dir / "CANONICAL_REVIEWED_BUNDLE.md", render_bundle(source_files, wiki_root))
    write_file(output_dir / "RAW_INDEX.md", render_raw_index(raw_files, wiki_root))
    write_file(output_dir / "SOURCE_FILES.txt", "\n".join(relative(path, wiki_root) for path in source_files))
    return output_dir


def main() -> None:
    parser = argparse.ArgumentParser(description="Export Life OS reviewed/canonical context pack.")
    parser.add_argument("--wiki-root", default="~/wiki", help="wiki root path")
    parser.add_argument("--profile", default="quick", help="context pack profile name")
    parser.add_argument("--date", default=date.today().isoformat(), help="export date YYYY-MM-DD")
    parser.add_argument("--output-dir", help="custom output directory")
    args = parser.parse_args()

    wiki_root = Path(args.wiki_root).expanduser().resolve()
    output_dir = Path(args.output_dir).expanduser().resolve() if args.output_dir else None
    written = export_context_pack(wiki_root, args.profile, args.date, output_dir)
    print(f"wrote {written}")


if __name__ == "__main__":
    main()
