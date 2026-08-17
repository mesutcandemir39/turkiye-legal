---
argument-hint: ''
description: Eldeki maddi olayın bir norma uyup uymadığını adım adım göstermek gerektiğinde;
  vakıaları norm unsurlarına yerleştirip gerekçeli bir hukuki sonuca varmak için kullanılır.
name: somut-olaya-uygulama-altlama
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Somut Olaya Uygulama (Altlama / Subsumption)

## Görev
Maddi olayı (küçük önerme) norm unsurlarına (büyük önerme) yerleştirerek, her unsuru ayrı ayrı denetleyip gerekçeli ve izlenebilir bir hukuki sonuç üretmek.

## Soğuk başlangıç (intake)
- Hukuken önemli vakıalar nelerdir; çekişmeli olan hangileri?
- Talep/iddianın dayandığı norm ve onun unsurları neler?
- Hangi unsur tartışmalı, hangisi açıkça sağlanmış?
- Karşı tarafın def'i/itirazı hangi unsuru hedefliyor?

## Denetim şeması
1. **Talep temelini bul** — "Kim kimden, neye dayanarak, ne istiyor?" Norm seçilir (örn. tazminat için TBK m.49; ifa için sözleşme + TBK m.112).
2. **Normu unsurlara ayır** — Hükmün her bir unsuru (örn. TBK m.49: fiil, hukuka aykırılık, kusur, zarar, illiyet bağı) liste hâline getirilir.
3. **Unsur-unsur altlama** — Her unsur için: ilgili vakıa + o unsurun sağlanıp sağlanmadığı + kısa gerekçe. Çekişmeli unsurda yorum/içtihat devreye sokulur; çekişmesiz unsur kısa geçilir.
4. **İspat yükü** — TMK m.6 / HMK m.190: her unsuru, lehine sonuç çıkaran taraf ispatlar. Karşı taraf, karşı vakıaları (def'i, itiraz) ispatla yükümlüdür. Unsur ispatlanamazsa o unsur "gerçekleşmemiş" sayılır.
5. **Karşı normlar** — Hak düşürücü/engelleyici/bozucu itirazlar (örn. zamanaşımı def'i, ifa, ibra) ayrı altlanır.
6. **Ara sonuç ve nihai sonuç** — Her unsur grubunda ara sonuç verilir; tüm unsurlar sağlanıyorsa talep haklı, biri eksikse reddedilir. Sonuç, TMK m.2 dürüstlük süzgecinden geçirilir.

## Çıktı modülleri
- Vakıa listesi (çekişmeli/çekişmesiz ayrımı).
- Norm + unsur tablosu.
- Unsur-unsur altlama (vakıa → değerlendirme → ara sonuç).
- İspat yükü dağılımı ve nihai sonuç.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

