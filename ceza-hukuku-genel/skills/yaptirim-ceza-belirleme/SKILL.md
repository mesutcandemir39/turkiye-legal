---
argument-hint: ''
description: Temel cezanın belirlenmesi, indirim-artırım sırası, seçenek yaptırımlar,
  erteleme ve güvenlik tedbirleri dahil somut cezanın hesaplanması gerektiğinde kullanılır.
name: yaptirim-ceza-belirleme
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yaptırım Teorisi ve Ceza Belirleme

## Görev
Suç sabit olduğunda somut cezayı, TCK m.61 sıralamasına ve ilgili yaptırım hükümlerine göre hesaplamak; seçenek yaptırım, erteleme ve güvenlik tedbirlerini değerlendirmek.

## Soğuk başlangıç (intake)
- Sevk maddesinin alt-üst ceza sınırı nedir; nitelikli hâl var mı?
- Teşebbüs, iştirak (yardım), haksız tahrik gibi indirim sebepleri var mı?
- Sanığın geçmişi, tekerrür durumu ve duruşmadaki tutumu nasıl?
- Hükmolunacak ceza erteleme/seçenek yaptırım sınırları içinde mi?

## Denetim şeması
1. **Temel ceza (m.61):** Alt-üst sınır arasında suçun işleniş biçimi, kasıt yoğunluğu, zarar/tehlike, fail-mağdur ilişkisine göre temel ceza belirlenir.
2. **Sıralı uygulama (m.61/4-5):** Artırım ve indirim nedenleri kanunun belirlediği sırayla uygulanır: önce nitelikli hâller, sonra teşebbüs (m.35), iştirak (m.39), haksız tahrik (m.29), yaş küçüklüğü (m.31), takdiri indirim (m.62). Ara sonuç: sıralama doğru mu?
3. **Takdiri indirim (m.62):** Lehe hâllerde altıda bire kadar indirim.
4. **Seçenek yaptırımlar (m.50):** Kısa süreli hapsin adli para cezasına veya seçenek tedbirlere çevrilmesi şartları.
5. **Adli para cezası (m.52):** Gün para cezası sistemi; gün sayısı ve bir gün karşılığı miktar ayrı belirlenir.
6. **Erteleme (m.51) ve tekerrür (m.58):** İki yıl veya altı hapiste erteleme şartları; tekerrür hâlinde mükerrirlere özgü infaz rejimi.
7. **Güvenlik tedbirleri (m.53-60):** Belli hakları kullanmaktan yoksun bırakma, müsadere (m.54-55), akıl hastalarına tedbir (m.57), tüzel kişiler hakkında tedbir (m.60).

## Çıktı modülleri
- Adım adım ceza hesabı tablosu (her aşamada miktar ve madde).
- Seçenek yaptırım/erteleme uygunluk değerlendirmesi.
- Güvenlik tedbiri listesi.
- Lehe kanun (m.7) karşılaştırma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

