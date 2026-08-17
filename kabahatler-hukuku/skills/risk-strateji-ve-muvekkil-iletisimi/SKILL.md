---
argument-hint: ''
description: Birden çok seçeneğin (başvuru, ödeme, itiraz, bekleme) sonuçlarını tartıp
  bir risk haritası çıkarmak ve müvekkile sade dille tavsiye iletmek gerektiğinde
  kullanılır.
name: risk-strateji-ve-muvekkil-iletisimi
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk-Strateji ve Müvekkil İletişimi

## Görev
Dosyadaki tüm seçenekleri olasılık-maliyet-sonuç ekseninde tartmak, bir risk haritası ve eylem planı çıkarmak, müvekkile anlaşılır bir tavsiye sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin önceliği ne: maliyeti düşürmek mi, sicili/itibarı korumak mı, ilkesel itiraz mı?
- Cezanın tutarı ve müvekkilin ekonomik durumu nedir?
- Sübut ve sakatlık iddialarının gücü ne düzeyde?
- Süreler ne durumda (başvuru/itiraz/peşin ödeme)?

## Denetim şeması
1. **Seçeneklerin haritası:** (a) Süresinde peşin ödeme (1/4 indirim — 5326 m.17/6); (b) sulh ceza hâkimliğine başvuru (m.27); (c) başvuru + itiraz (m.29); (d) zamanaşımını bekleyip infaz edilemezlik (m.21). Her seçeneğin olasılık ve maliyetini yaz.
2. **Sübut/sakatlık değerlendirmesi:** Yetki-şekil sakatlığı ve zamanaşımı varsa başvuru şansı yüksektir; sübut güçlü ve sakatlık yoksa indirimli ödeme rasyoneldir.
3. **Maliyet analizi:** Başvuruda harç/masraf ve red riski; ödemede indirim kazancı; gecikmede tahsil/haciz ve yerine getirme zamanaşımı dengesi.
4. **İtibar/ikincil etkiler:** Ruhsat, faaliyet, tekrar/sicil etkileri varsa idari yargı boyutunu (m.27/8) gözet.
5. **Tavsiye ve onay:** Tek bir önerilen yolu, gerekçesini ve alternatifini sun; müvekkilin bilgilendirilmiş onayını al, süre uyarısını yaz.
6. **Ara sonuç:** Karar verilen yolu takvime bağla ve sorumluyu belirle.

İspat ve süre belirsizliklerini açıkça paylaş; kesin sonuç vaadinden kaçın.

## Çıktı modülleri
- Risk haritası tablosu (seçenek × olasılık × maliyet × sonuç).
- Müvekkile sade dilde bilgilendirme/tavsiye notu.
- Eylem planı ve süre takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

