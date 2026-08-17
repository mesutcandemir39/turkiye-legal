"""cekirdek/scripts/sure_hesapla.py icin birim testler.

Bu, docs/ARCHITECTURE_DECISIONS.md ADR-006'nin dogrulamasidir: hukuki sure
aritmetigi deterministik oldugu icin klasik unit test ile tam kapsanabilir
(golden/LLM testine ihtiyac YOKTUR).
"""
from __future__ import annotations

import sys
from datetime import date
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "cekirdek" / "scripts"))

from sure_hesapla import (  # noqa: E402
    gun_ekle_resmi_tatil_atlayarak,
    hmk_sure_bitis_hesapla,
    is_adli_tatil_donemi,
    is_sabit_resmi_tatil,
)


class TestAdliTatilDonemi:
    def test_20_temmuz_adli_tatil_baslangici(self):
        assert is_adli_tatil_donemi(date(2026, 7, 20)) is True

    def test_31_agustos_adli_tatil_sonu(self):
        assert is_adli_tatil_donemi(date(2026, 8, 31)) is True

    def test_19_temmuz_adli_tatil_disinda(self):
        assert is_adli_tatil_donemi(date(2026, 7, 19)) is False

    def test_1_eylul_adli_tatil_disinda(self):
        assert is_adli_tatil_donemi(date(2026, 9, 1)) is False

    def test_ortasi_15_agustos(self):
        assert is_adli_tatil_donemi(date(2026, 8, 15)) is True


class TestSabitResmiTatil:
    def test_yilbasi(self):
        assert is_sabit_resmi_tatil(date(2026, 1, 1)) is True

    def test_cumhuriyet_bayrami(self):
        assert is_sabit_resmi_tatil(date(2026, 10, 29)) is True

    def test_zafer_bayrami(self):
        assert is_sabit_resmi_tatil(date(2026, 8, 30)) is True

    def test_sıradan_gun_tatil_degil(self):
        assert is_sabit_resmi_tatil(date(2026, 3, 15)) is False

    def test_dini_bayram_kapsam_disi_tatil_olarak_isaretlenmez(self):
        """Kasitli sinir testi: bu fonksiyon dini bayramlari BILMEZ (kapsam
        disi, bkz. sure_kurallari.yaml). Rastgele bir tarih icin False donmesi
        beklenir — bu, yanlislikla dini bayram tarihi hardcode edilmedigini
        dolayli olarak dogrular."""
        assert is_sabit_resmi_tatil(date(2026, 3, 20)) is False


class TestHmkSureBitisHesapla:
    def test_adli_tatile_tabi_degilse_degismez(self):
        bitis = date(2026, 8, 10)
        sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=False)
        assert sonuc.nihai_bitis_tarihi == bitis
        assert sonuc.adli_tatile_rastladi is False

    def test_adli_tatile_tabi_ama_donem_disinda(self):
        bitis = date(2026, 3, 1)
        sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=True)
        assert sonuc.nihai_bitis_tarihi == bitis
        assert sonuc.adli_tatile_rastladi is False

    def test_adli_tatile_tabi_ve_donem_icinde_uzuyor(self):
        """HMK m.104: 20 Temmuz-31 Agustos arasina rastlayan bitis, 8 Eylul'e uzar."""
        bitis = date(2026, 8, 25)
        sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=True)
        assert sonuc.adli_tatile_rastladi is True
        assert sonuc.nihai_bitis_tarihi == date(2026, 9, 8)

    def test_adli_tatil_ilk_gunu_de_uzuyor(self):
        bitis = date(2026, 7, 20)
        sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=True)
        assert sonuc.nihai_bitis_tarihi == date(2026, 9, 8)

    def test_adli_tatil_son_gunu_de_uzuyor(self):
        bitis = date(2026, 8, 31)
        sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=True)
        assert sonuc.nihai_bitis_tarihi == date(2026, 9, 8)

    def test_farkli_yillarda_dogru_calisir(self):
        """Yil-bagimsiz formul dogrulamasi (artik yil dahil, 2028 artik yil)."""
        for yil in (2025, 2026, 2027, 2028):
            bitis = date(yil, 8, 1)
            sonuc = hmk_sure_bitis_hesapla(bitis, adli_tatile_tabi=True)
            assert sonuc.nihai_bitis_tarihi == date(yil, 9, 8), f"{yil} icin hatali"

    def test_sonuc_kaynak_atfi_icerir(self):
        sonuc = hmk_sure_bitis_hesapla(date(2026, 8, 1), adli_tatile_tabi=True)
        assert any("104" in k for k in sonuc.kaynaklar)
        assert any("102" in k for k in sonuc.kaynaklar)


class TestGunEkleResmiTatilAtlayarak:
    def test_hafta_sonu_atlanir(self):
        # 2026-08-14 Cuma; +1 is gunu -> Pazartesi 2026-08-17 (17 Agustos adli
        # tatile denk gelse de bu fonksiyon adli tatili degil, yalniz sabit
        # resmi tatilleri ve hafta sonunu dikkate alir.
        sonuc = gun_ekle_resmi_tatil_atlayarak(date(2026, 8, 14), 1)
        assert sonuc.weekday() < 5  # hafta ici bir gun olmali
        assert sonuc > date(2026, 8, 14)

    def test_resmi_tatil_atlanir(self):
        # 2026-04-22 Carsamba (varsayimsal); +1 is gunu 23 Nisan'a denk gelirse atlanmali
        baslangic = date(2026, 4, 22)
        sonuc = gun_ekle_resmi_tatil_atlayarak(baslangic, 1)
        assert sonuc != date(2026, 4, 23), "23 Nisan resmi tatili atlanmadi"

    def test_negatif_gun_hata_verir(self):
        import pytest

        with pytest.raises(ValueError):
            gun_ekle_resmi_tatil_atlayarak(date(2026, 1, 1), -1)
