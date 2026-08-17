#!/usr/bin/env python3
"""Tier 3 MCP'ler için skill generator (600+ skill)."""

import json
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
DATA_PATH = REPO_ROOT / "scripts" / "generate" / "tier3_mcps_data.json"

def build_skill_frontmatter(slug, description, category, mcp_name, risk, sources):
    """Skill frontmatter oluştur."""
    sources_json = json.dumps([
        {"tur": s["type"], "ad": s["name"]} for s in sources
    ], ensure_ascii=False)

    return f"""---
name: {slug}
description: "{description[:200]}"
argument-hint: ""
user-invocable: true
turkiye_legal:
  version: 0.8.0
  category: {category}
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope:
      - TR
  risk_level: {risk}
  requires_human_review: {str(risk in ("high", "critical")).lower()}
  inputs:
    - "[giriş tanımlanmadı]"
  outputs:
    - "[çıktı tanımlanmadı]"
  sources: {sources_json}
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

def main():
    # Load data
    with open(DATA_PATH) as f:
        data = json.load(f)

    print(f"\n{'='*60}")
    print(f"Tier 3 MCP Skills Generator")
    print(f"{'='*60}\n")

    total_skills = 0

    for mcp_config in data["mcps"]:
        mcp_name = mcp_config["name"]
        risk = mcp_config["risk"]
        sources = mcp_config["sources"]
        categories = mcp_config["categories"]

        mcp_path = REPO_ROOT / mcp_name
        skills_path = mcp_path / "skills"
        skills_path.mkdir(parents=True, exist_ok=True)

        # Create README
        readme_path = mcp_path / "README.md"
        if not readme_path.exists():
            readme_path.write_text(
                f"# {mcp_name}\n\n{mcp_config['description']}\n\n"
                f"## Skill Kategorileri\n\n"
                + "\n".join([
                    f"- {cat['name'].replace('-', ' ').title()}: {cat['count']} skill"
                    for cat in categories
                ])
                + "\n\n## License\n\nApache-2.0\n"
            )

        # Generate skills
        count = 0
        for category_config in categories:
            category_name = category_config["name"]
            category_count = category_config["count"]

            for i in range(category_count):
                title = f"{category_name.replace('-', ' ').title()} {i+1}"
                description = f"{title} - {mcp_name}'den veri sorgula"

                slug = slugify(f"{category_name}-{i+1}")
                skill_dir = skills_path / slug
                skill_dir.mkdir(parents=True, exist_ok=True)

                skill_path = skill_dir / "SKILL.md"
                content = build_skill_frontmatter(
                    slug, description, category_name, mcp_name, risk, sources
                )
                skill_path.write_text(content, encoding="utf-8")
                count += 1

        total_skills += count
        print(f"✓ {mcp_name}: {count} skills")

    print(f"\n{'='*60}")
    print(f"✓ Toplam: {total_skills} skill üretildi")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
