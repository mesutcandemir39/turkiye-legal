---
argument-hint: ''
description: Bir kişinin başkası adına işlem yaptığı, temsil yetkisinin varlığı/kapsamı
  tartışmalı olduğu veya yetkisiz temsil ile yapılan işlemin akıbeti sorulduğunda
  kullanılır.
name: temsil-ve-yetkisiz-temsil
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


# Temsil ve Yetkisiz Temsil

## Görev
Bir işlemin temsilci eliyle geçerli yapılıp yapılmadığını, yetkinin kapsamını ve yetkisiz temsilde işlemin akıbetini belirlemek.

## Soğuk başlangıç (intake)
- İşlemi yapan kişi kimin adına ve hangi yetkiyle hareket etti?
- Temsil yetkisi nasıl verildi (vekâletname, ticari temsil, kanun)?
- Yetki işlem anında mevcut, kapsamı yeterli miydi; sonradan sona ermiş mi?
- Karşı taraf temsilcinin yetkisine iyiniyetle güvendi mi?

## Denetim şeması
1. Doğrudan/dolaylı temsil: TBK m.40 — doğrudan temsilde hukuki sonuçlar temsil olunana ait olur; temsilcinin başkası adına hareket ettiğini bildirmesi veya karşı tarafça anlaşılması gerekir.
2. Yetkinin kaynağı ve kapsamı: İradi temsilde yetki belgesi/vekâletname; kapsam yorumu dar/geniş. Olağan işler için verilen yetki olağanüstü tasarrufları (bağışlama, kefalet, taşınmaz devri) kapsamaz — özel yetki gerekir.
3. Yetkinin sona ermesi: m.42-45 — azil, istifa, ölüme/ehliyetsizliğe bağlı son bulma; iyiniyetli üçüncü kişilerin korunması (m.45). Yetki belgesinin geri verilmemesinden doğan sorumluluk (m.44).
4. Yetkisiz temsil: m.46-47 — temsil olunan icazet verirse işlem baştan itibaren onu bağlar; icazet vermezse işlem onu bağlamaz, yetkisiz temsilci karşı tarafın menfi zararından (icazet vermezse) veya müspet zarardan (kusurluysa) sorumlu olur (m.47).
5. Temsilcinin kendisiyle işlem yapması/çıkar çatışması: kural olarak geçersiz, izin/icazet ile geçerli.
6. İspat yükü: Yetkinin varlığını ve kapsamını işleme dayanan taraf ispatlar.

## Çıktı modülleri
- Yetki kapsamı ve geçerlilik analizi.
- İcazet/ret beyanı taslağı iskeleti.
- Yetkisiz temsilde sorumluluk ve rücu şeması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

