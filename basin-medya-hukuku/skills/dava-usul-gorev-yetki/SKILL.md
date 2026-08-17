---
argument-hint: ''
description: Basın-medya uyuşmazlıklarında doğru yargı kolunu, görevli ve yetkili
  mahkemeyi, dava türünü ve ihtiyati tedbir imkânını belirlemek gerektiğinde kullanılır.
name: dava-usul-gorev-yetki
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


# Dava, Usul, Görev ve Yetki

## Görev
Uyuşmazlığın hangi yargı kolunda (adli/idari), hangi görevli mahkemede ve nerede açılacağını belirlemek; uygun dava türünü ve ihtiyati tedbiri kurgulamak.

## Soğuk başlangıç (intake)
1. Talep ne (tazminat, men, erişim engelleme, idari işlem iptali)?
2. Karşı taraf özel hukuk kişisi mi, idare (RTÜK) mi?
3. Davacı/davalı yerleşim yeri ve haksız fiilin işlendiği yer neresi?
4. Acil ve telafisi güç zarar tehlikesi var mı (ihtiyati tedbir)?

## Denetim şeması
1. **Yargı kolu**: Kişilik hakkı/tazminat davaları adli yargıda; RTÜK ve BTK işlemlerinin iptali idari yargıda (İYUK). 5651 m.9 erişim engelleme sulh ceza hâkimliğinde; ceza şikâyeti ceza yargısında.
2. **Görev**: Kişilik hakkı ve tazminat davalarında genel görevli mahkeme asliye hukuk mahkemesidir (HMK m.2). Cevap-düzeltme ve erişim engelleme talepleri sulh ceza hâkimliğindedir.
3. **Yetki**: Genel yetki davalının yerleşim yeri (HMK m.6); haksız fiilde fiilin işlendiği veya zararın doğduğu ya da doğma ihtimalinin bulunduğu yer mahkemesi de yetkilidir (HMK m.16).
4. **Dava türü ve dilekçe**: Talep sonucu net olmalı (tespit/men/önleme/tazminat); dilekçe HMK m.119 unsurlarını taşımalıdır.
5. **İhtiyati tedbir**: HMK m.389 vd. çerçevesinde, devam eden veya tekrarlanacak ihlalde içeriğin yayımının/erişiminin durdurulması istenebilir; ifade özgürlüğü nedeniyle ölçülülük sıkı denetlenir.
6. **Ara sonuç**: Doğru yargı kolu + görevli/yetkili mahkeme + uygun dava türü belirlenince layiha hazırlanır.

## Çıktı modülleri
- Yargı kolu/görev/yetki karar ağacı
- İhtiyati tedbir talebi gerekçesi
- Dilekçe başlığı ve talep sonucu taslağı



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

