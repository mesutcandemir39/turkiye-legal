#!/usr/bin/env python3
"""MCP'lerin yalnızca resmî kaynaklardan veri alıp almadığını doğrula."""

import json
import re
from pathlib import Path
from collections import defaultdict

REPO_ROOT = Path(__file__).resolve().parents[2]

# Resmî kaynak tanımları
OFFICIAL_SOURCES = {
    # Kanunlar
    "TCK": ["Türk Ceza Kanunu", "5237"],
    "TMK": ["Türk Medeni Kanunu", "4721"],
    "CMK": ["Ceza Muhakemesi Kanunu", "5271"],
    "HMK": ["Hukuk Muhakemesi Kanunu", "1086"],
    "İK": ["İş Kanunu", "4857"],
    "TBK": ["Türk Borçlar Kanunu", "6102"],
    "GK": ["Gümrük Kanunu", "4458"],
    "KVK": ["Kurumlar Vergisi Kanunu", "5520"],
    "GVK": ["Gelir Vergisi Kanunu", "193"],
    "KDV": ["Katma Değer Vergisi Kanunu", "3065"],
    "İİK": ["İcra ve İflas Kanunu", "2004"],
    "TTK": ["Ticaret Kanunu", "6102"],
    "SGK": ["Sosyal Sigorta Kanunu", "5510"],
    "Anayasa": ["T.C. Anayasası", "1982"],

    # Mahkemeler
    "Yargıtay": ["Yargıtay Kararları", "yargitay.gov.tr"],
    "Anayasa Mahkemesi": ["Anayasa Mahkemesi", "anayasa.gov.tr"],
    "Danıştay": ["Danıştay Kararları", "danistay.gov.tr"],
    "AİHM": ["Avrupa İnsan Hakları Mahkemesi", "echr.coe.int"],
    "İş Mahkemeleri": ["İş Mahkemesi Kararları"],

    # Bakanlıklar
    "Adalet Bakanlığı": ["adalet.gov.tr", "uyap.adalet.gov.tr"],
    "Maliye Bakanlığı": ["gib.gov.tr"],
    "Gümrük Bakanlığı": ["gumruk.gov.tr"],
    "Çalışma Bakanlığı": ["çalişma.gov.tr"],
    "Sosyal Güvenlik Kurumu": ["sgk.gov.tr"],
    "Ticaret Bakanlığı": ["ticaret.gov.tr"],
    "Çevre Bakanlığı": ["çevre.gov.tr"],

    # Kamu Kurumları
    "Resmi Gazete": ["resmigazete.gov.tr"],
    "Ticaret Sicili": ["ticaret-sicili.gov.tr"],
    "Tapu Müdürlüğü": ["tapu.gov.tr"],
    "Türkiye Barolar Birliği": ["tbb.org.tr"],
    "TÜRMOB": ["turmob.org.tr"],
}

# Uyarıcı kelimeler - bu kullanıldığında insan gözü gerekir
WARNING_PATTERNS = [
    r"\basla[rm]ı taşanızın",  # kişisel tahmin
    r"\bbelki\b",  # belirsizlik
    r"\bihtimal ki\b",  # tahmin
    r"\bsanırım\b",  # zan
    r"\bursa|bulunur mu",  # sorgulamalı
    r"\buydurma\b",  # fabrication flag
    r"\btahmin\b",  # speculation
]

def is_official_source(text):
    """Metinde resmî kaynak referansı var mı kontrol et."""
    for source_aliases in OFFICIAL_SOURCES.values():
        for alias in source_aliases:
            if alias.lower() in text.lower():
                return True
    return False

def has_warning_pattern(text):
    """Metinde uyarıcı kelime var mı kontrol et."""
    for pattern in WARNING_PATTERNS:
        if re.search(pattern, text, re.IGNORECASE):
            return True
    return False

