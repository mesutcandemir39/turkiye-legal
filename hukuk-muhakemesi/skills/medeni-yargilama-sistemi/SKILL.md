---
argument-hint: ''
description: Bir hukuk davasının HMK'daki bütün iskeletini (yargı yolu, dava şartı,
  dilekçeler, ön inceleme, tahkikat, hüküm, kanun yolu) tanımak ve dosyayı doğru aşamaya
  yerleştirmek gerektiğinde; usulün hangi ad
name: medeni-yargilama-sistemi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Medeni Yargılama Sistematiği ve Aşamalar

## Görev
Bir hukuk uyuşmazlığını 6100 sayılı HMK'nın aşamalı yargılama mimarisine oturtmak; dosyanın hangi aşamada olduğunu, sıradaki adımı ve o adımdaki usuli imkân/kısıtları belirlemek.

## Soğuk başlangıç (intake)
- Talep maddi hukukta ne? (alacak, tazminat, tespit, tescil, men, terditli mi?)
- Dosya hangi aşamada? (dilekçeler / ön inceleme / tahkikat / hüküm / kanun yolu)
- Yargılama usulü hangisi? (yazılı m.118 vd. mı, basit m.316 vd. mı?)
- Dava şartı arabuluculuk kapsamında mı, son tutanak var mı?

## Denetim şeması
1. **Yargı yolu**: Uyuşmazlık adli yargıda mı? İdari/ceza/özel mahkeme görevi dışlanır mı? (HMK m.114/1-b dava şartı).
2. **Usul tipi**: Basit yargılamada (m.316-322) cevap süresi iki hafta (m.317), delillerin dilekçeyle sunulması ve ön inceleme + tahkikatın bütünleşmesi; yazılıda dört aşama ayrı işler.
3. **Dilekçeler aşaması**: Dava dilekçesi (m.119) → cevap (m.126-129, süre m.127) → cevaba cevap/ikinci cevap (m.136). Bu aşama bitince iddia/savunma genişletme yasağı (m.141) doğar.
4. **Ön inceleme** (m.137-142): Dava şartları ve ilk itirazlar (m.116) incelenir; uyuşmazlık konuları tespit edilir; sulh teşviki; deliller bağlanır; tutanak (m.140) düzenlenir. Tutanak yargılamanın çerçevesini dondurur.
5. **Tahkikat** (m.143 vd.): Bağlanan deliller toplanır, tanık-bilirkişi-keşif icra edilir; ispat yükü dağılımına göre ilerlenir.
6. **Sözlü yargılama ve hüküm** (m.184-186, m.294 vd.): Gerekçeli karar (m.297) yazılır; hüküm fıkrası talep sonucuyla örtüşmeli.
7. **Kanun yolu**: İstinaf iki hafta (m.345), temyiz iki hafta (m.361); kesinlik (parasal had) yıllık tarifeden teyit edilir.

Ara sonuç: Her aşama geçişinde bir hak/yasak doğar; özellikle ön inceleme tutanağı sonrası genişletme yasağı en sık hak kaybı noktasıdır.

## Çıktı modülleri
- Aşama tespit tablosu (mevcut aşama, tamamlanan/eksik işlemler).
- Sıradaki adım ve son işlem tarihi/süre uyarısı.
- Usuli risk notu (genişletme yasağı, ıslah ihtiyacı, eksik delil bağlama).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

