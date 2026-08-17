---
argument-hint: ''
description: Birden fazla hukuki yorum veya yol mümkün olduğunda her seçeneği lehte-aleyhte
  tartıp olasılık diliyle gerekçeli bir nihai kanaat oluşturmak gerektiğinde kullanılır;
  mütalaanın sonuç bölümünü üretir.
name: seceneklerin-tartilmasi-ve-gorus
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Seçeneklerin Tartılması ve Gerekçeli Görüş

## Görev
Olası hukuki yorumları, talep yollarını veya stratejik seçenekleri karşılaştırmalı tartmak ve gerekçeli, olasılık diliyle ifade edilmiş bir nihai kanaat üretmek. Mütalaanın değeri "kesin" demesinde değil, belirsizliği dürüstçe derecelendirmesindedir.

## Soğuk başlangıç (intake)
- Kaç farklı hukuki yorum/yol var?
- Her yolun dayanağı (norm + içtihat) ne kadar güçlü?
- Müvekkilin önceliği ne? (Hız / maliyet / kesinlik / ilişkiyi koruma)
- Karşı tarafın muhtemel argümanı ne?

## Denetim şeması
1. Seçenekleri listele: Her hukuki yorum veya talep yolu (ör. sözleşmeye aykırılık tazminatı vs. haksız fiil; aynen ifa vs. dönme) ayrı başlık altında.
2. Lehte-aleyhte analiz: Her seçenek için dayanak normun gücü, içtihat desteği, ispat zorluğu, süre/zamanaşımı durumu ve karşı argümanlar tartılır.
3. Olasılık dili: Sonuç tek bir derecelendirmeyle ifade edilir — "kuvvetle muhtemel kabul edilir / tartışmalıdır, %50 civarı / zayıf ihtimaldir". Mutlak ifadeden kaçınılır; hâkimin takdir alanı belirtilir.
4. Yarışma ve seçimlik haklar: Birden çok talep yarışıyorsa (TBK'da sözleşme/haksız fiil yarışması, ayıpta seçimlik haklar) hangisinin müvekkil lehine olduğu gerekçelenir.
5. Gerekçeli kanaat: Mütalaa, hangi seçeneği neden önerdiğini açıkça yazar; aleyhe ihtimali gizlemez.
6. Ara sonuç: Önerilen yol + olasılık derecesi + temel gerekçe + alternatif yol notu.

## Çıktı modülleri
- Seçenek karşılaştırma tablosu (yol | dayanak gücü | ispat | risk | süre)
- Olasılık derecelendirmesi gerekçesiyle
- Gerekçeli nihai kanaat paragrafı
- "Şu koşulda tercih değişir" senaryo notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

