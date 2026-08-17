---
argument-hint: ''
description: Avalin geçerlilik şartlarını, avalistin sorumluluk kapsamını ve kambiyo
  borçlularının müteselsil sorumluluğunu çözümlemek; teminat ve borçlu çevresi analizi
  gerektiğinde kullanılır.
name: aval-musteselsil-sorumluluk
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
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aval ve Müteselsil Sorumluluk

## Görev
Senet borcuna kefil niteliğindeki aval ilişkisini denetlemek, avalistin kime ve hangi kapsamda sorumlu olduğunu belirlemek; tüm kambiyo borçlularının hamile karşı müteselsil sorumluluğunu çözümlemek.

## Soğuk başlangıç (intake)
- Senet üzerinde aval kaydı ("aval içindir", "kefil") veya senet yüzünde sadece imza var mı?
- Aval kimin için verilmiş; belirtilmemişse kimin lehine sayılır?
- Müvekkil avalist mi, yoksa avalistten talep eden hamil mi?
- Borçlu çevresi (düzenleyen, cirantalar, kabul eden) çıkarıldı mı?

## Denetim şeması
1. Aval şekli: TTK m.700 — aval senet üzerine/alonja "aval içindir" benzeri ibare ve imzayla verilir; poliçe yüzündeki keşideci ve muhatap dışındaki salt imza aval sayılır.
2. Kimin için: aval kimin için verildiği yazılmamışsa poliçede keşideci, bonoda düzenleyen lehine verilmiş sayılır (m.700/4).
3. Sorumluluğun kapsamı: avalist, lehine aval verdiği kişiyle aynı derecede sorumludur (TTK m.702/1). Aval, kefaletten farklı olarak fer'i değildir; lehine aval verilenin taahhüdü şekil dışında bir sebeple geçersiz olsa da aval geçerli kalır (m.702/2 — bağımsızlık).
4. Rücu: ödeyen avalist, lehine aval verdiği kişiye ve ona karşı sorumlu olanlara rücu eder (m.702/3).
5. Müteselsil sorumluluk: düzenleyen, kabul eden, cirantalar ve avalistler hamile karşı müteselsilen sorumludur; hamil sıraya bakmaksızın her birine başvurabilir (TTK m.724). Ödeyen borçlu kendinden önceki borçlulara müracaat eder.
6. Ara sonuç: aval geçerliyse avalist asıl borçlu gibi takip edilebilir; aval lehtarının belirsizliği veya şekil eksikliği halinde sorumluluk yeniden değerlendirilir.

## Çıktı modülleri
- Borçlu çevresi ve sorumluluk haritası (kim-kime-müteselsil).
- Aval geçerlilik ve kapsam notu (m.700-702 dayanaklı).
- Avalist için savunma / hamile karşı talep stratejisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

