---
argument-hint: ''
description: Borç uyuşmazlığında dava/sulh kararı, kazanma şansı, maliyet-tahsilat
  riski değerlendirilirken ve müvekkile yalın bir yol haritası sunulurken kullanılır.
name: risk-strateji-ve-iletisim
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Borç uyuşmazlığında hukuki ve pratik riskleri tartmak, dava/sulh/uyarlama seçenekleri arasında strateji önermek ve müvekkile anlaşılır bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin önceliği ne: para tahsili, ilişkiyi sürdürme, hızlı çözüm, risk minimizasyonu?
- Karşı tarafın ödeme gücü ve mal varlığı durumu biliniyor mu?
- Elde edilebilir delil ne kadar güçlü; tanık/belge eksiği var mı?
- Zaman baskısı veya zamanaşımı riski var mı?

## Denetim şeması
1. Hukuki güç analizi: Talebin dayanağı (sözleşme/haksız fiil/sebepsiz zenginleşme), unsurların kanıtlanabilirliği, karşı tarafın olası def'ileri (zamanaşımı m.161, ifa, takas m.139) ve emredici hüküm engelleri.
2. Tahsilat/icra riski: Lehe karar alınsa bile İİK çerçevesinde tahsil edilebilirlik; borçlunun aciz/iflas riski, teminat ve haciz imkânları, ihtiyati haciz (İİK m.257) gereği.
3. Maliyet-fayda: Harç ve yargılama gideri (HMK m.323), vekâlet ücreti riski, yargılama süresi; küçük alacakta dava şartı arabuluculuk ve sulhün avantajı.
4. Strateji seçimi: İhtarname/ödeme baskısı, dava şartı arabuluculuk, sulh/uyarlama (m.138) ya da dava; menfi tespit ile savunmaya geçiş. Süre korumak için belirsiz alacak/ihtiyati tedbir.
5. Çatışma ve etik: Çıkar çatışması taraması, sır saklama; iletişimde gerçekçi beklenti yönetimi, sonucu garanti etmeme.
6. Ara sonuç: Önerilen senaryo(lar), olasılık aralığı ve eylem sıralaması.

## Çıktı modülleri
- Risk matrisi (hukuki güç x tahsilat x maliyet).
- Strateji önerisi ve alternatif senaryolar.
- Müvekkile yalın dille yol haritası ve karar noktaları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

