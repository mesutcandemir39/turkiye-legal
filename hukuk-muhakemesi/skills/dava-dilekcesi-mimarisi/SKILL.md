---
argument-hint: ''
description: HMK m.119'a uygun, zorunlu unsurları eksiksiz bir dava dilekçesi taslamak;
  vakıa-hukuki sebep-talep sonucu yapısını kurmak, delilleri vakıalarla bağlamak ve
  eksik unsurlardan doğan reddi önlemek için.
name: dava-dilekcesi-mimarisi
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


# Dava Dilekçesi Mimarisi (HMK m.119)

## Görev
HMK m.119'un zorunlu unsurlarını taşıyan, vakıaları delillerle bağlanmış, talep sonucu açık ve infaza elverişli bir dava dilekçesi iskeleti üretmek.

## Soğuk başlangıç (intake)
- Talep türü ne? (eda / tespit / inşai; terditli/seçimlik/kısmi mi?)
- Dava değeri belirli mi, belirsiz alacak davası (m.107) mı?
- Hangi vakıalar hangi delillerle ispatlanacak?
- Faiz türü ve başlangıç tarihi ne olacak?

## Denetim şeması
1. **Zorunlu unsurlar** (HMK m.119/1): mahkeme adı; tarafların ad-soyad/unvan, adres ve TC/vergi no; varsa vekil bilgisi; davanın konusu ve dava değeri; **vakıaların açık özeti** (a-h bentleri); ileri sürülen her vakıanın **hangi delille ispat edileceği** (m.119/1-f, delil bağlama); **dayanılan hukuki sebepler**; **açık talep sonucu**; imza.
2. **Eksiklik sonucu** (m.119/2): Bazı unsurlardaki eksiklik için bir haftalık kesin süre verilir; tamamlanmazsa dava açılmamış sayılır. Vakıa ve talep sonucu gibi çekirdek unsurlar bu kapsamdadır.
3. **Talep sonucu tasarımı**: Eda davasında miktar/ifa açık; **belirsiz alacak** (m.107) veya **kısmi dava** (m.109) tercihi bilinçli yapılır — belirsiz alacakta sonradan artırım faiz ve zamanaşımı bakımından avantajlıdır.
4. **Delil bağlama disiplini**: Her vakıanın altına dayandığı delil (senet, tanık, bilirkişi, keşif, yemin) yazılır; "her türlü delil" ibaresi tek başına yetersiz sayılabilir; senetle ispat zorunlu vakıada (m.200) tanık delili sınırlıdır.
5. **Harç ve gider avansı**: Dava değerine göre nispi/maktu harç ve gider avansı (m.120) yatırılır; eksikse dava şartı eksikliği (m.114/1-g) doğar.

Ara sonuç: Unsur kontrol listesi tamamlanmadan dilekçe sonuçlandırılmaz.

## Çıktı modülleri
- m.119 unsur kontrol listesi (var/eksik).
- Vakıa–delil eşleştirme tablosu.
- Talep sonucu (faiz/masraf/vekâlet ücreti dâhil) ve [doldurulacak] yer tutucular.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

