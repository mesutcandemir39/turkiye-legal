---
argument-hint: ''
description: Erken aşama finansmanda SAFE, dönüştürülebilir tahvil/borç gibi pay dönüşümü
  taahhüt eden enstrümanlar kullanılırken; bunların Türk hukukundaki niteliği, dönüşüm
  mekaniği, indirim/tavan ve sermaye art
name: safe-donusturulebilir-enstruman
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


# SAFE ve Dönüştürülebilir Enstrümanlar

## Görev
Pay dönüşümü taahhüt eden enstrümanı (SAFE, dönüştürülebilir borç) Türk hukukuna geçerli biçimde uyarlamak; dönüşüm mekaniğini, indirim/değerleme tavanını ve gelecekteki sermaye artırımına bağlanmasını kurmak.

## Soğuk başlangıç (intake)
1. Enstrüman SAFE mi, dönüştürülebilir borç/tahvil mi (geri ödeme/faiz var mı)?
2. Dönüşüm tetikleyicisi ne: nitelikli yatırım turu, çıkış, vade sonu?
3. İndirim oranı (discount) ve/veya değerleme tavanı (valuation cap) var mı?
4. Yatırımcı para girişini ne zaman yaptı; şirkete fiilen ödendi mi?
5. Şirket AŞ mi; kayıtlı sermaye sistemi mevcut mu?

## Denetim şeması
1. Hukuki nitelik: Türk hukukunda SAFE isimsiz/karma sözleşmedir (TBK m.26 sözleşme serbestisi). Borç (geri ödenebilir) niteliği taşıyorsa karz/tüketim ödüncü hükümleri (TBK m.386 vd.); salt pay taahhüdü ise gelecekteki sermaye artırımına katılma taahhüdü olarak kurgulanır.
2. Dönüşüm = sermaye artırımı: Dönüşüm anında yatırımcıya pay, bir bedelli sermaye artırımıyla (TTK m.456 vd.) verilir; rüçhan hakkının (m.461) bu yatırımcı lehine kullandırılması/sınırlanması GK kararıyla kurgulanmalı.
3. Sermayenin korunması: Para girişi sermaye taahhüdüne mahsup edilecekse, nakdî sermaye ödeme kuralları (m.344) ve takas/mahsup geçerliliği denetlenmeli; ayni nitelik doğarsa değerleme (m.343) gündeme gelir.
4. İndirim ve tavan: Discount ve cap yalnızca dönüşüm fiyatını/pay adedini belirleyen sözleşmesel parametrelerdir; cap table'a etkisi en olumsuz senaryoyla modellenir.
5. Tahvil yolu: Dönüştürülebilir tahvil resmi yolla ihraç edilecekse TTK m.504-507 (borçlanma senetleri) ve SPK mevzuatı; halka kapalı kurguda genellikle sözleşmesel dönüştürülebilir borç tercih edilir.
6. İspat/şekil: Yazılı sözleşme; para girişi banka kaydıyla; dönüşüm için GK/YK kararı ve tescil. Eşik/oran değerlerini [doldurulacak] bırak.

## Çıktı modülleri
- SAFE/dönüştürülebilir borç sözleşmesi taslağı (tetikleyici, indirim, tavan).
- Dönüşüm mekaniği ve sermaye artırımı adım planı.
- En olumsuz senaryo cap table dönüşüm tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

