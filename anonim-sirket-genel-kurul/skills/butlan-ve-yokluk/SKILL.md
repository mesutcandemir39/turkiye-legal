---
argument-hint: ''
description: Genel kurul kararinin iptal degil butlan veya yokluk yaptirimina tabi
  oldugu degerlendirilecekse; vazgecilemez haklara, sermayenin korunmasina aykirilik
  ve cagri yoklugu gibi hallerde suresiz tespit d
name: butlan-ve-yokluk
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
  version: 0.1.0
user-invocable: true
---


# Butlan ve Yokluk Tespiti

## Görev
İptal edilebilirlik eşiğini aşan ağır sakatlıkları — butlan (m.447) ve yokluk — teşhis etmek; süresiz ileri sürülebilen tespit davası stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Sakatlık, pay sahibinin vazgeçilemez/müktesep haklarına mı, sermayenin korunmasına mı, AŞ'nin temel yapısına mı ilişkin?
2. Çağrı hiç yapılmadı mı veya toplantı/karar iradesi hiç oluşmadı mı (yokluk göstergeleri)?
3. Karar üzerine işlemler yapıldı, tescil edildi mi (iyiniyetli üçüncü kişi sorunu)?
4. Aynı sakatlık için üç aylık iptal süresi kaçırıldı mı?

## Denetim şeması
1. **Butlan sebepleri (m.447):** GK kararı özellikle; (a) pay sahibinin GK'ye katılma, asgari oy, dava ve kanundan kaynaklanan **vazgeçilmez haklarını sınırlandıran** veya ortadan kaldıran, (b) pay sahibinin **bilgi alma, inceleme ve denetleme** haklarını kanunen izin verilen ölçü dışında kısıtlayan, (c) AŞ'nin **temel yapısını bozan** veya **sermayenin korunması** hükümlerine aykırı kararlardır. Bu hâllerde karar batıldır; herkes, süresiz olarak tespit davası açabilir.
2. **Yokluk:** Kararın hukuken var sayılabilmesi için gereken kurucu unsurların hiç bulunmaması hâli yokluktur (örn. hiç çağrı yapılmadan ve çağrısız toplantı şartları da olmadan "karar" alınması, gerçek bir toplantı/oylama iradesinin hiç oluşmaması). Yokluk da süresiz ileri sürülür.
3. **İptalle sınır:** Salt usul aykırılıkları (süre, gündem, nisap hatası) kural olarak iptal sebebidir; bunları butlana çevirmemeye dikkat et. Butlan/yokluk dar yorumlanır, aksi hukuki güvenliği zedeler.
4. **Yargı yolu:** Tespit/butlan davası asliye ticaret mahkemesinde, şirket merkezinde, şirkete karşı açılır; m.448-450 hükümleri kıyasen uygulanır. Hukuki yarar dava şartıdır.
5. **İspat yükü/ara sonuç:** Butlan/yokluk sebebini ileri süren ispatlar; mahkeme re'sen de gözetebilir. Karar baştan itibaren hüküm doğurmaz; ancak iyiniyetli üçüncü kişilerin tescile dayanan kazanımları ayrıca değerlendirilir.

## Çıktı modülleri
- Butlan/yokluk sebebi nitelendirme notu (m.447 alt-bent eşleştirmesi).
- Tespit davası dilekçe iskeleti (hukuki yarar vurgusuyla).
- İptal/butlan/yokluk ayrım tablosu ve süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

