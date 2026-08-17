---
argument-hint: ''
description: Saha olayları, seyirden yasaklanma, şike, teşvik primi veya müsabaka
  güvenliği suçlarını 6222 sayılı Kanun çerçevesinde değerlendirmek ve ceza savunması
  ya da müşteki stratejisi kurmak gerektiğinde ku
name: spor-siddet-6222-ceza
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sporda Şiddet ve Spor Suçları (6222)

## Görev
Spor müsabakaları ile bağlantılı suç ve idari yaptırımları 6222 sayılı Kanun çerçevesinde değerlendirmek; seyirden yasaklanma, şike/teşvik primi ve saha güvenliği suçlarında unsur analizi yaparak savunma ya da şikâyet stratejisi kurmaktır.

## Soğuk başlangıç (intake)
1. Olay ne: saha içi/dışı şiddet, hakaret/çirkin tezahürat, sahaya girme, şike iddiası?
2. Müvekkilin sıfatı: sporcu, taraftar, yönetici, görevli?
3. Adli süreç hangi aşamada (soruşturma, kovuşturma) ve idari (seyirden yasaklanma) tedbir var mı?
4. Görüntü kaydı, tutanak ve tanık var mı?
5. Tedbir/yasak kararının tebliğ tarihi nedir?

## Denetim şeması
1. **Norm tespiti**: 6222 sayılı Kanunun ilgili maddesi belirlenir — örn. şike ve teşvik primi (m.11), seyirden yasaklanma (m.18), müsabaka alanına usulsüz girme, hakaret içeren tezahürat gibi fiiller.
2. **Suç unsurları**: Maddi unsur (fiil, netice), manevi unsur (kast), faillik ve iştirak; şikede edim-karşı edim ilişkisi ve teşebbüs tartışılır.
3. **İdari tedbir-ceza ayrımı**: Seyirden yasaklanma idari tedbir niteliğindedir; adli ceza süreciyle paralel yürür. Tedbire karşı **sulh ceza hâkimliği** itiraz yolu ve süresi kontrol edilir.
4. **Görev ve usul**: Suçlar adli yargıda (CMK 5271) görülür; soruşturma, koruma tedbirleri, iddianame ve istinaf/temyiz aşamaları izlenir. Disiplin süreci federasyonda ayrıca yürür (non bis in idem tartışması).
5. **Delil**: Güvenlik kamerası kayıtları, hakem/gözlemci ve emniyet tutanakları, elektronik bilet/PASSOLIG kayıtları değerlendirilir.
6. **Ara sonuç**: İsnadın sübut ihtimali, lehe deliller ve hem adli hem idari ayakta savunma çizgisi belirlenir.

## Çıktı modülleri
- Unsur analizi tablosu (madde → unsur → eldeki delil)
- Savunma ya da şikâyet dilekçesi taslağı
- Seyirden yasaklanmaya itiraz dilekçesi
- Adli/idari/disiplin paralel süreç haritası



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

