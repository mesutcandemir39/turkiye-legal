---
argument-hint: ''
description: İfade ve basın özgürlüğü, örgütlenme/toplantı ve gösteri, din ve vicdan
  özgürlüğüne yönelik yaptırım, ceza, yasak veya müdahaleler iddia edildiğinde kullanılır.
name: ifade-toplanma-din-ozgurlugu
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


# İfade, Toplanma ve Din Özgürlüğü İhlali

## Görev
m.26 (ifade), m.28 (basın), m.33-34 (örgütlenme, toplantı-gösteri) ve m.24 (din-vicdan) kapsamındaki müdahalelerin m.13 süzgecinden geçirilerek ölçülü olup olmadığını değerlendirmek.

## Soğuk başlangıç (intake)
- Müdahale neye yöneldi (söz, yazı, paylaşım, gösteri, dernek/sendika eylemi, inanç pratiği)?
- Müdahale türü: ceza, idari yaptırım, yasak, görevden uzaklaştırma, erişim engeli?
- Müdahalenin kanuni dayanağı ve güttüğü meşru amaç nedir?
- İfade/eylem kamusal tartışmaya, siyasete veya gazetecilik faaliyetine mi ilişkin?

## Denetim şeması
1. Müdahalenin varlığı — yaptırım, ceza, yasak veya caydırıcı (chilling) etki doğuran her tedbir müdahaledir.
2. Kanunilik — m.13: erişilebilir, öngörülebilir ve belirli kanun şartı; muğlak/aşırı geniş norm uygulaması ihlale yol açabilir.
3. Meşru amaç — m.26/2 ve ilgili maddelerdeki sınırlama sebepleri (millî güvenlik, kamu düzeni, başkalarının hak ve şöhreti vb.).
4. Demokratik toplumda gereklilik ve ölçülülük — "zorlayıcı toplumsal ihtiyaç" var mı; tedbir ile amaç orantılı mı; daha hafif araç mümkün mü. Siyasi söylem, kamu yararına haber ve eleştiriye geniş koruma; ifadenin değer yargısı mı olgu açıklaması mı olduğu; yaptırımın ağırlığı ve caydırıcı etkisi tartılır.
5. Toplanma/örgütlenme — barışçıl gösteriye ve dernek/sendika faaliyetine müdahalede aynı üçlü test; barışçıllık karinesi.
6. Din-vicdan — inancı açıklama özgürlüğüne müdahalede tarafsızlık ve çoğulculuk ölçütü.

Denge: İfade ile başkalarının kişilik hakkı (m.17/m.20) çatışıyorsa AYM çatışan haklar arasında adil denge kurar.

İspat yükü: müdahaleyi başvurucu; gerekliliği ve orantılılığı kamu makamı temellendirir.

Ara sonuç: hangi ölçütte ihlal bulunduğu.

## Çıktı modülleri
- Müdahale türü ve ilgili madde tespiti.
- Üçlü test altlaması (kanunilik–amaç–gereklilik/ölçülülük).
- Caydırıcı etki ve yaptırım ağırlığı notu.
- İlke kararlarına atıf [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

