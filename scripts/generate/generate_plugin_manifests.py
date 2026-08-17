#!/usr/bin/env python3
"""Her pratik alani dizinini kurulabilir bir Claude Code eklentisine cevirir.

Sorun: `<alan>/skills/<ad>/SKILL.md` yapisindaki beceriler bir eklenti
manifest'ine bagli olmadigi icin `claude plugin install` ile kurulamiyordu.

Bu script her alan dizinine `.claude-plugin/plugin.json` ve (yoksa) bir
`README.md` uretir, ardindan hepsini kok `.claude-plugin/marketplace.json`
dosyasina kaydeder. Idempotenttir: elle duzenlenmis mevcut manifest'lerin
`displayName`, `description` ve `keywords` alanlari korunur.

Kullanim:
    python scripts/generate/generate_plugin_manifests.py [--dry-run]
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
MARKETPLACE = REPO_ROOT / ".claude-plugin" / "marketplace.json"
SURUM = "0.5.0"
YAZAR = {"name": "Mesut Can Demir"}
LISANS = "Apache-2.0"

# Dizin adi -> insan tarafindan okunabilir baslik.
# Listede olmayan dizinler icin ad otomatik olarak baslik hale getirilir.
BASLIKLAR: dict[str, str] = {
    "aile-hukuku": "Aile Hukuku",
    "anayasa-hukuku": "Anayasa Hukuku",
    "anayasa-mahkemesi-bireysel-basvuru": "AYM Bireysel Başvuru",
    "anonim-sirket-genel-kurul": "Anonim Şirket Genel Kurul",
    "atif-turk-hukuku": "Atıf ve Kaynak Hijyeni",
    "avukatlik-meslek-kurallari": "Avukatlık Meslek Kuralları",
    "bankacilik-hukuku": "Bankacılık Hukuku",
    "basin-medya-hukuku": "Basın ve Medya Hukuku",
    "bilirkisi-rapor-inceleme": "Bilirkişi Raporu İncelemesi",
    "bilisim-hukuku-siber": "Bilişim ve Siber Hukuk",
    "birlesme-devralma-ma": "Birleşme ve Devralma",
    "borclar-hukuku-genel": "Borçlar Hukuku — Genel",
    "borclar-hukuku-ozel": "Borçlar Hukuku — Özel",
    "cevre-hukuku": "Çevre Hukuku",
    "ceza-hukuku-genel": "Ceza Hukuku — Genel",
    "ceza-hukuku-ozel": "Ceza Hukuku — Özel",
    "ceza-muhakemesi": "Ceza Muhakemesi",
    "dava-dilekce-atolyesi": "Dava Dilekçe Atölyesi",
    "dava-dosya-takip": "Dava Dosyası Takibi",
    "deniz-ticareti-hukuku": "Deniz Ticareti Hukuku",
    "e-ticaret-hukuku": "E-Ticaret Hukuku",
    "eczacilik-ilac": "Eczacılık ve İlaç Hukuku",
    "ekonomik-ceza": "Ekonomik Ceza Hukuku",
    "enerji-hukuku": "Enerji Hukuku",
    "esya-hukuku": "Eşya Hukuku",
    "fikri-mulkiyet-dava": "Fikri Mülkiyet Davaları",
    "gayrimenkul-hukuku": "Gayrimenkul Hukuku",
    "girisim-startup-hukuku": "Girişim ve Startup Hukuku",
    "goc-yabancilar-hukuku": "Göç ve Yabancılar Hukuku",
    "gumruk-disticaret": "Gümrük ve Dış Ticaret",
    "haksiz-fiil-tazminat": "Haksız Fiil ve Tazminat",
    "hukuk-burosu-yonetimi": "Hukuk Bürosu Yönetimi",
    "hukuk-felsefesi-genel-teori": "Hukuk Felsefesi ve Genel Teori",
    "hukuk-metodolojisi": "Hukuk Metodolojisi",
    "hukuk-muhakemesi": "Hukuk Muhakemesi",
    "hukuki-mutalaa": "Hukuki Mütalaa",
    "icra-iflas-hukuku": "İcra ve İflas Hukuku",
    "idare-hukuku-genel": "İdare Hukuku — Genel",
    "idari-yargilama": "İdari Yargılama",
    "ik-insan-kaynaklari": "İnsan Kaynakları",
    "imar-hukuku": "İmar Hukuku",
    "infaz-hukuku": "İnfaz Hukuku",
    "is-hukuku-bireysel": "İş Hukuku — Bireysel",
    "is-hukuku-toplu": "İş Hukuku — Toplu",
    "is-sagligi-guvenligi": "İş Sağlığı ve Güvenliği",
    "kabahatler-hukuku": "Kabahatler Hukuku",
    "kamu-ihale-hukuku": "Kamu İhale Hukuku",
    "kat-mulkiyeti": "Kat Mülkiyeti",
    "kendini-temsil-asliye": "Kendini Temsil (Asliye)",
    "kira-hukuku": "Kira Hukuku",
    "kisiler-hukuku": "Kişiler Hukuku",
    "kiymetli-evrak": "Kıymetli Evrak",
    "konkordato-yeniden-yapilandirma": "Konkordato ve Yeniden Yapılandırma",
    "kvkk-uyum-checker": "KVKK Uyum Denetleyici",
    "kvkk-veri-koruma": "KVKK ve Veri Koruma",
    "marka-hukuku": "Marka Hukuku",
    "medeni-hukuk-baslangic": "Medeni Hukuk — Başlangıç Hükümleri",
    "miras-hukuku": "Miras Hukuku",
    "patent-faydali-model": "Patent ve Faydalı Model",
    "rekabet-hukuku": "Rekabet Hukuku",
    "roma-hukuku": "Roma Hukuku",
    "sade-hukuk-dili": "Sade Hukuk Dili",
    "saglik-hukuku": "Sağlık Hukuku",
    "sebepsiz-zenginlesme": "Sebepsiz Zenginleşme",
    "sermaye-piyasasi-hukuku": "Sermaye Piyasası Hukuku",
    "sigorta-hukuku": "Sigorta Hukuku",
    "sirketler-hukuku": "Şirketler Hukuku",
    "sosyal-guvenlik": "Sosyal Güvenlik",
    "sozlesme-inceleme-redline": "Sözleşme İnceleme ve Redline",
    "spor-hukuku": "Spor Hukuku",
    "tahkim-arabuluculuk": "Tahkim ve Arabuluculuk",
    "tapu-kadastro": "Tapu ve Kadastro",
    "tasarim-hukuku": "Tasarım Hukuku",
    "tasima-hukuku": "Taşıma Hukuku",
    "telekomunikasyon-bilisim": "Telekomünikasyon ve Bilişim",
    "telif-haklari": "Telif Hakları",
    "ticari-isletme-hukuku": "Ticari İşletme Hukuku",
    "tuketici-hukuku": "Tüketici Hukuku",
    "vergi-davalari": "Vergi Davaları",
    "vergi-hukuku": "Vergi Hukuku",
    "yapay-zeka-hukuku": "Yapay Zekâ Hukuku",
}


def baslik(dizin: str) -> str:
    if dizin in BASLIKLAR:
        return BASLIKLAR[dizin]
    return " ".join(p.capitalize() for p in dizin.split("-"))


def skill_adlari(alan: Path) -> list[str]:
    if not (alan / "skills").is_dir():
        return []
    return sorted(p.parent.name for p in (alan / "skills").glob("*/SKILL.md"))


def kanun_numaralari(alan: Path) -> list[str]:
    """Alandaki becerilerin atif yaptigi kanun numaralarini toplar."""
    bulunan: set[str] = set()
    if not (alan / "skills").is_dir():
        return []
    for skill in (alan / "skills").glob("*/SKILL.md"):
        try:
            metin = skill.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        for eslesme in re.finditer(r"numara:\s*['\"]?(\d{3,5})['\"]?", metin):
            bulunan.add(eslesme.group(1))
    return sorted(bulunan)[:4]


def aciklama_uret(alan: Path, ad: str) -> str:
    adlar = skill_adlari(alan)
    if not adlar:
        return f"{baslik(ad)} — turkiye-legal ortak altyapı bileşeni (hooks, script ve referanslar)."
    kanunlar = kanun_numaralari(alan)
    ornekler = ", ".join(a.replace("-", " ") for a in adlar[:3])
    metin = f"{baslik(ad)} alanında {len(adlar)} beceri: {ornekler}"
    if len(adlar) > 3:
        metin += f" ve {len(adlar) - 3} tane daha"
    if kanunlar:
        metin += f". İlgili mevzuat: {', '.join(kanunlar)} sayılı kanunlar"
    return metin + "."


def anahtar_kelimeler(ad: str, alan: Path) -> list[str]:
    kelimeler = [p for p in ad.split("-") if len(p) > 2][:4]
    return kelimeler + kanun_numaralari(alan)[:2]


def readme_uret(ad: str, alan: Path, aciklama: str) -> str:
    adlar = skill_adlari(alan)
    satirlar = [
        f"# {baslik(ad)}",
        "",
        aciklama,
        "",
        "## Kurulum",
        "",
        "```bash",
        "claude plugin marketplace add https://github.com/mesutcandemir39/turkiye-legal",
        f"claude plugin install {ad}@turkiye-legal",
        "```",
        "",
        f"## Beceriler ({len(adlar)})",
        "",
    ]
    for a in adlar:
        satirlar.append(f"- `/{ad}:{a}`")
    satirlar += [
        "",
        "## Sorumluluk reddi",
        "",
        "Bu eklenti bir yardımcı araçtır, avukat değildir. Her çıktıyı birincil",
        "kaynaktan doğrulayın; nihai kararı yetkin bir hukukçu vermelidir.",
        "Ayrıntı için deponun kök [`README.md`](../README.md) dosyasına bakınız.",
        "",
    ]
    return "\n".join(satirlar)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--dry-run", action="store_true", help="Yalniz raporla, yazma")
    args = ap.parse_args()

    # Iki kaynak birlestirilir:
    #  1) Beceri iceren dizinler (skills/*/SKILL.md)
    #  2) Zaten bir manifest'i olan dizinler - beceri sunmasalar da hooks/
    #     scripts/references sagladiklari icin gecerli eklentidirler (or. cekirdek)
    beceri_dizinleri = {
        p.parent for p in REPO_ROOT.glob("*/skills") if p.is_dir() and any(p.glob("*/SKILL.md"))
    }
    manifestli = {
        p.parent.parent for p in REPO_ROOT.glob("*/.claude-plugin/plugin.json")
    }
    alanlar = sorted(beceri_dizinleri | manifestli, key=lambda p: p.name)

    market = json.loads(MARKETPLACE.read_text(encoding="utf-8"))
    mevcut = {p["name"]: p for p in market.get("plugins", [])}

    yeni_manifest = 0
    yeni_readme = 0
    kayitlar: list[dict] = []

    for alan in alanlar:
        ad = alan.name
        manifest_yolu = alan / ".claude-plugin" / "plugin.json"

        if manifest_yolu.exists():
            manifest = json.loads(manifest_yolu.read_text(encoding="utf-8"))
            manifest["version"] = SURUM
        else:
            aciklama = aciklama_uret(alan, ad)
            manifest = {
                "name": ad,
                "displayName": baslik(ad),
                "version": SURUM,
                "description": aciklama,
                "author": YAZAR,
                "license": LISANS,
                "keywords": anahtar_kelimeler(ad, alan),
            }
            yeni_manifest += 1

        if not args.dry_run:
            manifest_yolu.parent.mkdir(parents=True, exist_ok=True)
            manifest_yolu.write_text(
                json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
            )

        readme_yolu = alan / "README.md"
        if not readme_yolu.exists():
            yeni_readme += 1
            if not args.dry_run:
                readme_yolu.write_text(
                    readme_uret(ad, alan, manifest["description"]), encoding="utf-8"
                )

        kayit = mevcut.get(ad, {})
        kayitlar.append({
            "name": ad,
            "displayName": manifest["displayName"],
            "source": f"./{ad}",
            "description": kayit.get("description", manifest["description"]),
            "author": YAZAR,
        })

    market["plugins"] = sorted(kayitlar, key=lambda p: p["name"])
    if not args.dry_run:
        MARKETPLACE.write_text(
            json.dumps(market, ensure_ascii=False, indent=2) + "\n", encoding="utf-8"
        )

    print(f"Eklenti dizini      : {len(alanlar)}")
    print(f"Yeni manifest       : {yeni_manifest}")
    print(f"Yeni README         : {yeni_readme}")
    print(f"Marketplace kaydı   : {len(kayitlar)}")
    if args.dry_run:
        print("\n(--dry-run: hiçbir dosya yazılmadı)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
