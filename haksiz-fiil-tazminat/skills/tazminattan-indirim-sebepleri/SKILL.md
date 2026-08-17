---
argument-hint: ''
description: Karşı taraf zarar görenin kendi kusurunu, zararı ağırlaştıran davranışını
  veya failin az kusurunu ileri sürerek tazminatın azaltılmasını istediğinde; indirim
  sebeplerini değerlendirmek için kullanılır
name: tazminattan-indirim-sebepleri
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


# Tazminattan İndirim Sebepleri

## Görev
TBK m.52'deki indirim sebeplerini (zarar görenin kendi kusuru/müterafik kusur, durumu ağırlaştırması, rıza) ve m.51'in kusur-zarar dengesini denetleyerek tazminat miktarının hakkaniyetle azaltılıp azaltılmayacağını belirlemek. İndirim, sorumluluğu kaldırmaz; miktarı düşürür.

## Soğuk başlangıç (intake)
- Zarar gören kendi davranışıyla zarara katkıda bulundu mu (örn. emniyet kemeri, talimata aykırılık)?
- Zarar görenin zararı azaltma yükümünü ihmal ettiği bir durum var mı?
- Failin kusuru hafif mi; tazminat onu yoksulluğa düşürür mü?
- Zarar görenin rızası ya da riski göze alması söz konusu mu?

## Denetim şeması
1. **Müterafik (birlikte) kusur (m.52/1).** Zarar gören kendi kusuruyla zararın doğmasına/artmasına yol açmışsa hâkim tazminatı indirir; katkı oranı somut olarak belirlenir.
2. **Zararı azaltma yükümü.** Zarar gören, makul önlemlerle zararı azaltabilecekken kaçınmışsa artan kısımdan sorumlu tutulmaz (dürüstlük kuralı TMK m.2 ile birlikte değerlendirilir).
3. **Durumu ağırlaştıran davranış.** Zarar görenin zararı genişleten eylemleri indirim sebebidir; illiyeti tümden kesiyorsa sorumluluk kalkar.
4. **Hafif kusur ve yoksulluk (m.52/2).** Fail hafif kusurluysa ve tazminat onu yoksulluğa düşürecekse, hakkaniyet gerektiriyorsa hâkim tazminatı indirebilir; bu istisnai bir denkleştirmedir.
5. **Rıza ve riski göze alma.** Geçerli rıza aykırılığı kaldırabilir (m.63); kısmî/örtülü rıza ise indirim sebebi olabilir.
6. **Ara sonuç ve ispat.** İndirim sebeplerini ileri süren ve katkı oranını ispatlayan taraf (genelde davalı) yükü taşır (TMK m.6). İndirim oranı gerekçelendirilir; kalan tazminat miktarı netleştirilir.

## Çıktı modülleri
- İndirim sebepleri kontrol listesi (sebep + katkı oranı + dayanak).
- Müterafik kusur değerlendirme notu.
- Net tazminat etkisi hesabı (indirim öncesi/sonrası).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

