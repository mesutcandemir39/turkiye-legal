---
argument-hint: ''
description: Tıbbi sorumluluk talebinde hangi zamanaşımı süresinin (sözleşme, haksız
  fiil, idari, cezai) işlediğini ve başlangıç anını hesaplamak için kullanılır; rejim
  seçiminin tazminat hakkına etkisini ortaya k
name: sureler-zamanasimi
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


# Süreler ve Zamanaşımı

## Görev
Talebin hangi zamanaşımına tabi olduğunu, sürelerin başlangıç anını ve kesilme/durma hâllerini hesaplamak; en lehe rejimi tespit etmek.

## Soğuk başlangıç (intake)
1. Hukuki sebep sözleşme mi, haksız fiil mi, idari mi, cezai mi?
2. Zararın ve failin öğrenildiği tarih nedir?
3. Olay üzerinden kaç yıl geçti?
4. Daha ağır cezayı gerektiren bir suç söz konusu mu (ceza zamanaşımı)?

## Denetim şeması
1. **Sözleşmesel sorumluluk (vekâlet)**: Kural olarak TBK m.146 — 10 yıllık genel zamanaşımı. Sözleşme rejimi davacı için süre avantajı sağlar.
2. **Haksız fiil**: TBK m.72 — fiil ve failin öğrenilmesinden itibaren 2 yıl, her hâlde 10 yıl. Fiil aynı zamanda suç ise daha uzun ceza zamanaşımı uygulanır (uzamış zamanaşımı).
3. **İdari (tam yargı)**: İYUK m.13 — zararın öğrenilmesinden itibaren 1 yıl ve her hâlde olaydan itibaren 5 yıl içinde idareye başvuru; dava süreleri İYUK m.7.
4. **Cezai**: Dava zamanaşımı TCK m.66; taksirle öldürme/yaralamada suçun cezasına göre değişir. Şikâyete bağlı yaralamada TCK m.73 — 6 ay şikâyet süresi.
5. **Başlangıç anı sorunu**: Geç ortaya çıkan zararlarda (gizli sakatlık) öğrenme anı kritiktir; objektif öğrenme aranır.
6. **Ara sonuç**: Birden çok rejim varsa davacı için en uzun olan seçilir; zamanaşımı def'i karşı tarafça ileri sürülmedikçe re'sen dikkate alınmaz.

## Çıktı modülleri
- Rejim bazlı zamanaşımı tablosu (süre + başlangıç)
- En lehe süre seçimi gerekçesi
- Kesilme/durma ve başvuru takvimi
- Süre riski uyarısı (kritik tarih)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

