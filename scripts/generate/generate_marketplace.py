#!/usr/bin/env python3
"""Her plugin'in .claude-plugin/plugin.json dosyasindan kok dizindeki
.claude-plugin/marketplace.json dosyasini uretir.

--check modu (CI icin): mevcut marketplace.json'un, yeniden uretilseydi
ne olacagiyla AYNI oldugunu dogrular. Farkli ise CI basarisiz olur —
boylece bir gelistirici plugin.json'i guncelleyip marketplace.json'i
guncellemeyi unutamaz.

Kullanim:
    python scripts/generate/generate_marketplace.py          # dosyayi yazar
    python scripts/generate/generate_marketplace.py --check  # yalniz kontrol eder, CI icin
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE_PATH = REPO_ROOT / ".claude-plugin" / "marketplace.json"

# Excluded top-level dirs that are not plugins even though they may contain
# a .claude-plugin subfolder in the future.
NON_PLUGIN_DIRS = {".git", ".github", ".claude", ".devcontainer", "docs", "scripts", "sources", "evaluations"}


def find_plugins(repo_root: Path) -> list[dict]:
    plugins = []
    for plugin_json in sorted(repo_root.glob("*/.claude-plugin/plugin.json")):
        plugin_dir = plugin_json.parent.parent
        if plugin_dir.name in NON_PLUGIN_DIRS:
            continue
        try:
            data = json.loads(plugin_json.read_text(encoding="utf-8"))
        except json.JSONDecodeError as e:
            print(f"HATA: {plugin_json} parse edilemedi: {e}", file=sys.stderr)
            sys.exit(1)

        plugins.append({
            "name": data["name"],
            "displayName": data.get("displayName", data["name"]),
            "source": f"./{plugin_dir.name}",
            "description": data.get("description", ""),
            "author": data.get("author", {"name": "Mesut Can Demir"}),
        })
    return plugins


def build_marketplace(plugins: list[dict]) -> dict:
    return {
        "$schema": "https://anthropic.com/claude-code/marketplace.schema.json",
        "name": "turkiye-legal",
        "description": (
            "Türkiye hukukuna özgü, açık kaynak Legal AI plugin ekosistemi — "
            "KVKK, iş hukuku, sözleşmeler, icra-iflas, mevzuat takibi ve daha fazlası."
        ),
        "owner": {"name": "Mesut Can Demir"},
        "plugins": plugins,
    }


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    plugins = find_plugins(REPO_ROOT)
    generated = build_marketplace(plugins)
    generated_text = json.dumps(generated, ensure_ascii=False, indent=2) + "\n"

    if args.check:
        if not MARKETPLACE_PATH.exists():
            if not plugins:
                print("Henuz hicbir plugin.json yok; marketplace.json da yok. Tutarli. (Faz 4 oncesi beklenen durum.)")
                return 0
            print(f"HATA: {MARKETPLACE_PATH} bulunamadi ama {len(plugins)} plugin.json mevcut.")
            return 1
        current_text = MARKETPLACE_PATH.read_text(encoding="utf-8")
        if current_text != generated_text:
            print(f"HATA: {MARKETPLACE_PATH} guncel degil. `python scripts/generate/generate_marketplace.py` calistirip commit'leyin.")
            return 1
        print(f"{MARKETPLACE_PATH} guncel ({len(plugins)} plugin).")
        return 0

    MARKETPLACE_PATH.parent.mkdir(parents=True, exist_ok=True)
    MARKETPLACE_PATH.write_text(generated_text, encoding="utf-8")
    print(f"{MARKETPLACE_PATH} yazildi ({len(plugins)} plugin).")
    return 0


if __name__ == "__main__":
    sys.exit(main())
