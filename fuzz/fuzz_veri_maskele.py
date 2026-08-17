#!/usr/bin/env python3
"""atheris fuzz harness — cekirdek/scripts/veri_maskele.py

Hedef: maskele() ve _tc_kimlik_gecerli_mi() fonksiyonlarina rastgele/
duşmanca (adversarial) metin vererek cökme (crash), sonsuz dongu veya
beklenmedik istisna (exception) uretmediklerini dogrulamak. Bu fonksiyonlar
DUZENLI OLARAK guvenilmeyen kullanici belgelerini (dilekce, sozlesme)
isledigi icin bu bir bicimsel dogrulama katmani degil, gercek bir
dayaniklilik (robustness) testidir.

NOT: atheris yalnizca Linux'ta (manylinux wheel) guvenilir sekilde derlenir;
yerel gelistirme ortaminda (orn. macOS) calismayabilir. CI'da
.github/workflows/fuzzing.yml ubuntu-latest uzerinde calistirir.

Calistirma (CI icinde):
    python fuzz/fuzz_veri_maskele.py -max_total_time=60
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "cekirdek" / "scripts"))

import atheris  # noqa: E402

from veri_maskele import maskele, _tc_kimlik_gecerli_mi  # noqa: E402


def test_one_input(data: bytes) -> None:
    fdp = atheris.FuzzedDataProvider(data)
    metin = fdp.ConsumeUnicodeNoSurrogates(fdp.remaining_bytes())

    # Her iki fonksiyon da HERHANGI BIR metin/string girdisiyle cagrilinca
    # cokme veya beklenmedik istisna URETMEMELIDIR - tek beklenen istisna
    # yoktur, cunku bu fonksiyonlar guvenilmeyen belge metnini islemek
    # icin tasarlanmistir.
    sonuc = maskele(metin)
    assert isinstance(sonuc.maskelenmis_metin, str)
    assert isinstance(sonuc.bulunan_sayisi, dict)

    # Checksum fonksiyonu herhangi bir string ile cagrilabilmeli, ValueError
    # veya benzeri beklenmedik bir istisna firlatmamali - yalnizca True/False
    # donmelidir.
    gecerli = _tc_kimlik_gecerli_mi(metin)
    assert isinstance(gecerli, bool)


def main() -> None:
    atheris.Setup(sys.argv, test_one_input)
    atheris.Fuzz()


if __name__ == "__main__":
    main()
