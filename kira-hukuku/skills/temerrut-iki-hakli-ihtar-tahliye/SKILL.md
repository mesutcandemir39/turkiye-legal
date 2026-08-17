---
argument-hint: ''
description: Kiracı kira veya yan gider ödemediğinde, temerrüt nedeniyle tahliye veya
  iki haklı ihtara dayalı tahliye değerlendirildiğinde ya da ihtarname içeriği ve
  süreleri tartışıldığında bu beceriyi kullan.
name: temerrut-iki-hakli-ihtar-tahliye
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


# Kira Bedelinin Ödenmemesi, Temerrüt ve İki Haklı İhtar

## Görev
Ödenmeyen kira/yan gider üzerinden temerrüt yoluyla tahliyenin (TBK m.315) ve iki haklı ihtar yoluyla tahliyenin (TBK m.352/2) şartlarını kurmak; ihtar süresini ve içeriğini doğru oluşturmak; ilamsız tahliye takibiyle bağlantısını kurmak.

## Soğuk başlangıç (intake)
- Hangi dönem kiraları/yan giderler ödenmedi, tutar ne?
- Kira ödemesinin yeri ve zamanı sözleşmede nasıl belirlenmiş?
- Daha önce kaç kez yazılı ihtar gönderildi, tarihleri ve içerikleri?
- İhtar noterden mi, taahhütlü mü gönderildi?

## Denetim şeması
1. **Temerrüt — süreli ihtar (TBK m.315)**: Kiracı muaccel kira/yan gideri ödemezse, kiraya veren yazılı olarak **en az otuz gün** süre verir (konut ve çatılı işyerinde bu süre otuz günden az olamaz) ve bu süre içinde ödenmezse sözleşmeyi feshedeceğini bildirir. Süre, ihtarın kiracıya ulaşmasıyla başlar.
2. **İhtar içeriği**: Hangi dönem borcu, tutar, ödeme yeri, süre ve ödenmezse fesih/tahliye uyarısı açıkça yer almalı. Eksik/belirsiz ihtar sonuç doğurmaz.
3. **Sonuç**: Süre sonunda ödenmezse fesih ile tahliye davası veya İİK m.272 vd. ilamsız tahliye takibi başlatılabilir.
4. **İki haklı ihtar (TBK m.352/2)**: Bir kira yılı (veya bir yıldan kısa süreli sözleşmede tüm kira süresi) içinde kira bedelini ödememesi nedeniyle kiracıya yazılı olarak **iki haklı ihtar** yapılmışsa, kiraya veren kira süresinin/dönemin bitiminden başlayarak **bir ay** içinde dava ile tahliye isteyebilir. İhtarların ayrı dönemlere ait ve haklı olması gerekir; aynı dönem için tek ihtar sayılır.
5. **İspat yükü**: Kiraya veren ihtarları ve tebliği; kiracı ödemeyi (makbuz/banka kaydı — HMK m.200) ispatlar.
6. **Ara sonuç**: Hangi yolun (temerrüt feshi mi, iki haklı ihtar mı) somut olayda elverişli olduğu ve süre durumu.

## Çıktı modülleri
- Otuz günlük temerrüt ihtarnamesi taslağı.
- İki haklı ihtar dosyası kontrol listesi.
- İlamsız tahliye takip talebine köprü notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

