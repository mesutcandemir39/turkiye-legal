---
argument-hint: ''
description: Hangi vakıayı kimin, hangi delille ispatlayacağını planlamak; senetle
  ispat zorunluluğu, kesin/takdiri delil ayrımı, ikrar-yemin-tanık-bilirkişi-keşif
  rejimini doğru kurmak gerektiğinde başvurulur.
name: ispat-yuku-deliller
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
  version: 0.1.0
user-invocable: true
---


# İspat Yükü ve Delil Sistemi

## Görev
Uyuşmazlıktaki çekişmeli vakıaları belirleyip ispat yükünü dağıtmak ve her vakıa için elverişli, hukuken kabul edilebilir delili eşleştirmek.

## Soğuk başlangıç (intake)
- Çekişmeli (ispatı gereken) vakıalar hangileri?
- İşlemin değeri senetle ispat sınırının üstünde mi?
- Elde senet/belge var mı, yoksa tanık/bilirkişiye mi gidilecek?
- Karşı tarafın elindeki belge için ibraz (m.219-222) gerekiyor mu?

## Denetim şeması
1. **İspat yükü** (HMK m.190; TMK m.6): Bir vakıadan kendi lehine hak çıkaran taraf onu ispatla yükümlüdür. Karinelerin (TMK) ispat yükünü yer değiştirdiği hallere dikkat edilir.
2. **İspatın konusu** (m.187): Yalnızca **çekişmeli** ve hukuken önemli vakıalar ispatlanır; ikrar edilen (m.188) veya herkesçe bilinen vakıa ispat gerektirmez.
3. **Senetle ispat zorunluluğu** (m.200): Belirli parasal sınırı aşan hukuki işlemler senetle ispatlanır; bu sınır yıllık tarifeden teyit edilir. **Senede karşı tanıkla ispat** kural olarak yasaktır (m.201); istisna: yazılı delil başlangıcı (m.202) veya delil başlangıcı sayılan haller.
4. **Kesin deliller**: senet (m.199, m.204-206), kesin hükme bağlanan ikrar (m.188), yemin (m.225 vd.). **Takdiri deliller**: tanık (m.240 vd.), bilirkişi (m.266 vd.), keşif (m.288 vd.), uzman görüşü (m.293).
5. **Belge ibrazı**: Karşı taraf veya üçüncü kişi elindeki belge için ibraz istenebilir (m.219-221); ibrazdan kaçınmanın sonuçları (m.220) değerlendirilir.
6. **Delil sunma anı**: Yazılı yargılamada deliller dilekçelerde gösterilir ve ön incelemede bağlanır; basit yargılamada (m.318) dilekçelerle birlikte sunulur — sonradan delil ancak istisnai koşullarla kabul edilir.

Ara sonuç: Her çekişmeli vakıa için "yük kimde + delil türü + kabul edilebilir mi" satırı.

## Çıktı modülleri
- İspat planı tablosu (vakıa / yük / delil / dayanak madde).
- Senetle ispat ve istisna analizi.
- Eksik/elde edilmesi gereken delil listesi (ibraz/keşif talepleri).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

