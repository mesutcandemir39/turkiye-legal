---
argument-hint: ''
description: Adli para cezasının ödenmesi, taksitlendirme, kamuya yararlı işe çevirme
  ve ödenmemesi hâlinde hapse çevrilmesini değerlendirmek gerektiğinde kullanılır.
name: adli-para-cezasi-infazi
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Adli Para Cezasının İnfazı ve Hapse Çevirme

## Görev
Adli para cezasının infaz seçeneklerini ve ödenmemesi hâlinde hapse çevrilme riskini 5275 m.106 ekseninde yönetmek.

## Soğuk başlangıç (intake)
- Adli para cezasının toplam tutarı nedir; ödeme emri tebliğ edildi mi?
- Hükümlünün ödeme gücü ve taksit talebi var mı?
- Daha önce kısmi ödeme yapıldı mı?
- Ceza, hapisten çevrilmiş adli para cezası mı yoksa doğrudan mı (hapse iade kuralı farkı)?

## Denetim şeması
1. Ödeme süreci: kesinleşen adli para cezası tebliğ edilen ödeme emriyle istenir; süresinde ödenmezse Cumhuriyet savcılığınca tahsil/çevirme işlemleri başlar (5275 m.106).
2. Taksitlendirme: hükümlünün talebiyle, kanunda öngörülen koşullarda taksitlendirme mümkündür; bir taksitin ödenmemesi kalanın muacceliyetine yol açabilir. Ara sonuç: ödeme planı uygunluğu.
3. Kamuya yararlı işe çevirme: ödenmeyen para cezası, hükümlünün rızası ve uygunluk hâlinde kamuya yararlı bir işte çalıştırmaya çevrilebilir (5275 m.106). İspat: çalışma uygunluğu ve denetimli serbestlik müdürlüğü değerlendirmesi.
4. Hapse çevirme: ödenmeyen ve çevrilemeyen para cezası, kanunda öngörülen hesaba göre hapse çevrilir; ancak doğrudan hükmedilen adli para cezasında ödendiğinde hükümlü serbest bırakılır. Çevrilen hapis için üst sınır ve hesap kuralları kontrol edilir.
5. İtiraz: çevirme/infaz işlemine karşı infaz hâkimliği yolu (4675 sayılı Kanun). İlkesel içtihat karararama.yargitay.gov.tr, künye `[DOĞRULANMADI]`.
6. Ara sonuç: ödeme/taksit/çevirme seçeneği + hapse çevrilme riski.

## Çıktı modülleri
- Ödeme seçenekleri tablosu.
- Hapse çevirme hesabı taslağı.
- Taksit veya kamuya yararlı işe çevirme talep dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

