#!/usr/bin/env python3
"""Tier 1 MCP'ler için skill generator (380-420 skill)."""

import json
import os
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]

# MCP tanımlamaları
MCPS = {
    "turkiye-legal-resmigaze-mcp": {
        "categories": [
            ("gazete-arşivi-sorguları", 20),
            ("normlar-yürürlük", 25),
            ("kararname-atamalar", 20),
            ("tüzük-yönetmelikler", 15),
        ],
        "risk": "medium",
        "sources": [{"tur": "gazete", "ad": "Resmi Gazete"}],
    },
    "turkiye-legal-uyap-mcp": {
        "categories": [
            ("dava-sorgulaması", 35),
            ("karar-analizi", 30),
            ("dava-akışı", 25),
            ("icra-işlemleri", 20),
            ("emsal-istatistik", 15),
        ],
        "risk": "high",
        "sources": [{"tur": "mahkeme", "ad": "UYAP Sistemi"}],
    },
    "turkiye-legal-emsal-kararlar-mcp": {
        "categories": [
            ("yargıtay-emsal", 20),
            ("anayasa-landmark", 15),
            ("danıştay-içtihat", 10),
            ("karar-benzerlik", 5),
        ],
        "risk": "medium",
        "sources": [
            {"tur": "mahkeme", "ad": "Yargıtay"},
            {"tur": "mahkeme", "ad": "Anayasa Mahkemesi"},
            {"tur": "mahkeme", "ad": "Danıştay"},
        ],
    },
    "turkiye-legal-sicil-tescil-mcp": {
        "categories": [
            ("ticaret-sicili-sorgulaması", 20),
            ("kuruluş-sözleşmeleri", 10),
            ("gayrimenkul-tescili", 20),
            ("mülkiyet-tarihçesi", 10),
        ],
        "risk": "medium",
        "sources": [
            {"tur": "kamu", "ad": "Ticaret Sicili"},
            {"tur": "kamu", "ad": "Tapu Müdürlüğü"},
        ],
    },
    "turkiye-legal-mevzuat-degisiklikleri-mcp": {
        "categories": [
            ("yeni-yasalar", 10),
            ("iptal-değişiklikler", 10),
            ("geçiş-hükümleri", 8),
            ("yürürlük-takvimi", 2),
        ],
        "risk": "high",
        "sources": [{"tur": "gazete", "ad": "Resmi Gazete"}],
    },
}

