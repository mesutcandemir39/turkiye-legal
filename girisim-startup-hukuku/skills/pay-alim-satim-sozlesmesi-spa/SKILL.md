---
argument-hint: ''
description: Bir turda veya çıkışta pay devri (SPA) ya da yeni pay iştiraki (SSA)
  sözleşmesi hazırlanırken; satın alma fiyatı, beyan ve tekeffüller, tazminat rejimi,
  kapanış ön şartları ve kapanış mekaniği kurgula
name: pay-alim-satim-sozlesmesi-spa
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Pay Alım/Satım ve İştirak Sözleşmesi (SPA/SSA)

## Görev
İşlemin kesin sözleşmesini kurmak: mevcut paylar devrediliyorsa SPA, yeni pay ihraç ediliyorsa SSA; fiyat, beyan-tekeffül, tazminat, ön şart ve kapanış mekaniğini dengeli biçimde yazmak.

## Soğuk başlangıç (intake)
1. İşlem mevcut pay devri mi (SPA), yeni pay iştiraki mi (SSA)?
2. Satın alma bedeli sabit mi; earn-out, fiyat düzeltmesi (locked box / completion accounts) var mı?
3. Beyan ve tekeffüllerin kapsamı; sınır (cap), eşik (de minimis/basket), süre?
4. Kapanış ön şartları neler (DD, onaylar, rekabet izni, üçüncü kişi onayları)?
5. İmza-kapanış aynı anda mı, araya süre mi giriyor (interim period)?

## Denetim şeması
1. Konu ve tip: Pay devri SPA — devir TTK m.490 şekli + pay defteri (m.499); yeni pay SSA — sermaye artırımına iştirak (m.456). Hangi yapı, hangi kurumsal kararı gerektirir baştan belirle.
2. Bedel ve düzeltme: Sabit bedel; locked box (referans bilanço + leakage yasağı) veya completion accounts (kapanış hesapları); earn-out hedef ve ödeme koşulları. Müzakere riski earn-out tetikleyicilerinde toplanır.
3. Beyan ve tekeffüller (R&W): Satıcının/şirketin kurumsal, IP, iş hukuku, vergi, KVKK beyanları. Bilgiye dayalı (knowledge) ve maddilik (materiality) eşikleri; açıklama mektubu (disclosure letter) ile sınırlama.
4. Tazminat (indemnity): R&W ihlalinde tazminat — TBK genel hükümleri (sözleşmeye aykırılık m.112 vd.) üzerine inşa; cap (tavan), basket/de minimis, zamanaşımı süreleri sözleşmesel. Özel tazminatlar (specific indemnity) bilinen riskler için.
5. Ön şartlar ve ara dönem: Kapanış ön şartları (rekabet izni 4054 m.7, onaylar); ara dönemde olağan işleyiş taahhüdü (conduct of business) ve MAC (material adverse change) maddesi.
6. Kapanış mekaniği: Eşzamanlı veya ertelenmiş kapanış; teslim listesi (kararlar, pay defteri kaydı, imza sirküleri, tescil); SHA ve esas sözleşmenin eş zamanlı yürürlüğü.
7. İhtilaf ve hukuk: Uygulanacak hukuk, tahkim (6325/4686) veya asliye ticaret mahkemesi (TTK m.5).
8. İspat/şekil: Yazılı; pay devri için TTK m.490 şekli; sayısal değerler [doldurulacak].

## Çıktı modülleri
- SPA/SSA iskeleti (bedel, R&W, tazminat, ön şart, kapanış).
- Beyan-tekeffül listesi ve açıklama mektubu çerçevesi.
- Kapanış teslim listesi (closing checklist).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

