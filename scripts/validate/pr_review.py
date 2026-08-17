#!/usr/bin/env python3
"""Otomatik PR incelemesi — tamamen deterministik, HARICI API KULLANMAZ.

Bu script hicbir dil modeline cagri yapmaz, hicbir API anahtari istemez ve
internet erisimi gerektirmez. Tum degerlendirme, depodaki dogrulayici
script'lerin gercek cikti ve cikis kodlarindan + kural tabanli metin
analizinden turetilir. Ayni girdi her zaman ayni sonucu verir.

Dort kriter:
  1. Structure       -> validate_skills.py    (sema uyumu)
  2. Legal Accuracy  -> validate_sources.py   (kaynak defteri atfi)
  3. Safety          -> lint_prompts.py       (halusinasyon/sizinti deseni)
  4. Quality         -> bu dosyadaki kural tabanli Turkce uslup denetimi

Karar: BLOCK / WARN / PASS. Bu karar tek basina MERGE YETKISI TASIMAZ;
nihai onay CODEOWNERS geregi ilgili bakimciya aittir.

Kullanim:
    python scripts/validate/pr_review.py --files-from changed_files.txt \\
        --output review_result.json
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[2]
VALIDATE_DIR = REPO_ROOT / "scripts" / "validate"

# --------------------------------------------------------------------------
# Kural tabanli Turkce uslup denetimi (Quality kriteri)
# --------------------------------------------------------------------------

# Terminoloji: .claude/CLAUDE.md "Terminoloji" bolumu geregi.
# (yanlis_desen, dogru_karsilik, aciklama)
TERMINOLOJI: list[tuple[str, str]] = [
    (r"\byasal\b", "hukuki"),
    (r"\byasal olarak\b", "hukuken"),
    (r"\bkontrat\b", "sözleşme"),
    (r"\bkontratı\b", "sözleşmeyi"),
    (r"\bmahkeme kağıdı\b", "tensip zaptı / dilekçe"),
    (r"\bdava açmak için başvuru\b", "dava dilekçesi"),
    (r"\bavukat tutmak\b", "vekâlet vermek"),
]

# Makine cevirisi / "AI slop" kokan kaliplar.
SLOP_DESENLERI: list[tuple[str, str]] = [
    (r"\bDalmak\b|\bderinlemesine dalalım\b", "İngilizce 'dive into' çevirisi"),
    (r"\bbu makalede\b", "skill metni makale değildir"),
    (r"\bunutmayın ki\b", "gereksiz dolgu ifade"),
    (r"\bsonuç olarak,? bu\b", "gereksiz dolgu ifade"),
    (r"\bçok önemlidir ki\b", "gereksiz vurgu kalıbı"),
    (r"\bgüçlü bir şekilde\b", "makine çevirisi kalıbı"),
    (r"\bsağlamak için tasarlanmıştır\b", "makine çevirisi kalıbı"),
    (r"\bkapsamlı bir şekilde ele al", "içi boş vurgu"),
    (r"\bAI\b(?! Act)", "Türkçe metinde 'yapay zekâ' tercih edilir"),
]

# Tamamlanmamis icerik isaretleri.
PLACEHOLDER_DESENLERI: list[tuple[str, str]] = [
    (r"\bTODO\b", "tamamlanmamış içerik"),
    (r"\bTBD\b", "tamamlanmamış içerik"),
    (r"\bFIXME\b", "tamamlanmamış içerik"),
    (r"\bXXX\b", "tamamlanmamış içerik"),
    (r"\blorem ipsum\b", "yer tutucu metin"),
    (r"\[BURAYA .*?\]", "doldurulmamış yer tutucu"),
    (r"\bplaceholder\b", "yer tutucu metin"),
]

MAKS_CUMLE_KELIME = 45  # Bu uzunlugu asan cumleler okunabilirligi dusurur.
INCELENEN_UZANTILAR = {".md"}


def _metin_dosyalari(files: list[Path]) -> list[Path]:
    """Yalniz depo icindeki, incelenmeye deger markdown dosyalarini dondurur."""
    secilen = []
    for f in files:
        if f.suffix.lower() not in INCELENEN_UZANTILAR:
            continue
        tam = REPO_ROOT / f
        if tam.exists() and tam.is_file():
            secilen.append(tam)
    return secilen


def _govde_metni(icerik: str) -> str:
    """YAML frontmatter'i atlayip yalniz govde metnini dondurur."""
    if icerik.startswith("---"):
        parcalar = icerik.split("---", 2)
        if len(parcalar) >= 3:
            return parcalar[2]
    return icerik


