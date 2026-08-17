---
argument-hint: ''
description: Hukuka aykırı bir idari işlemin iptali için dava şartlarını, ehliyet-menfaat
  ilişkisini, süreyi ve esas sebeplerini kurgulamak amacıyla kullanılır; idari işleme
  karşı dava açılacağında temel beceridir
name: iptal-davasi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İptal Davası Stratejisi

## Görev
İdari işlemin iptali için davayı baştan sona kurgulamak: dava şartları, ehliyet ve menfaat, süre, görev-yetki ve esas iptal sebepleri. İYUK m.2/1-a çerçevesinde iptal davasının iskeletini üretir.

## Soğuk başlangıç (intake)
1. Dava edilecek kesin/yürütülebilir bir işlem var mı; tebliğ/öğrenme tarihi nedir?
2. Müvekkilin işlemle ihlal edilen kişisel, güncel ve meşru menfaati nedir?
3. İYUK m.11 üst makama başvuru yapıldı/yapılacak mı; zımni ret oluştu mu?
4. İşlem bireysel mi düzenleyici mi (yönetmelik/genelge)?

## Denetim şeması
1. **Dava türü.** İptal davası: yetki, şekil, sebep, konu, maksat yönünden hukuka aykırı işlemin iptali (İYUK m.2/1-a). Menfaat ihlali yeterlidir; subjektif hak şart değildir.
2. **Ehliyet ve menfaat.** Davacının işlemle kişisel, güncel ve meşru bir menfaat ilişkisi bulunmalı. Düzenleyici işlemlerde menfaat daha geniş yorumlanır.
3. **Süre.** Genel dava açma süresi 60 gün (İYUK m.7/1); tebliğ/ilan/öğrenme tarihinden işler. İYUK m.11 başvurusu süreyi durdurur; 60 gün sessizlik zımni rettir (m.10/m.11). Düzenleyici işlemde hem düzenlemeye hem uygulama işlemine karşı dava imkânı (m.7/4).
4. **Görev ve yetki.** Kural olarak idare mahkemesi; ilk derecede Danıştay'da görülecek işlemler (2575 sayılı K. ile belirli düzenleyici işlemler) ayrıdır. Yer yönünden yetki İYUK m.32 vd. (işlemi yapan idarenin bulunduğu yer kuralı ve özel yetki kuralları).
5. **Esas sebepler.** Beş unsur denetiminden (bkz. unsur denetimi becerisi) çıkan aykırılıkları hukuki sebep olarak diz; her birini madde ve delille bağla.
6. **Yürütmenin durdurulması.** İYUK m.27/2: telafisi güç veya imkânsız zarar **ve** açık hukuka aykırılık koşullarını birlikte gerekçelendir.
7. **Ara sonuç.** Dava şartları karşılanıyorsa esas sebeplerle iptal talebi; karşılanmıyorsa eksik giderme yolu (m.11 başvurusu, süre, ehliyet düzeltimi).

## Çıktı modülleri
- Dava şartları kontrol listesi (süre, ehliyet, menfaat, görev, yetki).
- İptal sebepleri ile madde/delil eşleşmesi.
- Yürütmenin durdurulması gerekçesi taslağı.
- Dilekçe için talep sonucu önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

