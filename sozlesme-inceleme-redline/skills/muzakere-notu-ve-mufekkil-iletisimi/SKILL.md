---
argument-hint: ''
description: İnceleme bulgularını önceliklendirilmiş bir müzakere stratejisine ve
  müvekkilin anlayacağı sade bir özete dönüştürmek gerektiğinde kullanılır.
name: muzakere-notu-ve-mufekkil-iletisimi
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


# Müzakere Notu ve Müvekkil İletişimi

## Görev
Madde madde inceleme ve redline çıktısını, önceliklendirilmiş bir müzakere stratejisine ve müvekkile sunulacak sade, karar verdirici bir özete dönüştürmek.

## Soğuk başlangıç (intake)
- Müvekkilin işlemden ana hedefi ve risk iştahı ne?
- Müzakerede pazarlık gücü kimde; zaman baskısı var mı?
- Hangi talepler "olmazsa olmaz", hangileri "isterse" düzeyinde?
- Müvekkilin teknik hukuk bilgisi ne düzeyde (dil sadeliği için)?

## Denetim şeması
1. **Öncelik matrisi**: Bulgular "deal-breaker / yüksek öncelik pazarlık / düşük öncelik / kabul" olarak sıralanır; her birine anchor ve fallback bağlanır.
2. **Taviz haritası**: Müvekkilin verebileceği tavizler ile karşılığında alınacak kazanımlar eşleştirilir (paket pazarlık mantığı).
3. **Gerekçe zırhı**: Her talep için müzakere masasında kullanılacak gerekçe — emredici dayanak (TBK m.27, m.115, m.182), "market standard" veya karşılıklılık argümanı.
4. **Risk-karar bağlama**: Müvekkile her kritik madde için "kabul edersen şu risk, reddedersen şu sonuç" netliğiyle karar seçeneği sunulur.
5. **Sade dil süzgeci**: Hukuki doğruluk korunarak teknik terimler açıklanır; tablo ve madde işaretleriyle özetlenir.
6. **İmza öncesi kontrol**: Son metin değişiklikleri, açık kalan `[doldurulacak]` alanlar, vekâlet/yetki teyidi ve nüsha düzeni hatırlatılır.

## Çıktı modülleri
- Önceliklendirilmiş müzakere notu (talep / gerekçe / fallback / öncelik).
- Müvekkile tek sayfalık sade özet ve karar seçenekleri.
- İmza öncesi son kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

