---
argument-hint: ''
description: Sigorta tazminatı, rücu veya zorunlu sigorta taleplerinde zamanaşımı
  süresinin hesaplanması, başlangıç anı, kesilme-durma ve uzamış ceza zamanaşımı tartışıldığında
  kullanılır; süre kaybı riskini önlem
name: zamanasimi-sureler
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
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı (Sigorta İstemleri)

## Görev
Sigorta sözleşmesinden ve zorunlu sigortalardan doğan istemlerin zamanaşımını doğru hesaplamak: süre, başlangıç anı, kesilme/durma ve uzamış ceza zamanaşımının uygulanıp uygulanmayacağı.

## Soğuk başlangıç (intake)
1. İstem türü ne: tazminat, prim, rücu, zorunlu trafik sigortası tazminatı?
2. Riziko/ödeme tarihi ve talep tarihi nedir?
3. Olay aynı zamanda suç oluşturuyor mu (ceza zamanaşımı?)
4. Daha önce başvuru/ihtar/dava ile süre kesildi mi?

## Denetim şeması
1. **Genel kural — TTK m.1420.** Sigorta sözleşmesinden doğan bütün istemler iki yılda; sigorta tazminatına/bedeline ilişkin istemler her halde rizikonun gerçekleştiği tarihten itibaren altı yılda zamanaşımına uğrar. Ara sonuç: hangi sürelerden hangisi önce dolar?
2. **Sorumluluk sigortaları.** Sorumluluk sigortalarında zarar görenin doğrudan talebi ve özel süreler; rücu istemlerinde başlangıç ödeme tarihidir.
3. **Zorunlu trafik sigortası — KTK m.109.** Kural iki yıl (zararın ve sorumlunun öğrenildiği tarihten) ve her halde kaza tarihinden sekiz yıl. **Uzamış ceza zamanaşımı:** fiil suç oluşturup TCK'da daha uzun zamanaşımı öngörülüyorsa o (daha uzun) süre tazminat istemi için de uygulanır (KTK m.109/3).
4. **Kesilme ve durma.** TBK m.154-158 ve m.153 (durma); sigortacıya başvuru, dava, tahkim başvurusu, borç ikrarı süreyi keser. İhtar tek başına kesmez; usulüne uygun talep gerekir.
5. **Hak düşürücü süreler.** Cayma için on beş gün (TTK m.1440), prim ihtar süresi (m.1434); bunlar zamanaşımından farklı, durmaz/kesilmez. İspat: zamanaşımı definin koşullarını ileri süren taraf.

## Çıktı modülleri
- İstem bazında zamanaşımı tablosu (süre / başlangıç / dolma tarihi).
- Uzamış ceza zamanaşımı değerlendirmesi (KTK m.109/3).
- Kesilme/durma olayları kronolojisi.
- Acil süre uyarısı ve önerilen koruyucu işlem (dava/başvuru).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

