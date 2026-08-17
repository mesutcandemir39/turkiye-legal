---
argument-hint: ''
description: Sigortacının eksik veya yanlış beyan nedeniyle sözleşmeden cayması, tazminatı
  reddetmesi veya prim farkı talep etmesi söz konusu olduğunda; sigortalının bildirim
  yükümlülüğünün ihlal edilip edilmediği
name: beyan-yukumlulugu
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
  - ad: Bankalar Kanunu
    numara: '5684'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sözleşme Öncesi Beyan (İhbar) Yükümlülüğü

## Görev
Sigorta ettirenin sözleşme kurulurken rizikoyu etkileyecek hususları doğru ve eksiksiz beyan edip etmediğini, ihlal varsa bunun kasıt/kusur ayrımıyla doğuracağı sonucu (cayma, prim farkı, tazminattan indirim) tespit etmek.

## Soğuk başlangıç (intake)
1. Beyan, sigortacının yazılı sorularına mı dayanıyor, yoksa serbest beyan mı?
2. Hangi husus eksik/yanlış beyan edildi; bu husus rizikoyu ne ölçüde etkiliyor?
3. Sigorta ettiren bunu bilerek mi (kasıt) yoksa kusurla mı yaptı?
4. Sigortacı durumu ne zaman öğrendi; cayma süresine uyuldu mu?

## Denetim şeması
1. **Yükümlülüğün kapsamı.** TTK m.1435: sigorta ettiren bildiği veya bilmesi gereken, rizikonun değerlendirilmesi için önemli hususları bildirmek zorundadır. Sigortacının yazılı sorduğu hususlar önemli sayılır (m.1435/2).
2. **İhlalin tespiti.** Beyan ile gerçek durum arasında, sigortacının sözleşmeyi yapmamasına ya da farklı şartla yapmasına yol açacak bir fark var mı? Ara sonuç: önemli husus eksik/yanlış mı?
3. **Yaptırım — kasıt halinde.** TTK m.1439/1: sigortacı sözleşmeden cayabilir; riziko gerçekleşmişse tazminatı ödemez, primler sigortacıya kalır.
4. **Yaptırım — kusur/kusursuzluk halinde.** TTK m.1439/2: caymanın riziko gerçekleşmesine etkisi varsa tazminat, ödenen prim ile ödenmesi gereken prim oranında indirilir (orantılı indirim). İhlalin riziko ile illiyeti yoksa tam ödeme.
5. **Süre ve usul.** TTK m.1440: sigortacı, ihlali öğrendiği tarihten itibaren on beş gün içinde cayma hakkını kullanmalı; süre geçerse hak düşer. İspat yükü: ihlali ve önemliliği sigortacı, illiyetsizliği/iyiniyeti sigorta ettiren ileri sürer.

## Çıktı modülleri
- Beyan ihlali tespit tablosu (husus / soruldu mu / önemli mi / kasıt-kusur).
- Yaptırım sonucu (cayma / orantılı indirim / etkisiz).
- Cayma süresi ve usul kontrolü.
- Sigortalı veya sigortacı için savunma/itiraz argümanı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

