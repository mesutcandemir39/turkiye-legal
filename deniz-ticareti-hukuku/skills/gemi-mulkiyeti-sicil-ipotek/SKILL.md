---
argument-hint: ''
description: Gemi alım-satımı, gemi siciline tescil, gemi mülkiyetinin devri ve gemi
  ipoteği/kanuni rehin hakları söz konusu olduğunda; geminin ayni hak durumunu, takyidatları
  ve finansman teminatını incelemek içi
name: gemi-mulkiyeti-sicil-ipotek
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gemi Mülkiyeti, Sicil ve Gemi İpoteği

## Görev
Geminin ayni hak durumunu (mülkiyet, ipotek, kanuni rehin, haciz şerhi) tespit etmek; mülkiyet devri ve ipotek tesisi işlemlerini denetlemek; finansman ve teminat yapısını kurmak veya zayıflıklarını saptamak.

## Soğuk başlangıç (intake)
- Gemi Türk Gemi Siciline mi yoksa yabancı sicile mi kayıtlı; bayrağı nedir?
- İşlem bir satış mı, ipotek tesisi mi, yoksa takyidat tespiti mi?
- Gemi üzerinde mevcut ipotek, kanuni rehin (gemi alacaklısı hakkı) veya ihtiyati haciz var mı?
- Banka/finansör kim; teminat kapsamı (navlun, sigorta tazminatı) genişletildi mi?

## Denetim şeması
1. **Sicil durumu**: Geminin tescilli olup olmadığını belirle (TTK m.954 vd.). Tescilli gemilerde mülkiyet ve ipotek tapu benzeri sicil ilkelerine tabidir; sicil kaydını ve şerhleri çıkar.
2. **Mülkiyetin devri**: Tescilli gemide mülkiyet devri için yazılı sözleşme ve sicile tescil aranır; tescilsiz gemide zilyetliğin devri esas alınır. Devirde geminin yük ve navlun üzerindeki ilişkilerini ayrıca değerlendir.
3. **Gemi ipoteği**: İpotek ancak tescilli gemi üzerinde, sicile tescille kurulur (TTK m.1014 vd.). İpoteğin kapsamı, derecesi, sabit/üst sınır ipoteği ayrımı ve eklentilere (sigorta tazminatı, navlun) sirayetini denetle.
4. **Kanuni rehin / gemi alacaklısı hakkı**: TTK m.1320 vd. kapsamındaki gemi alacaklısı haklarının ipotekten önce mi sonra mı geldiğini belirle; bu haklar genellikle ipoteğe öncelikli olabilir — teminat değerlemesinde kritik.
5. **İspat ve ara sonuç**: Sicil kaydı ayni hak durumunun temel delilidir; iyiniyetli üçüncü kişinin sicile güveni korunur. Çıktıda takyidat sırasını ve teminatın gerçek değerini gerekçeli olarak ortaya koy.

## Çıktı modülleri
- Sicil/takyidat özeti ve rehin sırası tablosu
- Mülkiyet devri veya ipotek tesisi adım listesi
- Teminat zayıflığı/risk notu ve finansör tavsiyesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

