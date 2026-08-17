---
argument-hint: ''
description: Tıbbi uyuşmazlıkta dava dilekçesi, onam formu, sağlık hizmeti sözleşmesi
  veya idareye başvuru gibi belgelerin iskeletini üretmek için kullanılır; yer tutucu
  disipliniyle hazır taslak sağlar.
name: dilekce-sozlesme-taslagi
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe, Sözleşme ve Başvuru Taslağı

## Görev
Tıbbi uyuşmazlığa uygun usul ve içerikte dilekçe, sözleşme veya başvuru taslağını, doğrulanması gereken her veriyi [doldurulacak] yer tutucuyla işaretleyerek üretmek.

## Soğuk başlangıç (intake)
1. Hangi belge gerekli: dava dilekçesi, idari başvuru, onam formu, hizmet sözleşmesi?
2. Yargı kolu adli mi idari mi; mahkeme/merci belli mi?
3. Taraflar, vekiller ve talep sonucu net mi?
4. Dayanak vakıalar ve deliller listelendi mi?

## Denetim şeması
1. **Belge türü ve usul çerçevesi**: Adli dava → HMK m.119 dava dilekçesi zorunlu unsurları. İdari dava → İYUK m.3 dilekçe unsurları. Onam → Hasta Hakları Yönetmeliği m.15/24-31 içerik standardı.
2. **Dava dilekçesi mimarisi**: Mahkeme, taraflar, dava değeri/harç, açık talep sonucu, vakıaların sıralı anlatımı, hukuki sebepler (TBK m.49/112/502, TCK ilgili maddeler), her vakıanın dayandığı delil (HMK m.119/f.1-e,f).
3. **Talep sonucu**: Maddi tazminat kalemleri (tedavi gideri, iş gücü/destek kaybı), manevi tazminat, faiz başlangıcı ve türü, yargılama gideri ve vekâlet ücreti.
4. **Onam/sözleşme taslağı**: Aydınlatma içeriği (tanı, yöntem, riskler, alternatifler, başarısızlık olasılığı), tarih ve makul süre, imza alanları; sorumluluğu tamamen kaldıran şartların geçersizliği (TBK m.115).
5. **Yer tutucu disiplini**: Tüm tarih, tutar, ad ve teknik veri [doldurulacak] olarak işaretlenir; uydurma veri girilmez.
6. **Ara sonuç**: Zorunlu unsur eksikse dilekçe reddi/HMK m.119/2 süre verme riski; taslakta bu kontrol yapılır.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlıklı, yer tutuculu)
- Zorunlu unsur kontrol listesi (HMK m.119 / İYUK m.3)
- Talep sonucu ve faiz bloğu
- Doldurulacak veri listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

