#!/usr/bin/env python3
"""Tier 2 MCP'ler için skill generator (345-420 skill)."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# Tier 2 MCP tanımlamaları
MCPS = {
    "turkiye-legal-aihm-insan-haklari-mcp": {
        "categories": [
            ("aihm-kararları", 30),
            ("bireysel-başvuru", 20),
            ("türkiye-istatistikleri", 10),
        ],
        "risk": "medium",
        "sources": [
            {"tur": "mahkeme", "ad": "AİHM"},
            {"tur": "mahkeme", "ad": "Anayasa Mahkemesi"}
        ],
    },
    "turkiye-legal-danistay-gorisleri-mcp": {
        "categories": [
            ("idari-işlem-denetimi", 20),
            ("kamu-personeli", 15),
            ("vergi-hukuku", 10),
        ],
        "risk": "high",
        "sources": [{"tur": "mahkeme", "ad": "Danıştay"}],
    },
    "turkiye-legal-sgk-emeklilik-mcp": {
        "categories": [
            ("sigortalılık", 25),
            ("emeklilik-hakları", 30),
            ("hesaplamalar", 15),
        ],
        "risk": "high",
        "sources": [{"tur": "kamu", "ad": "Sosyal Güvenlik Kurumu"}],
    },
    "turkiye-legal-vergi-muhasebe-mcp": {
        "categories": [
            ("gelir-vergisi", 30),
            ("kurumlar-vergisi", 25),
            ("kdv", 15),
            ("muhasebe", 10),
        ],
        "risk": "high",
        "sources": [
            {"tur": "kamu", "ad": "Maliye Bakanlığı"},
            {"tur": "kamu", "ad": "TÜRMOB"}
        ],
    },
    "turkiye-legal-gumruk-mcp": {
        "categories": [
            ("tarife-tarifesi", 25),
            ("gümrük-vergileri", 20),
            ("dış-ticaret", 5),
        ],
        "risk": "medium",
        "sources": [{"tur": "kamu", "ad": "Gümrük ve Ticaret Bakanlığı"}],
    },
    "turkiye-legal-bilirkisi-arabulucu-mcp": {
        "categories": [
            ("bilirkişilik", 25),
            ("arabuluculuk", 20),
            ("uzlaştırma", 5),
        ],
        "risk": "medium",
        "sources": [{"tur": "kamu", "ad": "Adalet Bakanlığı"}],
    },
}

def build_skill_frontmatter(slug, description, category, mcp_name, risk, sources):
    """Skill frontmatter oluştur."""
    return f"""---
name: {slug}
description: "{description[:200]}"
argument-hint: ""
user-invocable: true
turkiye_legal:
  version: 0.7.0
  category: {category}
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope:
      - TR
  risk_level: {risk}
  requires_human_review: {str(risk == "high").lower()}
  inputs:
    - "[giriş tanımlanmadı]"
  outputs:
    - "[çıktı tanımlanmadı]"
  sources: {json.dumps(sources, ensure_ascii=False)}
  attribution:
    original_author: "Mesut Can Demir"
    original_repository: "https://github.com/mesutcandemir39/turkiye-legal"
    license: "Apache-2.0"
---

# {description.split('.')[0]}

## Görev
Skill tarafından sağlanan araç kullanarak {mcp_name}'den veri sorgula ve analiz et.

## Kaynak kuralı
- **MCP araçları varsa resmî metni onlardan çek.**
- **Her karar/norm doğrulanabilir künyeyle.**
- **Varsayımları açıkça işaretle.**
"""

def slugify(text):
    """Text'i kebab-case slug'a çevir."""
    return (
        text.lower()
        .replace("ş", "s")
        .replace("ç", "c")
        .replace("ğ", "g")
        .replace("ı", "i")
        .replace("ü", "u")
        .replace("ö", "o")
        .replace(" ", "-")
        .replace("/", "-")
        .replace(".", "-")
        .replace("'", "")
    )

def generate_skills_for_mcp(mcp_name, categories, risk_level, sources):
    """MCP için skilleri generate et."""
    mcp_path = REPO_ROOT / mcp_name
    skills_path = mcp_path / "skills"
    skills_path.mkdir(parents=True, exist_ok=True)

    total = 0
    for category_name, count in categories:
        for i in range(count):
            title = f"{category_name.replace('-', ' ').title()} {i+1}"
            description = f"{title} - {mcp_name}'den veri sorgula"

            slug = slugify(f"{category_name}-{i+1}")
            skill_dir = skills_path / slug
            skill_dir.mkdir(parents=True, exist_ok=True)

            skill_path = skill_dir / "SKILL.md"
            content = build_skill_frontmatter(
                slug, description, category_name, mcp_name, risk_level, sources
            )
            skill_path.write_text(content, encoding="utf-8")
            total += 1

    return total

def main():
    print(f"\n{'='*60}")
    print(f"Tier 2 MCP Skills Generator")
    print(f"{'='*60}\n")

    total_skills = 0
    for mcp_name, config in MCPS.items():
        count = generate_skills_for_mcp(
            mcp_name,
            config["categories"],
            config["risk"],
            config["sources"],
        )
        total_skills += count
        print(f"✓ {mcp_name}: {count} skills")

    print(f"\n{'='*60}")
    print(f"✓ Toplam: {total_skills} skill üretildi")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
