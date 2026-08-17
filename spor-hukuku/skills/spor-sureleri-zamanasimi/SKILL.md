---
argument-hint: ''
description: Disiplin, itiraz, tahkim, CAS ve sözleşmesel alacaklarda süre rejimini
  ve zamanaşımını hesaplamak, hak kaybını önlemek için süre takvimi çıkarmak gerektiğinde
  kullanın.
name: spor-sureleri-zamanasimi
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


# Spor Hukukunda Süreler, Hak Düşürücü Süreler ve Zamanaşımı

## Görev
Spor uyuşmazlıklarında geçerli süre rejimini doğru kurmak; itiraz, tahkim, CAS ve sözleşmesel alacak süreleri ile hak düşürücü süreleri ayırmak ve geriye sayımlı bir süre takvimi üretmektir.

## Soğuk başlangıç (intake)
1. Hangi işlem için süre soruluyor (disiplin itirazı, tahkim, CAS, alacak davası)?
2. Tebliğ/öğrenme tarihi nedir; tebligat usulü ne (elektronik, federasyon bildirimi)?
3. Federasyon ve uygulanacak talimat hangisi?
4. Sözleşmesel alacak mı, ceza/idari karar mı?
5. Süre içinde herhangi bir başvuru yapıldı mı?

## Denetim şeması
1. **Süre türü**: Disiplin ve tahkim başvuru süreleri kural olarak **hak düşürücü** süredir; durmaz, kesilmez ve resen dikkate alınır. Sözleşmesel alacaklarda **zamanaşımı** (TBK) işler; def'i olarak ileri sürülür.
2. **Başlangıç anı**: Sürenin tebliğ mi, öğrenme mi, yoksa kararın kesinleşmesiyle mi başladığı talimat metninden tespit edilir; tebligatın usulüne uygunluğu kontrol edilir.
3. **Talimat sürelerinin önceliği**: Federasyon disiplin/itiraz/tahkim süreleri ilgili talimatta düzenlenir ve genelde günlerle ölçülür; metin ve yürürlük tarihi mutlaka doğrulanır (talimat sık değişir).
4. **CAS süresi**: Milletlerarası boyutta CAS başvuru süresi, ilgili federasyon kuralının atıf yaptığı süredir; kaçırılması başvuruyu reddettirir.
5. **Sözleşmesel zamanaşımı**: Sporcu ücret/prim alacaklarında TBK genel ve özel zamanaşımı süreleri uygulanır; alacağın niteliğine göre süre belirlenir.
6. **Ara sonuç**: Her işlem için son gün, kalan gün ve risk seviyesi tabloya yazılır.

## Çıktı modülleri
- Süre takvimi tablosu (işlem → başlangıç → son gün → kalan gün)
- Hak düşürücü/zamanaşımı ayrım notu
- Acil aksiyon uyarısı
- Talimat/süre doğrulama notu `[DOĞRULANMADI]`



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

