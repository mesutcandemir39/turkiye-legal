---
argument-hint: ''
description: Kira dosyasında kiraya veren veya kiracı vekili olarak strateji kurarken,
  dava ile sulh/uzlaşma arasında seçim yaparken, riskleri tartarken ya da müvekkile
  durumu sade dille anlatırken bu beceriyi kul
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
Kira dosyasında tarafın (kiraya veren/kiracı) konumunu bütüncül değerlendirmek; dava, icra, sulh ve arabuluculuk seçeneklerini süre-maliyet-başarı ekseninde tartmak; müvekkile gerçekçi, sade ve doğru bir tablo sunmak.

## Soğuk başlangıç (intake)
- Müvekkil hangi taraf, asıl hedefi ne (tahliye, bedel, süre kazanma)?
- Eldeki belgeler güçlü mü; zayıf noktalar neler?
- Karşı tarafın muhtemel tutumu ve ödeme gücü?
- Zaman baskısı var mı (ihtiyaç, satış, yeni kiracı)?

## Denetim şeması
1. **Pozisyon analizi**: Uygulanabilir tahliye/talep sebebi başına şekil-süre-ispat şartlarının somut olayda tamam olup olmadığı; en güçlü dayanağın seçimi.
2. **Yol karşılaştırması**: (a) İlamsız tahliye icrası — hızlı ama itirazla genel yargıya düşme riski; (b) tahliye davası — sonuç kesin ama süre uzun; (c) dava şartı arabuluculuk/sulh — hız ve tahsil avantajı, esneklik. Her yolun süre, harç/masraf ve tahsil edilebilirlik riski tartılır.
3. **Risk haritası**: Hak düşürücü sürenin kaçırılması, geçersiz tahliye taahhüdü, eksik ihtar, emredici hükme aykırı sözleşme kaydı, yeniden kiralama yasağı (m.355) gibi tipik tuzaklar işaretlenir.
4. **Karşı tarafın savunması**: Olası def'iler (ödeme, ihtarın geçersizliği, ihtiyacın samimi olmaması) önceden listelenir; her birine yanıt hazırlanır.
5. **Müvekkil iletişimi**: Hukuki dil sadeleştirilerek; kesinlik vaadi verilmeden, en iyi/orta/kötü senaryo ve tahmini süre-maliyet aktarılır; karar müvekkile bırakılır.
6. **Ara sonuç**: Önerilen strateji + gerekçe + bir sonraki somut adım ve süre.

## Çıktı modülleri
- Senaryo bazlı strateji notu (en iyi/orta/kötü).
- Risk ve tuzak kontrol listesi.
- Müvekkile yönelik sade bilgilendirme metni.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

