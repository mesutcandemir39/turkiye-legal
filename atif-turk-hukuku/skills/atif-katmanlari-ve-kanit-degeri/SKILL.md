---
argument-hint: ''
description: Bir metindeki her önermenin mevzuat mı içtihat mı doktrin mi yoksa kişisel
  çıkarım mı olduğunu ayırmak ve her katmanın bağlayıcılık/kanıt değerini doğru sunmak
  gerektiğinde kullanılır.
name: atif-katmanlari-ve-kanit-degeri
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Atıf Katmanları ve Kanıt Değeri

## Görev
Bir hukuki metinde geçen her önermeyi doğru kaynak katmanına (mevzuat / içtihat / doktrin / çıkarım) yerleştirmek ve her katmanın bağlayıcılık derecesini abartmadan ve eksiltmeden göstermek.

## Soğuk başlangıç (intake)
- Metin ne tür: layiha, mütalaa, sözleşme şerhi, iç değerlendirme mi?
- Hangi önerme bağlayıcı kurala, hangisi tartışmalı görüşe dayanıyor?
- İddialar arasında "kanun böyle diyor" ile "doktrin/içtihat böyle diyor" karışmış mı?
- Okuyucu kararı kim verecek (hâkim, müvekkil, karşı vekil)?

## Denetim şeması
1. **Katman ayrımı** — Her cümle dört kutudan birine konur: (a) yürürlükteki mevzuat (bağlayıcı kural, Anayasa m.138/1), (b) içtihat (emsal; İBK bağlayıcı, diğeri ikna edici), (c) doktrin (bağlamayan görüş, TMK m.1/3), (d) yazarın çıkarımı/yorumu.
2. **Bağlayıcılık sıralaması** — Anayasa/AYM kararı (m.153/son: herkesi bağlar) > kanun/CB kararnamesi > İBK (Yargıtay K. m.45: bağlar) > yerleşik daire/genel kurul içtihadı (ikna edici) > tek karar > doktrin > kişisel çıkarım.
3. **Sunum disiplini** — Bağlayıcı kural "…m.X uyarınca" diye kesin; içtihat "Yargıtay'ın yerleşik uygulamasına göre"; doktrin "öğretide … savunulmaktadır" diye kiplenir. Çıkarım açıkça "kanaatimce/değerlendirildiğinde" ile ayrılır.
4. **Abartma denetimi** — Tek bir daire kararı "yerleşik içtihat" diye sunulmaz; bir yazarın görüşü "kural" gibi yazılmaz; tartışmalı konuda tek yön gösterilmez.
5. **İspat-hukuk ayrımı** — Vakıa iddiası (ispatı gerekir, HMK m.190) ile hukuk önermesi (iura novit curia) ayrı işaretlenir; atıf yalnızca hukuk katmanına yapılır, vakıa için delil gösterilir.

## Çıktı modülleri
- Önerme → katman eşleme tablosu.
- Bağlayıcılık derecesi notu (her önerme için).
- Kiplenme düzeltme önerileri (kesin/ikna edici/görüş).
- Abartılmış/temelsiz atıf uyarı listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