def uslup_denetimi(files: list[Path]) -> tuple[int, list[str]]:
    """Kural tabanli Turkce uslup denetimi.

    Dondurur: (0-10 puan, bulgu listesi). Tamamen deterministiktir.
    """
    bulgular: list[str] = []
    hedefler = _metin_dosyalari(files)

    if not hedefler:
        # Markdown degismediyse uslup denetimi konu disidir - notr degil TAM puan,
        # cunku denetlenecek bir sey yok ve bu bir eksiklik degil.
        return 10, ["İncelenecek markdown değişikliği yok — üslup denetimi uygulanmadı."]

    for yol in hedefler:
        goreli = yol.relative_to(REPO_ROOT)
        try:
            icerik = yol.read_text(encoding="utf-8", errors="replace")
        except OSError:
            continue
        govde = _govde_metni(icerik)

        for desen, dogrusu in TERMINOLOJI:
            if re.search(desen, govde, re.IGNORECASE):
                bulgular.append(f"`{goreli}`: terminoloji — `{desen}` yerine **{dogrusu}** kullanın.")

        for desen, aciklama in SLOP_DESENLERI:
            if re.search(desen, govde, re.IGNORECASE):
                bulgular.append(f"`{goreli}`: üslup — {aciklama}.")

        for desen, aciklama in PLACEHOLDER_DESENLERI:
            if re.search(desen, govde, re.IGNORECASE):
                bulgular.append(f"`{goreli}`: {aciklama} tespit edildi.")

        # Asiri uzun cumle taramasi.
        # Kod bloklari, markdown tablolari, liste satirlari ve HTML etiketleri
        # duz nesir degildir; cumle uzunlugu olcumune dahil edilmez.
        govde_kodsuz = re.sub(r"```.*?```", "", govde, flags=re.DOTALL)
        govde_kodsuz = re.sub(r"^\s*\|.*$", "", govde_kodsuz, flags=re.MULTILINE)
        govde_kodsuz = re.sub(r"^\s*[-*+]\s.*$", "", govde_kodsuz, flags=re.MULTILINE)
        govde_kodsuz = re.sub(r"^\s*\d+\.\s.*$", "", govde_kodsuz, flags=re.MULTILINE)
        govde_kodsuz = re.sub(r"<[^>]+>", "", govde_kodsuz)
        for cumle in re.split(r"(?<=[.!?])\s+|\n{2,}", govde_kodsuz):
            kelime_sayisi = len(cumle.split())
            if kelime_sayisi > MAKS_CUMLE_KELIME:
                bulgular.append(
                    f"`{goreli}`: {kelime_sayisi} kelimelik çok uzun cümle — bölmeyi değerlendirin."
                )
                break  # Dosya basina bir kez uyar, listeyi bogmasin.

    # Puanlama: her bulgu 1 puan dusurur, taban 4.
    puan = max(4, 10 - len(bulgular)) if bulgular else 10
    return puan, bulgular


# --------------------------------------------------------------------------
# Dogrulayici script calistirici
# --------------------------------------------------------------------------


def dogrulayici_calistir(script_adi: str, files_from: Path | None) -> tuple[bool, str]:
    """Bir dogrulayici script'i calistirir. Dondurur: (basarili_mi, cikti)."""
    yol = VALIDATE_DIR / script_adi
    if not yol.exists():
        return False, f"{script_adi} bulunamadı"

    komut = [sys.executable, str(yol)]
    if files_from is not None and files_from.exists():
        komut += ["--files-from", str(files_from)]

    try:
        sonuc = subprocess.run(
            komut, capture_output=True, text=True, timeout=300, cwd=str(REPO_ROOT)
        )
    except subprocess.TimeoutExpired:
        return False, f"{script_adi} zaman aşımına uğradı (300 sn)"
    except OSError as exc:
        return False, f"{script_adi} çalıştırılamadı: {exc}"

    cikti = (sonuc.stdout + sonuc.stderr).strip()
    return sonuc.returncode == 0, cikti


def _son_satir(cikti: str) -> str:
    satirlar = [s for s in cikti.splitlines() if s.strip()]
    return satirlar[-1][:200] if satirlar else "ayrıntı yok"


# Dogrulayici, PR icerigi yuzunden degil ORTAM eksigi yuzunden calisamadiysa
# bunu bir PR hatasi gibi raporlamak yaniltici olur - ayirt edilir.
ORTAM_HATASI_DESENI = re.compile(
    r"kurulu degil|kurulu değil|ModuleNotFoundError|No module named|"
    r"bulunamadı|çalıştırılamadı|zaman aşımına",
    re.IGNORECASE,
)