def build_skill_frontmatter(
    slug, description, category, mcp_name, risk, sources
):
    """Skill frontmatter oluştur."""
    return f"""---
name: {slug}
description: "{description[:200]}"
argument-hint: ""
user-invocable: true
turkiye_legal:
  version: 0.6.0
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

SKILL_TEMPLATES = {
    "gazete-arşivi-sorguları": [
        ("Yıl Aralığında Gazete Taraması", "Verilen yıl aralığında Resmi Gazete sayılarını tara ve listele."),
        ("Konu Anahtarı Araması", "Konuya göre Resmi Gazete'deki gazete sayılarını bul."),
        ("Sayfa Numarası ile Norm Bulma", "Verilen gazete ve sayfa numarası ile norm'u getir."),
        ("Yayın Tarihi Sorgulaması", "Belirli tarihte çıkan gazete sayısını ara."),
        ("Hazine/Mali Müşevirlik Bulunması", "Hazinenin aldığı kararları Resmi Gazete'den tara."),
        ("Başbakanlık Kararnameleri", "Başbakanın kararnamelerini tarih aralığında bulma."),
        ("Dış Ticaret Resimleri", "Gümrük ve dış ticaret tabelalarını Gazete'de ara."),
        ("Memuriyete Atama Bulunması", "Merkezi memuriyete atama kararlarını Gazete'den filtrele."),
        ("Dönem Hukuku Değişikliği", "Yeni hükümet kurması sırasında yasama kararlarını tara."),
        ("Sihhi Tedbir Gazetesi", "Sihhi tedbirlerle ilgili yazılar Gazete'de bulma."),
        ("Mali Müşevirlik Kuralı Araması", "Mali müşevirlik esaslarını Gazete'de tara."),
        ("Büyükelçilik Belgesi Araması", "Dış temsilcilik belgelerini Gazete'de ara."),
        ("Köy Muhtarı Seçim Sonuçları", "Muhtarlık seçim sonuçlarını Gazete'de bul."),
        ("Dernek/Vakıf Kuruluşu", "Yeni dernek ve vakıf kurulma belgelerini ara."),
        ("Marka Tescil Resmigaze", "Tescil edilmiş markaları Gazete'de ara."),
        ("Patent Yayınları", "Patent tescilleri Gazete'de tara."),
        ("Oymayan Seçim Sonuçları", "Belediye seçim sonuçlarını yıla göre ara."),
        ("Mezuniyete Konu Gazete", "Rectorluk kararlarında mezuniyeti ara."),
        ("Yeni Kamu Kurumu Kuruluşu", "Yeni kamu kurum kuruluş kararlarını Gazete'de tara."),
        ("Teknoloji Şirketleri Listesi", "Teknoloji firmaları listesini Gazete'de ara."),
    ],
    "normlar-yürürlük": [
        ("Yürürlük Tarihi Tespiti", "Kanun'un tam yürürlük giriş tarihini tespit et."),
        ("Geçiş Hükümleri Analizi", "Eski kanundan yenisine geçiş kurallarını analiz et."),
        ("Yürürlükten Kaldırma Takibi", "İptal veya kaldırılan maddelerin takip kaydı."),
        ("Kısmi Yürürlülük", "Yasanın bazı maddeleri henüz yürürlükte değilse uyar."),
        ("Geri Yürürlülük Kontrolü", "Kanun'un geriye yürümesi var mı kontrol et."),
        ("Mühlet Dönemleri", "Norm'ların uygulamaya başlama süreleri."),
        ("İnsan Hakları Açısından Geçiş", "Yeni norm insani haklara uygun mu değerlendir."),
        ("Vergi Kanunları Yürürlük", "Vergi kanunlarında özel yürürlük kuralları."),
        ("Emeklilik Geçişi", "Eski-yeni emeklilik kanunları arasındaki geçiş."),
        ("Cezalandırılabilirlik Süreleri", "Ceza hukuku yürürlülüğü ilkeleri."),
        ("İş Hukuku Geçiş Hükümleri", "İş hukuku norm değişiklikleri geçişi."),
        ("Aile Hukuku Yürürlük", "Aile kanun değişikliklerinin geçiş şartları."),
        ("Gayrimenkul Kanunları Yürürlük", "Tapu ve gayrimenkul yasalarının geçişi."),
        ("Ticaret Kanunları Geçişi", "Ticaret hukuku norm değişliklerinin geçişi."),
        ("Kamulaştırma Kanunları", "Kamulaştırma yasa değişliklerinde geçiş."),
        ("Sosyal Sigorta Geçişi", "Sosyal sigorta kanunlarında yürürlük geçişi."),
        ("Koruma Amacı Yürürlülüğü", "Koruma amaçlı kanunların geriye yürürlülüğü."),
        ("Sıfır Numaralı Fasikül", "Yasanın özel sıfırıncı fasikülü yürürlügü."),
        ("Yönetmelik Yürürlüğü", "Ana kanun ile aynı zamanda yürürlüğe girer."),
        ("Cumhuriyet Bayramı Yürürlüğü", "Bayram günü yürürlüğe giren kanunlar."),
        ("Ara Tatil Yürürlüğü", "Tatil dönemleri yürürlüğe giren yasalar."),
        ("Resmi Gazete Yayın Sonrası", "Gazete'de yayınlandıktan 3 gün sonra yürürlük."),
        ("Taraflı Yürürlük", "Tarafça kabulünün yürürlüğü."),
        ("Onayla Yürürlük", "Senatoda onaylandıktan sonra yürürlüğü."),
    ],
    "kararname-atamalar": [
        ("Bakanların Atanması", "Yeni atanan bakanları Gazete'de bul."),
        ("Vali Atama Kararı", "Vali atamalarını tarih aralığında ara."),
        ("Rektör Seçimi ve Atanması", "Üniversite rektörlerini Gazete'de filtrele."),
        ("Yönetici Atama Kararı", "Kurumsal atama kararnamelerini ara."),
        ("Emeklilik Kararları", "Emeklilik ve görevden alma kararlarını bul."),
        ("Dönem Atama Kararı", "Belirli bir dönemi kapsayan atama kararları."),
        ("Tercih ve Dönüşüm", "Memur tercih ve dönüşüm kararlarını ara."),
        ("Görev Süresi Uzatma", "Görev süresi uzatılmış yöneticileri bul."),
        ("Ön Lisans Kararı", "Ön lisans atama kararlarını Gazete'de ara."),
        ("Kurumlar Arası Denizlik", "Kurum ve kuruluşlar arası yönetici dengesi."),
        ("İtfaiyeci Tayin Kararı", "İtfaiye teşkilatında görev tayinleri."),
        ("Emniyet Atama Kararı", "Polis ve emniyet müfettişi atamalarını ara."),
        ("Asker Atama Kararı", "Asker ve polis rütbe atamalarını filtrele."),
        ("Kaymakam Atama Kararı", "Kaymakam görevlerine yapılan atamalar."),
        ("İmam Atama Kararı", "Din görevlileri atamalarını ara."),
        ("Protokol Sırasına Etki", "Atama kararlarında protokol değişiklikleri."),
        ("Görevden Alma Kararı", "Görevden alınanların listesini bul."),
        ("Ücret Artışı Muhasebesi", "Atamaya bağlı ücret artış kararları."),
        ("Yaş Sınırına Çıkan Emeklilik", "Yaş sınırına ulaşan memur emekliliği."),
        ("Mahalli İdare Atama", "Belediye ve muhtar atamalarını ara."),
    ],
    "tüzük-yönetmelikler": [
        ("Bakanlık Yönetmeliği", "Bakanlık kurumsal yönetmeliklerini bul."),
        ("Üniversite Statüsü", "Üniversite yönetimsel statülerini ara."),
        ("Kuruluş Yönetmeliği", "Kurum kuruluş yönetmeliklerini filtrele."),
        ("İç Yönetmelik", "Kurumsal iç işleyiş yönetmeliklerini ara."),
        ("İnsan Kaynakları Yönetmeliği", "Personel yönetimi yönetmeliklerini bul."),
        ("Hazine Bütçe Yönetmeliği", "Bütçe ve muhasebe yönetmeliklerini ara."),
        ("Bilir Kişi Yönetmeliği", "Bilir kişi görevlendirme yönetmeliklerini tara."),
    ],
}

def generate_skills_for_mcp(mcp_name, categories, risk_level, sources):
    """MCP için skilleri generate et."""
    mcp_path = REPO_ROOT / mcp_name
    skills_path = mcp_path / "skills"
    skills_path.mkdir(parents=True, exist_ok=True)

    total = 0
    for category_name, count in categories:
        # Template'den veya default'tan skill oluştur
        templates = SKILL_TEMPLATES.get(category_name, [])

        for i in range(count):
            if i < len(templates):
                title, description = templates[i]
            else:
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
    print(f"Tier 1 MCP Skills Generator")
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
