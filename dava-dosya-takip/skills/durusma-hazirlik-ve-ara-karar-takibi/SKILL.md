---
argument-hint: ''
description: Yaklaşan duruşmaya hazırlanmak, tensip ve ara kararların gereklerini
  izlemek, her celse için yapılacaklar ve verilecek beyanları listelemek gerektiğinde
  kullan.
name: durusma-hazirlik-ve-ara-karar-takibi
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


# Duruşma Hazırlığı ve Ara Karar Takibi

## Görev
Her duruşma öncesi dosyanın güncel durumunu, ara kararların gereğini ve celsede yapılacak işlemleri bir hazırlık çek-listesine dönüştürmek; ara kararların kaçırılmasını önlemek.

## Soğuk başlangıç (intake)
- Bir sonraki duruşma tarihi ve aşaması (ön inceleme, tahkikat, sözlü yargılama) ne?
- En son ara karar ne idi ve gereği yerine getirildi mi?
- Bu celsede sunulacak beyan, delil veya itiraz var mı?
- Tanık/bilirkişi/keşif gibi bekleyen işlem var mı?

## Denetim şeması
1. Ara karar dökümü: tensip zaptı ve her celse zaptındaki ara kararları madde madde çıkar; her birinin muhatabı, gereği ve süresi (ör. iki hafta kesin süre, HMK m.94 kesin süre sonucu) ile takip et.
2. Aşamaya göre gündem: ön inceleme celsesinde sulh teşviki, ilk itiraz ve dava şartı incelemesi (HMK m.137-140); tahkikatta delil toplama ve tanık dinleme; sözlü yargılamada esas hakkında beyan.
3. Kesin süre riski: kesin süreye bağlanan işlemler (delil avansı, gider avansı HMK m.120, delil bildirimi) yerine getirilmedi ise hak kaybı uyarısı.
4. Sunulacaklar: bu celsede ibraz edilecek beyan/delil listesi ve dayanağı; mazeret gerekiyorsa mazeret dilekçesi notu.
5. Ara sonuç: celse-bazlı hazırlık çek-listesi ve açık ara karar gerekleri. Tarih ve ara karar metni evraktan alınır.

## Çıktı modülleri
- Ara karar takip tablosu (karar, muhatap, gereği, süre, durum).
- Duruşma hazırlık çek-listesi.
- Kesin süre / hak kaybı uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

