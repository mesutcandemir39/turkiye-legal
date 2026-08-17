---
argument-hint: ''
description: Aynı fiilin hem kabahat hem suç oluşturduğu, ya da birden çok kabahatin
  birleştiği durumlarda fikri içtima, zincirleme kabahat ve mükerrer cezalandırma
  yasağını çözümlemek gerektiğinde kullanılır.
name: kabahat-suc-ayrimi-ve-ictima
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kabahat-Suç Ayrımı ve İçtima

## Görev
Bir fiilin hem kabahat hem suç sayıldığı veya birden çok kabahatin çakıştığı hallerde, hangi yaptırımın uygulanacağını ve mükerrer cezalandırma riskini 5326 m.15 çerçevesinde çözmek.

## Soğuk başlangıç (intake)
- Aynı fiil hem idari yaptırıma hem ceza soruşturmasına mı konu?
- Tek fiil mi, aynı türden birden çok fiil mi (zincirleme) söz konusu?
- Hangi kanunlar devrede (özel kanun kabahati + TCK suçu)?
- Daha önce verilmiş bir ceza/yaptırım var mı (kesinleşme durumu)?

## Denetim şeması
1. **Fikri içtima — kabahat/suç çakışması (5326 m.15/3):** Bir fiil hem kabahat hem suç oluşturuyorsa kural olarak yalnızca **suçtan** dolayı yaptırım uygulanır; suçtan ceza verilemeyen hallerde kabahat yaptırımı devreye girer. Bu, ne bis in idem (aynı fiilden iki kez cezalandırılmama) ile uyumludur.
2. **Bir fiille birden çok kabahat (5326 m.15/1):** En ağır idari para cezası uygulanır; idari tedbirler ayrıca tatbik edilebilir.
3. **Aynı kabahatin birden çok işlenmesi (5326 m.15/2):** Her bir kabahat için ayrı ceza; istisnaları madde metniyle kontrol et.
4. **Suçtan beraat/düşme etkisi:** Suçtan mahkûmiyet dışı bir sonuç çıkarsa kabahat yaptırımı yolunun açık kalıp kalmadığını, zamanaşımıyla birlikte değerlendir (5326 m.15/3, m.20).
5. **Kesinleşme ve ne bis in idem:** Aynı maddi fiil için idari ve adli yaptırımın birlikte uygulanması, AYM/AİHM içtihadında ne bis in idem yönünden tartışmalıdır; ilkesel atıf yapılır, künye `[DOĞRULANMADI]` işaretlenir (kararlarbilgibankasi.anayasa.gov.tr).

İspatta her iki sürecin dosyası karşılaştırılır; fiil kimliği (aynı maddi olay) belirleyicidir.

## Çıktı modülleri
- İçtima nitelendirme notu (m.15 hangi fıkra).
- Mükerrer cezalandırma riski değerlendirmesi.
- Strateji önerisi (hangi yaptırımın akıbeti beklenmeli).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

