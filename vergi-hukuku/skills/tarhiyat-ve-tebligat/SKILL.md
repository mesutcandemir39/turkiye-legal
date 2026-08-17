---
argument-hint: ''
description: İkmalen, re'sen veya idarece yapılan tarhiyatın hukuka uygunluğunu ve
  tebligatın geçerliliğini denetlemek; ihbarnamenin biçim ve süre yönünden incelenmesi
  gerektiğinde kullanılır.
name: tarhiyat-ve-tebligat
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
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tarhiyat Türleri ve Tebligat Denetimi

## Görev
Mükellefe tebliğ edilen vergi/ceza ihbarnamesindeki tarhiyatın türünü, şartlarının oluşup oluşmadığını ve tebligatın geçerliliğini denetleyerek savunma veya dava stratejisinin temelini kurmak.

## Soğuk başlangıç (intake)
1. İhbarnamede tarhiyat türü belirtilmiş mi (ikmalen / re'sen / idarece)?
2. Re'sen tarh ise dayanak (defter ibraz etmeme, takdir komisyonu, VTR) nedir?
3. İhbarname kime, nasıl ve hangi tarihte tebliğ edildi?
4. Matrah farkının dayanağı (vergi tekniği raporu, tutanak) elde var mı?
5. Tarh edilen verginin ait olduğu dönem ve zamanaşımı durumu nedir?

## Denetim şeması
1. **Tarh türü tespiti:** Beyana dayanan tarh asıl usuldür; ek tarhiyatta ikmalen tarh (VUK m.29 — defter/belgeye veya kanuni ölçülere dayanan matrah farkı) ile re'sen tarh (VUK m.30 — matrahın defter-belge-kanuni ölçülerle tespiti mümkün olmadığında) ayrımını yap. Türün yanlış seçimi tek başına iptal sebebi olabilir.
2. **Re'sen takdir sebebi:** VUK m.30/2 bentlerinden hangisinin gerçekleştiğini doğrula (beyanname verilmemesi, defter tutulmaması/ibraz edilmemesi, kayıtların gerçeği yansıtmaması). Sebep yoksa re'sen tarh sakattır.
3. **Takdir/rapor dayanağı:** Matrah farkı vergi inceleme raporu (VUK m.140) veya takdir komisyonu kararına (VUK m.72 vd.) dayanmalı; gerekçesiz, somut tespite dayanmayan takdir denetlenir.
4. **İhbarnamenin unsurları:** VUK m.35 — ihbarnamede bulunması gereken zorunlu bilgiler (verginin nev'i, dönem, matrah, oran, dayanak, vergi/ceza miktarı, itiraz yolları). Eksiklik savunulabilirliği etkiler.
5. **Tebligat geçerliliği:** VUK m.93-109. Tebligat usulsüzse süre başlamaz; muhatap dışı kişiye tebliğ, adres yokluğu, ilanen tebliğ şartlarının (VUK m.103) oluşmaması incelenir. Ara sonuç: süre işlemeye başladı mı?
6. **İspat yükü:** Tarhiyatın maddi dayanağını idare ispatlar; mükellef tebligat/şekil sakatlığını ileri sürerse onu ispatlar.

## Çıktı modülleri
- Tarhiyat tür-şart uygunluk tablosu (sebep / dayanak / sonuç).
- Tebligat geçerlilik kontrol listesi ve süre başlangıç tarihi.
- İhbarname şekil denetimi notu (VUK m.35 eksiklik listesi).
- Savunma/dava argüman taslağı ve istenecek rapor listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

