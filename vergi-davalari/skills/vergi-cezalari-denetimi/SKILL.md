---
argument-hint: ''
description: Vergi ziyaı, usulsüzlük ve özel usulsüzlük cezalarının tipikliğini, kusur
  unsurunu, kat oranını ve indirim imkânlarını ayrı ayrı denetlerken kullanılır.
name: vergi-cezalari-denetimi
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi Cezalarının Denetimi

## Görev
İhbarname ile kesilen idari nitelikteki vergi cezalarını (vergi ziyaı, usulsüzlük, özel usulsüzlük) unsurları, oranı ve uygulanabilir indirimler bakımından denetlemek; ceza ile vergi aslını birbirinden ayırarak savunma kurmak.

## Soğuk başlangıç (intake)
1. Hangi ceza kesildi: vergi ziyaı mı (VUK m.341/344), usulsüzlük mü (m.351-352), özel usulsüzlük mü (m.353, mük.355)?
2. Cezanın oranı/katı ne; üç kat (m.344/2, m.359 fiilleri) uygulandı mı?
3. Fiil tek mi yoksa birden çok dönem/belge mi; tekerrür (VUK m.339) var mı?
4. Daha önce uzlaşma veya ceza indirimi (VUK m.376) talep edildi mi?

## Denetim şeması
1. **Tipiklik.** Her ceza türü için fiilin kanuni tarife uyup uymadığı denetlenir: vergi ziyaı için ziyaın gerçekleşmesi (m.341); usulsüzlük için şekli ödevin ihlali; özel usulsüzlük için belge düzenine aykırılık (fatura/belge alıp vermeme, m.353).
2. **Kusur ve kat.** Vergi ziyaı cezası kural olarak bir kat; VUK m.359'daki kaçakçılık fiilleriyle işlenmişse üç kat (m.344/2). Üç kat uygulamasının dayanağı (sahte belge kullanma/düzenleme tespiti) somut delille aranır.
3. **İndirim ve af mekanizmaları.** VUK m.376 — ihbarnamenin tebliğinden itibaren 30 gün içinde başvuru ile cezada indirim. Uzlaşma (Ek m.1) ile karşılaştır; her iki yol birlikte kullanılamaz, dava hakkıyla ilişkisi tartılır.
4. **Zamanaşımı.** VUK m.374 — ceza kesmede zamanaşımı süreleri (vergi ziyaında 5 yıl, usulsüzlükte 2 yıl) ve başlangıç tarihi denetlenir.
5. **Tek fiil-içtima.** VUK m.336 — aynı fiille hem vergi ziyaı hem usulsüzlük doğmuşsa ağır olanın uygulanması. Ara sonuç: kesilen cezaların ayrı ayrı mı, içtima ile mi değerlendirilmesi gerektiği belirlenir.

## Çıktı modülleri
- Ceza türü / unsur / oran / indirim karşılaştırma tablosu.
- VUK m.376 indirim başvuru taslağı (alternatif: uzlaşma).
- Cezaya özgü iptal gerekçeleri (dilekçeye eklenecek).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

