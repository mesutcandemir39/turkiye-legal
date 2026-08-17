---
argument-hint: ''
description: Yayın öncesi hukuki risk denetimi, müvekkilin medya kuruluşu veya mağdur
  olmasına göre strateji ve müzakere-sulh seçeneklerini değerlendirmek gerektiğinde
  kullanılır.
name: risk-strateji-medya
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Yönetimi ve Strateji

## Görev
Yayın öncesi/sonrası hukuki riski haritalamak, müvekkilin konumuna (yayıncı/mağdur) göre strateji belirlemek, sulh ve müzakere ile dava arasında seçim yapmak.

## Soğuk başlangıç (intake)
1. Müvekkil yayıncı/medya kuruluşu mu, mağdur mu?
2. Yayın henüz yapılmadı mı (önleyici denetim), yapıldı mı (zarar yönetimi)?
3. Hedef: itibar onarımı, tazminat, içeriğin kaldırılması, yargısal zafer?
4. Kamuoyu/medya etkisi (Streisand etkisi) riski var mı?

## Denetim şeması
1. **Yayıncı tarafı (önleyici)**: Yayın öncesi gerçeklik, kaynak güvenilirliği, kamu yararı, öz-biçim dengesi ve KVKK uyumu denetlenir. Riskli ifadeler için değer yargısı/maddi vakıa ayrımı netleştirilir, hukuka uygunluk dayanağı belgelenir.
2. **Mağdur tarafı**: Yol kombinasyonu seçilir (cevap-düzeltme + içerik kaldırma + tazminat + ceza şikâyeti). Hızlı sonuç için 5651 m.9 ve cevap-düzeltme; tatmin için tazminat önceliklenir.
3. **Sulh-müzakere**: Özür/düzeltme yayımı, içeriğin çıkarılması ve makul tazminatla erken çözüm değerlendirilir; özellikle Streisand etkisi riskinde dava maliyeti tartılır.
4. **Maliyet-fayda**: Yargılama süresi, ispat zorluğu, tazminat takdir aralığı ve itibar etkisi birlikte değerlendirilir.
5. **Ara sonuç**: Konuma göre öncelikli yol ve yedek plan belirlenir; süre disiplini korunur.

## Çıktı modülleri
- Risk haritası (olasılık/etki)
- Yayıncı için yayın öncesi kontrol listesi
- Strateji seçenekleri ve sulh-müzakere notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

