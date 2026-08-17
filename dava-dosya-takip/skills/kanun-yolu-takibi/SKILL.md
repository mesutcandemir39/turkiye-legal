---
argument-hint: ''
description: Karar sonrası istinaf ve temyiz yollarının açık olup olmadığını, süreleri,
  kesinlik sınırlarını ve dilekçe gereklerini izlemek gerektiğinde kullan.
name: kanun-yolu-takibi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kanun Yolu Takibi (İstinaf ve Temyiz)

## Görev
Verilen kararın hangi kanun yoluna tabi olduğunu, süresini, kesinlik sınırını ve başvuru gereklerini takvime bağlamak; kanun yolu hakkının süre veya parasal sınır nedeniyle kaybını önlemek.

## Soğuk başlangıç (intake)
- Karar hangi mahkemeden ve ne zaman tebliğ edildi?
- Karar miktarı/değeri ne (kesinlik sınırı kontrolü için)?
- Hukuk, ceza, icra yoksa idari karar mı?
- Aleyhe olan kısım ve başvuru sebepleri belirlendi mi?

## Denetim şeması
1. Yol tespiti: ilk derece kararına istinaf (BAM), istinaf kararına temyiz (Yargıtay/Danıştay). Hukukta istinaf süresi 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361); cezada istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291); idaride istinaf/temyiz süreleri İYUK m.45-46.
2. Kesinlik sınırı: parasal sınır altında istinaf/temyiz kapalı olabilir (HMK m.341 istinaf, m.362 temyiz kesinlik sınırları; her yıl güncellenir → sınır [DOĞRULANMADI]). Sınırı yıl bazında doğrulat.
3. Başlangıç: süre tebliğ ile başlar; gerekçeli karar tebliğ edilmemişse süre işlemeye başlamaz, bu durumu not et.
4. Dilekçe gereği: istinaf/temyiz dilekçesinde sebeplerin gösterilmesi (HMK m.342, m.364); harç ve gider yatırma şartı (eksiklik halinde başvurudan vazgeçilmiş sayılma riski).
5. Ara sonuç: hangi yol açık, son gün, parasal sınır durumu ve hazırlanacak dilekçe. Tarih ve miktar evraktan alınır; sınır değerleri doğrulanmak üzere işaretlenir.

## Çıktı modülleri
- Kanun yolu takvimi (yol, süre, son gün, kesinlik durumu).
- Kesinlik sınırı doğrulama notu ([DOĞRULANMADI]).
- Başvuru dilekçesi gerekleri çek-listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

