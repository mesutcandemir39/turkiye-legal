---
argument-hint: ''
description: Marka hakkına tecavüz suçu (SMK m.30) ile FSEK telif suçlarında (m.71-72)
  şikâyet, uzlaşma, arama-el koyma ve adli süreç değerlendirmesi gerektiğinde kullanılır.
name: ceza-boyutu-marka-telif
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


# Ceza Boyutu (Marka ve Telif Suçları)

## Görev
Fikri-sınai tecavüzün ceza boyutunu (marka suçları SMK m.30, telif suçları FSEK m.71-72) şikâyet, soruşturma ve koruma tedbiri yönünden değerlendirmek.

## Soğuk başlangıç (intake)
- Tecavüz markaya mı yoksa telife mi ilişkin; hak tescilli mi?
- Taklit ürün üretimi/satışı/ithali var mı; ticari ölçek nedir?
- Şikâyet süresi içinde misiniz; uzlaşma kapsamı düşünüldü mü?
- Arama-el koyma için yeterli somut delil var mı?

## Denetim şeması
1. Marka suçları: SMK m.30 — taklit marka taşıyan ürünü üretmek, satmak, ithal/ihraç etmek, marka hakkına tecavüz suçtur. Suçun oluşması için markanın tescilli olması şarttır (SMK m.30/4). Şikâyete bağlıdır (m.30/5).
2. Telif suçları: FSEK m.71 — eseri izinsiz çoğaltma, yayma, umuma iletim, manevi haklara tecavüz; m.72 koruyucu programları etkisiz kılma. Şikâyet ve uzlaşma rejimi (CMK m.253) uygulanır.
3. Şikâyet: Suçlar takibi şikâyete bağlıdır; şikâyet süresi fiili ve faili öğrenmeden itibaren işler (TCK m.73 — 6 ay). Süre ve şikâyet hakkı sahipliği denetlenir.
4. Koruma tedbirleri: Arama ve el koyma CMK m.116 vd. ve m.127; taklit ürünlere el konulması. Hukuk davasındaki delil tespitinden ayrı, ceza muhakemesi disiplini geçerlidir.
5. İspat ve görev: Suçun sübutu ceza standardıyla (şüpheden sanık yararlanır); görevli mahkeme FSHM Ceza/asliye ceza. Bilirkişi taklit/iltibas tespiti yapar.
6. Ara sonuç: Ceza ve hukuk yolları paralel yürütülebilir; ceza davasındaki tespit hukuk davasında delil değeri taşır, ancak hukuk hâkimi bağlı değildir (HMK/maddî vakıa ayrımı).

## Çıktı modülleri
- Şikâyet dilekçesi iskeleti ve süre uyarısı.
- Arama-el koyma talep gerekçesi.
- Ceza-hukuk yolu koordinasyon notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

