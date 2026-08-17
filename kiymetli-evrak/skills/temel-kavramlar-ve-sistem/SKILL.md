---
argument-hint: ''
description: Kıymetli evrakın türlerini, kambiyo senedi kavramını ve genel ilkeleri
  ayırt etmek; bir belgenin kıymetli evrak/kambiyo senedi olup olmadığını ve hangi
  rejime tabi olduğunu belirlemek gerektiğinde kul
name: temel-kavramlar-ve-sistem
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
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Önüne gelen belgenin kıymetli evrak olup olmadığını, eğer öyleyse hangi tür (nama, emre, hamiline) ve hangi alt rejim (kambiyo senedi / diğer) içinde bulunduğunu belirlemek; çek-bono-poliçe ayrımını ve uygulanacak temel normları sabitlemek.

## Soğuk başlangıç (intake)
- Belge fiziken hangi senet tipi olarak adlandırılmış (çek, bono/senet, poliçe) ve metinde bu kelime geçiyor mu?
- Senet emre mi, nama mı, hamiline mi düzenlenmiş; üzerinde "emre" veya "emre yazılı değildir" kaydı var mı?
- Bedel, vade, taraflar, imza ve tanzim yeri-tarihi okunabiliyor mu; eksik unsur var mı?
- Belge alacaklı için takip mi, müvekkil için savunma mı amaçlanıyor?

## Denetim şeması
1. Kıymetli evrak tanımı: hak senetten ayrı ileri sürülemiyor/devredilemiyorsa kıymetli evraktır (TTK m.645). Salt ispat belgesi (örn. adi senet, makbuz) bu kapsamda değildir.
2. Tür tayini: senedin devir biçimi nama (m.654), emre (m.824 vd. genel; kambiyoda m.681) ya da hamiline (m.658) midir? Çek ve bono emre senet olarak doğar, aksi kayıtla nama dönüşebilir.
3. Kambiyo senedi süzgeci: senet çek (m.780), bono (m.776) veya poliçe (m.671) tanımına ve şekil şartlarına uyuyor mu? Uyuyorsa kambiyo hukukunun sertleştirilmiş rejimi (mücerretlik, müteselsil sorumluluk, kambiyo takibi) devreye girer.
4. Ara sonuç — eksiklik: zorunlu unsur eksikse kambiyo vasfı yoktur (m.672/m.777/m.781); senet yalnızca adi yazılı delil olur, kambiyo takibi yapılamaz. Beyaz/açık senet ise anlaşmaya aykırı doldurma def'i (m.680) gündeme gelir; ispat yükü bunu ileri sürene aittir.
5. İlke seti: mücerretlik (sebepten soyutluk), şekle bağlılık, kambiyo taahhütlerinin bağımsızlığı (m.677) ve müteselsil sorumluluk (m.724) sonuçlarını not et.

## Çıktı modülleri
- Senet niteliği değerlendirme notu (tip + rejim + dayanak madde).
- Eksik/kusurlu unsur listesi ve kambiyo vasfına etkisi.
- Uygulanacak temel norm haritası (TTK ilgili maddeleri + gerekiyorsa 5941).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

