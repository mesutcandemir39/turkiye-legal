---
argument-hint: ''
description: Bir haber veya yayının ifade özgürlüğü kapsamında korunup korunmadığını,
  kişilik hakkı ihlali oluşturup oluşturmadığını AYM ve AİHM ölçütleriyle değerlendirmek
  gerektiğinde kullanılır.
name: ifade-basin-ozgurlugu-dengesi
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İfade ve Basın Özgürlüğü ile Kişilik Hakkı Dengesi

## Görev
Somut yayının Anayasa m.26/m.28 ve AİHS m.10 koruması altında olup olmadığını; kişilik hakkı (TMK m.24, Anayasa m.17) ile çatışmada hangi menfaatin üstün geldiğini ölçütlü biçimde belirlemek.

## Soğuk başlangıç (intake)
1. İçerik maddi vakıa iddiası mı, değer yargısı mı, karikatür/abartılı eleştiri mi?
2. Konu kamusal tartışmaya katkı sunuyor mu (kamu yararı)?
3. Hedef kişi siyasetçi/kamu görevlisi mi, sıradan birey mi?
4. İddianın olgusal temeli (kaynak, doğrulama) var mı?

## Denetim şeması
1. **Koruma alanı**: Haber, eleştiri ve değer yargıları Anayasa m.26 kapsamındadır; basın için m.28 ek güvence sağlar. Sınırlama Anayasa m.13 ölçütlerine (kanunilik, meşru amaç, ölçülülük) tabidir.
2. **Çatışan menfaatlerin tartımı**: AİHM ve AYM içtihadında kullanılan ölçütler — kamuya katkı, kişinin tanınırlığı ve önceki davranışı, haberin elde ediliş yöntemi, içeriğin biçimi ve sonuçları, yaptırımın ağırlığı [doğrulanacak — kararlarbilgibankasi.anayasa.gov.tr ve hudoc.echr.coe.int].
3. **Vakıa-değer yargısı ayrımı**: Maddi vakıa iddiası ispata elverişlidir; gerçek değilse koruma zayıflar. Değer yargısı ispata tabi değildir ancak yeterli olgusal temel gerektirir.
4. **Görünür gerçeklik ve özen**: Yayın anında mevcut verilere göre özenli davranılmış, kamu yararı, güncellik ve öz-biçim dengesi sağlanmışsa hukuka uygunluk doğar.
5. **Ara sonuç**: Üstün menfaat ifade özgürlüğü lehineyse talep reddedilir; kişilik hakkı lehineyse ihlal tespit edilir.

## Çıktı modülleri
- Tartım tablosu (ölçüt bazında lehe/aleyhe)
- Vakıa/değer yargısı sınıflandırması
- Üstün menfaat sonucu ve gerekçe taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

