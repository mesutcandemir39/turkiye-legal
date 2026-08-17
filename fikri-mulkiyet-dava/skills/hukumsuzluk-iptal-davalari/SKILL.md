---
argument-hint: ''
description: Bir marka, patent veya tasarımın geçersiz kılınması (hükümsüzlük) yahut
  markanın kullanılmama/jenerikleşme nedeniyle iptali iddialarında şartları ve idari/adli
  yol ayrımını değerlendirmek gerektiğinde
name: hukumsuzluk-iptal-davalari
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hükümsüzlük ve İptal Davaları

## Görev
Tescilli bir hakkın hükümsüzlüğü veya iptali talebini, sebep ve usul yönünden SMK çerçevesinde denetlemek; idari iptal yetkisi geçişini gözetmek.

## Soğuk başlangıç (intake)
- Hangi hak hedefleniyor (marka, patent, tasarım) ve tescil no nedir?
- Sebep mutlak/nispi ret sebebi mi, kullanmama mı, yenilik eksikliği mi?
- Davacının menfaati/sıfatı var mı; nispi sebepte itiraz/önceki hak sahipliği var mı?
- Hak kaç yıldır tescilli; sessiz kalma yoluyla hak kaybı (m.25/6) gündemde mi?

## Denetim şeması
1. Marka hükümsüzlüğü: Mutlak ret sebepleri (SMK m.5) ve nispi ret sebepleri (m.6) hükümsüzlük sebebidir (m.25). Menfaati olanlar dava açabilir; nispi sebeplerde önceki hak sahibi. Sessiz kalma (m.25/6 — 5 yıl) ve kötüniyet istisnası tartılır.
2. Marka iptali: Kullanmama (m.9 — kesintisiz 5 yıl ciddi kullanmama), jenerik hâle gelme, yanıltıcılık (m.26). İptal yetkisi geçiş süreciyle TÜRKPATENT'e bırakılmıştır (m.26 ve geçici m.4); bu süreçte idari/adli yol doğru seçilir.
3. Patent hükümsüzlüğü: Patentlenebilirlik şartlarının yokluğu, yetersiz açıklama, kapsam aşımı, gerçek hak sahipliği (SMK m.138). Tekniğin bilinen durumu delili.
4. Tasarım hükümsüzlüğü: Yenilik ve ayırt edici nitelik eksikliği, kamu düzeni, hak sahipliği (SMK m.77). Önceki tasarım/yayın delili.
5. İspat ve etki: Hükümsüzlük sebebini ileri süren ispatla yükümlü (HMK m.190). Hükümsüzlük kararı geçmişe etkilidir (SMK m.157/ilgili hükümler), iptal kural olarak ileriye etkili (m.27).
6. Ara sonuç: Hükümsüzlük genellikle tecavüz davasına karşı def'i veya karşı dava olarak gelir; süre, sıfat ve idari aşama tamamlanmadan dava reddi riski izlenir.

## Çıktı modülleri
- Hükümsüzlük/iptal sebebi haritası (madde atıflı).
- İdari (TÜRKPATENT) - adli yol seçim notu.
- Sıfat, süre ve sessiz kalma kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

