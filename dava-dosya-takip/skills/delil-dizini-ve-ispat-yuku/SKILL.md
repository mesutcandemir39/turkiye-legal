---
argument-hint: ''
description: Dosyadaki delilleri dizinleyip her birini ilgili vakıaya ve ispat yüküne
  bağlamak, sunulan-beklenen-itirazlı delilleri ayırt etmek gerektiğinde kullan.
name: delil-dizini-ve-ispat-yuku
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
  version: 0.1.0
user-invocable: true
---


# Delil Dizini ve İspat Yükü

## Görev
Dosyadaki tüm delilleri türü, ibraz edeni, dayandığı vakıa ve durumuyla dizinlemek; her çekişmeli vakıada ispat yükünün kimde olduğunu eşlemek.

## Soğuk başlangıç (intake)
- Hangi deliller dosyada (senet, fatura, tanık listesi, bilirkişi raporu, keşif tutanağı, yazışma)?
- Hangi vakıalar çekişmeli, hangileri ikrar edilmiş?
- Henüz sunulmamış ama dayanılan delil var mı?
- Karşı tarafın delillerine itiraz edilmiş mi?

## Denetim şeması
1. Delil satırı: delil adı, türü, ibraz eden, dayandığı vakıa, durum (sunuldu / beklenen / itirazlı). Delil türleri: senet (HMK m.199 vd.), tanık (HMK m.240 vd.), bilirkişi (HMK m.266 vd.), keşif (HMK m.288), yemin.
2. İspat yükü eşlemesi: HMK m.190 ve TMK m.6 uyarınca bir vakıadan lehine hak çıkaran tarafın ispatla yükümlü olduğunu uygula; her çekişmeli vakıanın karşısına yükümlü tarafı yaz.
3. Senetle ispat kuralı: belirli tutarı aşan hukuki işlemlerde senetle ispat zorunluluğu (HMK m.200) ve tanıkla ispat sınırı (HMK m.201) gözetilerek tanık deliline güvenilirlik notu düşülür.
4. Eksik delil: dayanılan ama sunulmamış delil ve celbi gereken belge (HMK m.219-221 ibraz yükümlülüğü, müzekkere) ayrı liste.
5. Ara sonuç: hangi vakıa hangi delille ispatlanıyor, hangisi açıkta — boşluk haritası. Delil içeriği evraktan alınır; var olmayan delil yazılmaz.

## Çıktı modülleri
- Delil-tür-ibraz eden-vakıa-durum kolonlu dizin tablosu.
- İspat yükü eşleme tablosu (çekişmeli vakıa → yükümlü taraf).
- Eksik/celbi gereken delil listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

