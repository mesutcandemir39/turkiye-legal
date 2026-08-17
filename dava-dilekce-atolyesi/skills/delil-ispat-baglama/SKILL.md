---
argument-hint: ''
description: Vakıaları doğru delillere bağlamak; ispat yükü, senetle ispat zorunluluğu,
  delil listesi ve delil tespiti taleplerini kurmak gerektiğinde kullanılır.
name: delil-ispat-baglama
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Delil, İspat ve Delillerin Bağlanması

## Görev
Vakıaları kabul edilebilir delillerle desteklemek; ispat yükünü doğru dağıtmak; senetle ispat sınırlarını gözetmek ve delil listesini dilekçeye sağlam bağlamak. Somutlaştırılmamış delil dikkate alınmaz (HMK m.194).

## Soğuk başlangıç (intake)
- Hangi vakıa hangi delille ispatlanacak?
- Senet/yazılı delil var mı, yoksa tanık mı dayanılacak?
- Karşı tarafın elindeki belgeler gerekli mi (ibraz)?
- Delil tespiti veya bilirkişi gerekiyor mu?

## Denetim şeması
1. İspat yükü (HMK m.190; TMK m.6): Bir hakkın varlığını iddia eden, dayandığı vakıayı ispatla yükümlüdür. Karşı ispat ve aksini ispat ayrımını gözetin.
2. Delil türleri (HMK m.187 vd.): Kesin deliller (senet, yemin, kesin hüküm) ve takdiri deliller (tanık, bilirkişi, keşif, uzman görüşü). Her vakıaya en güçlü delili eşleyin.
3. Senetle ispat zorunluluğu (HMK m.200-201): Belirli tutarı aşan hukuki işlemler senetle ispatlanır; senede karşı tanık kural olarak dinlenmez. İstisnalar (m.203): yakın hısımlar, delil başlangıcı, örf-adet.
4. Belge ibrazı ve delil tespiti: Karşı taraftaki/üçüncü kişideki belge için ibraz (HMK m.219-222); kaybolma riski varsa delil tespiti (m.400-406). Fikri-sınai uyuşmazlıkta ihtiyati tedbirle birlikte.
5. Somutlaştırma (HMK m.194): Hangi delilin hangi vakıa için sunulduğunu açıkça yazın; tanıkla ispatı caiz olmayan vakıada tanık göstermeyin. Ara sonuç: vakıa-delil eşleşmesi tamsa delil listesi kapanır.

## Çıktı modülleri
- Vakıa-delil eşleşme tablosu
- Delil listesi (senet/tanık/bilirkişi/keşif)
- Senetle ispat sınırı uyarısı
- Delil tespiti/ibraz talebi taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

