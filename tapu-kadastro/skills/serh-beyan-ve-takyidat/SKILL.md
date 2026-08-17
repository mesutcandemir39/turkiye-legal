---
argument-hint: ''
description: Tapu kaydına kişisel hak, tasarruf kısıtlaması, aile konutu, satış vaadi,
  kira, önalım gibi bir şerh veya beyan işlenmesi, terkin edilmesi ya da var olan
  takyidatın hukuki etkisinin değerlendirilmesi
name: serh-beyan-ve-takyidat
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Şerh, Beyan ve Takyidat İşlemleri

## Görev
Tapu kaydına işlenecek/terkin edilecek şerh ve beyanları doğru hukuki dayanakla belirlemek ve mevcut takyidatların üçüncü kişilere etki gücünü çözümlemek.

## Soğuk başlangıç (intake)
- İşlem türü ne: şerh/beyan tesisi mi, terkin mi, mevcut takyidatın yorumu mu?
- Hangi hak: taşınmaz satış vaadi, kira, önalım/alım/geri alım, aile konutu, ihtiyati tedbir/haciz?
- Şerhin amacı kişisel hakkı güçlendirmek mi, tasarrufu kısıtlamak mı, durumu açıklamak mı?
- Lehine/aleyhine işlenecek kişi ve dayanak belge (sözleşme, mahkeme kararı) nedir?

## Denetim şeması
1. **Şerh türünü ayır (TMK m.1009-1010).** (a) Kişisel hakların şerhi: satış vaadi, kira, önalım/alım/geri alım, bağışlamadan dönme — şerhle kişisel hak güçlendirilir, sonraki maliklere ileri sürülebilir hale gelir (TMK m.1009). (b) Tasarruf yetkisi kısıtlamaları: ihtiyati tedbir, haciz, konkordato mühleti, çekişmeli hakların korunması (TMK m.1010). (c) Geçici tescil şerhi (TMK m.1011).
2. **Beyanı ayır.** Beyanlar hak kurmaz; mevcut fiili/hukuki durumu açıklar (ör. aile konutu beyanı, eklenti, kamulaştırma şerhi). Aile konutu için TMK m.194 — diğer eşin rızası ve şerh imkânı.
3. **Etki gücünü değerlendir.** Şerhli kişisel hak, taşınmazı sonradan edinen herkese karşı ileri sürülebilir; şerhsiz kişisel hak yalnızca taraf arasında etkilidir. İhtiyati tedbir/haciz şerhi sonraki kazanımları sakatlar.
4. **Süre ve geçerlilik.** Bazı şerhlerin süreyle sınırı vardır (ör. satış vaadi şerhinin etkisi — 2644 sayılı Tapu Kanunu ve TMK uygulaması; süre dolunca terkin edilebilir). Şerhin dayanağı sona ererse terkin istenir.
5. **Usul.** Şerh/terkin tapu müdürlüğünde talep ve dayanak belgeyle; mahkeme kararına dayanan şerhlerde ilam/tedbir kararı gerekir. Reddi halinde Tapu Kanunu m.26 işlemlerine karşı yol ve dava.
6. **Ara sonuç.** İstenen sonuç için şerh mi beyan mı, dayanağı ve etkisi netleştirilir.

## Çıktı modülleri
- Şerh/beyan türü–dayanak–etki tablosu.
- Tapu müdürlüğü talep dilekçesi veya terkin talebi iskeleti.
- Mevcut takyidatların alıcı/müvekkil açısından risk değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

