---
argument-hint: ''
description: Markanın tanınmışlık düzeyi ve sınıf-aşırı koruması tartışmalıysa veya
  tanınmış marka taklidi/sulandırma iddiası varsa; m.6/4-5 ile Paris 1. mük. 6. md.
  korumasını denetlemek için kullanılır.
name: taninmis-marka-korumasi
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tanınmış Marka Koruması

## Görev
Bir markanın tanınmışlığını ve buna bağlı genişletilmiş korumayı SMK m.6/4 (Paris Sözleşmesi 1. mük. 6. md. anlamında tanınmış marka) ve m.6/5 (Türkiye'de ulaşılan tanınmışlık düzeyi nedeniyle farklı mal/hizmette koruma) çerçevesinde değerlendirmek. Tanınmışlık, normal karıştırılma sınırlarını aşan koruma sağlar.

## Soğuk başlangıç (intake)
- Marka hangi mal/hizmette, hangi coğrafyada ne kadar tanınıyor?
- Tanınmışlığa ilişkin somut delil var mı (pazar payı, tanıtım, süre, tüketici anketi)?
- İhtilaflı kullanım aynı sınıfta mı, farklı sınıfta mı?
- Haksız yarar/itibara veya ayırt ediciliğe zarar somut mu?

## Denetim şeması
1. **Tanınmışlık türü.** m.6/4 Paris kapsamı tanınmış marka (tescilsiz dahi olabilir) ile m.6/5 Türkiye'de ulaşılmış tanınmışlık ayrımı yapılır.
2. **Tanınmışlık ispatı.** İlgili tüketici kesimindeki bilinirlik; kullanım süresi-yoğunluğu, coğrafi yaygınlık, tanıtım yatırımı, pazar payı, TÜRKPATENT tanınmış marka siciline kayıt (karine değil, delil) değerlendirilir.
3. **m.6/4 (aynı/benzer mal).** Tanınmış markayla aynı/benzer mal-hizmette karıştırılma ihtimali; tescilsiz tanınmış marka da bu kapsamda korunur.
4. **m.6/5 (farklı mal).** Üç koşuldan biri: (i) tanınmış markanın itibarından haksız yarar sağlama, (ii) itibarına zarar, (iii) ayırt edici karakterinin zedelenmesi (sulandırma). Koşul ispatlanamazsa farklı sınıf koruması doğmaz.
5. **Sınır.** Tanınmışlık her sınıfa otomatik koruma vermez; haklı sebep (m.6/5) ve dürüst kullanım savunması değerlendirilir.

## Çıktı modülleri
- Tanınmışlık delil dosyası kontrol listesi.
- m.6/4 mü m.6/5 mi belirleme notu ve koşul altlaması.
- Sınıf-aşırı koruma kapsamı değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

