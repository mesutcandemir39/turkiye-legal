---
argument-hint: ''
description: Kambiyo senedi alacak/borç ilişkisinde tahsil kabiliyetini, ceza riskini
  ve süreç seçeneklerini tartmak; müvekkile yön verecek strateji ve müvekkil/karşı
  taraf iletişimi gerektiğinde kullanılır.
name: risk-strateji-danismanlik
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
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Strateji

## Görev
Bir kambiyo senedi uyuşmazlığında müvekkilin (alacaklı veya borçlu) konumunu bütünsel tartmak; tahsil/ödeme, ceza riski, süre durumu ve uzlaşma seçeneklerini değerlendirip eyleme dönük strateji üretmek ve müvekkile sade dille aktarmak.

## Soğuk başlangıç (intake)
- Müvekkil alacaklı (hamil) mı, borçlu (keşideci/ciranta/avalist) mı?
- Senedin türü, bedeli, vade/ibraz durumu ve borçluların mali durumu nedir?
- Süreler ve def'iler bakımından zayıf/güçlü yönler neler?
- Müvekkilin önceliği hızlı tahsil mi, ceza baskısı mı, masrafı sınırlamak mı, uzlaşma mı?

## Denetim şeması
1. Hak envanteri: senet kambiyo vasfı, yetkili hamil, devir zinciri, def'i ve süre durumu — her biri için güçlü/zayıf değerlendirmesi yap (ilgili becerilere yolla).
2. Borçlu çevresi ve tahsil kabiliyeti: müteselsil borçlular (TTK m.724) içinde mali gücü olanı belirle; hacze elverişli malvarlığı araştırması (UYAP/tapu/araç) planla.
3. Çek özelinde ceza kaldıracı: karşılıksız çekte 5941 s. K. m.5 adli para cezası ve çek yasağı, ödeme/uzlaşma için baskı aracıdır; şikâyet süresi ve usulünü gözet.
4. Yol seçimi: kambiyo takibi (İİK m.167) hızlı ama itirazla karşılaşabilir; menfi tespit (İİK m.72) borçlu için tedbir gerektirir; sulh/protokolle yapılandırma masrafı düşürür.
5. Süre riski: zamanaşımı (TTK m.808/m.749) ve hak düşümü tarihlerini öne çıkar; gerekirse sebep alacağı planını hazır tut.
6. Ara sonuç: olasılık-maliyet-süre matrisiyle önerilen strateji ve alternatif planı belirle; karşı tarafa yapılacak bildirim/teklifin tonunu ayarla.

## Çıktı modülleri
- SWOT/risk matrisi (güçlü-zayıf yön, olasılık, tahsil kabiliyeti).
- Strateji ve aksiyon planı (öncelik sıralı, süre uyarılı).
- Müvekkile sade dilde bilgilendirme notu ve karşı tarafa ihtar/teklif taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

