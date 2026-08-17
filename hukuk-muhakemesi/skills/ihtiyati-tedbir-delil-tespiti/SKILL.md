---
argument-hint: ''
description: Dava açılmadan veya yargılama sırasında bir hakkın güvence altına alınması
  (HMK m.389-399) ya da kaybolma riski olan delilin tespiti (m.400-405) gerektiğinde;
  teminat, itiraz ve tedbirin uygulanması s
name: ihtiyati-tedbir-delil-tespiti
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


# İhtiyati Tedbir ve Delil Tespiti

## Görev
Hak veya delili korumak için geçici hukuki koruma talebi kurmak; tedbir şartlarını, teminatı, uygulama ve itiraz sürelerini yönetmek.

## Soğuk başlangıç (intake)
- Korunacak menfaat ne? (mevcut durumun değişme/zarar riski var mı?)
- Tedbir dava açılmadan mı, dava sırasında mı isteniyor?
- Hakkın varlığı yaklaşık olarak ispatlanabilir mi (m.390/3)?
- Kaybolma riski olan delil mi söz konusu (tanık yaşlı/hasta, durum değişecek)?

## Denetim şeması
1. **Tedbir sebebi** (HMK m.389): Mevcut durumda meydana gelebilecek bir değişme nedeniyle hakkın elde edilmesinin önemli ölçüde zorlaşacağı veya tamamen imkânsız hâle geleceği ya da gecikme sebebiyle ciddi zarar doğacağı hallerde tedbir istenir.
2. **Yaklaşık ispat** (m.390/3): Talep eden, davanın esası yönünden kendisinin haklılığını **yaklaşık olarak** ispat etmek zorundadır; kesin ispat aranmaz.
3. **Talep ve karar** (m.390-391): Tedbir, dava açılmadan önce esas hakkında görevli/yetkili mahkemeden; dava sırasında davaya bakan mahkemeden istenir. Karar gerekçeli olur.
4. **Teminat** (m.392): Tedbir kural olarak teminat karşılığı verilir; resmi belgeye/kesin delile dayanan haklarda teminattan vazgeçilebilir.
5. **Uygulama ve dava açma zorunluluğu** (m.393-397): Tedbir kararı **bir hafta** içinde uygulanması istenmezse kendiliğinden kalkar (m.393); **dava açılmadan** alınan tedbirde **iki hafta** içinde esas dava açılmazsa tedbir kendiliğinden kalkar (m.397/1).
6. **İtiraz** (m.394): Aleyhine tedbir kararı verilen, tedbirin uygulanmasından itibaren bir hafta içinde itiraz edebilir.
7. **Delil tespiti** (m.400-405): Henüz inceleme sırası gelmemiş veya ileride elde edilmesi imkânsızlaşacak delil için tespit istenir; hukuki yarar (m.401) gerekir.

Ara sonuç: "Tedbir şartı + teminat + uygulama ve dava açma süreleri" çizelgesi.

## Çıktı modülleri
- Tedbir/delil tespiti talep dilekçesi iskeleti (yaklaşık ispat gerekçeli).
- Süre kontrol listesi (1 hafta uygulama, 2 hafta esas dava, 1 hafta itiraz).
- Teminat değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