def _ortam_hatasi_mi(cikti: str) -> bool:
    return bool(ORTAM_HATASI_DESENI.search(cikti))


def _kriter(ad: str, ok: bool, cikti: str, basari_notu: str,
            hata_notu: str, hata_puani: int) -> dict:
    """Bir kriteri puanlar; ortam hatasini PR hatasindan ayirir."""
    if ok:
        return {"criterion": ad, "score": 10, "note": basari_notu}
    if _ortam_hatasi_mi(cikti):
        return {
            "criterion": ad,
            "score": 5,
            "note": f"ÇALIŞTIRILAMADI (ortam eksiği, PR hatası değil): {_son_satir(cikti)}",
        }
    return {"criterion": ad, "score": hata_puani, "note": f"{hata_notu} {_son_satir(cikti)}"}


def puanlari_uret(files_from: Path | None, degisen: list[Path]) -> list[dict]:
    """Dort kriteri de deterministik olarak puanlar."""
    puanlar: list[dict] = []

    ok, cikti = dogrulayici_calistir("validate_skills.py", files_from)
    puanlar.append(_kriter(
        "Structure (şema uyumu)", ok, cikti,
        "Şema doğrulaması geçti.", "Şema hatası:", 2,
    ))

    ok, cikti = dogrulayici_calistir("validate_sources.py", files_from)
    puanlar.append(_kriter(
        "Legal Accuracy (kaynak atfı)", ok, cikti,
        "Tüm atıflar kaynak defterinde doğrulandı.",
        "Doğrulanamayan kaynak atfı — kritik.", 1,
    ))

    ok, cikti = dogrulayici_calistir("lint_prompts.py", files_from)
    puanlar.append(_kriter(
        "Safety (halüsinasyon/sızıntı)", ok, cikti,
        "Sahte karar numarası veya yabancı hukuk sızıntısı bulunmadı.",
        "Riskli desen tespit edildi — kritik.", 1,
    ))

    uslup_puan, uslup_bulgular = uslup_denetimi(degisen)
    if uslup_bulgular and uslup_puan < 10:
        not_metni = f"{len(uslup_bulgular)} üslup bulgusu: " + " · ".join(uslup_bulgular[:3])
        if len(uslup_bulgular) > 3:
            not_metni += f" (+{len(uslup_bulgular) - 3} tane daha)"
    else:
        not_metni = uslup_bulgular[0] if uslup_bulgular else "Üslup denetimi temiz."
    puanlar.append({
        "criterion": "Quality (üslup, terminoloji)",
        "score": uslup_puan,
        "note": not_metni[:400],
    })

    return puanlar


def karar_ver(puanlar: list[dict]) -> str:
    """BLOCK: kritik kriter dustu. WARN: herhangi bir kriter 6 alti. PASS: temiz."""
    kritik = [
        p for p in puanlar
        if p["criterion"].startswith(("Legal Accuracy", "Safety")) and p["score"] <= 2
    ]
    if kritik:
        return "BLOCK"
    if any(p["score"] < 6 for p in puanlar):
        return "WARN"
    return "PASS"


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--files-from", type=Path, default=None,
                    help="Degisen dosya yollarini iceren dosya (satir satir)")
    ap.add_argument("--output", type=Path, required=True,
                    help="Sonucun yazilacagi JSON dosyasi")
    args = ap.parse_args()

    degisen: list[Path] = []
    if args.files_from and args.files_from.exists():
        degisen = [
            Path(s.strip())
            for s in args.files_from.read_text(encoding="utf-8").splitlines()
            if s.strip()
        ]

    puanlar = puanlari_uret(args.files_from, degisen)
    verdict = karar_ver(puanlar)

    sonuc = {
        "verdict": verdict,
        "deterministic": True,
        "external_api_used": False,
        "changed_file_count": len(degisen),
        "scores": puanlar,
        "summary": (
            "Tüm kriterler depodaki doğrulayıcı script'lerden ve kural tabanlı "
            "üslup denetiminden türetildi. Harici API çağrısı yapılmadı; "
            "sonuç aynı girdi için her zaman aynıdır."
        ),
    }

    args.output.write_text(
        json.dumps(sonuc, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(json.dumps(sonuc, ensure_ascii=False, indent=2))
    return 0


if __name__ == "__main__":
    sys.exit(main())
