---
argument-hint: ''
description: Bir tarafın yanılarak, aldatılarak veya korkutularak sözleşme yaptığını
  ileri sürdüğü ve iptal hakkı ile sürelerin değerlendirilmesi gerektiği hâllerde
  kullanılır.
name: irade-sakatliklari
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


# İrade Sakatlıkları — Hata, Hile, Korkutma

## Görev
Sözleşme iradesinin hata, hile veya korkutma ile sakatlanıp sakatlanmadığını, iptal hakkını, süresini ve tazminat sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Taraf neye dayanarak iradesinin sakat olduğunu söylüyor: yanılma mı, aldatılma mı, baskı mı?
- Yanılma esaslı mı (sözleşmenin niteliği, karşı taraf, miktar, temel vasıf)?
- Aldatma/korkutma karşı taraftan mı, üçüncü kişiden mi geldi?
- Sakatlığın öğrenildiği/ortadan kalktığı tarih nedir (bir yıllık süre için)?

## Denetim şeması
1. Hata (yanılma): TBK m.30-35. Esaslı yanılma türleri m.31 (sözleşmenin niteliği, karşı taraf kimliği, miktar) ve temel vasıfta yanılma m.32; saik yanılması kural olarak esaslı değildir. İletmede yanılma m.33. Dürüstlük kuralına aykırı şekilde iptal hakkı kullanılamaz (m.34); yanılan kusurluysa tazminatla yükümlüdür (m.35).
2. Hile (aldatma): m.36 — esaslı olmayan yanılmaya yol açsa bile iptal sağlar. Üçüncü kişinin hilesinde karşı taraf bilmiyor/bilmesi gerekmiyorsa sözleşme ayakta kalır (m.36/f.2).
3. Korkutma (ikrah): m.37-38 — ağır ve yakın bir tehlike, kişi veya yakınına yönelik; haklı korku yaratacak ciddiyette. Üçüncü kişinin korkutmasında iyiniyetli karşı tarafa tazminat gerekebilir (m.38/f.2).
4. İptal beyanı ve süre: m.39 — sakatlığın öğrenildiği veya korkutmanın etkisinin kalktığı andan itibaren bir yıl içinde diğer tarafa bildirilerek; aksi hâlde sözleşmeye icazet verilmiş sayılır. Bu hak bozucu yenilik doğuran haktır.
5. İspat yükü: Sakatlığı ileri süren unsurları ve süreyi koruduğunu ispatlar.
6. Ara sonuç: İptal hakkı var mı, süre içinde mi, tazminat yükümlülüğü doğuyor mu?

## Çıktı modülleri
- Sakatlık türü ve esaslılık değerlendirmesi.
- İptal beyanı/ihtarname taslağı iskeleti (süre uyarısıyla).
- İptal hâlinde iade ve tazminat sonuç şeması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

