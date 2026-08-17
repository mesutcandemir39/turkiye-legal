#!/usr/bin/env python3
"""81 plugin / 1002 skill'i sources/import/'dan üret."""

import json
import os
import shutil
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
CATALOG_PATH = REPO_ROOT / "sources" / "import" / "catalog.json"
CONTENT_PATH = REPO_ROOT / "sources" / "import" / "content.json"
KANUNLAR_PATH = REPO_ROOT / "sources" / "mevzuat" / "kanunlar.yaml"

# Load law registry for name lookups
def load_kanun_names():
    """Kanun numarası -> ad mapping'ini yükle."""
    import yaml
    try:
        with open(KANUNLAR_PATH) as f:
            data = yaml.safe_load(f)
            return {k["numara"]: k["ad"] for k in data.get("kanunlar", [])}
    except:
        return {}

def kaynak_footer(slug):
    return f"""

## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**
"""

def sanitize_slug(slug_candidate):
    """Slug'ın kebab-case ve a-z ile başlamasını sağla."""
    import re
    # Eğer sayı ile başlıyorsa 'hukum-' prefix'i ekle
    if slug_candidate and slug_candidate[0].isdigit():
        slug_candidate = "hukum-" + slug_candidate
    return slug_candidate

def build_skill(plugin, beceri, kanun_names=None):
    """Tek skill'i SKILL.md formatında oluştur."""
    if kanun_names is None:
        kanun_names = {}

    slug = plugin["slug"]
    b_slug = beceri.get("slug", beceri.get("ad", "").replace(" ", "-").lower())
    b_slug = sanitize_slug(b_slug)
    aciklama = beceri.get("aciklama", "")

    # Description'ı optimize et (max 200 char, temiz)
    if len(aciklama) > 200:
        aciklama = aciklama[:197].rsplit(' ', 1)[0]
        if not aciklama.endswith(('.', '?', '!')):
            aciklama += '.'

    govde = (beceri.get("govde_md") or "").strip()

    risk = "medium"  # varsayılan; tipine göre artırılabilir
    if "dilekçe" in b_slug or "hesap" in b_slug or "triyaj" in b_slug:
        risk = "high"
    if "genel-bakis" in b_slug:
        risk = "medium"

    requires_review = risk in ("high", "critical")

    # Sources: kanunlar listesini normalize et
    sources = []
    for kanun_token in kanunlar_list:
        # "6698", "4857 İş K." → numara çıkar
        import re
        m = re.search(r'\d+', kanun_token)
        if m:
            num = m.group()
            # Look up full name from registry, or use upstream name
            ad = kanun_names.get(num, kanun_token)
            sources.append({
                "tur": "kanun",
                "numara": num,
                "ad": ad
            })

    frontmatter = f"""---
name: {b_slug}
description: "{aciklama[:200]}"
argument-hint: ""
user-invocable: true
turkiye_legal:
  version: 0.5.0
  category: litigation
  jurisdiction: {{ country: TR, legal_system: civil_law, scope: [TR] }}
  risk_level: {risk}
  requires_human_review: {str(requires_review).lower()}
  inputs: ["[giriş tanımlanmadı — beceri gövdesinden çıkarılacak]"]
  outputs: ["[çıktı tanımlanmadı — beceri gövdesinden çıkarılacak]"]
  sources: {json.dumps(sources, ensure_ascii=False)}
  attribution:
    original_author: "Mesut Can Demir"
    original_repository: "https://github.com/mesutcandemir39/turkiye-legal"
    license: "Apache-2.0"
---

{govde or "# " + aciklama}

{kaynak_footer(slug)}
"""
    return frontmatter

def main():
    import sys
    full_mode = "--full" in sys.argv

    cat = json.load(open(CATALOG_PATH))
    content = json.load(open(CONTENT_PATH))
    kanun_names = load_kanun_names()

    # Her eklenti için skill dizini yaz
    plugins_to_process = cat['eklentiler'] if full_mode else cat['eklentiler'][:3]
    skills_to_process_per_plugin = None if full_mode else 2

    total_skills = 0
    for e in plugins_to_process:
        slug = e['slug']
        base = REPO_ROOT / slug
        os.makedirs(base / "skills" / "genel-bakis", exist_ok=True)

        c = content.get(slug, {})
        beceriler = c.get("beceriler", [])

        skills_for_this_plugin = beceriler if full_mode else beceriler[:skills_to_process_per_plugin]

        for b in skills_for_this_plugin:
            b_slug = b.get("slug", b.get("ad", "").replace(" ", "-").lower())
            skill_path = base / "skills" / b_slug / "SKILL.md"
            skill_path.parent.mkdir(parents=True, exist_ok=True)
            skill_path.write_text(build_skill(e, b, kanun_names), encoding="utf-8")
            total_skills += 1

    if full_mode:
        print(f"✓ Tam üretim: {len(plugins_to_process)} plugin × ortalama {total_skills // len(plugins_to_process)} beceri = {total_skills} SKILL.md dosyası yazıldı")
    else:
        print(f"✓ Test edildi: ilk {len(plugins_to_process)} plugin × {skills_to_process_per_plugin} beceri = {total_skills} SKILL.md dosyası yazıldı")

if __name__ == "__main__":
    main()
