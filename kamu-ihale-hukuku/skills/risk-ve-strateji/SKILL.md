---
argument-hint: ''
description: İstekli ya da idare adına bir ihale uyuşmazlığında başvuru/dava yoluna
  gitmenin başarı şansını, maliyetini ve alternatif çözümlerini tartmak; strateji
  ve öncelik belirlemek için kullanılır.
name: risk-ve-strateji
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Strateji

## Görev
İhale uyuşmazlığında müvekkilin (istekli veya idare) konumunu, başvuru/dava yolunun başarı olasılığını, maliyet ve sürelerini değerlendirip uygulanabilir bir strateji önerisi sunmak.

## Soğuk başlangıç (intake)
1. Müvekkil kim: istekli mi, idare mi, alt yüklenici mi?
2. Hedef ne: ihaleyi kazanmak, kararı iptal ettirmek, zarar tazmini, yasaklamadan kurtulmak?
3. Süre durumu: başvuru/dava süresi açık mı, sıkışık mı?
4. İhale ekonomik olarak hâlâ değerli mi; sözleşme imzalandı mı?

## Denetim şeması
1. **Pozisyon tespiti:** İddianın hukuki gücü, yerleşik KİK/Danıştay içtihadıyla uyumu ve karşı argümanlar değerlendirilir. Süre uygunluğu ilk filtredir; süre kaçmışsa esasa girilmez.
2. **Yol seçimi:** Şikâyet-itirazen şikâyet zorunlu yoldur; bu yol tüketilmeden iptal davası açılamaz. Düzeltici işlem mi, iptal mi, tam yargı mı hedefleniyor netleştirilir.
3. **Maliyet-fayda:** İtirazen şikâyet başvuru bedeli, dava harç/masrafları, vekâlet ücreti riski ile beklenen kazanç (ihale bedeli, kâr) karşılaştırılır. Düşük katma değerli ihalede agresif strateji önerilmez.
4. **Zaman riski:** Sözleşme imzalanmışsa düzeltici işlem fiilen sonuçsuz kalabilir; bu durumda tam yargı (zarar) yoluna ağırlık verilir.
5. **Alternatifler:** Bir sonraki ihaleye odaklanma, idareyle uyumlu çözüm, yasaklamada savunma stratejisi gibi seçenekler tartılır.
6. **Ara sonuç:** Önerilen yol, gerekçesi, başarı tahmini (yüksek/orta/düşük) ve eylem sırası verilir.

İspat yükü: Strateji, mevcut delil gücüne göre kalibre edilir.

## Çıktı modülleri
- SWOT benzeri pozisyon tablosu (güçlü/zayıf iddialar).
- Yol seçeneği karşılaştırma matrisi (süre/maliyet/şans).
- Önerilen strateji ve aksiyon sırası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

