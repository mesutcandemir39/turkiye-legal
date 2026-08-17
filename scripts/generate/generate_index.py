#!/usr/bin/env python3
"""Tum plugin'lerdeki SKILL.md dosyalarini tarayip kok dizinde bir
discovery dosyasi (skills/index.json benzeri, burada index.json) uretir.

Bu dosya, monorepo genelinde "hangi skill'ler var, hangi risk seviyesinde,
hangi kanuna dayaniyor" sorusuna CI disi araclarin (orn. gelecekteki bir
web katalog sayfasi) hizli cevap verebilmesi icindir. Claude Code'un kendisi
bu dosyayi okumaz; yalniz insan/arac tuketimi icindir.

Kullanim:
    python scripts/generate/generate_index.py
    python scripts/generate/generate_index.py --check
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("HATA: pyyaml kurulu degil.", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
INDEX_PATH = REPO_ROOT / "index.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def build_index(repo_root: Path) -> dict:
    entries = []
    for skill_path in sorted(repo_root.glob("*/skills/*/SKILL.md")):
        plugin_name = skill_path.parts[-3]
        text = skill_path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        if not m:
            continue
        try:
            data = yaml.safe_load(m.group(1)) or {}
        except yaml.YAMLError:
            continue
        tl = data.get("turkiye_legal", {}) if isinstance(data, dict) else {}
        entries.append({
            "plugin": plugin_name,
            "skill": data.get("name"),
            "path": str(skill_path.relative_to(repo_root)),
            "category": tl.get("category"),
            "risk_level": tl.get("risk_level"),
            "requires_human_review": tl.get("requires_human_review"),
            "sources_count": len(tl.get("sources", []) or []),
        })
    return {"generated_from": "SKILL.md frontmatter (turkiye_legal blogu)", "skills": entries}


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    generated = build_index(REPO_ROOT)
    generated_text = json.dumps(generated, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        if not INDEX_PATH.exists():
            if not generated["skills"]:
                print("Henuz skill yok; index.json da yok. Tutarli.")
                return 0
            print(f"HATA: {INDEX_PATH} bulunamadi ama {len(generated['skills'])} skill mevcut.")
            return 1
        current_text = INDEX_PATH.read_text(encoding="utf-8")
        if current_text != generated_text:
            print(f"HATA: {INDEX_PATH} guncel degil. `python scripts/generate/generate_index.py` calistirip commit'leyin.")
            return 1
        print(f"{INDEX_PATH} guncel ({len(generated['skills'])} skill).")
        return 0

    INDEX_PATH.write_text(generated_text, encoding="utf-8")
    print(f"{INDEX_PATH} yazildi ({len(generated['skills'])} skill).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
