---
argument-hint: ''
description: Göç İdaresi veya Bakanlık işlemine (ikamet ret, sınır dışı, çalışma izni
  ret, vatandaşlık ret) karşı dava açılacağında; görevli-yetkili mahkemeyi, süreyi
  ve yürütmenin durdurulmasını saptamak için kul
name: idari-dava-yargi-yolu
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Dava ve Yargı Yolu

## Görev
Göç ve yabancılar alanındaki idari işlemlere karşı doğru yargı yolunu, görevli-yetkili mahkemeyi ve süreyi belirlemek; iptal davası ve yürütmenin durdurulması stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem türü nedir (ikamet, sınır dışı, gözetim, çalışma izni, vatandaşlık)?
2. İşlemin tebliğ/öğrenme tarihi nedir?
3. İdari itiraz/komisyon yolu öngörülmüş mü, tüketildi mi?
4. Yabancı gözetim altında mı, yürütmenin acilen durdurulması gerekiyor mu?

## Denetim şeması
1. **Yargı yolu ayrımı**: Çoğu işlem idari yargı (İYUK m.2 iptal davası). İstisna: idari gözetim kararına karşı **sulh ceza hâkimliği** (YUKK m.57/6); ceza irtibatlı (göçmen kaçakçılığı TCK m.79, insan ticareti m.80) konular adli yargı.
2. **Görev ve yetki**: İdare mahkemesi görevli; sınır dışı kararına karşı dava tek hâkimli idare mahkemesinde görülür (YUKK m.53). Yetki, işlemi tesis eden idarenin/yabancının bulunduğu yer üzerinden İYUK m.32-33 ile belirlenir.
3. **Süreler**: Genel iptal davası süresi İYUK m.7 — 60 gün; sınır dışı kararına karşı YUKK m.53'teki özel kısa süre; idari gözetime karşı m.57'deki süre. Süreler işlemden işleme değişir, her dosyada ayrı hesaplanır.
4. **Dava şartları**: İYUK m.2 — ehliyet ve menfaat (yabancı ya da vekili), kesin/yürütülebilir işlem, süre. İdari merci tecavüzü (m.15) ve idari başvuru yolları kontrol edilir.
5. **Yürütmenin durdurulması**: İYUK m.27 — açıkça hukuka aykırılık + telafisi güç/imkânsız zarar; sınır dışıda zaten dava işlemi durdurabilir, çalışma/ikamette YD ayrıca talep edilir.
**Ara sonuç**: Tek bir görevli-yetkili mahkeme, kesin bir son gün ve YD gerekçesi netleştirilir.

## Çıktı modülleri
- Yargı yolu/görev-yetki/süre karar tablosu.
- İptal davası dilekçesi iskeleti (işlem-vakıa-hukuki sebep-YD-talep).
- Süre takvimi ve kanun yolları (istinaf/temyiz) notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

