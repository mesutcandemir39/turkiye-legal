#!/usr/bin/env python3
"""SKILL.md ve agents/*.md govdelerini iki riske karsi tarar:

1. Sahte/ornek gorunumlu icthad karar numarasi deseni (E. 20XX/..., K. 20XX/...)
   - Skill'ler karar numarasi URETEMEZ (bkz. ADR-005 madde 2). Ornekler
     '____' placeholder'i kullanmak ZORUNDADIR.
2. Yabancı hukuk sizintisi - GDPR, CCPA, FRE, "Avrupa Birligi", ABD eyalet
   hukuku terimleri gibi Turk hukuku disi kavramlarin sizmasi (bkz. ADR-005
   madde 4). Bir skill bu terimleri ACIKCA KARSILASTIRMA amaciyla
   kullaniyorsa (orn. "GDPR'dan farkli olarak KVKK...") bu kabul edilebilir;
   script boyle bir baglami "karsilastirma" anahtar kelimeleriyle ayirt eder
   ve yalniz supheli/context'siz kullanimlari BLOCK eder.

Kullanim:
    python scripts/validate/lint_prompts.py
    python scripts/validate/lint_prompts.py --files-from changed_files.txt
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Gercekci gorunen Esas/Karar deseni: E. 2019/1234, K. 2020/567 gibi.
# Placeholder'lar (E. ____/____, E. YIL/SIRA_NO) bu desenle eslesmez cunku
# rakam grubu icermezler.
REAL_LOOKING_DECISION_RE = re.compile(
    r"\b[EK]\.\s*20\d{2}\s*/\s*\d+\b"
)

FOREIGN_LAW_TERMS = [
    "GDPR", "CCPA", "FRE", "Federal Rules of Evidence",
    "Avrupa Birliği Genel Veri Koruma Tüzüğü",
    "eyalet hukuku", "common law",  # civil_law odagimizla celisen genel terimler
]

# Bu kelimeler yakinda geciyorsa, yabancı terim bilinçli bir karsilastirma
# baglaminda kullaniliyor demektir - izin verilir.
COMPARISON_MARKERS = [
    "farklı olarak", "aksine", "karşılaştır", "değil", "yerine", "benzer şekilde",
    "tersine", "kıyasla", "karşıtı",
]

CONTEXT_WINDOW = 80  # yabancı terimin etrafindan kac karakter kontrol edilecek


def find_target_files(repo_root: Path) -> list[Path]:
    return sorted(repo_root.glob("*/skills/*/SKILL.md")) + sorted(repo_root.glob("*/agents/*.md"))


def strip_frontmatter(text: str) -> str:
    m = re.match(r"^---\n.*?\n---\n", text, re.DOTALL)
    return text[m.end():] if m else text


def check_fake_decisions(path: Path, body: str) -> list[str]:
    errors = []
    for m in REAL_LOOKING_DECISION_RE.finditer(body):
        line_no = body[: m.start()].count("\n") + 1
        errors.append(
            f"{path}:{line_no}: gercekci gorunen karar numarasi tespit edildi: "
            f"'{m.group(0)}'. Skill'ler karar numarasi uretemez (ADR-005 madde 2). "
            f"Ornek gostermek icin 'E. ____/____' gibi acik bir placeholder kullanin."
        )
    return errors


def check_foreign_law_leakage(path: Path, body: str) -> list[str]:
    warnings = []
    for term in FOREIGN_LAW_TERMS:
        for m in re.finditer(re.escape(term), body, re.IGNORECASE):
            start = max(0, m.start() - CONTEXT_WINDOW)
            end = min(len(body), m.end() + CONTEXT_WINDOW)
            context = body[start:end]
            if any(marker.lower() in context.lower() for marker in COMPARISON_MARKERS):
                continue  # bilincli karsilastirma baglaminda, izin ver
            line_no = body[: m.start()].count("\n") + 1
            warnings.append(
                f"{path}:{line_no}: yabanci hukuk terimi '{term}' baglamsiz kullanilmis "
                f"gibi gorunuyor. Eger bilincli bir karsilastirmaysa yakinina "
                f"'farklı olarak' / 'aksine' gibi bir ifade ekleyin; degilse kaldirin "
                f"(bkz. ADR-005 madde 4)."
            )
    return warnings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--files-from", type=Path, default=None)
    args = ap.parse_args()

    if args.files_from:
        if not args.files_from.exists():
            print(f"UYARI: {args.files_from} bulunamadi, degisen dosya yok sayiliyor.")
            return 0
        candidates = [
            REPO_ROOT / line.strip()
            for line in args.files_from.read_text(encoding="utf-8").splitlines()
            if line.strip().endswith(".md")
        ]
        targets = [p for p in candidates if p.exists() and ("/skills/" in str(p) or "/agents/" in str(p))]
    else:
        targets = find_target_files(REPO_ROOT)

    if not targets:
        print("Taranacak skill/agent dosyasi bulunamadi. (Faz 4 tamamlanana kadar bu normaldir.)")
        return 0

    errors: list[str] = []
    warnings: list[str] = []
    for path in targets:
        body = strip_frontmatter(path.read_text(encoding="utf-8"))
        errors.extend(check_fake_decisions(path, body))
        warnings.extend(check_foreign_law_leakage(path, body))

    print(f"{len(targets)} dosya tarandi.")

    if warnings:
        print(f"\n{len(warnings)} UYARI:\n")
        for w in warnings:
            print(f"  ~ {w}")

    if errors:
        print(f"\n{len(errors)} HATA bulundu:\n")
        for e in errors:
            print(f"  - {e}")
        return 1

    print("\nTumu gecti." if not warnings else "\nHata yok, ancak yukaridaki uyarilari gozden gecirin.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
