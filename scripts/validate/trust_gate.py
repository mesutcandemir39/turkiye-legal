#!/usr/bin/env python3
"""Topluluk Skill Guven Kapisi — bkz. docs/TOPLULUK_SKILL_GUVENI.md, ADR-015.

anthropics/claude-for-legal'deki `legal-builder-hub` plugin'i, Claude Cowork
uzerinde CALISMA ZAMANINDA ucuncu parti skill kesfi/kurulumu yapan bir "app
store" katmanidir. turkiye-legal boyle bir calisma-zamani marketplace'i
SUNMAZ (kullanicilar `claude plugin install` ile dogrudan bu repodan kurar) —
bu yuzden ayni ozellik birebir tasinamaz. Bunun yerine, bu script GitHub PR
surecinde ayni GUVEN KRITERLERINI (bkz. TOPLULUK_SKILL_GUVENI.md) mekanik
olarak denetleyen bir "kapi" gorevi gorur.

Kullanim:
    python scripts/validate/trust_gate.py --files-from changed_files.txt
    python scripts/validate/trust_gate.py --files-from changed_files.txt --json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
FRONTMATTER_RE = re.compile(r"^---\n(.*?)\n---\n", re.DOTALL)


def run_validator(module: str, files_from: Path | None) -> tuple[bool, str]:
    cmd = [sys.executable, str(REPO_ROOT / "scripts" / "validate" / module)]
    if files_from:
        cmd += ["--files-from", str(files_from)]
    proc = subprocess.run(cmd, capture_output=True, text=True, cwd=REPO_ROOT)
    return proc.returncode == 0, (proc.stdout + proc.stderr).strip()


def find_skill_files(files_from: Path | None) -> list[Path]:
    if files_from and files_from.exists():
        candidates = [
            REPO_ROOT / line.strip()
            for line in files_from.read_text(encoding="utf-8").splitlines()
            if line.strip().endswith("SKILL.md")
        ]
        return [p for p in candidates if p.exists()]
    return sorted(REPO_ROOT.glob("*/skills/*/SKILL.md"))


def check_attribution_gate(skill_files: list[Path]) -> list[dict]:
    """Gate 1: Lisans/atif alanlari eksiksiz mi (bkz. TOPLULUK_SKILL_GUVENI.md #1)."""
    findings = []
    for path in skill_files:
        text = path.read_text(encoding="utf-8")
        m = FRONTMATTER_RE.match(text)
        rel = path.relative_to(REPO_ROOT)
        if not m:
            findings.append({"file": str(rel), "ok": False, "reason": "frontmatter bulunamadi"})
            continue
        try:
            import yaml

            data = yaml.safe_load(m.group(1)) or {}
        except Exception as exc:  # noqa: BLE001
            findings.append({"file": str(rel), "ok": False, "reason": f"YAML parse hatasi: {exc}"})
            continue
        tl = data.get("turkiye_legal", {}) if isinstance(data, dict) else {}
        attribution = tl.get("attribution", {}) if isinstance(tl, dict) else {}
        missing = [
            k for k in ("original_author", "original_repository", "license")
            if not attribution.get(k)
        ]
        if missing:
            findings.append({"file": str(rel), "ok": False, "reason": f"attribution eksik: {missing}"})
        elif attribution.get("license") != "Apache-2.0":
            findings.append({"file": str(rel), "ok": False, "reason": "lisans Apache-2.0 degil"})
        else:
            findings.append({"file": str(rel), "ok": True, "reason": "attribution tam"})
    return findings


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--files-from", type=Path, default=None)
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    skill_files = find_skill_files(args.files_from)

    gates = []

    # Gate 1: Allowlist/lisans (attribution alanlari)
    attribution_findings = check_attribution_gate(skill_files) if skill_files else []
    gate1_ok = all(f["ok"] for f in attribution_findings) if attribution_findings else True
    gates.append({
        "name": "Allowlist/Lisans Kapısı",
        "ok": gate1_ok,
        "detail": attribution_findings,
    })

    # Gate 2: Sema uyumu (yapisal)
    ok, out = run_validator("validate_skills.py", args.files_from)
    gates.append({"name": "Şema/Yapı Kapısı", "ok": ok, "detail": out.splitlines()[-3:] if out else []})

    # Gate 3: Kaynak defteri dogrulamasi (freshness/provenance)
    ok, out = run_validator("validate_sources.py", args.files_from)
    gates.append({"name": "Kaynak Doğrulama Kapısı (freshness)", "ok": ok, "detail": out.splitlines()[-3:] if out else []})

    # Gate 4: Guvenlik/injection taramasi
    ok, out = run_validator("lint_prompts.py", args.files_from)
    gates.append({"name": "Güvenlik/Halüsinasyon Kapısı", "ok": ok, "detail": out.splitlines()[-3:] if out else []})

    all_pass = all(g["ok"] for g in gates)
    any_structural_fail = any(not g["ok"] for g in gates[1:])  # sema/kaynak/guvenlik kritik

    if all_pass:
        verdict = "TRUSTED"
    elif any_structural_fail:
        verdict = "REJECTED"
    else:
        verdict = "NEEDS-REVIEW"

    result = {
        "verdict": verdict,
        "skill_files_checked": len(skill_files),
        "gates": gates,
    }

    if args.json:
        print(json.dumps(result, ensure_ascii=False, indent=2))
    else:
        print(f"Topluluk Skill Güven Kapısı — {len(skill_files)} SKILL.md dosyası tarandı.")
        for g in gates:
            print(f"  [{'OK' if g['ok'] else 'HATA'}] {g['name']}")
        print(f"\nSonuç: {verdict}")
        if verdict == "NEEDS-REVIEW":
            print("Not: Yapısal/güvenlik kapıları geçti ama içerik/üslup incelemesi (bakımcı onayı) gerekiyor.")
        elif verdict == "REJECTED":
            print("Not: En az bir yapısal/güvenlik kapısı başarısız oldu — merge edilemez.")

    return 0 if verdict != "REJECTED" else 1


if __name__ == "__main__":
    sys.exit(main())
