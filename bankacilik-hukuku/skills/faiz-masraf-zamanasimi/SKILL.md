---
argument-hint: ''
description: Banka alacağında veya müşteri iade talebinde akdi/temerrüt/bileşik faiz,
  komisyon-masraf kalemleri ile uygulanacak zamanaşımı sürelerini ayrıştırıp hesap
  denetimi yapmak gerektiğinde kullanılır.
name: faiz-masraf-zamanasimi
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Faiz, Komisyon Hesabı ve Zamanaşımı Analizi

## Görev
Bir bankacılık alacağında veya iade talebinde faiz ve eklenti kalemlerini ayrıştırmak, hesabı denetlemek ve doğru zamanaşımı süresini belirlemek; aşan/dayanaksız kalemleri ve zamanaşımına uğramış talepleri işaretlemek.

## Soğuk başlangıç (intake)
- Talep yönü: banka tahsilatı mı, müşteri iade/itiraz talebi mi?
- Faiz tipi: akdi faiz, temerrüt faizi, bileşik faiz; oran ve dönem nedir?
- Hesap kalemleri: dosya masrafı, komisyon, hesap işletim, sigorta, ekspertiz?
- İlişki ticari mi tüketici mi; alacağın doğum ve son işlem tarihleri neler?

## Denetim şeması
1. **Faiz türü ayrımı**: Akdi faiz sözleşmeyle, temerrüt faizi TBK m.120 ile (kararlaştırılmamışsa kanuni oran) belirlenir. Adi işlerde bileşik faiz yasaktır; ticari işlerde TTK m.8 sınırlı istisna ve cari hesapta TTK m.89-101 özel rejim uygulanır. Tüketici işleminde aşırı/dengesiz faiz haksız şart denetimine tabidir.
2. **Eklenti kalemleri**: Dosya masrafı/komisyon gibi kalemler ancak gerçek maliyet ve açık onaya dayanıyorsa geçerlidir; aksi halde tüketici lehine iadeye konu olur (TKHK m.4, m.5). Her kalem ayrı dayanak ister.
3. **Hesap denetimi**: Tahakkuk dönemleri, faiz başlangıç tarihi, kapital-faiz ayrımı ve mükerrer/çifte tahakkuk kontrol edilir; bilirkişi hesabıyla karşılaştırılır.
4. **Zamanaşımı**: Genel sözleşmesel alacakta TBK m.146 (10 yıl); faiz ve dönemsel edimlerde TBK m.147 (5 yıl); kambiyo senetlerinde TTK'nın özel kısa süreleri; haksız fiil unsurunda TBK m.72. İade talebinde sebepsiz zenginleşme süreleri (TBK m.82 — 2 ve 10 yıl) ayrıca değerlendirilir. Zamanaşımının kesilmesi/durması (TBK m.153-154) kontrol edilir.
5. **Ara sonuç**: Geçerli kalemler, iadeye/itiraza konu kalemler ve zamanaşımına uğramış talepler ayrı listelenir; net talep tutarı yazılır.

## Çıktı modülleri
- Kalem kalem faiz/masraf denetim tablosu.
- Zamanaşımı haritası (her talep için süre ve başlangıç).
- Düzeltilmiş alacak/iade hesap özeti ve itiraz noktaları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

