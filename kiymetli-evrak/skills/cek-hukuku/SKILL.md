---
argument-hint: ''
description: Çekin unsurlarını, ibraz ve karşılıksız işlemlerini, çek düzenleme yasağı
  ve adli para cezasını ele almak; çekle ilgili takip, savunma veya 5941 sayılı Kanun
  kapsamında ceza riski değerlendirmesinde k
name: cek-hukuku
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


# Çek Hukuku ve Karşılıksız Çek

## Görev
Çekin geçerliliğini, ibraz ve ödeme sürecini, karşılıksız çıkması halinde hukuki ve cezai sonuçlarını değerlendirmek; alacaklı için tahsil/takip, keşideci için savunma stratejisi kurmak.

## Soğuk başlangıç (intake)
- Çek üzerinde keşide tarihi, bedel, banka (muhatap) ve imza tam mı; çek "ileri tarihli" mi?
- Çek bankaya ibraz edildi mi; karşılıksızdır işlemi yapıldı mı, kısmi ödeme var mı?
- Müvekkil keşideci mi, lehtar/hamil mi, ciranta mı?
- Çek hesabı kime ait, tüzel kişi ise imza yetkilisi kim?

## Denetim şeması
1. Şekil şartları: TTK m.780 unsurları (çek kelimesi, kayıtsız şartsız ödeme emri, muhatap banka, ödeme yeri, keşide yeri-tarihi, imza). Eksiklik m.781 ile değerlendirilir; bazı eksiklikler yorum kurallarıyla tamamlanır.
2. İbraz süreleri: TTK m.796 — aynı yerde 10 gün, farklı yerde 1 ay; sürede ibraz başvurma hakkının korunması için şarttır. Çekte vade yoktur; gösterildiğinde ödenir (m.795).
3. Karşılıksız işlemi: banka kısmen/tamamen karşılıksızlığı çek arkasına/sisteme işler (5941 s. K. m.3). Hamil sürede ibraz ve karşılıksız işlemi şartını yerine getirmelidir.
4. Cezai sonuç: karşılıksız çekte, hamilin şikâyeti üzerine keşideci hakkında adli para cezası ve çek düzenleme/çek hesabı açma yasağı uygulanır (5941 s. K. m.5). Şikâyet süresi ve çek bedelinin ödenmesi halinde davanın/cezanın akıbeti m.5/10-11 çerçevesinde değerlendirilir. İspat yükü ve fail: hesap sahibi gerçek/tüzel kişi ayrımına dikkat.
5. Takip yolu: çek kambiyo senedi olduğundan kambiyo senetlerine özgü takip yapılır (İİK m.167 vd.); menfi tespit/istirdat için İİK m.72.
6. Ara sonuç: ibraz süresi kaçırılmışsa cezai süreç ve cirantalara başvuru zayıflar; çek yine TTK m.808 (3 yıl) zamanaşımına dek kambiyo takibine konu olabilir, sebep alacağı saklıdır.

## Çıktı modülleri
- Çek geçerlilik ve ibraz takvimi tablosu.
- Karşılıksız çek şikâyet dilekçesi taslağı (5941 m.5) — bedel/tarih [doldurulacak].
- Keşideci için savunma notu (yetki, ileri tarih, ödeme defi, şikâyet süresi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

