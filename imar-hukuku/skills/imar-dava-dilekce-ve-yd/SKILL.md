---
argument-hint: ''
description: İmar uyuşmazlığında iptal veya tam yargı dilekçesi, yürütmenin durdurulması
  talebi ya da idari başvuru/itiraz dilekçesi hazırlanacağında; vakıa-hukuki sebep-talep
  mimarisi ve YD koşulları sorulduğunda
name: imar-dava-dilekce-ve-yd
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İmar Davası Dilekçesi ve Yürütmenin Durdurulması

## Görev
İmar uyuşmazlığına uygun, İYUK formatında dava/başvuru dilekçesi üretmek; yürütmenin durdurulması talebini gerekçeli kurmak.

## Soğuk başlangıç (intake)
- Dava türü iptal mi, tam yargı mı, ikisi birlikte mi?
- Dava konusu işlem ve tarafları (davalı idare) net mi?
- Süre durumu uygun mu, YD talebi gerekiyor mu?
- Eldeki belgeler ve talep edilen sonuç (iptal/tazminat tutarı) ne?

## Denetim şeması
1. **Dava türü ve taraf (İYUK m.2)**: İptal davası (yetki-şekil-sebep-konu-maksat sakatlığı) mı, tam yargı (tazminat/el atma) mı belirlenir; davalı idare doğru gösterilir (işlemi tesis eden makam). Husumet hatası ret riskidir.
2. **Dilekçe mimarisi (İYUK m.3)**: Taraflar, konu, **tebliğ/öğrenme tarihi**, vakıalar (olay kronolojisi), hukuki sebepler (3194 ilgili maddeleri + İYUK + Anayasa m.35), deliller ve net **talep sonucu** (iptal / tazminat miktarı / YD). Her vakıa bir delile bağlanır.
3. **Yürütmenin durdurulması (İYUK m.27)**: İki koşul birlikte: **(a) işlemin açıkça hukuka aykırılığı ve (b) telafisi güç/imkânsız zarar.** Yıkım, inşaatın başlaması, parselin elden çıkması gibi geri dönülemez sonuçlar zarar koşulunu, üst plana/yönetmeliğe aykırılık hukuka aykırılık koşulunu somutlaştırır. Gerekçe iki koşulu da ayrı ayrı işlemelidir.
4. **İspat yükü kurgusu**: İşlemin hukuka uygunluğunu idare savunur; davacı sakatlığı ve menfaat ihlalini somut delille gösterir. Bilirkişi/keşif talebi dilekçede istenir.
5. **Yer tutucu disiplini**: Bilinmeyen veriler `[doldurulacak]` ile bırakılır; uydurma tarih/sayı/karar yazılmaz. İçtihat gerekiyorsa ilkesel atıf + `[DOĞRULANMADI]` ve karararama.danistay.gov.tr / kararlarbilgibankasi.anayasa.gov.tr kaynak notu.
6. **Ara sonuç**: Süre, husumet ve talep sonucu son kez kontrol edilir; harç/gider ve ekler listesi tamamlanır.

## Çıktı modülleri
- İYUK formatlı dava dilekçesi iskeleti (vakıa-sebep-talep).
- YD talebi gerekçe bloğu (iki koşul ayrı).
- Delil listesi ve bilirkişi/keşif talep paragrafı.
- Üst makama başvuru/itiraz dilekçesi alternatifi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

