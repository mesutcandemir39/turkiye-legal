#!/usr/bin/env python3
"""SKILL.md frontmatter'ini scripts/validate/schema/skill.schema.json'a karsi dogrular.

Kullanim:
    python scripts/validate/validate_skills.py --strict
    python scripts/validate/validate_skills.py --strict --files-from changed_files.txt

Cikis kodu: basari=0, herhangi bir hata=1 (CI icin).

ONEMLI YAML NOTU: SKILL.md frontmatter'inda kanun/karar numarasi alani
ASLA "no:" olarak yazilmaz. YAML 1.1'de unquoted "no" degeri boolean False'a
cozumlenir (PyYAML SafeLoader ile dogrulandi, "Norway problem" olarak bilinir).
Bu yuzden alan adi "numara" olarak secildi. Bu script boyle bir hatayi
yakalarsa (sources[].numara eksik ama sources[].False anahtari varsa)
kullaniciya bunu acikca soyler.
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
    print("HATA: pyyaml kurulu degil. `pip install -r scripts/requirements.txt` calistirin.", file=sys.stderr)
    sys.exit(1)

try:
    import jsonschema
except ImportError:
    print("HATA: jsonschema kurulu degil. `pip install -r scripts/requirements.txt` calistirin.", file=sys.stderr)
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parents[2]
SCHEMA_PATH = REPO_ROOT / "scripts" / "validate" / "schema" / "skill.schema.json"
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


class ValidationError(Exception):
    pass


def find_skill_files(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("*/skills/*/SKILL.md"))


def parse_frontmatter(path: Path) -> dict:
    text = path.read_text(encoding="utf-8")
    m = FRONTMATTER_RE.match(text)
    if not m:
        raise ValidationError(f"{path}: YAML frontmatter bulunamadi (dosya '---' ile baslamiyor)")
    try:
        data = yaml.safe_load(m.group(1))
    except yaml.YAMLError as e:
        raise ValidationError(f"{path}: YAML parse hatasi: {e}") from e
    if not isinstance(data, dict):
        raise ValidationError(f"{path}: frontmatter bir mapping (dict) olmali")
    # Norway-problem erken tespiti: sources listesinde True/False anahtari varsa
    # bu, birisi "no:" yazdi ve YAML onu boolean'a cevirdi demektir.
    tl = data.get("turkiye_legal", {})
    for i, src in enumerate(tl.get("sources", []) if isinstance(tl, dict) else []):
        if isinstance(src, dict) and (True in src or False in src):
            raise ValidationError(
                f"{path}: turkiye_legal.sources[{i}] icinde boolean anahtar tespit edildi. "
                f"Muhtemel neden: 'no:' alani unquoted yazildi ve YAML 1.1 onu False'a cozdu. "
                f"Duzeltme: 'no:' yerine 'numara:' kullanin."
            )
    return data


def validate_one(path: Path, schema: dict) -> list[str]:
    errors: list[str] = []
    try:
        data = parse_frontmatter(path)
    except ValidationError as e:
        return [str(e)]

    validator = jsonschema.Draft7Validator(schema)
    for err in sorted(validator.iter_errors(data), key=lambda e: e.path):
        loc = " -> ".join(str(p) for p in err.path) or "(kok)"
        errors.append(f"{path}: [{loc}] {err.message}")

    # Sema disi, semantik kontrol: risk_level >= high => requires_human_review true
    # (semada allOf ile de kontrol ediliyor, burada ikinci bir savunma katmani)
    tl = data.get("turkiye_legal", {})
    if isinstance(tl, dict):
        risk = tl.get("risk_level")
        rhr = tl.get("requires_human_review")
        if risk in ("high", "critical") and rhr is not True:
            errors.append(
                f"{path}: risk_level='{risk}' iken requires_human_review=true OLMALI "
                f""
            )

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true", help="Herhangi bir uyariyi hataya cevirir (CI icin varsayilan davranis)")
    ap.add_argument("--files-from", type=Path, default=None, help="Yalniz bu dosyadaki SKILL.md yollarini dogrula (satir satir)")
    args = ap.parse_args()

    if not SCHEMA_PATH.exists():
        print(f"HATA: sema dosyasi bulunamadi: {SCHEMA_PATH}", file=sys.stderr)
        return 1
    schema = json.loads(SCHEMA_PATH.read_text(encoding="utf-8"))

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
        all_errors.extend(validate_one(path, schema))

    print(f"{len(skill_files)} SKILL.md dosyasi tarandi.")
    if all_errors:
        print(f"\n{len(all_errors)} HATA bulundu:\n")
        for e in all_errors:
            print(f"  - {e}")
        return 1

    print("Tumu gecti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
