---
argument-hint: ''
description: Bir kural veya uygulamanın Anayasa m.10 eşitlik ilkesine veya ayrımcılık
  yasağına aykırı olup olmadığını değerlendirmek; karşılaştırılabilir durum, farklı
  muamele ve haklı sebep analizinin gerektiği h
name: esitlik-ve-ayrimcilik
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eşitlik İlkesi ve Ayrımcılık Yasağı

## Görev
Bir norm veya uygulamanın Anayasa m.10 (kanun önünde eşitlik) ve m.13 ile birlikte ayrımcılık yasağına uygunluğunu denetlemek; eşit olanlara eşit, farklı olanlara farklı muamele mantığını somut olaya uygulamak.

## Soğuk başlangıç (intake)
1. Şikâyet konusu farklı muamele kim/hangi grup arasında yapılıyor?
2. Karşılaştırılan durumlar gerçekten benzer (karşılaştırılabilir) mi?
3. Farklı muamelenin dayandığı ölçüt ne (cinsiyet, yaş, statü, ekonomik durum)?
4. Bu ölçüt, AİHS Ek 12 No.lu Protokol / AİHS m.14 kapsamında şüpheli bir kategori mi?

## Denetim şeması
1. **Karşılaştırılabilirlik.** İki durum/grup hukuken benzer konumda mı? Benzer değillerse eşitlik ihlali kural olarak doğmaz; farklı muamele meşru olabilir.
2. **Farklı muamele tespiti.** Aynı durumdakilere farklı, farklı durumdakilere aynı muamele var mı? Doğrudan ve dolaylı ayrımcılık ayrımını gözetin.
3. **Haklı sebep testi.** Farklı muamelenin objektif ve makul bir dayanağı var mı, meşru bir amaca yöneliyor mu? (m.10 ile m.13 birlikte). Ara sonuç: haklı sebep yoksa ayrımcılık vardır.
4. **Ölçülülük.** Haklı sebep varsa dahi, kullanılan ayrım aracı ile amaç arasında orantı bulunmalı; aşırı ya da gereksiz farklılaştırma aykırıdır.
5. **Şüpheli kategoriler.** Cinsiyet, ırk, din gibi ölçütlerde daha sıkı denetim uygulanır; kamu makamının ispat yükü ağırlaşır.
İspat: farklı muameleyi başvurucu gösterir; bunun haklı ve orantılı olduğunu kamu makamı temellendirir. AYM ve AİHM eşitlik içtihadına ilke düzeyinde atıf yapın, künyeyi `[DOĞRULANMADI]` işaretleyin.

## Çıktı modülleri
- Karşılaştırma matrisi (gruplar, muamele farkı, ölçüt, haklı sebep değerlendirmesi).
- Doğrudan/dolaylı ayrımcılık nitelendirmesi ve sonuç.
- Norm denetimi veya bireysel başvuru için eşitlik gerekçesi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

