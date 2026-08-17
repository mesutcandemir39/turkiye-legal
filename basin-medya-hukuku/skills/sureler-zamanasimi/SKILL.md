---
argument-hint: ''
description: Basın-medya uyuşmazlıklarında cevap-düzeltme, şikâyet, dava açma ve tazminat
  zamanaşımı sürelerini doğru hesaplamak ve hak kaybını önlemek gerektiğinde kullanılır.
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı

## Görev
İlgili tüm süreleri (cevap-düzeltme, şikâyet, idari dava, tazminat zamanaşımı) tespit etmek, başlangıç anlarını belirlemek ve bir süre takvimi kurmak.

## Soğuk başlangıç (intake)
1. Yayın/ihlal tarihi tam olarak nedir?
2. Mağdur ihlali ve faili ne zaman öğrendi?
3. Hedeflenen yol nedir (düzeltme, şikâyet, tazminat, iptal)?
4. İhlal süregelen (online erişilebilir) nitelikte mi?

## Denetim şeması
1. **Cevap-düzeltme**: Basın Kanunu m.14 uyarınca yayından itibaren iki ay içinde sorumlu müdüre başvuru; reddi/ihmali hâlinde hâkimliğe başvuru süresi de kısadır ve hak düşürücüdür.
2. **Ceza şikâyeti**: Şikâyete bağlı suçlarda (örn. hakaret) şikâyet süresi, fiil ve failin öğrenilmesinden itibaren altı aydır (TCK m.73). Basın Kanunu m.26 basın suçlarında dava açma sürelerini özel düzenler.
3. **Haksız fiil/tazminat zamanaşımı**: TBK m.72 — zarar görenin zararı ve faili öğrendiği tarihten itibaren iki yıl, her hâlde fiilin işlenmesinden itibaren on yıl. Fiil aynı zamanda suç oluşturuyor ve ceza zamanaşımı daha uzunsa, o uzun süre tazminata da uygulanır.
4. **İdari dava**: RTÜK/BTK işlemlerine karşı iptal davası tebliğden itibaren altmış gün (İYUK m.7).
5. **Süregelen ihlal**: Online içerikte erişilebilirlik sürdükçe ihlalin sürdüğü ve zamanaşımının buna göre değerlendirileceği yaklaşımı dikkate alınır [ilkesel; Yargıtay içtihadı doğrulanacak].
6. **Ara sonuç**: Her yol için ayrı süre takvimi çıkarılır; en yakın süre öncelikli işaretlenir.

## Çıktı modülleri
- Süre takvimi tablosu (yol-süre-başlangıç-bitiş)
- Hak düşürücü/zamanaşımı ayrımı notu
- Acil aksiyon uyarı listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

