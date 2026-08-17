---
argument-hint: ''
description: Vasiyet ya da atama yokken kimin mirasçı olduğunu ve paylarını hesaplamak;
  eş ile zümrelerin birlikte mirasçılığı, halefiyet, evlatlık ve evlilik dışı çocuk
  durumları söz konusu olduğunda kullanılır.
name: yasal-mirascilik-zumre-ve-pay
turkiye_legal:
  attribution:
    license: Apache-2.0
    original_author: Mesut Can Demir
    original_repository: https://github.com/mesutcandemir39/turkiye-legal
  category: litigation
  inputs:
  - '[giriş tanımlanmadı — beceri gövdesinden çıkarılacak]'
  jurisdiction:
    country: TR
    legal_system: civil_law
    scope:
    - TR
  outputs:
  - '[çıktı tanımlanmadı — beceri gövdesinden çıkarılacak]'
  requires_human_review: false
  risk_level: medium
  sources:
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yasal Mirasçılık, Zümre Sistemi ve Pay Hesabı

## Görev
Ölüme bağlı geçerli bir tasarruf yoksa veya tasarruf terekenin bir kısmını kapsıyorsa, yasal mirasçıları ve paylarını TMK m.495-501 ve m.499 uyarınca kesin kesirlerle belirlemek.

## Soğuk başlangıç (intake)
- Mirasbırakanın altsoyu (çocuk, torun) var mı, hayatta mı?
- Sağ kalan eş var mı? Mal rejimi tasfiyesi yapıldı mı?
- Altsoy yoksa ana-baba veya kardeşler/yeğenler hayatta mı?
- Evlatlık, evlilik dışı (soybağı kurulu) çocuk var mı?
- Önceden ölen mirasçının yerine halefiyet (torunlar) söz konusu mu?

## Denetim şeması
1. **Mal rejimini önce tasfiye et.** Edinilmiş mallara katılmada sağ kalan eşin katılma alacağı (TMK m.236) terekeye dahil değildir; önce ayrılır, kalan tereke paylaşılır. Bu sıra atlanırsa pay hesabı yanlış çıkar.
2. **Zümreyi belirle.** Birinci zümre altsoy (m.495); yoksa ikinci zümre ana-baba ve altsoyu (m.496); yoksa üçüncü zümre büyük ana-baba ve altsoyu (m.497). Üst zümre varsa alt zümre mirasçı olamaz.
3. **Halefiyeti uygula (m.495/2, m.496/2).** Önceden ölen mirasçının payı kök içinde onun altsoyuna geçer (örn. ölen çocuğun payı torunlara eşit).
4. **Sağ kalan eşin payını ekle (m.499):** altsoyla 1/4, ikinci zümreyle 1/2, üçüncü zümreyle 3/4; üçüncü zümrede büyük ana-baba altsoyu yoksa eş tek başına mirasçı olur (m.499/4 sınırı).
5. **Özel durumlar:** evlatlık ve altsoyu mirasçıdır ama evlat edinenin mirasçısı olmaz (m.500); evlilik dışı çocuk soybağı kurulunca altsoy gibidir (m.498); mirasçı yoksa Devlet (m.501).
6. **Ara sonuç:** her mirasçının kesirli payını yaz; ispat için nüfus kaydı/vukuatlı aile belgesi ve soybağı kaydını dayanak göster (TMK m.6).

## Çıktı modülleri
- Kesirli pay tablosu (mal rejimi tasfiyesi ayrıştırılmış)
- Mirasçılık belgesi (veraset ilamı) talebi taslağı (TMK m.598)
- Halefiyet/kök şeması
- Eksik belge listesi (nüfus, soybağı, evlat edinme kararı)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

