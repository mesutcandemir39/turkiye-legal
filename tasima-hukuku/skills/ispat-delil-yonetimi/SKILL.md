---
argument-hint: ''
description: Taşıma uyuşmazlığında zararın taşıma süresinde doğduğunun, eşyanın durumunun
  ve kurtuluş sebeplerinin ispatı, ispat yükünün dağılımı ve delillerin (belge, ekspertiz,
  kayıt) toplanması gerektiğinde kul
name: ispat-delil-yonetimi
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
  version: 0.1.0
user-invocable: true
---


# İspat ve Delil Yönetimi

## Görev
Taşıma davasında kimin neyi ispatlayacağını belirlemek, taşıma belgelerinden doğan karineleri işletmek ve delil setini eksiksiz oluşturmak.

## Soğuk başlangıç (intake)
1. İddia ne: eşya teslimde sağlam değildi / zarar taşıma süresinde doğdu / taşıyıcı kusurlu?
2. Hangi belgeler mevcut: taşıma senedi/CMR, teslim makbuzu, rezerv şerhleri, ekspertiz?
3. Eşyanın teslim alındığı andaki durumu nasıl kayıtlandı?
4. Karşı taraf hangi kurtuluş sebebini ileri sürüyor?

## Denetim şeması
1. **Temel ispat yükü:** Hak sahibi, zararın eşya taşıyıcının zilyetliğinde (teslim alma-teslim arası) doğduğunu ispatlar; taşıyıcı kurtuluş sebebini ispatlar (TTK m.875, m.876; CMR m.18/1).
2. **Belgeden doğan karineler:** TTK m.858 / CMR m.9 — rezervsiz/şerhsiz teslim alma, eşyanın senette yazılı iyi durumda teslim alındığı karinesini doğurur; taşıyıcının teslimde rezerv koymaması, iyi teslim karinesini güçlendirir.
3. **Özel risk karineleri:** TTK m.878 / CMR m.18/2 — sayılan risklerden biri varsa zararın o sebepten doğduğu karine sayılır; hak sahibi aksini ispatla yükümlü olur.
4. **Delil türleri:** Taşıma senedi/CMR belgesi, teslim-tesellüm tutanakları, tartım/sayım kayıtları, dijital takip (GPS/telematik) verileri, sıcaklık kayıtları (soğuk zincir), ekspertiz/sürvey raporu, faturalar.
5. **Delil tespiti ve bilirkişi:** Eşyanın hasar durumu için HMK m.400 delil tespiti; teknik değerlendirme için bilirkişi/sürveyör raporu; hesap için ticari defterler (TTK m.83, HMK m.222).
6. **İspat ölçüsü:** Tam ispat aranır; karinelerin kaydırdığı yük dikkate alınır.
7. **Ara sonuç:** Lehte-aleyhte ispat dağılımı ve eksik delillerin tamamlanma planı.

## Çıktı modülleri
- İspat yükü dağılım tablosu (iddia / yük sahibi / dayanak madde).
- Delil dizini ve eksik delil tamamlama listesi.
- Karine analizi ve aksini ispat stratejisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

