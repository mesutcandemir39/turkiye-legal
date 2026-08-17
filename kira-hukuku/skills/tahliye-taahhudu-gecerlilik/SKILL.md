---
argument-hint: ''
description: Bir tahliye taahhütnamesinin geçerliliği, düzenleme tarihi-tahliye tarihi
  ilişkisi, baskı/boş tarihle alınma iddiası veya taahhüde dayalı icra takibi söz
  konusu olduğunda bu beceriyi kullan.
name: tahliye-taahhudu-gecerlilik
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


# Yazılı Tahliye Taahhüdü — Geçerlilik ve İcra

## Görev
Tahliye taahhüdünün TBK m.352/1 şartlarını taşıyıp taşımadığını denetlemek; geçerlilik itirazlarını (sözleşme ile aynı tarihte/öncesinde verilme, irade sakatlığı, boş tarih) değerlendirmek; taahhüde dayalı icra/dava yolunu kurmak.

## Soğuk başlangıç (intake)
- Taahhüt yazılı mı, kim imzalamış (kiracı mı)?
- Taahhüdün düzenleme tarihi ve boşaltma tarihi ne?
- Kira sözleşmesi ile aynı tarihte mi alınmış?
- Tahliye tarihi geçti mi; üzerinden ne kadar süre geçti?

## Denetim şeması
1. **Şekil ve taraf (TBK m.352/1)**: Taahhüt **yazılı** olmalı ve **kiracı (veya yetkili temsilcisi)** tarafından verilmelidir. Kiraya verenin değil kiracının iradesi esastır.
2. **Tarih ilişkisi**: Yerleşik uygulamaya göre taahhüt, kiralananın tesliminden/sözleşmenin kurulmasından **sonra** verilmiş olmalıdır; teslimle eş zamanlı veya öncesinde alınan taahhüt, kiracının korunması gereği geçersiz sayılır. Bu ilkesel kabul için güncel Yargıtay içtihadını karararama.yargitay.gov.tr üzerinden doğrula `[DOĞRULANMADI]`.
3. **İrade sakatlığı / boş tarih iddiası**: Kiracı, taahhüdün baskı altında veya boş/ileri tarihli alındığını ileri sürerse ispat yükü kendisindedir; senede karşı senetle/kesin delille ispat kuralı (HMK m.200-201) işler.
4. **Süre (TBK m.352/1)**: Taahhüt edilen boşaltma tarihinden başlayarak **bir ay** içinde icra takibi (İİK m.272) veya dava açılır.
5. **İcra yolu (İİK m.272 vd.)**: Yazılı tahliye taahhüdüne dayanarak ilamsız tahliye takibi yapılabilir; itiraz halinde icra mahkemesinde itirazın kaldırılması.
6. **Ara sonuç**: Taahhüdün geçerli olup olmadığı ve süresinde harekete geçilip geçilmediği.

## Çıktı modülleri
- Geçerlilik kontrol listesi (şekil-taraf-tarih-süre).
- Taahhüde dayalı icra takip talebi taslağı.
- Olası kiracı itirazlarına karşı argüman notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

