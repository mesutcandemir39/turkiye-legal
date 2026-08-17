---
argument-hint: ''
description: Tarh, ceza kesme ve tahsil zamanaşımı ile dava-uzlaşma-düzeltme sürelerini
  hesaplamak ve durma/kesilme hallerini tespit etmek; her vergi dosyasında süre riski
  yönetilirken kullanılır.
name: zamanasimi-ve-sureler
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı Haritası

## Görev
Vergi dosyasındaki tüm hak düşürücü süreleri ve zamanaşımlarını tek bir takvimde toplayıp durma/kesilme hallerini hesaplamak; süre kaynaklı hak kaybı riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Vergiyi doğuran olay hangi takvim yılında gerçekleşti?
2. İhbarname/ödeme emri/işlem hangi tarihte tebliğ edildi?
3. Uzlaşma, düzeltme veya inceleme talebi/işlemi var mı?
4. Borcun vadesi ne zaman doldu?
5. Mücbir sebep veya adli tatil etkisi olabilir mi?

## Denetim şeması
1. **Tarh zamanaşımı:** VUK m.114 — vergi alacağının doğduğu takvim yılını izleyen yılın başından itibaren 5 yıl. Takdir komisyonuna sevk, işleyen zamanaşımını durdurur (m.114/2); duran süre, kararın vergi dairesine tevdiini izleyen günden itibaren işlemeye devam eder (azami bir yıl durma).
2. **Ceza kesme zamanaşımı:** VUK m.374 — vergi ziyaı cezasında tarh zamanaşımı süresi (5 yıl); usulsüzlükte 2 yıl. Süreler vergiyi doğuran olay/usulsüzlüğün işlendiği yılı izleyen yılbaşından işler.
3. **Tahsil zamanaşımı:** AATUHK m.102 — vadeyi izleyen yılbaşından 5 yıl; m.103 kesen haller (ödeme, haciz, teminat, mal bildirimi, cebren tahsil) ve her kesilmede sürenin yeniden başlaması.
4. **Dava/itiraz süreleri:** İYUK m.7 (30 gün), ödeme emri AATUHK m.58 (15 gün), uzlaşma başvurusu 30 gün (VUK Ek m.1), düzeltme talebi tarh zamanaşımı içinde (VUK m.126).
5. **Durma/uzama:** Uzlaşma talebi dava süresini durdurur (VUK Ek m.7); İYUK m.8 sürelerin hesabı, adli/idari tatil; mücbir sebep VUK m.13 ve sürelerin işlememesi VUK m.15. Ara sonuç: her sürenin başlangıç-bitiş tarihi ve kritik gün netleşir.
6. **İspat:** Tebliğ tarihi ve kesen-durduran işlemlerin tarihi belgeyle sabitlenir; tartışmalı tebligatta delil eksikliği işaretlenir.

## Çıktı modülleri
- Birleşik süre takvimi (tarh / ceza / tahsil / dava / uzlaşma — başlangıç ve dolum tarihleriyle).
- Durma-kesilme olay günlüğü (madde dayanağıyla).
- Kritik gün uyarı listesi (en yakın hak düşürücü tarih).
- Belgelendirilmesi gereken tebliğ/kesinti tarihleri listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

