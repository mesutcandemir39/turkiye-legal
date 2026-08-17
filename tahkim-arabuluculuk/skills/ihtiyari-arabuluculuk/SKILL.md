---
argument-hint: ''
description: Taraf iradesiyle yürütülen, dava şartı olmayan arabuluculukta süreci
  başlatmak, yürütmek ve anlaşma belgesini icra edilebilir hale getirmek gerektiğinde
  kullanılır.
name: ihtiyari-arabuluculuk
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtiyari Arabuluculuk Süreci

## Görev
HUAK kapsamında ihtiyari arabuluculuk sürecini tasarlamak ve anlaşmayı bağlayıcı/icra
edilebilir hale getirmek; gizlilik ve beyanların kullanılamaması ilkelerini korumak.

## Soğuk başlangıç (intake)
1. Uyuşmazlık tarafların serbestçe tasarruf edebileceği bir konuya mı ilişkin?
2. Taraflar arabuluculuğa başvurmaya istekli mi, arabulucu seçildi mi?
3. Hedef nedir: tam anlaşma, kısmi anlaşma, yoksa müzakere zemini mi?
4. Anlaşma sonrası icra edilebilirlik şerhi gerekiyor mu?

## Denetim şeması
1. **Elverişlilik**: **HUAK m.1/2** — tarafların üzerinde serbestçe tasarruf edebileceği,
   yabancılık unsuru taşıyabilen özel hukuk uyuşmazlıkları. Aile içi şiddet içeren konular
   dışlanır.
2. **İlkeler**: İradilik ve eşitlik (**HUAK m.3**), **gizlilik** (**HUAK m.4**) ve
   arabuluculukta ileri sürülen beyan/belgelerin sonraki davada **delil olarak
   kullanılamaması** (**HUAK m.5**). Bu ilkeler süreç boyunca korunur.
3. **Arabulucunun rolü**: Arabulucu karar veremez, çözüm dayatamaz; tarafları
   buluşturur (**HUAK m.2/b, m.15**). Sicile kayıtlı olmalıdır.
4. **Anlaşma ve icra edilebilirlik**: Anlaşma belgesi düzenlenir; taraflar ve avukatları
   imzaladığı belge **icra edilebilirlik şerhi** niteliğindedir, aksi halde sulh
   hukuk mahkemesinden şerh alınır (**HUAK m.18**). Anlaşılan konular yönünden dava
   açılamaz.
5. **Ara sonuç**: Anlaşma kapsamı, açık kalan konular ve icra yolu.

## Çıktı modülleri
- Arabuluculuk anlaşma belgesi taslağı ([doldurulacak] yer tutucularıyla).
- Gizlilik/beyan kullanılamazlığı uyarı notu.
- İcra edilebilirlik şerhi başvuru rehberi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

