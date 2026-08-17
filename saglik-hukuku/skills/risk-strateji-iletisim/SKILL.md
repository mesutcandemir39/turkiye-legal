---
argument-hint: ''
description: Tıbbi uyuşmazlıkta hekim, hastane veya hasta tarafının dava başarı şansını,
  risklerini ve müzakere/sulh seçeneklerini değerlendirmek ve müvekkile sade bir yol
  haritası sunmak için kullanılır.
name: risk-strateji-iletisim
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Mevcut delil ve hukuki duruma göre tarafın kazanma/kaybetme riskini değerlendirmek, dava-sulh-arabuluculuk seçeneklerini tartmak ve müvekkile anlaşılır bir strateji sunmak.

## Soğuk başlangıç (intake)
1. Temsil edilen taraf kim: hasta/yakını, hekim, hastane, sigorta?
2. Eldeki en güçlü ve en zayıf delil hangisi?
3. Tarafın önceliği: tazminat miktarı, hız, mesleki itibar, ceza riskini bertaraf?
4. Mesleki sorumluluk (zorunlu/ihtiyari) sigortası var mı?

## Denetim şeması
1. **Olgu-hukuk uyumu**: Sorumluluk unsurları (kusur, illiyet, zarar, onam) mevcut delille ne ölçüde karşılanıyor? Her unsur için güç skoru (zayıf/orta/güçlü).
2. **Karşı taraf senaryosu**: Komplikasyon savunması, müterafik kusur (TBK m.52), aydınlatmanın ispatı, zamanaşımı def'i gibi olası savunmalar öngörülür.
3. **Bilirkişi/ATK riski**: Sonuç büyük ölçüde rapora bağlı; rapor lehe/aleyhe çıkma olasılığı strateji belirler.
4. **Sigorta ve rücu**: Hekim mesleki sorumluluk sigortası, kamu hekiminde idarenin rücu riski (3359 Ek m.18) değerlendirilir.
5. **Çözüm yolu seçimi**: Dava, sulh, arabuluculuk; ceza riski varsa savunma stratejisiyle eşgüdüm. Maliyet-fayda ve süre karşılaştırması.
6. **Müvekkil iletişimi**: Sonuç olasılıkları abartısız ve sade dille; garanti verilmez, en iyi/orta/en kötü senaryo sunulur. Ara sonuç: önerilen yol ve gerekçesi.

## Çıktı modülleri
- Unsur bazlı güç skoru tablosu
- Senaryo analizi (en iyi/orta/en kötü)
- Strateji önerisi (dava/sulh/arabuluculuk)
- Müvekkile sade dilde özet ve yapılacaklar listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

