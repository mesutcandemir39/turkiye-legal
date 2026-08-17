---
argument-hint: ''
description: Krediye bağlanan kefalet, ipotek, taşınır rehni veya banka teminat mektubunun
  geçerlilik şartlarını, kapsamını ve paraya çevrilmesini denetlemek; özellikle kefalette
  şekil ve eş rızası eksikliğini tes
name: teminat-kefalet-ipotek
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Banka Teminatları (Kefalet, İpotek, Rehin, Teminat Mektubu)

## Görev
Bir banka alacağının teminatını (kefalet, ipotek, taşınır rehni, teminat mektubu) geçerlilik, kapsam ve sorumluluk üst sınırı bakımından denetlemek; teminatın paraya çevrilmesinde izlenecek yolu belirlemek.

## Soğuk başlangıç (intake)
- Teminat türü: adi/müteselsil kefalet, ipotek, ticari işletme rehni/taşınır rehni, banka teminat mektubu?
- Kefil/rehin veren gerçek kişi mi; evli ise eş rızası alınmış mı?
- Teminat belirli bir borç için mi yoksa "doğmuş/doğacak tüm borçlar" için mi (üst sınır ipoteği/azami kefalet)?
- Asıl borç muaccel mi; temerrüt ve ihtar süreci tamam mı?

## Denetim şeması
1. **Kefalette geçerlilik (TBK m.583)**: Kefalet sözleşmesi yazılı şekilde olmalı; kefilin sorumlu olacağı azami miktar, kefalet tarihi ve müteselsil kefil olunuyorsa bu husus kefilin **el yazısıyla** belirtilmelidir. Bu unsurların eksikliği kefaleti geçersiz kılar.
2. **Eşin rızası (TBK m.584)**: Eşlerden biri diğerinin yazılı rızası olmadan kefil olamaz; rıza en geç sözleşme kurulurken alınmalıdır. Ticari işletmeyle ilgili kefaletlerde m.584/3 istisnası (ticaret siciline kayıtlı tacirin verdiği kefalet vb.) ayrıca değerlendirilir.
3. **Kefaletin kapsamı ve süre**: Müteselsil kefilden doğrudan talep şartları (TBK m.586), kefile rücu, alacaklının özen ve teminatları koruma yükümlülüğü (TBK m.594) incelenir. Belirsiz süreli kefalette m.598 fesih imkânı kontrol edilir.
4. **İpotek/rehin**: İpoteğin tapuda tesisi, üst sınır (limit) ipoteğinde kapsam, fekki; taşınır/ticari işletme rehninde tescil. Paraya çevirme İİK m.145 vd. (rehnin paraya çevrilmesi yolu) ile yürür; krediye dayalı rehinde takip yolu doğru seçilmelidir.
5. **Teminat mektubu**: Banka teminat mektubu kural olarak bağımsız (garanti) niteliktedir; ilk talepte ödeme kaydı, def'ilerden bağımsızlık, süre ve istisnaen kötüniyet/açık hukuka aykırılık (def'i hakkı) değerlendirilir. Ara sonuç olarak teminatın geçerli/geçersiz olduğunu, kapsamını ve uygulanabilir takip yolunu yaz.

## Çıktı modülleri
- Teminat geçerlilik kontrol listesi (şekil, üst sınır, eş rızası, tescil).
- Sorumluluk kapsamı ve üst sınır analizi.
- Paraya çevirme/talep yolu adımları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

