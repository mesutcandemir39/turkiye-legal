---
argument-hint: ''
description: Riskli maddeler için somut düzeltme metni, alternatif lafız ve yedek
  (fallback) pozisyonlar üretip gerekçelendirmek gerektiğinde kullanılır.
name: redline-ve-alternatif-lafiz
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


# Redline ve Alternatif Lafız Üretimi

## Görev
Tespit edilen her riskli madde için "mevcut lafız → önerilen lafız → gerekçe (madde atfıyla)" üçlüsünü ve yedek pozisyonları üreterek müzakereye hazır redline metni oluşturmak.

## Soğuk başlangıç (intake)
- Hangi maddeler redline'a girecek (risk haritasından gelen öncelikli liste)?
- Müvekkilin ideal ve kabul edilebilir asgari pozisyonu ne (anchor + fallback)?
- Karşı tarafın metni değiştirme esnekliği ve pazarlık gücü ne?
- Üslup: agresif tam redline mi, dengeli "market standard" mı?

## Denetim şeması
1. **Önceliklendirme**: Deal-breaker maddeler tam yeniden yazılır; pazarlık maddelerine alternatif sunulur; kabul edilebilir maddelere yalnız not düşülür.
2. **Lafız tasarımı**: Her öneri için (a) mevcut metin, (b) önerilen metin, (c) gerekçe — emredici dayanak (TBK m.27, m.115, m.182) veya denge/menfaat gerekçesi. Belirsiz ifadeler ölçülebilir/tetikleyicili hale getirilir.
3. **Karşılıklılık enjeksiyonu**: Tek taraflı hak/yükümlülükler karşılıklı hale getirilir (fesih, ceza, gizlilik, tazminat).
4. **Yedek pozisyon (fallback)**: Her kritik talep için 1-2 kademeli geri çekilme lafzı (örn. sınırsız tavan → işlem bedeli tutarında tavan → 2 katı tavan).
5. **Tutarlılık denetimi**: Değiştirilen madde tanımlar, çapraz atıflar ve diğer maddelerle çelişmesin; "severability/bölünebilirlik" ve "tüm sözleşme" kayıtlarıyla uyum.
6. **Yer tutucu disiplini**: Bilinmeyen veriler (tutar, süre, taraf) `[doldurulacak]`; teyit gereken mevzuat/içtihat `[DOĞRULANMADI]` etiketiyle bırakılır, uydurulmaz.

## Çıktı modülleri
- Redline tablosu: madde / mevcut lafız / önerilen lafız / gerekçe / öncelik.
- Yedek pozisyon (fallback) basamakları.
- Markup'lı sözleşme metni veya değişiklik listesi (track-changes mantığı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

