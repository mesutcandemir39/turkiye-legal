---
argument-hint: ''
description: Bir ilamlı veya ilamsız icra takibinin aşamasını, itiraz/itirazın iptali
  sürelerini, haciz ve satış adımlarını izlemek gerektiğinde kullan.
name: icra-ve-takip-dosyasi-takibi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İcra ve Takip Dosyası Takibi

## Görev
İcra takip dosyasının türünü, aşamasını ve kritik sürelerini izleyip haciz-satış-paraya çevirme zincirini takip etmek; itiraz ve süre kaynaklı hak kayıplarını önlemek.

## Soğuk başlangıç (intake)
- Takip türü ne: ilamlı, ilamsız, kambiyo senetlerine özgü, rehnin paraya çevrilmesi?
- Ödeme/icra emri tebliğ edildi mi, tarihi ne?
- Borçlu itiraz etti mi, ettiyse hangi tarihte?
- Haciz uygulandı mı, satış aşamasına gelindi mi?

## Denetim şeması
1. Tür ve aşama: ilamsız takipte ödeme emrine itiraz 7 gün (İİK m.62) → itiraz takibi durdurur → alacaklı itirazın iptali (İİK m.67, 1 yıl) ya da itirazın kaldırılması (İİK m.68) yoluna gider. Kambiyo takibinde itiraz 5 gün ve icra mahkemesine (İİK m.168, m.170).
2. İlamlı takip: ilama dayalı takipte icranın geri bırakılması (İİK m.33) dışında itirazla durmaz; tehir-i icra şartlarını kontrol et.
3. Haciz-satış zinciri: haciz talebi süresi (İİK m.78, ödeme emrinin kesinleşmesinden itibaren), satış isteme süresi (İİK m.106) ve düşme riski (İİK m.110); kıymet takdiri ve satış ilanı.
4. İstihkak ve şikâyet: üçüncü kişi istihkak iddiası (İİK m.96 vd.), icra memuru işlemine şikâyet (İİK m.16, kural 7 gün).
5. Ara sonuç: takibin kesinleşip kesinleşmediği, açık süreler ve sıradaki adım. Tarihler ve tutarlar yalnızca takip dosyasından alınır.

## Çıktı modülleri
- Takip aşaması ve süre takvimi tablosu.
- İtiraz/itirazın iptali/kaldırılması karar ağacı notu.
- Haciz-satış adım takibi ve düşme riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