def check_skill_file(skill_path):
    """Tek skill dosyasını kontrol et."""
    try:
        content = skill_path.read_text(encoding="utf-8")

        # Frontmatter'dan sources çıkar
        fm_match = re.search(r"---\n(.*?)\n---", content, re.DOTALL)
        if not fm_match:
            return None

        fm_text = fm_match.group(1)

        # YAML'dan sources field'ını çıkar
        sources_match = re.search(r"sources:\s*(\[.*?\]|\n.*?(?=\n  [a-z]))", fm_text, re.DOTALL)
        if not sources_match:
            return {"status": "NO_SOURCES", "file": str(skill_path.relative_to(REPO_ROOT))}

        # İçeriği kontrol et
        body = content.split("---")[-1]

        # Resmî kaynak referansı var mı?
        has_official = is_official_source(body)

        # Uyarıcı kalıp var mı?
        has_warning = has_warning_pattern(body)

        if not has_official and not has_warning:
            return {
                "status": "MISSING_OFFICIAL_SOURCE",
                "file": str(skill_path.relative_to(REPO_ROOT)),
                "description": skill_path.parent.parent.name
            }

        if has_warning:
            return {
                "status": "WARNING_PATTERN",
                "file": str(skill_path.relative_to(REPO_ROOT)),
                "note": "Metinde tahmin/belirsizlik kalıpları - insan gözü kontrol gerekli"
            }

        return {"status": "OK"}

    except Exception as e:
        return {"status": "ERROR", "file": str(skill_path), "error": str(e)}

def main():
    print(f"\n{'='*70}")
    print(f"SISTEM DOĞRULAMA: MCP'ler Yalnızca Resmî Kaynaklardan Veri Alıyor mu?")
    print(f"{'='*70}\n")

    # Tüm SKILL.md dosyalarını bul
    skill_files = list(REPO_ROOT.glob("turkiye-legal-*/skills/*/SKILL.md"))

    results = defaultdict(list)
    total = len(skill_files)

    for skill_file in skill_files:
        result = check_skill_file(skill_file)
        if result:
            results[result["status"]].append(result)

    # Sonuçları raporla
    print(f"✓ Kontrol edilen skill: {total}\n")

    ok_count = len(results["OK"])
    warning_count = len(results["WARNING_PATTERN"])
    error_count = len(results["MISSING_OFFICIAL_SOURCE"])
    no_sources = len(results["NO_SOURCES"])

    print(f"✅ Doğru (resmî kaynak): {ok_count}/{total}")
    print(f"⚠️  Uyarı (tahmin/belirsizlik): {warning_count}/{total}")
    print(f"❌ Sorun (kaynak yok): {error_count}/{total}")
    print(f"❓ Kayıt yok: {no_sources}/{total}")

    if warning_count > 0:
        print(f"\n⚠️  UYARI SAHİBİ SKİLL'LER (İnsan Gözü Gerekli):")
        for item in results["WARNING_PATTERN"][:5]:
            print(f"  - {item.get('file', 'unknown')}")
        if len(results["WARNING_PATTERN"]) > 5:
            print(f"  ... ve {len(results['WARNING_PATTERN']) - 5} daha")

    if error_count > 0:
        print(f"\n❌ SORUN SAHİBİ SKİLL'LER:")
        for item in results["MISSING_OFFICIAL_SOURCE"][:5]:
            print(f"  - {item.get('file', 'unknown')}")
        if len(results["MISSING_OFFICIAL_SOURCE"]) > 5:
            print(f"  ... ve {len(results['MISSING_OFFICIAL_SOURCE']) - 5} daha")

    print(f"\n{'='*70}")

    # Özet güvenlik skoru
    total_valid = ok_count + warning_count
    accuracy = (total_valid / total * 100) if total > 0 else 0

    print(f"📊 DOĞRULUK SKORU: {accuracy:.1f}%")
    print(f"{'='*70}\n")

    return 0 if error_count == 0 else 1

if __name__ == "__main__":
    exit(main())
