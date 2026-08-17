---
argument-hint: ''
description: Bedel belirleme, faiz, ödeme koşulları, mücbir sebep ve aşırı ifa güçlüğü
  uyarlama maddelerinin denetimi gerektiğinde kullanılır.
name: bedel-faiz-odeme-ve-uyarlama
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


# Bedel, Faiz, Ödeme ve Uyarlama Şartları

## Görev
Bedel, faiz, ödeme takvimi, fiyat artış mekanizması, mücbir sebep ve uyarlama (hardship) maddelerini denetlemek; belirsizlikleri ve dengesizlikleri gidermek.

## Soğuk başlangıç (intake)
- Bedel sabit mi, endeksli mi, dövizli mi (kambiyo/yasak riski)?
- Temerrüt faizi oranı ve türü kararlaştırılmış mı?
- Mücbir sebep tanımı var mı; uyarlama/yeniden müzakere kaydı bulunuyor mu?
- Ödeme tetikleyicileri (milestone, teslim, kabul) net mi?

## Denetim şeması
1. **Bedel belirliliği**: Edim ve karşı edim belirli/belirlenebilir olmalı; "ayrıca anlaşılacaktır" gibi açık uçlu bedel uyuşmazlık doğurur. Endeks/artış formülü ölçülebilir yazılmalı.
2. **Faiz**: Temerrüt faizi kararlaştırılmamışsa kanuni faiz (TBK m.120, 3095 s.K.); ticari işlerde avans faizi/TTK rejimi. Sözleşmeyle kararlaştırılan faiz fahişse TBK m.120/f.2-3 ve dürüstlük denetimi; bileşik faiz yasağı (yalnız cari hesap/ticari ödünçte istisna).
3. **Para birimi**: Döviz/dövize endeksli bedellerde yürürlükteki kambiyo mevzuatı ve TBK m.99 (yabancı para borcu) kontrol edilir; yasak kapsamı `[DOĞRULANMADI]` güncel mevzuattan teyit edilir.
4. **Mücbir sebep**: Tanım, sayılan haller (kapsayıcı/sınırlı), bildirim süresi, ispat ve sonuç (askı/fesih). Mücbir sebep ifa imkânsızlığına (TBK m.136) köprülenir.
5. **Uyarlama (hardship)**: TBK m.138 — sözleşme yapılırken öngörülemeyen olağanüstü durum ifayı aşırı güçleştirirse hâkimden uyarlama, mümkün değilse dönme/fesih istenebilir; bu hak emredici çekirdek taşır, sözleşmesel hardship klozu bunu somutlaştırır.
6. **İspat/usul**: Ödemeyi borçlu (TBK m.6/genel), temerrüdü ve faizi alacaklı ispatlar; makbuz/dekont düzeni önerilir.

## Çıktı modülleri
- Bedel-faiz-ödeme denetim notu ve belirsizlik listesi.
- Dengeli mücbir sebep + uyarlama (m.138) lafzı önerisi.
- Para birimi/kambiyo ve fahiş faiz riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

