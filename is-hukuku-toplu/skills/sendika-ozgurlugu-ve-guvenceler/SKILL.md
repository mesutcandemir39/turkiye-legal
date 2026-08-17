---
argument-hint: ''
description: Sendika kurma/uyelik ozgurlugu, sendikal ayrimcilik, sendikal tazminat
  ve isyeri sendika temsilcisi guvencesi sorunlarinda; ozellikle uyelik veya sendikal
  faaliyet nedeniyle fesih iddialarinda kullani
name: sendika-ozgurlugu-ve-guvenceler
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sendika Özgürlüğü ve Sendikal Güvenceler

## Görev
Sendika özgürlüğünün bireysel (üyelik/çekilme) ve kolektif boyutunu, sendikal ayrımcılık yasağını ve sendikal tazminat ile temsilci güvencesini uygulamak. Sendikal nedenle fesih iddialarının ana çalışma alanıdır.

## Soğuk başlangıç (intake)
- İşçi sendika üyesi mi, üyelik/çekilme tarihi nedir, işveren bunu biliyor muydu?
- Fesih veya olumsuz işlem sendikal faaliyetin hemen ardından mı geldi?
- İşçi iş güvencesi kapsamında mı (30+ işçi, 6 ay kıdem — 4857 m.18)?
- Mağdur işyeri sendika temsilcisi mi?

## Denetim şeması
1. **Özgürlüğün kapsamı:** 6356 m.17-19 üyelik, üyelikten çekilme (e-Devlet üzerinden) serbestisini güvenceler. Any. m.51 ve ILO 87/98 yorum dayanağıdır.
2. **Sendikal ayrımcılık yasağı:** 6356 m.25/1-3 — işe alımda, çalışma şartlarında, fesihte sendika üyeliği/faaliyeti nedeniyle ayrım yapılamaz.
3. **Sendikal tazminat:** 6356 m.25/4-5 — ihlalde işçinin bir yıllık ücretinden az olmamak üzere sendikal tazminat. Fesih dışı işlemlerde de talep edilebilir.
4. **İş güvencesi ile yarışma:** İşçi 4857 m.18 kapsamındaysa, sendikal nedenle fesihte işe iade davası açılır; iş güvencesi kapsamında olmasa dahi 6356 m.25/5 uyarınca doğrudan sendikal tazminat istenebilir (Yargıtay'ın yerleşik yaklaşımı — künye `[DOĞRULANMADI]`, karararama.yargitay.gov.tr).
5. **İspat yükü:** 6356 m.25/7 — işçi sendikal nedeni kuvvetle muhtemel kılan olguları (üyelik tarihi, fesihle yakınlık, aynı dönemde örgütlenme) ortaya koyar; ispat yükü işverene geçer, geçerli/haklı neden ispatı işverende.
6. **Temsilci güvencesi:** 6356 m.23-24 — işyeri sendika temsilcisinin iş sözleşmesi haklı neden olmadıkça ve yazılı sebep gösterilmeden feshedilemez; özel güvence işler.

## Çıktı modülleri
- Sendikal ayrımcılık değerlendirme tablosu (olgu-emare-madde).
- İşe iade / sendikal tazminat strateji notu.
- İspat planı ve delil listesi (üyelik kaydı, e-Devlet, tanık, fesih yazışmaları).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

