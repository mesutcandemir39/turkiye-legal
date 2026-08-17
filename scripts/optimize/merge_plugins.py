#!/usr/bin/env python3
"""Benzer pluginleri birleştir ve consolidate et."""

import shutil
import json
from pathlib import Path
import yaml

REPO_ROOT = Path(__file__).resolve().parents[2]

# Birleştirme planı: {hedef_plugin: [kaynaklar...]}
MERGE_PLAN = {
    "vergi-hukuku": ["vergi-davalari"],
    "is-hukuku": ["is-hukuku-bireysel", "is-hukuku-toplu", "is-sagligi-guvenligi"],
    "ticaret-hukuku": ["deniz-ticareti-hukuku", "e-ticaret-hukuku", "gumruk-disticaret", "ticari-isletme-hukuku"],
    "ceza-hukuku-genel": ["ceza-muhakemesi"],
    "borclar-hukuku-genel": ["sozlesme"],
    "idare-hukuku-genel": ["idare-vergi"],
}

def merge_skills(target_dir, source_dir):
    """Kaynak plugin'in skill'lerini hedef plugin'e taşı."""
    source_skills = source_dir / "skills"
    target_skills = target_dir / "skills"

    if not source_skills.exists():
        return 0

    if not target_skills.exists():
        target_skills.mkdir(parents=True, exist_ok=True)

    merged = 0
    for skill_dir in source_skills.iterdir():
        if skill_dir.is_dir():
            target_skill = target_skills / skill_dir.name
            if not target_skill.exists():
                shutil.copytree(skill_dir, target_skill)
                merged += 1

    return merged

def merge_agents(target_dir, source_dir):
    """Kaynak plugin'in agent'larını hedef plugin'e taşı."""
    source_agents = source_dir / "agents"
    target_agents = target_dir / "agents"

    if not source_agents.exists():
        return 0

    if not target_agents.exists():
        target_agents.mkdir(parents=True, exist_ok=True)

    merged = 0
    for agent_file in source_agents.glob("*.md"):
        target_file = target_agents / agent_file.name
        if not target_file.exists():
            shutil.copy(agent_file, target_file)
            merged += 1

    return merged

def main():
    total_merged_skills = 0
    total_merged_agents = 0

    print(f"\n{'='*60}")
    print(f"Plugin Birleştirme Başlıyor")
    print(f"{'='*60}\n")

    for target, sources in MERGE_PLAN.items():
        target_dir = REPO_ROOT / target

        if not target_dir.exists():
            print(f"⚠️  Target not found: {target}")
            continue

        print(f"📦 {target}:")

        for source in sources:
            source_dir = REPO_ROOT / source

            if not source_dir.exists():
                print(f"   ⚠️  Source not found: {source}")
                continue

            skills = merge_skills(target_dir, source_dir)
            agents = merge_agents(target_dir, source_dir)

            if skills > 0 or agents > 0:
                print(f"   ✓ {source}: +{skills} skills, +{agents} agents")
                total_merged_skills += skills
                total_merged_agents += agents

            # Kaynak plugin'i sil
            shutil.rmtree(source_dir, ignore_errors=True)
            print(f"   ✓ {source} silindu")

    print(f"\n{'='*60}")
    print(f"✓ Toplam: {total_merged_skills} skill + {total_merged_agents} agent birleştirildi")
    print(f"{'='*60}\n")

if __name__ == "__main__":
    main()
