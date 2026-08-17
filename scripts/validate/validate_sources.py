#!/usr/bin/env python3
"""Her SKILL.md'nin turkiye_legal.sources atiflarini sources/mevzuat/kanunlar.yaml
kayit defterine karsi dogrular.

Bu, docs/ARCHITECTURE_DECISIONS.md ADR-005'in birinci savunma katmanidir:
"Uydurma kanun adi veya numarasi PR'da CI hatasi verir." Bir SKILL.md, tur=kanun
olan bir kaynak atfi yapiyorsa ve o numara defterde yoksa, bu script CI'i
basarisiz kilar.

Kullanim:
    python scripts/validate/validate_sources.py
    python scripts/validate/validate_sources.py --files-from changed_files.txt
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("HATA: pyyaml kurulu degil. `pip install -r scripts/requirements.txt` calistirin.", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
KANUNLAR_PATH = REPO_ROOT / "sources" / "mevzuat" / "kanunlar.yaml"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)

# Yalniz bu turler kanunlar.yaml'a karsi dogrulanir. Digerleri (ictihat,
# doktrin, teblig, genelge) henuz kendi defterlerine sahip degil (sources/ictihat,
# sources/kurumsal bkz. README'leri) - Faz 4'te doldurulacak, o zamana kadar
# bu turler icin yalniz bicimsel kontrol yapilir (bos numara/ad olmasin).
REGISTRY_CHECKED_TYPES = {"kanun"}


def load_registry(path: Path) -> dict[str, dict]:
    if not path.exists():
        return {}
    data = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
    entries = data.get("kanunlar", [])
    return {str(e["numara"]): e for e in entries if isinstance(e, dict) and "numara" in e}


def find_skill_files(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("*/skills/*/SKILL.md"))


def parse_frontmatter(path: Path) -> dict | None:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        return None
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError:
        return None
    return data if isinstance(data, dict) else None


def validate_one(path: Path, registry: dict[str, dict]) -> list[str]:
    errors: list[str] = []
    data = parse_frontmatter(path)
    if data is None:
        # validate_skills.py zaten bu durumu raporlar; burada tekrar etmiyoruz.
        return errors

    tl = data.get("turkiye_legal", {})
    if not isinstance(tl, dict):
        return errors

    sources = tl.get("sources", [])
    if not isinstance(sources, list):
        errors.append(f"{path}: turkiye_legal.sources bir liste olmali")
        return errors

    for i, src in enumerate(sources):
        if not isinstance(src, dict):
            errors.append(f"{path}: sources[{i}] bir mapping olmali")
            continue

        tur = src.get("tur")
        numara = src.get("numara")
        ad = src.get("ad")

        if not numara or not ad:
            errors.append(f"{path}: sources[{i}] icinde 'numara' veya 'ad' eksik")
            continue

        if tur in REGISTRY_CHECKED_TYPES:
            entry = registry.get(str(numara))
            if entry is None:
                errors.append(
                    f"{path}: sources[{i}] -> '{numara}' sayili kanun "
                    f"sources/mevzuat/kanunlar.yaml defterinde BULUNAMADI. "
                    f"Once deftere ekleyin (resmi kaynaga karsi dogrulayarak), sonra bu atfi kullanin."
                )
            elif entry.get("ad") != ad:
                errors.append(
                    f"{path}: sources[{i}] -> '{numara}' sayili kanunun adi "
                    f"defterle uyusmuyor. Skill'de: '{ad}', defterde: '{entry.get('ad')}'"
                )
            elif entry.get("durum") == "yururlukten_kalkti":
                errors.append(
                    f"{path}: sources[{i}] -> '{numara}' sayili kanun defterde "
                    f"'yururlukten_kalkti' olarak isaretli. Guncel mevzuata atif yapin."
                )

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--files-from", type=Path, default=None)
    args = ap.parse_args()

    registry = load_registry(KANUNLAR_PATH)
    if not registry:
        print(f"UYARI: {KANUNLAR_PATH} bos veya bulunamadi. Kanun atifli hicbir skill dogrulanamayacak.")

    if args.files_from:
        if not args.files_from.exists():
            print(f"UYARI: {args.files_from} bulunamadi, degisen dosya yok sayiliyor.")
            return 0
        candidates = [
            REPO_ROOT / line.strip()
            for line in args.files_from.read_text(encoding="utf-8").splitlines()
            if line.strip().endswith("SKILL.md")
        ]
        skill_files = [p for p in candidates if p.exists()]
    else:
        skill_files = find_skill_files(REPO_ROOT)

    if not skill_files:
        print("Dogrulanacak SKILL.md dosyasi bulunamadi. (Faz 4 tamamlanana kadar bu normaldir.)")
        return 0

    all_errors: list[str] = []
    for path in skill_files:
        all_errors.extend(validate_one(path, registry))

    print(f"{len(skill_files)} SKILL.md dosyasi, {len(registry)} kayitli kanuna karsi tarandi.")
    if all_errors:
        print(f"\n{len(all_errors)} HATA bulundu:\n")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("Tumu gecti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
