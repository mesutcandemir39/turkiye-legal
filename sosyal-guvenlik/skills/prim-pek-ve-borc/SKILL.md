---
argument-hint: ''
description: Prim oranları, prime esas kazancın hesabı, eksik/geç bildirim, idari
  para cezası ve SGK prim borcuna itiraz konularında; işveren veya sigortalı prim
  yükümlülüğünü değerlendirmek gerektiğinde kullanılı
name: prim-pek-ve-borc
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Prim, Prime Esas Kazanç ve Borç İhtilafları

## Görev
Prime esas kazancın doğru hesaplanması, prim borcunun ve sorumluluğun tespiti, eksik bildirim ve idari para cezalarına karşı itiraz stratejisini kurmak.

## Soğuk başlangıç (intake)
- Uyuşmazlık prim oranı, PEK unsuru, eksik gün/kazanç bildirimi mi, idari para cezası mı?
- Borç hangi döneme ait; SGK'dan tebliğ edilen belge (ödeme emri, idari para cezası, resen tahakkuk) var mı?
- İşveren asıl işveren-alt işveren ilişkisi içinde mi?
- Yapılandırma/af kanunu kapsamına giren dönem var mı?

## Denetim şeması
1. Prime esas kazanç — 5510 m.80: Hangi ödemelerin PEK'e dahil (ücret, prim, ikramiye) hangilerinin istisna (yemek, çocuk, aile yardımı sınırları) olduğu belirlenir.
2. Prim oranları ve sınırlar — m.81 ve m.82: Kısa-uzun vade ve GSS oranları; PEK alt sınırı (asgari ücret) ve üst sınırı (tavan) uygulanır.
3. Sorumluluk — m.88: Prim borcundan işveren sorumludur; alt işveren çalışması varsa asıl işverenin müteselsil sorumluluğu (4857 m.2 ile birlikte) değerlendirilir.
4. İdari para cezası — m.102: Bildirge ve belgelerin süresinde verilmemesi cezayı doğurur; tebliğden itibaren süresinde önce SGK'ya itiraz (idari aşama), reddi/sükut halinde dava.
5. Zamanaşımı — m.93: Kurum prim alacaklarında 10 yıllık zamanaşımı. Ara sonuç: borcun doğruluğu, miktarı ve takip edilebilirliği belirlenir. İspat: SGK tahakkuk kayıtları ve işyeri muhasebe belgeleri.

## Çıktı modülleri
- PEK hesap tablosu (dahil/istisna kalemler).
- İdari para cezasına itiraz/dava dilekçesi iskeleti.
- Zamanaşımı ve yapılandırma değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

