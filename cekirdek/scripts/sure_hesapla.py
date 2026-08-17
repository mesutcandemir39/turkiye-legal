#!/usr/bin/env python3
"""Deterministik hukuki sure hesaplayici — cekirdek plugin.

BU MODUL, docs/ARCHITECTURE_DECISIONS.md ADR-006'nin uygulamasidir: hukuki
sure aritmetigi LLM'e birakilmaz. Tum sabitler cekirdek/references/sure_kurallari.yaml
dosyasindan turetilir ve her biri kaynak atfi tasir.

KAPSAM (bkz. sure_kurallari.yaml "kapsam_disi" blogu):
  - HMK'ya tabi genel hukuk yargilamasindaki adli tatil kurali (m.102, m.104)
  - 2429 sayili Kanun'daki SABIT tarihli resmi tatiller
  - KAPSAM DISI: dini bayramlar (kameri takvim, harici veri gerektirir),
    IIK/IYUK'un kendi sure rejimleri (henuz eklenmedi)

Bu script bir LLM tarafindan degil, dogrudan Python olarak veya bir skill
icinden alt surec (subprocess) olarak cagrilir.

Kullanim (CLI):
    python cekirdek/scripts/sure_hesapla.py --bitis-tarihi 2026-08-25 --adli-tatile-tabi
"""
from __future__ import annotations

import argparse
import json
import sys
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
KURALLAR_PATH = REPO_ROOT / "cekirdek" / "references" / "sure_kurallari.yaml"

ADLI_TATIL_BASLANGIC = (7, 20)  # (ay, gun) — HMK m.102
ADLI_TATIL_BITIS = (8, 31)  # HMK m.102
ADLI_TATIL_SONRASI_UZATILMIS_BITIS = (9, 8)  # 1 Eylul + 7 gun, HMK m.104

SABIT_RESMI_TATILLER = [
    (1, 1), (4, 23), (5, 1), (5, 19), (7, 15), (8, 30), (10, 29),
]  # 2429 sayili Kanun m.2 — kaynak: cekirdek/references/sure_kurallari.yaml


@dataclass
class SureSonucu:
    girdi_bitis_tarihi: date
    nihai_bitis_tarihi: date
    adli_tatile_rastladi: bool
    aciklama: str
    kaynaklar: list[str]

    def to_dict(self) -> dict:
        return {
            "girdi_bitis_tarihi": self.girdi_bitis_tarihi.isoformat(),
            "nihai_bitis_tarihi": self.nihai_bitis_tarihi.isoformat(),
            "adli_tatile_rastladi": self.adli_tatile_rastladi,
            "aciklama": self.aciklama,
            "kaynaklar": self.kaynaklar,
        }


def is_adli_tatil_donemi(gun: date) -> bool:
    """HMK m.102: 20 Temmuz - 31 Agustos (dahil) adli tatildir."""
    ay_gun = (gun.month, gun.day)
    return ADLI_TATIL_BASLANGIC <= ay_gun <= ADLI_TATIL_BITIS


def is_sabit_resmi_tatil(gun: date) -> bool:
    """2429 sayili Kanun m.2 — yalniz SABIT tarihli resmi tatiller.
    Dini bayramlar KAPSAM DISIDIR (bkz. modul basligi)."""
    return (gun.month, gun.day) in SABIT_RESMI_TATILLER


def hmk_sure_bitis_hesapla(bitis_tarihi: date, adli_tatile_tabi: bool) -> SureSonucu:
    """HMK'ya tabi bir surenin bitis tarihini, adli tatil uzatmasini
    dikkate alarak hesaplar.

    onemli_sinir (bkz. sure_kurallari.yaml): bu fonksiyon adli tatile tabi
    olup olmadigini KENDİSİ tespit etmez — cagiran taraf (skill) bunu
    HMK m.103'e gore onceden belirleyip `adli_tatile_tabi` parametresiyle
    bildirmek ZORUNDADIR.
    """
    kaynaklar = ["6100 sayılı HMK m.102", "6100 sayılı HMK m.104"]

    if not adli_tatile_tabi:
        return SureSonucu(
            girdi_bitis_tarihi=bitis_tarihi,
            nihai_bitis_tarihi=bitis_tarihi,
            adli_tatile_rastladi=False,
            aciklama=(
                "Bu iş adli tatile tabi olarak işaretlenmedi; HMK m.104 uzatması "
                "uygulanmadı. Bitiş tarihi değişmedi."
            ),
            kaynaklar=kaynaklar,
        )

    if not is_adli_tatil_donemi(bitis_tarihi):
        return SureSonucu(
            girdi_bitis_tarihi=bitis_tarihi,
            nihai_bitis_tarihi=bitis_tarihi,
            adli_tatile_rastladi=False,
            aciklama="Bitiş tarihi adli tatil dönemine (20 Temmuz-31 Ağustos) rastlamıyor.",
            kaynaklar=kaynaklar,
        )

    uzatilmis = date(bitis_tarihi.year, *ADLI_TATIL_SONRASI_UZATILMIS_BITIS)
    return SureSonucu(
        girdi_bitis_tarihi=bitis_tarihi,
        nihai_bitis_tarihi=uzatilmis,
        adli_tatile_rastladi=True,
        aciklama=(
            f"Bitiş tarihi ({bitis_tarihi.isoformat()}) adli tatil dönemine rastladı. "
            f"HMK m.104 gereği süre, adli tatilin bittiği günden (1 Eylül) itibaren "
            f"7 gün uzamış sayılır. Yeni bitiş tarihi: {uzatilmis.isoformat()}."
        ),
        kaynaklar=kaynaklar,
    )


def gun_ekle_resmi_tatil_atlayarak(baslangic: date, is_gunu_sayisi: int) -> date:
    """Baslangictan itibaren N 'is gunu' ekler; hafta sonu VE sabit resmi
    tatilleri atlar. DIKKAT: bu genel amacli bir yardimci fonksiyondur —
    hangi kanunun 'is gunu' mu yoksa 'takvim gunu' mu saydigina karar vermek
    cagiran skill'in sorumlulugundadir; bu fonksiyon varsayim yapmaz."""
    if is_gunu_sayisi < 0:
        raise ValueError("is_gunu_sayisi negatif olamaz")
    gun = baslangic
    sayilan = 0
    while sayilan < is_gunu_sayisi:
        gun += timedelta(days=1)
        if gun.weekday() >= 5:  # 5=Cumartesi, 6=Pazar
            continue
        if is_sabit_resmi_tatil(gun):
            continue
        sayilan += 1
    return gun


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--bitis-tarihi", required=True, help="YYYY-MM-DD formatında")
    ap.add_argument("--adli-tatile-tabi", action="store_true", help="Bu iş HMK m.103 anlamında adli tatile tabi mi?")
    ap.add_argument("--json", action="store_true", help="Çıktıyı JSON olarak ver")
    args = ap.parse_args()

    try:
        bitis = date.fromisoformat(args.bitis_tarihi)
    except ValueError:
        print(f"HATA: '{args.bitis_tarihi}' gecerli bir YYYY-MM-DD tarihi degil.", file=sys.stderr)
        return 1

    sonuc = hmk_sure_bitis_hesapla(bitis, args.adli_tatile_tabi)

    if args.json:
        print(json.dumps(sonuc.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(sonuc.aciklama)
        print(f"Kaynaklar: {', '.join(sonuc.kaynaklar)}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
