---
argument-hint: ''
description: Limited şirkette ortağın çıkması/çıkarılması (TTK m.638-640), anonim
  ve limited şirkette haklı sebeple fesih davası (m.531, m.636/3) ve tasfiye süreçleri
  gündeme geldiğinde; çıkış payı, dava şartları
name: cikma-cikarilma-fesih-tasfiye
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ortaklıktan Çıkma, Çıkarılma ve Şirketin Feshi

## Görev
Ortağın şirketle ilişkisinin sona ermesini veya şirketin feshini/tasfiyesini hukuki temele oturtmak: çıkma-çıkarılma, ayrılma akçesi, haklı sebeple fesih ve tasfiye usulü.

## Soğuk başlangıç (intake)
1. Şirket Ltd. mi AŞ mi; talep çıkma, çıkarılma yoksa fesih mi?
2. Çıkma/çıkarılma için esas sözleşmede özel sebep var mı; haklı sebep iddiası nedir?
3. Fesih talebinde azlık hangi paya/orana sahip (AŞ m.531: sermayenin onda biri, halka açıkta yirmide biri)?
4. Şirketin devamlılığı için alternatif çözüm (pay bedelinin ödenmesi, ortağın çıkarılması) mümkün mü?
5. Tasfiyeye girilecekse tasfiye memuru/alacaklı durumu ne?

## Denetim şeması
1. Ltd. çıkma: m.638 — esas sözleşmeyle tanınan çıkma hakkı ve haklı sebeple çıkma davası (mahkemeden); çıkmaya katılma m.639.
2. Ltd. çıkarılma: m.640 — esas sözleşmede öngörülen sebeplerle genel kurul kararıyla; ayrıca haklı sebeple mahkemeden çıkarılma.
3. Ayrılma akçesi: m.641-642 — ayrılan ortağa gerçek değere uygun ayrılma akçesi; ödeme şartları ve muacceliyet.
4. Haklı sebeple fesih (AŞ): m.531 — azlık (sermayenin %10'u; halka açıkta %5) haklı sebeple feshi mahkemeden isteyebilir; mahkeme fesih yerine davacı pay sahiplerine paylarının gerçek değerinin ödenmesi gibi duruma uygun çözüme hükmedebilir.
5. Haklı sebeple fesih (Ltd.): m.636/3 — her ortak mahkemeden haklı sebeple fesih isteyebilir; mahkeme alternatif çözüme karar verebilir.
6. Sona erme sebepleri ve tasfiye: AŞ sona erme m.529-530; tasfiye m.536 vd. (tasfiye memurları, alacaklılara çağrı, aktiflerin paraya çevrilmesi, dağıtım). Ltd. m.636.
7. Görev/yetki: Asliye ticaret mahkemesi, şirket merkezi.
8. İspat: Haklı sebebi davacı somut vakıalarla ortaya koyar; ayrılma akçesi değeri bilirkişi ile saptanır.

## Çıktı modülleri
- Çıkma/çıkarılma veya fesih dava dilekçesi iskeleti (haklı sebep gerekçesi).
- Ayrılma akçesi/gerçek değer değerlendirme notu.
- Tasfiye adım planı ve alacaklı çağrısı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

