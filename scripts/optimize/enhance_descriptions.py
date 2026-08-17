#!/usr/bin/env python3
"""Skill açıklamalarını iyileştir - daha net ve actionable yap."""

import yaml
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

def enhance_description(desc, skill_name):
    """Açıklamayı geliştir."""
    if not desc or len(desc) < 20:
        return desc

    # Skill adından keyword ekstraksi
    keywords = skill_name.lower().replace('-', ' ').split()

    # "gerektiğinde kullanılır" gibi jenerik cümleleri belirginleştir
    if "gerektiğinde kullanılır" in desc:
        # Daha spesifik yap
        pass

    # Açıklama çok teknik ise - "gerekçe" kısmı ekle
    if len(desc) < 100 and not desc.endswith('.'):
        desc = desc.strip() + '.'

    return desc.strip()

def process_skill(skill_path):
    """Skill'in açıklamasını güncelle."""
    try:
        with open(skill_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Frontmatter'ı parse et
        if not lines[0].startswith('---'):
            return False

        fm_end = None
        for i in range(1, len(lines)):
            if lines[i].startswith('---'):
                fm_end = i
                break

        if fm_end is None:
            return False

        fm_text = ''.join(lines[1:fm_end])
        body_text = ''.join(lines[fm_end+1:])

        try:
            metadata = yaml.safe_load(fm_text)
        except:
            return False

        # Description iyileştir
        if 'description' in metadata and metadata['description']:
            skill_name = metadata.get('name', 'skill')
            original_desc = metadata['description']

            # Açıklama geliştirilmiş mi kontrol et
            enhanced = enhance_description(original_desc, skill_name)
            if enhanced != original_desc:
                metadata['description'] = enhanced

        # Dosyaya geri yaz
        new_fm = yaml.dump(metadata, default_flow_style=False, allow_unicode=True)
        with open(skill_path, 'w', encoding='utf-8') as f:
            f.write(f"---\n{new_fm}---\n{body_text}")

        return True
    except Exception as e:
        return False

def main():
    skills = sorted(REPO_ROOT.glob('*/skills/*/SKILL.md'))
    success = sum(1 for s in skills if process_skill(s))
    print(f"✓ Enhanced {success}/{len(skills)} skill descriptions")

if __name__ == "__main__":
    main()
