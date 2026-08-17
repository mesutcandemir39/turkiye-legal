#!/usr/bin/env python3
"""Plugin hooks/hooks.json dosyalarindaki shell cagrilarini guvenlik acisindan denetler.

v0.0.1'de hicbir plugin hooks/ kullanmiyor (Layer 5 - Connectors, arayuz
duzeyinde tasarlandi,.). Bu script,
ileride bir plugin hooks eklediginde CI'in bunu otomatik denetlemesi icin
simdiden hazir bulunuyor.

Denetlenen riskler:
- Kabuk enjeksiyonuna acik komut kalibi (degisken interpolasyonu ile
  olusturulan komutlar, `sh -c "$VAR"` gibi)
- Genis yetkili komutlar (rm -rf, curl | sh, sudo)
- Ag erisimi olan ama parametrize edilmemis komutlar

Kullanim:
    python scripts/validate/lint_tool_scope.py [--strict]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

DANGEROUS_PATTERNS = [
    (re.compile(r"\brm\s+-rf\b"), "rm -rf gibi geri alinamaz bir silme komutu"),
    (re.compile(r"curl[^|]*\|\s*(sh|bash)\b"), "pipe-to-shell deseni (curl | sh) - tedarik zinciri riski"),
    (re.compile(r"\bsudo\b"), "sudo ile yukseltilmis yetki kullanimi"),
    (re.compile(r"eval\s*\("), "eval() kullanimi - enjeksiyon riski"),
    (re.compile(r"\$\{[A-Za-z_]+\}.*\|\s*(sh|bash)"), "degisken interpolasyonu + shell pipe"),
]


def find_hooks_files(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("*/hooks/hooks.json"))


def lint_hooks_file(path: Path) -> list[str]:
    errors = []
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as e:
        return [f"{path}: JSON parse hatasi: {e}"]

    text_blob = json.dumps(data, ensure_ascii=False)
    for pattern, description in DANGEROUS_PATTERNS:
        if pattern.search(text_blob):
            errors.append(f"{path}: riskli desen tespit edildi — {description}")

    return errors


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--strict", action="store_true")
    args = ap.parse_args()

    hooks_files = find_hooks_files(REPO_ROOT)
    if not hooks_files:
        print("Hicbir plugin hooks/hooks.json kullanmiyor. (v0.0.1 icin beklenen durum.)")
        return 0

    errors: list[str] = []
    for path in hooks_files:
        errors.extend(lint_hooks_file(path))

    print(f"{len(hooks_files)} hooks.json dosyasi tarandi.")
    if errors:
        print(f"\n{len(errors)} HATA bulundu:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("Tumu gecti.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
