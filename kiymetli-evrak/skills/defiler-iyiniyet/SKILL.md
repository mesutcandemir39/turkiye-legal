---
argument-hint: ''
description: Kambiyo senedinde ileri sürülebilecek mutlak ve kişisel def'ileri ayırmak,
  iyiniyetli hamile karşı def'i sınırlamasını uygulamak; borçlunun savunma imkânlarını
  veya hamilin def'isiz konumunu değerlend
name: defiler-iyiniyet
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


# Def'iler ve İyiniyetli Hamilin Korunması

## Görev
Kambiyo borçlusunun hamile karşı ileri sürebileceği def'ileri tasnif etmek; senetten anlaşılan/herkese karşı ileri sürülen def'iler ile kişisel def'ileri ayırmak ve iyiniyetli hamile karşı kişisel def'i yasağını uygulamak.

## Soğuk başlangıç (intake)
- Borçlunun iddiası senedin geçerliliğine mi (şekil, ehliyet, sahtelik) yoksa temel ilişkiye mi (ödeme, bedelsizlik, anlaşmaya aykırı doldurma) dayanıyor?
- Hamil, def'inin dayandığı kişiyle doğrudan taraf mı, yoksa ciro yoluyla mı edindi?
- Hamilin senedi edinirken borçluya zarar verme kastı (kötüniyet) iddiası var mı?
- Senet tahsil cirosuyla mı geçti?

## Denetim şeması
1. Mutlak (senetten anlaşılan/herkese karşı) def'iler: şekil eksikliği, zamanaşımı, sahtelik, ehliyetsizlik, senet metnindeki kayıtlar — bunlar her hamile karşı ileri sürülebilir.
2. Kişisel (def'iler): temel ilişkiden doğan def'iler (ödeme, takas, bedelsizlik, anlaşmaya aykırı doldurma) yalnızca doğrudan taraf olunan hamile karşı ileri sürülür.
3. İyiniyetli hamil koruması: TTK m.687 — senedi devralırken borçlunun zararına hareket etmediyse, önceki hamillerle borçlu arasındaki kişisel def'iler kendisine karşı ileri sürülemez. Kötüniyet veya ağır kusur ispatlanırsa koruma kalkar; ispat yükü def'iyi ileri süren borçludadır.
4. Tahsil cirosu istisnası: tahsil cirosuyla edinen hamil temsilci olduğundan, borçlu cirantaya karşı sahip olduğu def'ileri bu hamile de ileri sürebilir (m.688).
5. Bağımsızlık ilkesi: bir imzanın geçersizliği diğer kambiyo taahhütlerini etkilemez (m.677); borçlu yalnızca kendi taahhüdüne ilişkin def'iyi ileri sürebilir.
6. Ara sonuç: def'inin türü ve hamilin iyiniyeti belirlendiğinde, savunmanın o hamile karşı dinlenip dinlenmeyeceği sonuçlanır.

## Çıktı modülleri
- Def'i tasnif tablosu (mutlak/kişisel + dayanak + muhatap hamil).
- İyiniyet/kötüniyet değerlendirme notu (ispat yükü dahil).
- Borçlu savunma dilekçesi veya hamil için def'isizlik argümanı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

