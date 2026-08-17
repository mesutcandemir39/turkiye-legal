---
argument-hint: ''
description: Sözleşmenin tamamını tarayıp her riskli maddeyi olasılık-etki ve deal-breaker/pazarlık/kabul
  edilebilir olarak etiketleyen yapılandırılmış bir risk tablosu üretmek gerektiğinde
  kullanılır.
name: risk-haritasi-ve-skorlama
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


# Madde Madde Risk Haritası ve Skorlama

## Görev
Sözleşmeyi baştan sona tarayarak müvekkil aleyhine her kaydı tespit etmek, olasılık ve etki üzerinden skorlamak ve önceliklendirilmiş bir risk tablosu çıkarmak.

## Soğuk başlangıç (intake)
- Müvekkilin işlemden beklediği temel menfaat ve kabul edemeyeceği "kırmızı çizgiler" neler?
- İşlem hacmi/tutarı ve sürekliliği nedir (etki ağırlığı için)?
- Karşı tarafın pazarlık gücü ve metni değiştirme esnekliği var mı?
- Acil/zaman baskısı veya sektörel zorunluluk var mı?

## Denetim şeması
1. **Tarama eksenleri**: (a) Edim-bedel dengesi, (b) sorumluluk/tazminat dağılımı (TBK m.112, m.115), (c) fesih/dönme hakları (m.125), (d) cezai şart (m.179), (e) süre/yenileme, (f) gizlilik/rekabet yasağı, (g) uyuşmazlık/yetki (HMK m.17), (h) mücbir sebep ve uyarlama (m.138).
2. **Asimetri testi**: Her hak/yükümlülük için "karşı tarafta da var mı?" sorulur; tek taraflı fesih, tek taraflı cezai şart, tek taraflı değişiklik yetkisi (m.24) işaretlenir.
3. **Skorlama**: Olasılık (riskin gerçekleşme ihtimali) × Etki (parasal + operasyonel + itibari) = risk düzeyi. Etiket: **Deal-breaker** (imzalanamaz), **Pazarlık** (redline şart), **Kabul edilebilir** (not düşülür).
4. **Emredici filtre**: Geçersiz kayıtlar (TBK m.27, m.115) ayrı "lehe risk" olarak işaretlenir — karşı tarafın dayanağı çökebilir.
5. **İspat/uygulanabilirlik**: Madde teoride lehe ama ispatı/icrası zor mu (belirsiz tetikleyici, ölçülemez ceza)?
6. **Ara sonuç**: Önceliklendirilmiş risk tablosu ve redline'a taşınacak maddeler.

## Çıktı modülleri
- Madde / risk / olasılık-etki / etiket / öneri sütunlu risk tablosu (Excel'lenebilir).
- Deal-breaker özeti ve karar notu.
- Müvekkile tek sayfalık risk skoru özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

