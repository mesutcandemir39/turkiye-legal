#!/usr/bin/env python3
"""Kisisel veri maskeleme — cekirdek plugin.

BU MODUL, KVKK m.4 (veri isleme ilkeleri: olcululuk, amacla sinirli olma)
ilkesini teknik olarak destekler: bir belge modele gonderilmeden once,
belgedeki dogrudan tanimlayici kisisel veriler (T.C. kimlik no, telefon,
IBAN, e-posta, kredi karti benzeri kart numaralari) DETERMINISTIK regex
desenleriyle tespit edilip yer tutucularla degistirilir.

ONEMLI SINIRLAR (dogrulukla ilgili durustluk):
- Bu bir NLP/named-entity-recognition sistemi DEGILDIR; yalniz BICIMSEL
  olarak taninabilir kaliplari (11 haneli TC kimlik, IBAN formati, TR
  telefon formati, e-posta, 16 haneli kart numarasi) yakalar.
- Isim/soyisim gibi bicimsel bir kaliba uymayan kisisel veriler bu script
  tarafindan YAKALANMAZ. Bu, skill'in kullanicisina acikca belirtilmelidir
  (bkz. cekirdek/skills/veri-maskeleme/SKILL.md).
- Bu script bir "PII redaction" garantisi DEGIL, bir ON FILTRE saglar.
  Hassas belgelerde nihai sorumluluk kullanicidadir.

Kullanim (CLI):
    python cekirdek/scripts/veri_maskele.py --dosya girdi.txt
    echo "T.C. Kimlik: 12345678901" | python cekirdek/scripts/veri_maskele.py --stdin
"""
from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field


# --- TC Kimlik No dogrulama (checksum algoritmasi ile) -----------------
# Kaynak: 5490 sayili Nufus Hizmetleri Kanunu'nun ongordugu TC Kimlik No
# algoritmasi (kamuya acik, yaygin bilinen bir sifre/checksum standardidir).
def _tc_kimlik_gecerli_mi(numara: str) -> bool:
    if not re.fullmatch(r"[1-9][0-9]{10}", numara):
        return False
    digits = [int(c) for c in numara]
    odd_sum = sum(digits[0:9:2])
    even_sum = sum(digits[1:8:2])
    d10 = ((odd_sum * 7) - even_sum) % 10
    d11 = sum(digits[0:10]) % 10
    return digits[9] == d10 and digits[10] == d11


TC_KIMLIK_RE = re.compile(r"\b\d{11}\b")
TELEFON_RE = re.compile(r"\b(?:\+90|0)?\s?5\d{2}[\s.-]?\d{3}[\s.-]?\d{2}[\s.-]?\d{2}\b")
IBAN_RE = re.compile(r"\bTR\d{2}[\s]?\d{4}[\s]?\d{4}[\s]?\d{4}[\s]?\d{4}[\s]?\d{4}[\s]?\d{2}\b", re.IGNORECASE)
EMAIL_RE = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
KART_RE = re.compile(r"\b\d{4}[\s-]?\d{4}[\s-]?\d{4}[\s-]?\d{4}\b")


@dataclass
class MaskelemeSonucu:
    maskelenmis_metin: str
    bulunan_sayisi: dict[str, int] = field(default_factory=dict)

    def to_dict(self) -> dict:
        return {
            "maskelenmis_metin": self.maskelenmis_metin,
            "bulunan_sayisi": self.bulunan_sayisi,
        }


def maskele(metin: str) -> MaskelemeSonucu:
    """Metindeki bicimsel olarak taninabilir kisisel verileri maskeler.
    Sira onemlidir: daha spesifik kaliplar (IBAN, kart no) once islenir ki
    TC_KIMLIK_RE gibi genel kaliplar onlarin bir parcasini yanlislikla
    yakalamasin."""
    sayac: dict[str, int] = {}

    def _mask(pattern: re.Pattern, etiket: str, text: str, dogrulayici=None) -> str:
        def repl(m: re.Match) -> str:
            if dogrulayici is not None:
                temiz = re.sub(r"\D", "", m.group(0))
                if not dogrulayici(temiz):
                    return m.group(0)
            sayac[etiket] = sayac.get(etiket, 0) + 1
            return f"[{etiket}]"
        return pattern.sub(repl, text)

    sonuc = metin
    sonuc = _mask(IBAN_RE, "IBAN", sonuc)
    sonuc = _mask(EMAIL_RE, "E_POSTA", sonuc)
    sonuc = _mask(KART_RE, "KART_NO", sonuc)
    sonuc = _mask(TELEFON_RE, "TELEFON", sonuc)
    sonuc = _mask(TC_KIMLIK_RE, "TC_KIMLIK", sonuc, dogrulayici=_tc_kimlik_gecerli_mi)

    return MaskelemeSonucu(maskelenmis_metin=sonuc, bulunan_sayisi=sayac)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    grp = ap.add_mutually_exclusive_group(required=True)
    grp.add_argument("--dosya", type=str, help="Maskelenecek dosyanin yolu")
    grp.add_argument("--stdin", action="store_true", help="Metni stdin'den oku")
    ap.add_argument("--json", action="store_true", help="Sonucu JSON olarak ver")
    args = ap.parse_args()

    if args.stdin:
        metin = sys.stdin.read()
    else:
        with open(args.dosya, encoding="utf-8") as f:
            metin = f.read()

    sonuc = maskele(metin)

    if args.json:
        import json
        print(json.dumps(sonuc.to_dict(), ensure_ascii=False, indent=2))
    else:
        print(sonuc.maskelenmis_metin)
        if sonuc.bulunan_sayisi:
            print("\n--- Maskelenen unsurlar ---", file=sys.stderr)
            for etiket, adet in sonuc.bulunan_sayisi.items():
                print(f"{etiket}: {adet}", file=sys.stderr)

    return 0


if __name__ == "__main__":
    sys.exit(main())
