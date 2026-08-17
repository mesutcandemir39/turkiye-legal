---
argument-hint: ''
description: Kamulaştırma, kamulaştırmasız el atma, vergi/idari yaptırım, alacağa
  erişememe, tapu iptali gibi nedenlerle mülkiyet hakkına müdahale edildiği iddia
  edildiğinde kullanılır.
name: mulkiyet-hakki-ihlali
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mülkiyet Hakkı İhlali

## Görev
Anayasa m.35 ve AİHS Ek 1 No'lu Protokol m.1 çerçevesinde mülkiyete müdahalenin var olup olmadığını, türünü ve ölçülülüğünü değerlendirmek.

## Soğuk başlangıç (intake)
- Söz konusu "mülk" nedir (taşınmaz, alacak, meşru beklenti, ekonomik değer)?
- Müdahale türü: yoksun bırakma (kamulaştırma), kullanımın kontrolü (yaptırım/imar), genel kural mı?
- Müdahalenin yasal dayanağı ve güttüğü kamu yararı nedir?
- Tazminat/denkleştirme sağlandı mı, sağlandıysa yeterli mi?

## Denetim şeması
1. Mülk kavramı — m.35: mevcut mallar yanında, icra edilebilir alacaklar ve yeterince somut "meşru beklenti" de mülk sayılır; salt umut yetmez.
2. Müdahale türü — üç kural: (a) mülkten yoksun bırakma, (b) kullanımın kontrolü, (c) genel müdahale. Her biri kendi ağırlığında incelenir.
3. Kanunilik — m.13/m.35: müdahale erişilebilir, öngörülebilir ve belirli bir kanuna dayanmalıdır. Kanuni dayanak yoksa diğer ölçütlere geçmeden ihlal doğar.
4. Meşru amaç — kamu yararı veya genel yarar güdülmelidir.
5. Ölçülülük (adil denge) — başvurucunun katlandığı külfet ile güdülen kamu yararı arasında makul denge aranır. Kamulaştırmada gerçek değer üzerinden ve makul sürede ödenen tazminat; kamulaştırmasız el atmada bedelin tam karşılanması; aşırı bireysel külfet ihlal doğurur.
6. Usuli güvenceler — başvurucuya itiraz ve görüşlerini sunma imkânı tanınmış olmalıdır.

İspat yükü: mülkün ve aşırı külfetin varlığını başvurucu; müdahalenin haklılığını idare/Devlet ortaya koyar.

Ara sonuç: müdahale türü ve hangi ölçütte (kanunilik/amaç/denge) ihlal bulunduğu.

## Çıktı modülleri
- Mülk niteliği ve müdahale türü tespiti.
- Kanunilik–amaç–ölçülülük altlaması.
- Tazminat/denkleştirme yeterlilik notu.
- İlke kararlarına atıf [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

