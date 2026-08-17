---
argument-hint: ''
description: Sözleşme uyuşmazlığında dava/sulh seçeneklerini tartmak, kazanma olasılığı
  ve maliyet-fayda analizini yapmak ve müvekkile anlaşılır bir yol haritası sunmak
  gerektiğinde kullanılır.
name: risk-strateji-ve-muvekkil-iletisimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
İsimli sözleşme uyuşmazlığında hukuki pozisyonu gerçekçi tartmak, dava/sulh/ihtar seçeneklerini maliyet-fayda ve süre ekseninde değerlendirmek, müvekkile sade ve dürüst bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (tahsil, tahliye, sözleşmeden kurtulma, ilişkiyi sürdürme)?
- Eldeki delillerin gücü ve karşı tarafın muhtemel savunması?
- Zaman baskısı (yakın süreler, ticari ihtiyaç)?
- Risk iştahı ve bütçe (harç, vekâlet ücreti, bilirkişi)?

## Denetim şeması
1. **Pozisyon analizi.** Maddi vakıaları hukuki unsurlarla altla; her unsur için delil gücünü (güçlü/zayıf/eksik) işaretle. Zayıf halka (ör. süresinde ihbar ispatı, kefalette şekil) belirginleştirilir.
2. **Senaryo matrisi.** En iyi/orta/en kötü sonuç; kazanma olasılığı kaba bant olarak (yüksek/orta/düşük) verilir, kesin oran vaadinden kaçınılır. Karşı dava/takas riski değerlendirilir.
3. **Maliyet-fayda.** Tahmini harç ve giderler, yargılama süresi (istinaf/temyiz dâhil), tahsil kabiliyeti (karşı tarafın ödeme gücü, İİK takip riski). Düşük tutarlı işte arabuluculuk/sulh önceliklenir.
4. **Süre ve usul riski.** Yakın zamanaşımı/hak düşürücü süre, dava şartı arabuluculuk eksikliği, görev-yetki hatası gibi usulden ret riskleri öne alınır.
5. **Strateji seçimi.** İhtar → arabuluculuk → dava sıralaması; ihtiyati tedbir/haciz (İİK m.257) gereği; delil tespiti ihtiyacı. Sulh için makul aralık ve müzakere kozları belirlenir.
6. **Müvekkil iletişimi.** Hukuki sonuç sade Türkçe ile, seçeneklerin artı/eksisi ve önerilen adım net olarak yazılır; varsayımlar ve `[DOĞRULANMADI]` veriler açıkça belirtilir, kesin kazanç taahhüdü verilmez. Ara sonuç: önerilen yol + gerekçe + sonraki adım listesi.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti.
- Müvekkile sade bilgilendirme notu ve aksiyon planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

