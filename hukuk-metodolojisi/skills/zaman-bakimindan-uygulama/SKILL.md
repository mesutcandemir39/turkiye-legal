---
argument-hint: ''
description: Olay eski yürürlükteyken doğmuş ama yeni bir kanun çıkmışsa ya da kanun
  değişikliği devam eden ilişkileri etkiliyorsa; hangi kanunun uygulanacağını ve geçmişe
  etki sorununu çözmek için kullanılır.
name: zaman-bakimindan-uygulama
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Normların Zaman Bakımından Uygulanması

## Görev
Bir olaya eski mi yeni mi kanunun uygulanacağını, geçmişe yürüme yasağı, geçiş hükümleri ve derhal uygulama ilkeleri çerçevesinde belirlemek.

## Soğuk başlangıç (intake)
- Olay/işlem hangi tarihte gerçekleşti; kanun değişikliği ne zaman yürürlüğe girdi?
- İlişki tamamlanmış mı, yoksa hâlâ devam eden bir durum mu (sürekli borç, kira, velayet)?
- Değişen kanunda geçici/geçiş maddesi var mı?
- Alan ceza mı (lehe kanun ilkesi farklı işler) yoksa özel hukuk mu?

## Denetim şeması
1. **Yürürlük tarihini sabitle** — Kanunun ve ilgili maddenin yürürlük tarihi (Resmî Gazete) ve geçici maddeleri tespit edilir; mevzuat.gov.tr karşılaştırmalı metni esas alınır.
2. **Kural: geçmişe etkisizlik** — Hukuki güvenlik gereği yeni kanun, tamamlanmış olaylara ve kazanılmış haklara kural olarak uygulanmaz; eski olay eski kanuna tabidir.
3. **Derhal uygulama** — Yeni kanun, yürürlükten sonraki olgulara ve devam eden hukuki durumların ileriye dönük sonuçlarına derhal uygulanır (özellikle kamu düzeni ve genel ahlakı ilgilendiren hükümler — TMK Yürürlük Kanunu mantığı).
4. **Geçiş hükmü önceliği** — Kanunda açık geçiş/geçici hüküm varsa o esas alınır; genel ilkeler ancak geçiş hükmü yoksa devreye girer.
5. **Ceza istisnası** — Suç ve cezada kanunilik ve **lehe kanunun geçmişe yürümesi** (TCK m.7) ilkesi ayrıdır; özel hukuk mantığıyla karıştırılmaz.
6. **Zamanaşımı/süre değişimi** — Süreye ilişkin yeni hükümlerin başlamış sürelere etkisi, çoğunlukla özel geçiş hükmüyle düzenlenir; yoksa lehe/derhal uygulama tartışılır.

## Çıktı modülleri
- Olay-kanun zaman çizgisi.
- Uygulanacak kanun + dayanak ilke (geçmişe etkisizlik/derhal uygulama/geçiş hükmü).
- Kazanılmış hak değerlendirmesi.
- Ceza ise lehe kanun notu + `[DOĞRULANMADI]` içtihat.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

