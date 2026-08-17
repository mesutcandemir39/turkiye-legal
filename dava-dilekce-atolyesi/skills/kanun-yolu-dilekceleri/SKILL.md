---
argument-hint: ''
description: İlk derece kararına karşı istinaf veya temyiz dilekçesi hazırlamak; istinaf
  sebeplerini somutlaştırmak, süre ve kesinlik sınırlarını denetlemek gerektiğinde
  kullanılır.
name: kanun-yolu-dilekceleri
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İstinaf ve Temyiz Dilekçeleri

## Görev
İlk derece veya istinaf kararına karşı kanun yolu dilekçesini kurmak; istinaf sebeplerini somut, gerekçeli ve süresinde ileri sürmek. Yanlış sebep ya da geçmiş süre, kanun yolunun reddini doğurur.

## Soğuk başlangıç (intake)
- Karar hangi mahkemeden, hangi tarihte tebliğ edildi?
- Karar miktar/değer olarak kesinlik sınırının üstünde mi?
- Hangi hukuka aykırılıklar var (maddi/hukuki/usuli)?
- İstinaf mı temyiz mi söz konusu (derece sırası)?

## Denetim şeması
1. Süre ve kesinlik (HMK m.341, m.345): İstinaf süresi kural olarak iki hafta, kararın tebliğinden işler. İstinaf parasal sınırı (m.341) ve temyiz sınırı (m.362) yıllık olarak güncellenir — yürürlükteki tutarı doğrulayın. İYUK'ta istinaf m.45, temyiz m.46.
2. İstinaf sebepleri (HMK m.342, m.355): Dilekçe istinaf sebeplerini içermeli; BAM kural olarak sebeplerle bağlı, kamu düzeni hariç. Sebepleri somutlaştırın: yanlış vakıa tespiti, delil değerlendirme hatası, hukukun yanlış uygulanması, usul hatası (gerekçe yokluğu HMK m.297).
3. Temyiz sebepleri (HMK m.371): Yargıtay yalnızca hukuka aykırılığı denetler; maddi vakıa yeniden incelenmez. Sebepleri hukuk normuna aykırılık ekseninde yazın.
4. Talep: Kararın kaldırılması/bozulması ve (istinafta) yeniden esas hakkında karar veya gönderme.
5. Harç ve ek: Kanun yolu harcı yatırılmalı; dilekçe karar örneğiyle sunulur. Ara sonuç: süre/sınır/sebep uygunsa dilekçe hazır; kesinse müvekkil bilgilendirilir.

## Çıktı modülleri
- İstinaf/temyiz dilekçesi taslağı (sebepler numaralı)
- Süre ve kesinlik sınırı denetim notu
- Sebep-gerekçe eşleşme tablosu
- Harç ve ek evrak kontrol listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

