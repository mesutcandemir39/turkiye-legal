---
argument-hint: ''
description: Askerlik, doğum, yurtdışı çalışma, doktora/avukat stajı gibi sürelerin
  borçlanılarak prim günü kazanılması ve emeklilik koşulunun tamamlanması istendiğinde
  kullanılır.
name: hizmet-borclanmasi
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Hizmet Borçlanması (Askerlik, Doğum, Yurtdışı)

## Görev
Borçlanılabilir sürelerin tespiti, borçlanma tutarının hesabı ve borçlanmanın emeklilik koşuluna etkisini değerlendirmek.

## Soğuk başlangıç (intake)
- Hangi süre borçlanılmak isteniyor: askerlik, doğum, yurtdışı çalışma, staj, ücretsiz izin mi?
- Kişinin halen veya geçmişte sigortalılığı var mı? (Bazı borçlanmalar mevcut sigortalılık şartına bağlı.)
- Borçlanmanın amacı eksik prim gününü tamamlamak mı, emeklilik tarihini öne almak mı?
- Yurtdışı borçlanmasında hangi ülke, hangi belgeler mevcut?

## Denetim şeması
1. Borçlanılabilir süreler — 5510 m.41: Askerlik, doğum (en fazla üç çocuk için, çocuk başına azami süre ve doğum sonrası çalışmama şartı), ücretsiz izin, doktora/uzmanlık, avukatlık stajı vb. sayılı haller.
2. Doğum borçlanması koşulu: Doğumdan önce tescilli sigortalılık ve doğum sonrası çalışılmamış olma; çocuğun yaşaması şartları aranır.
3. Yurtdışı borçlanması — 3201 sayılı Kanun: Yurtdışında geçen çalışma/ev hanımlığı süreleri; başvuru, döviz cinsinden tutar ve aylık bağlamada özel kurallar.
4. Tutar — m.41: Borçlanılan sürenin günü, seçilen prime esas kazanç (alt-üst sınır arası) üzerinden prim oranıyla hesaplanır; süresinde ödenmezse borçlanma geçersiz olur.
5. Etki: Borçlanılan süre prim gününe ve duruma göre sigortalılık süresine eklenir; ancak ilk sigortalılık tarihini geriye götürüp götürmediği (kademe avantajı) ayrıca incelenir. Ara sonuç: kazanılacak gün ve emeklilik koşuluna etkisi. İspat: askerlik terhis belgesi, doğum kaydı, yurtdışı hizmet belgesi.

## Çıktı modülleri
- Borçlanılabilir süre ve koşul kontrol listesi.
- Borçlanma tutarı tahmini (seçilen PEK senaryolarıyla).
- Emeklilik koşuluna katkı analizi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

