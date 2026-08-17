---
argument-hint: ''
description: Fikri-sınai tecavüzde maddi tazminat (yoksun kalınan kazanç, lisans bedeli),
  itibar ve manevi tazminat hesabı ile zararın ve tecavüz edenin kazancının ispatı,
  defter ibrazı ve bilirkişi gerektiğinde k
name: tazminat-hesabi-ispat
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tazminat Hesabı ve İspat-Delil

## Görev
Tecavüzden doğan zararı ve tazminatı SMK m.150-151 ile FSEK m.68/m.70 çerçevesinde hesaplamak; ispat ve delil stratejisini (defter ibrazı, bilirkişi) kurmak.

## Soğuk başlangıç (intake)
- Hak sahibinin fiili kaybı/yoksun kalınan kazancı belgelenebiliyor mu?
- Tecavüz edenin satış/üretim hacmine ve kazancına dair veri var mı?
- Lisans uygulaması/emsal lisans bedeli mevcut mu?
- İtibar zedelenmesi (kalitesiz taklit) ve manevi zarar var mı?

## Denetim şeması
1. Maddi tazminat türü: Yoksun kalınan kazanç esas alınır (SMK m.150/2). Davacı, m.151'deki üç hesap yönteminden birini seçer: (a) hak sahibinin elde edemediği gelir, (b) tecavüz edenin elde ettiği kazanç, (c) emsal/varsayımsal lisans bedeli.
2. FSEK tazminatı: Mali hak ihlalinde sözleşme yapılsaydı istenebilecek bedelin üç katına kadar (FSEK m.68/1); ayrıca m.70/2 maddi, m.70/1 manevi tazminat. SMK ve FSEK aynı fiilde yarışırsa mükerrer tahsil olmaz.
3. İtibar tazminatı: Markanın/eserin kötü/uygunsuz kullanımı itibarı zedelemişse ek tazminat (SMK m.150/3).
4. İspat ve defter ibrazı: Tecavüz edenin kazancının hesabı için ticari defter ve kayıtların ibrazı talep edilir (HMK m.219-222; TTK ilgili hükümleri). Sunmama, davacı lehine değerlendirme doğurabilir.
5. Bilirkişi: Mali müşavir/sektör bilirkişisi ile hesap yapılır; bilirkişiye yöneltilecek sorular netleştirilir. İspat yükü zarar ve illiyette davacıda; kazanç verisi davalının elindeyse ibraz mekanizması işletilir.
6. Faiz ve zamanaşımı: Tazminat alacağına temerrüt faizi; haksız fiil zamanaşımı TBK m.72 (2/10 yıl), süregelen ihlalde her gün yenilenir.

## Çıktı modülleri
- Tazminat yöntemi seçim ve gerekçe notu (SMK m.151).
- Defter ibrazı ve bilirkişi soru taslağı.
- Faiz ve zamanaşımı değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

