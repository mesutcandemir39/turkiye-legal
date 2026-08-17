---
argument-hint: ''
description: Yönetim kurulu üyeleri, müdürler, kurucular veya denetçiler aleyhine
  kusurla verdikleri zarardan doğan hukuki sorumluluk, farklılaştırılmış teselsül,
  ibra ve zamanaşımı (TTK m.549-561) gündeme geldiği
name: yonetici-sorumlulugu-553
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
  version: 0.1.0
user-invocable: true
---


# Yönetici ve Kurucu Sorumluluğu (TTK m.553 vd.)

## Görev
Şirkete, pay sahiplerine veya alacaklılara verilen zarardan doğan yönetici/kurucu/denetçi sorumluluğunu unsurlarıyla kurmak veya savunmak; teselsül, ibra ve zamanaşımını işletmek.

## Soğuk başlangıç (intake)
1. Sorumlu tutulan kim (YK üyesi, müdür, kurucu, denetçi) ve hangi fiil?
2. Zarar kimde doğdu: şirkette mi (dolayısıyla pay sahibi/alacaklı), doğrudan pay sahibinde mi?
3. İhlal edilen yükümlülük hangi kanun/sözleşme hükmü; özen/bağlılık ihlali mi (m.369)?
4. İbra kararı var mı; kim, ne zaman, hangi kapsamda?
5. Zararı ve sorumluyu öğrenme tarihi; fiilden bu yana geçen süre?

## Denetim şeması
1. Sorumluluk halleri: kuruluş/sermaye taahhüt belgelerinin gerçeğe aykırılığı, sermaye hakkında yanlış beyan (m.549-551); m.553 genel hüküm — kurucular, YK üyeleri, yöneticiler ve tasfiye memurları kanun ve esas sözleşmeden doğan yükümlülüklerini kusurlarıyla ihlal ederlerse verdikleri zarardan sorumlu.
2. Unsurlar: (i) sıfat, (ii) yükümlülük ihlali (m.369 özen/bağlılık, m.375 devredilemez yetki, ilgili özel hüküm), (iii) kusur, (iv) zarar, (v) illiyet bağı. Kusursuzluğunu ispat eden sorumlu olmaz (m.553/3 — kontrol dışı sebep).
3. Davacı ve zarar türü: Şirket ve pay sahibi (dolayısıyla zararda tazminat şirkete ödenir, m.555); alacaklılar şirketin iflası halinde (m.556). Doğrudan zararda pay sahibi/alacaklı kendi adına.
4. Farklılaştırılmış teselsül: m.557 — birden çok kişi aynı zarardan sorumluysa, kusur ve durumun gereklerine göre teselsül; rücu m.557/2.
5. İbra ve dava: Genel kurul ibrası ibra edilen konularda dava hakkını düşürür (m.558); ibraya olumsuz oy veren/sonradan pay alan için m.558/2; dava açma kararı ve azlık m.559.
6. Zamanaşımı: m.560 — zararı ve sorumluyu öğrenmeden iki yıl, her hâlde fiilden beş yıl; fiil suç oluşturuyor ve TCK'da daha uzun zamanaşımı varsa o uygulanır.
7. Kamu alacağı paralel sorumluluk: VUK m.10, 6183 mük. m.35 (vergi/prim borçları) ayrıca değerlendirilir.

## Çıktı modülleri
- Sorumluluk unsur analizi ve kusur/illiyet değerlendirmesi.
- Sorumluluk davası dilekçesi veya savunma iskeleti (zamanaşımı/ibra def'ileri).
- Teselsül ve rücu haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

