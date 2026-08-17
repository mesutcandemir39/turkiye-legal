"""cekirdek/scripts/veri_maskele.py icin birim testler.

Deterministik oldugu icin klasik unit test ile tam kapsanabilir; LLM
gerektirmez.
"""
from __future__ import annotations

import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(REPO_ROOT / "cekirdek" / "scripts"))

from veri_maskele import maskele, _tc_kimlik_gecerli_mi  # noqa: E402

# Checksum algoritmasiyla uretilmis GECERLI test TC kimlik numaralari.
# Bunlar gercek kisilere ait DEGILDIR, yalniz algoritmik olarak gecerlidir.
GECERLI_TC_ORNEKLERI = ["97684210030", "93003497342", "15149346698"]


class TestTcKimlikChecksum:
    def test_gecerli_numaralar_dogrulanir(self):
        for no in GECERLI_TC_ORNEKLERI:
            assert _tc_kimlik_gecerli_mi(no) is True, f"{no} gecerli olmali"

    def test_rastgele_11_haneli_sayi_dogrulanmaz(self):
        # Checksum'i saglamayan rastgele bir 11 haneli sayi (orn. fatura/dosya no)
        assert _tc_kimlik_gecerli_mi("12345678901") is False

    def test_sifirla_baslayan_numara_gecersiz(self):
        assert _tc_kimlik_gecerli_mi("01234567890") is False

    def test_10_haneli_numara_gecersiz(self):
        assert _tc_kimlik_gecerli_mi("1234567890") is False


class TestMaskeleTcKimlik:
    def test_gecerli_tc_maskelenir(self):
        no = GECERLI_TC_ORNEKLERI[0]
        sonuc = maskele(f"Basvuru sahibinin TC Kimlik No: {no} olarak kayitlidir.")
        assert no not in sonuc.maskelenmis_metin
        assert "[TC_KIMLIK]" in sonuc.maskelenmis_metin
        assert sonuc.bulunan_sayisi.get("TC_KIMLIK") == 1

    def test_checksum_saglamayan_11_haneli_sayi_maskelenmez(self):
        """Kritik regresyon testi: checksum kontrolu olmadan her 11 haneli
        sayi (dosya no, telefon santral kodu vb.) yanlislikla maskelenirdi."""
        sonuc = maskele("Dosya numarasi: 12345678901")
        assert "12345678901" in sonuc.maskelenmis_metin
        assert "TC_KIMLIK" not in sonuc.bulunan_sayisi


class TestMaskeleIban:
    def test_iban_maskelenir(self):
        sonuc = maskele("Odeme IBAN: TR330006100519786457841326 hesabina yapilacaktir.")
        assert "TR330006100519786457841326" not in sonuc.maskelenmis_metin
        assert "[IBAN]" in sonuc.maskelenmis_metin
        assert sonuc.bulunan_sayisi.get("IBAN") == 1

    def test_bosluklu_iban_maskelenir(self):
        sonuc = maskele("IBAN: TR33 0006 1005 1978 6457 8413 26")
        assert "[IBAN]" in sonuc.maskelenmis_metin


class TestMaskeleEposta:
    def test_eposta_maskelenir(self):
        sonuc = maskele("Iletisim: ahmet.yilmaz@ornek.com adresinden ulasilabilir.")
        assert "ahmet.yilmaz@ornek.com" not in sonuc.maskelenmis_metin
        assert "[E_POSTA]" in sonuc.maskelenmis_metin


class TestMaskeleTelefon:
    def test_telefon_maskelenir(self):
        sonuc = maskele("Telefon: 0532 123 45 67")
        assert "[TELEFON]" in sonuc.maskelenmis_metin

    def test_ulke_kodlu_telefon_maskelenir(self):
        sonuc = maskele("Telefon: +90 532 123 45 67")
        assert "[TELEFON]" in sonuc.maskelenmis_metin


class TestMaskeleKartNo:
    def test_kart_numarasi_maskelenir(self):
        sonuc = maskele("Kart No: 4532 7712 3456 9010")
        assert "4532 7712 3456 9010" not in sonuc.maskelenmis_metin
        assert "[KART_NO]" in sonuc.maskelenmis_metin


class TestMaskeleBirlesikMetin:
    def test_coklu_veri_turu_ayni_metinde(self):
        metin = (
            f"Musteri T.C. Kimlik No {GECERLI_TC_ORNEKLERI[0]}, "
            "telefon 0532 123 45 67, e-posta test@ornek.com ve "
            "IBAN TR330006100519786457841326 bilgilerini paylasmistir."
        )
        sonuc = maskele(metin)
        assert "[TC_KIMLIK]" in sonuc.maskelenmis_metin
        assert "[TELEFON]" in sonuc.maskelenmis_metin
        assert "[E_POSTA]" in sonuc.maskelenmis_metin
        assert "[IBAN]" in sonuc.maskelenmis_metin
        assert sonuc.bulunan_sayisi == {
            "TC_KIMLIK": 1, "TELEFON": 1, "E_POSTA": 1, "IBAN": 1,
        }

    def test_hicbir_hassas_veri_yoksa_metin_degismez(self):
        metin = "Bu sozlesme 6098 sayili TBK m.20 kapsaminda incelenmistir."
        sonuc = maskele(metin)
        assert sonuc.maskelenmis_metin == metin
        assert sonuc.bulunan_sayisi == {}

    def test_isim_soyisim_yakalanmaz_bilinen_sinir(self):
        """Bilincli sinir testi: bu script bicimsel olmayan (isim gibi)
        kisisel verileri YAKALAMAZ — bu, SKILL.md'de acikca belirtilen
        bir sinirdir, script'in bir hata degil."""
        sonuc = maskele("Davaci Ahmet Yilmaz, davali Ayse Kaya aleyhine dava acmistir.")
        assert "Ahmet Yilmaz" in sonuc.maskelenmis_metin
        assert "Ayse Kaya" in sonuc.maskelenmis_metin
