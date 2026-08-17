---
argument-hint: ''
description: Zarar sigortacısının ödediği tazminat için zarar veren üçüncü kişiye
  veya kusurlu sigortalıya başvurması (rücu) söz konusu olduğunda kullanılır; halefiyetin
  şartları, kapsamı ve sınırlarını denetler.
name: halefiyet-rucu
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


# Halefiyet ve Rücu (Sigortacının Geri Alım Hakkı)

## Görev
Tazminatı ödeyen zarar sigortacısının, sigortalının üçüncü kişiye karşı haklarına halef olarak rücu edip edemeyeceğini; zorunlu sorumluluk sigortalarında sigortalıya/işletene rücu şartlarını belirlemek.

## Soğuk başlangıç (intake)
1. Hangi sigortacı kime ödeme yaptı, ne kadar?
2. Zarara kim sebep oldu (üçüncü kişi, karşı taraf sürücüsü/işleteni)?
3. Rücu zarar sigortasından mı doğuyor yoksa zorunlu sorumluluk sigortasından mı?
4. Sigortalının zarar verene karşı talep hakkı mevcut/sona ermiş mi?

## Denetim şeması
1. **Halefiyetin doğumu.** TTK m.1472: zarar sigortacısı, ödediği tazminat tutarınca hukuken sigortalının yerine geçer; sigortalının zarardan sorumlu üçüncü kişilere karşı taleplerine halef olur. Ödeme yapılmadan halefiyet doğmaz. Ara sonuç: ödeme gerçekleşti mi?
2. **Kapsam ve sınır.** Halefiyet, ödenen tazminatla sınırlıdır ve sigortalının hakkından fazlasını içermez. Sigortalının dava/zamanaşımı durumu sigortacıya geçer (mevcut hakkın devri mantığı).
3. **Aile/birlikte yaşayan istisnası.** TTK m.1472/2: sigortalı ile birlikte yaşayan ve hareketlerinden sorumlu olduğu kişilere, kasıt yoksa rücu edilemez.
4. **Zorunlu sorumluluk sigortasında rücu.** Karayolları Motorlu Araçlar Zorunlu Mali Sorumluluk Sigortası Genel Şartları (alkol, ehliyetsizlik, çalınan araç, sürat vb. sayılı haller) ve KTK m.95 çerçevesinde sigortacı, zarar görene ödediği tazminatı kusurlu sigortalıya/işletene rücu edebilir. İstisnalar sınırlı ve dar yorumlanır.
5. **Zamanaşımı.** Rücu talebi, sigortacının ödeme yaptığı tarihten itibaren işler (TTK m.1420 ve ilgili özel süreler); zorunlu sigortalarda KTK m.109 dikkate alınır.

## Çıktı modülleri
- Rücu hukuki dayanağı (TTK m.1472 / KTK m.95 / genel şart maddesi).
- Rücu edilebilir tutar ve muhatap.
- İstisna/sınır değerlendirmesi (aile, kusur derecesi).
- Zamanaşımı başlangıç tarihi ve dava planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

