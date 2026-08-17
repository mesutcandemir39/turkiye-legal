#!/usr/bin/env python3
"""Surum kontrolu — cekirdek plugin.

Kurulu turkiye-legal surumunu, GitHub'daki en guncel Stable Release ile
KARSILASTIRIR. Hicbir kosulda kendisi guncelleme YAPMAZ — yalniz raporlar.

BU BILINCLI BIR TASARIM KARARIDIR: bir hukuki aracin kendi davranisini kullanicinin onayi olmadan
sessizce degistirmesi, ADR-005'in insan-in-the-loop ilkesiyle dogrudan
celisir. Bu script yalniz "surum X var, sizde Y kurulu, guncellemek icin
su komutu calistirin" der; `claude plugin update` komutunu KENDI BASINA
CALISTIRMAZ.

Ag erisimi: yalniz GitHub'in genel (public, kimlik dogrulamasiz) Releases
API'sine GET istegi atar (repos/{owner}/{repo}/releases/latest). Bu uc nokta
SADECE en son Stable (draft/prerelease OLMAYAN) surumu doner — bu, projenin
"her zaman yalniz Stable kullan" politikasiyla dogrudan uyumludur.

Kullanim (CLI):
    python cekirdek/scripts/surum_kontrol.py --kurulu-surum 0.2.0
    python cekirdek/scripts/surum_kontrol.py --kurulu-surum 0.1.0 --json
"""
from __future__ import annotations

import argparse
import json
import sys
import urllib.error
import urllib.request
from dataclasses import dataclass

REPO = "mesutcandemir39/turkiye-legal"
RELEASES_LATEST_URL = f"https://api.github.com/repos/{REPO}/releases/latest"
USER_AGENT = "turkiye-legal-surum-kontrol/1.0"


@dataclass
class SurumKontroluSonucu:
    kurulu_surum: str
    en_guncel_surum: str | None
    guncel_mi: bool | None
    hata: str | None
    release_url: str | None

    def to_dict(self) -> dict:
        return {
            "kurulu_surum": self.kurulu_surum,
            "en_guncel_surum": self.en_guncel_surum,
            "guncel_mi": self.guncel_mi,
            "hata": self.hata,
            "release_url": self.release_url,
        }


def _surum_tuple(surum: str) -> tuple[int, ...]:
    temiz = surum.lstrip("vV")
    try:
        return tuple(int(p) for p in temiz.split("."))
    except ValueError:
        raise ValueError(f"'{surum}' gecerli bir semver degil (X.Y.Z bekleniyor)")


def en_guncel_surumu_getir(timeout: float = 10.0) -> tuple[str | None, str | None, str | None]:
    """Donus: (surum, release_url, hata_mesaji). Basarili ise hata_mesaji None."""
    req = urllib.request.Request(RELEASES_LATEST_URL, headers={
        "User-Agent": USER_AGENT,
        "Accept": "application/vnd.github+json",
    })
    try:
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        return None, None, f"GitHub API hatasi: HTTP {e.code}"
    except urllib.error.URLError as e:
        return None, None, f"Ag hatasi: {e.reason}"
    except Exception as e:  # noqa: BLE001 - CLI icin genis yakalama kasitli
        return None, None, f"Beklenmeyen hata: {e}"

    tag = data.get("tag_name")
    url = data.get("html_url")
    if not tag:
        return None, None, "GitHub yaniti beklenmeyen formatta (tag_name eksik)"
    return tag.lstrip("vV"), url, None


def kontrol_et(kurulu_surum: str) -> SurumKontroluSonucu:
    try:
        _surum_tuple(kurulu_surum)
    except ValueError as e:
        return SurumKontroluSonucu(kurulu_surum, None, None, str(e), None)

    en_guncel, url, hata = en_guncel_surumu_getir()
    if hata:
        return SurumKontroluSonucu(kurulu_surum, None, None, hata, None)

    try:
        guncel_mi = _surum_tuple(kurulu_surum) >= _surum_tuple(en_guncel)
    except ValueError as e:
        return SurumKontroluSonucu(kurulu_surum, en_guncel, None, str(e), url)

    return SurumKontroluSonucu(kurulu_surum, en_guncel, guncel_mi, None, url)


def main() -> int:
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("--kurulu-surum", required=True, help="Su an kurulu olan surum (orn. 0.2.0)")
    ap.add_argument("--json", action="store_true")
    args = ap.parse_args()

    sonuc = kontrol_et(args.kurulu_surum)

    if args.json:
        print(json.dumps(sonuc.to_dict(), ensure_ascii=False, indent=2))
        return 0 if not sonuc.hata else 1

    if sonuc.hata:
        print(f"HATA: {sonuc.hata}", file=sys.stderr)
        return 1

    if sonuc.guncel_mi:
        print(f"Güncel. Kurulu sürüm ({sonuc.kurulu_surum}) en son Stable sürüme ({sonuc.en_guncel_surum}) eşit veya ondan yeni.")
    else:
        print(f"GÜNCELLEME MEVCUT: Kurulu sürüm {sonuc.kurulu_surum}, en son Stable sürüm {sonuc.en_guncel_surum}.")
        print(f"Release notları: {sonuc.release_url}")
        print("Güncellemek için (KENDİNİZ çalıştırın, otomatik yapılmaz):")
        print("  claude plugin update <plugin-adı>@turkiye-legal")

    return 0


if __name__ == "__main__":
    sys.exit(main())
