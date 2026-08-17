---
argument-hint: ''
description: Teklifin aşırı düşük olarak değerlendirilmesi, açıklama istenmesi veya
  açıklamanın yetersiz görülerek reddi tartışıldığında kullanılacak özel değerlendirme
  becerisidir.
name: asiri-dusuk-teklif
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aşırı Düşük Teklif Sorgulaması

## Görev
Bir teklifin aşırı düşük sayılarak açıklama istenmesi sürecinin ve açıklamanın kabul/reddinin hukuka uygunluğunu denetlemek; istekli adına savunulabilir açıklama stratejisi kurmak.

## Soğuk başlangıç (intake)
1. İhale türü nedir; aşırı düşük sınır değer/sorgulama nasıl hesaplandı?
2. İdare yazılı açıklama istedi mi, talep edilen hangi bileşenler için?
3. Açıklamaya hangi belgeler sunuldu (maliyet, fiyat teklifi, analiz)?
4. Açıklama hangi gerekçeyle reddedildi?

## Denetim şeması
1. **Tespit (m.38):** Diğer tekliflere veya yaklaşık maliyete göre aşırı düşük görünen teklifler reddedilmeden önce yazılı açıklama istenir; idare doğrudan reddedemez, sorgulama zorunludur.
2. **Açıklama konuları:** İmalat sürecinin/hizmetin ekonomikliği, seçilen teknik çözümler, istisnaî elverişli koşullar, teklif edilen işin özgünlüğü gibi unsurlar belgelenir. Yapım/hizmet ihalelerinde önemli maliyet bileşenleri ve sınır değer Kamu İhale Genel Tebliği'ndeki yönteme göre değerlendirilir.
3. **Belgelendirme:** Açıklamanın üçüncü kişilerden alınan proforma/fiyat teklifi, kamu kurumu fiyatları, kendi üretim maliyeti gibi tevsik edici belgelere dayanması gerekir; mevzuata uygun analiz formatı aranır.
4. **Değerlendirme:** Açıklama yeterliyse teklif geçerli kabul edilir; yetersiz/dayanaksızsa reddedilir. İdarenin değerlendirmesi gerekçeli olmalı, soyut ret iptal sebebidir.
5. **Ara sonuç:** Aşırı düşük açıklamasının reddi/kabulü kesinleşen karar bildirimiyle birlikte şikâyet-itirazen şikâyet konusu yapılır. Tebliğdeki güncel hesap yöntemi `[güncel Tebliğ doğrulanacak]` teyit edilir.

İspat yükü: Açıklamayı sunan istekli, fiyatın gerçekçiliğini belgelerle ispatlar; idare reddi somut analizle gerekçelendirir.

## Çıktı modülleri
- Sınır değer/sorgulama hesap kontrolü.
- Maliyet bileşeni bazlı açıklama taslağı iskeleti.
- Ret gerekçesi yeterlilik değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

