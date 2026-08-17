---
argument-hint: ''
description: Zenginleşenin yaptığı zorunlu/faydalı/lüks giderlerin mahsubu ile hukuka
  veya ahlaka aykırı amaçla yapılan kazandırmalarda iadenin reddi söz konusu olduğunda
  kullanılır.
name: giderler-ve-iade-engelleri
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


# Giderler, Mahsup ve İade İsteyememe Halleri

## Görev
İade alacaklısının talebine karşı zenginleşenin gider iadesi haklarını (TBK m.80) ve iadeyi tümden engelleyen halleri (TBK m.78/2 ve m.81) denetlemek; bu savunmaların çoğu davanın miktarını veya kaderini belirlediği için ihtarname ve dilekçe aşamasında öne alınmalıdır.

## Soğuk başlangıç (intake)
- Zenginleşen, iade edeceği şey için masraf/gider yaptı mı; türü ne (zorunlu, faydalı, lüks)?
- Kazandırma hukuka veya ahlaka aykırı bir amaç taşıyor muydu (rüşvet, yasak iş, vb.)?
- Ödeme zamanaşımına uğramış bir borç ya da ahlaki ödev için mi yapıldı?
- Lüks gider için söküp alma mümkün mü?

## Denetim şeması
1. **Gider türlerini ayır (m.80).** Zorunlu giderler (şeyin korunması için kaçınılmaz) ve faydalı giderler (değer artıran) iade alacaklısından istenebilir; lüks (zevki için) giderler istenemez ama zenginleşen, asıl şeye zarar vermeden söküp alabilir.
2. **İyiniyet etkisi.** İyiniyetli zenginleşenin faydalı giderleri geri verme anındaki değer artışı ölçüsünde; kötüniyetli zenginleşenin gider hakları sınırlıdır. Gider alacağı, iade borcundan mahsup edilir.
3. **Hukuka/ahlaka aykırı amaç (m.81).** Hukuka veya ahlaka aykırı bir sonucun gerçekleşmesi amacıyla verilen şey geri istenemez ("temiz el" ilkesi). Hâkim, bu şeyin Devlet Hazinesine gelir kaydedilmesine karar verebilir.
4. **m.81 sınırı.** İade yasağı, verenin de aykırılığa katıldığı hallerde işler; salt karşı tarafın amacının ahlaka aykırı olması her zaman iadeyi kapatmaz. Olayın somut ahlaki/hukuki değerlendirmesi yapılır.
5. **Geçerli sayılan ifalar (m.78/2).** Zamanaşımına uğramış borcun ödenmesi ve ahlaki ödevin ifası geri istenemez; bunlar iade engeli olarak ayrıca işaretlenir.
6. **İspat ve ara sonuç.** Giderleri ve türünü zenginleşen; aykırı amacı (m.81) iadeye karşı çıkan taraf ispatlar. Ara sonuç: net iade miktarı (gider mahsubu sonrası) ve iadenin tümden reddedilip reddedilmeyeceği.

## Çıktı modülleri
- Gider türü-mahsup tablosu.
- m.81 (ahlaka aykırılık) savunma/karşı savunma notu.
- İade engeli değerlendirmesi ve sonuç senaryosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

