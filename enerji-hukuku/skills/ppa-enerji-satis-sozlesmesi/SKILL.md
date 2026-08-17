---
argument-hint: ''
description: Elektrik/enerji alım satım anlaşmaları, ikili anlaşmalar, kurumsal PPA
  ve YEKA tipi satış sözleşmelerinin müzakeresi, hazırlanması veya risk incelemesi
  gerektiğinde kullanılır.
name: ppa-enerji-satis-sozlesmesi
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Satış Sözleşmeleri (PPA) İncelemesi

## Görev
Enerji alım satım (PPA/ikili anlaşma/kurumsal PPA) sözleşmesini fiyat, miktar, risk dağılımı ve düzenleyici uyum açısından incelemek; eksik/asimetrik hükümleri tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Taraflar ve sıfatları (üretici/tedarikçi/tüketici) ile lisans durumu?
2. Fiyat yapısı: sabit, endeksli, PTF bağlantılı, tavan/taban var mı?
3. Süre, miktar (take-or-pay var mı) ve teslim/ölçüm noktası?
4. Teminat, dengesizlik maliyeti ve mevzuat değişikliği riski kime ait?

## Denetim şeması
1. **Geçerlilik ve ehliyet**: TBK 6098 genel hükümler; tarafların lisans/yetki kapsamında bu satışı yapma ehliyeti (lisanssız tüketiciye doğrudan satış sınırları). Ara sonuç: sözleşme konusu mevzuata uygun mu.
2. **Fiyat ve endeks**: Fiyat formülünün belirli/belirlenebilir olması (TBK m.27 kesin hükümsüzlük riski); PTF/endeks bağlantısında veri kaynağı ve hesap günü netliği.
3. **Miktar ve take-or-pay**: Asgari alım taahhüdü, eksik çekiş bedeli ve mücbir sebep istisnası; cezai şart varsa TBK m.182 ve aşırı cezada m.182/3 indirimi.
4. **Risk dağılımı**: Dengesizlik/uzlaştırma maliyeti, YEKDEM tercihi, mevzuat değişikliği (change in law) ve vergi/harç değişiklikleri kime ait; teminat (teminat mektubu/avans) ve temerrüt faizi (ticari işte TBK m.120 + 3095 s.K.).
5. **Uyuşmazlık ve fesih**: Fesih sebepleri, askıya alma, tahkim/yetki şartı (4686/HMK 6100) ve uygulanacak hukuk. Emredici hükümlere ve EPDK piyasa kurallarına aykırı kayıtlar işaretlenir.

## Çıktı modülleri
- Madde madde risk/redline tablosu.
- Eksik veya kesin hükümsüzlük riski taşıyan kayıt listesi.
- Müzakere notu ve alternatif lafız önerileri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

