---
argument-hint: ''
description: İthalatta gümrük kıymetinin doğru hesaplanması, satış bedeli yönteminin
  reddi, kıymet artırımı ve buna bağlı ek tahakkuklarda; kıymet ihtilaflarını yöntem
  hiyerarşisi ve ilave kalemler üzerinden çözme
name: gumruk-kiymeti
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gümrük Kıymeti Belirleme ve İhtilafları

## Görev
İthal eşyasının gümrük kıymetini 4458 m.23-31 yöntem hiyerarşisine göre belirlemek; idarenin satış bedelini reddedip kıymet artırması veya ilave kalem eklemesi nedeniyle çıkan ek tahakkuk ihtilaflarını çözmek.

## Soğuk başlangıç (intake)
- Beyan edilen kıymet ve ödeme şekli nedir; alıcı-satıcı arasında ilişki var mı?
- Faturaya yansımayan royalti, lisans, komisyon, navlun, sigorta gibi kalemler var mı?
- İdare satış bedelini hangi gerekçeyle reddetti veya hangi referans/emsal kıymeti esas aldı?
- Kıymet araştırması, ek beyan veya sonradan kontrol raporu mevcut mu?

## Denetim şeması
1. Asıl yöntem: Gümrük kıymeti kural olarak satış bedelidir (m.24) — fiilen ödenen veya ödenecek bedel. Bu yöntemin uygulanabilmesi için m.24/3'teki şartlar (kısıtlama yokluğu, ilişkinin fiyatı etkilememesi) aranır.
2. İlaveler (m.27): Alıcı tarafından ödenen ve fiyata dahil olmayan komisyon, ambalaj, royalti/lisans ücreti, Türkiye'ye kadar navlun ve sigorta gibi kalemler kıymete eklenir. Royaltinin "satış şartı" olup olmadığı ayrıca denetlenir.
3. İndirimler (m.28): İthalattan sonraki montaj/nakliye, Türkiye'de ödenen vergiler gibi kalemler ayrıştırılabiliyorsa kıymete dahil edilmez.
4. Yöntem hiyerarşisi: Satış bedeli reddedilirse sırasıyla aynı eşyanın satış bedeli (m.25/a), benzer eşya, indirgeme (tutundurma), hesaplanmış kıymet ve son çare yöntemi (m.25-26) uygulanır. İdare sırayı atlamamalı ve reddi gerekçelendirmelidir.
5. İspat yükü: İdare satış bedelini reddederken somut şüphe ve veri ortaya koymalı; yükümlü beyanın gerçekliğini destekleyen banka ödemesi, sözleşme ve emsal verilerle savunur. Soyut "düşük kıymet" iddiası tek başına yetmez (Danıştay yerleşik içtihadı [DOĞRULANMADI], karararama.danistay.gov.tr).
6. Ara sonuç: Doğru yöntem ve kıymet tabanı belirlenir; ilave/indirim kalemleri hesaplanır; ek tahakkuk farkı ve buna bağlı m.234 cezası değerlendirilir.

## Çıktı modülleri
- Kıymet hesap tablosu (beyan vs. idare farkı, kalem kalem)
- Yöntem reddine karşı gerekçeli itiraz/dava taslağı
- Royalti ve ilişkili kişi analizi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

