"""cekirdek/scripts/surum_kontrol.py icin birim testler.

Ag cagrisi (en_guncel_surumu_getir) mock'lanir — bu testler CI'da
LLM'siz VE agsiz calisir, canli GitHub durumuna bagimli degildir.
"""
from __future__ import annotations

import sys
from pathlib import Path
from unittest.mock import patch

import pytest

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "cekirdek" / "scripts"))

from surum_kontrol import _surum_tuple, kontrol_et  # noqa: E402


class TestSurumTuple:
    def test_basit_surum(self):
        assert _surum_tuple("0.2.0") == (0, 2, 0)

    def test_v_onekli_surum(self):
        assert _surum_tuple("v0.2.0") == (0, 2, 0)

    def test_gecersiz_surum_hata_verir(self):
        with pytest.raises(ValueError):
            _surum_tuple("abc")

    def test_eksik_parca_hata_verir(self):
        with pytest.raises(ValueError):
            _surum_tuple("0.2.x")


class TestKontrolEt:
    def test_kurulu_surum_eskiyse_guncelleme_onerilir(self):
        with patch("surum_kontrol.en_guncel_surumu_getir", return_value=("0.3.0", "https://example.com/v0.3.0", None)):
            sonuc = kontrol_et("0.2.0")
        assert sonuc.guncel_mi is False
        assert sonuc.en_guncel_surum == "0.3.0"
        assert sonuc.hata is None

    def test_kurulu_surum_guncelse_guncel_raporlanir(self):
        with patch("surum_kontrol.en_guncel_surumu_getir", return_value=("0.2.0", "https://example.com/v0.2.0", None)):
            sonuc = kontrol_et("0.2.0")
        assert sonuc.guncel_mi is True

    def test_kurulu_surum_daha_yeniyse_guncel_sayilir(self):
        """On-surum (henuz release edilmemis local dev) durumu icin makul davranis."""
        with patch("surum_kontrol.en_guncel_surumu_getir", return_value=("0.2.0", "https://example.com/v0.2.0", None)):
            sonuc = kontrol_et("0.3.0")
        assert sonuc.guncel_mi is True

    def test_ag_hatasi_acikca_raporlanir(self):
        with patch("surum_kontrol.en_guncel_surumu_getir", return_value=(None, None, "Ag hatasi: timeout")):
            sonuc = kontrol_et("0.2.0")
        assert sonuc.hata is not None
        assert sonuc.guncel_mi is None
        assert "Ag hatasi" in sonuc.hata

    def test_gecersiz_kurulu_surum_ag_cagrisi_yapmadan_hata_verir(self):
        with patch("surum_kontrol.en_guncel_surumu_getir") as mock_getir:
            sonuc = kontrol_et("gecersiz-surum")
        mock_getir.assert_not_called()
        assert sonuc.hata is not None

    def test_kontrol_scripti_hicbir_komut_calistirmiyor(self):
        """Kritik ayrim testi (ADR-011): surum_kontrol.py SAF BIR KONTROL
        katmanidir - subprocess/os.system cagirmaz, yalniz VERİ dondurur.
        Gercek guncelleme eylemi bu script'te DEGIL, SKILL.md'nin talimatiyla
        cagrilan Bash aracinda gerceklesir (izin katmani orada devreye girer).
        Bu ayrim, deterministik kontrol ile eylemi birbirinden bagimsiz ve
        test edilebilir tutar."""
        import inspect
        import surum_kontrol

        kaynak = inspect.getsource(surum_kontrol)
        assert "subprocess" not in kaynak
        assert "os.system" not in kaynak
        assert "claude plugin update" in kaynak  # yalniz METIN olarak uretilir
