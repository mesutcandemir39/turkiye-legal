---
argument-hint: ''
description: SPA'daki beyan ve tekeffülleri (R&W) kapsam ve katalog olarak tasarlamak,
  disclosure letter ile sınırlamak ve ihlal halinde tazminat-sınırlama (cap, basket,
  süre) mimarisini kurmak için kullanılır.
name: beyan-tekefful-ve-tazminat
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Beyan ve Tekeffüller ile Tazminat Rejimi

## Görev
Satıcı beyan-tekeffül kataloğunu hazırlamak, disclosure letter ile istisnaları yönetmek ve ihlal halinde tazminat ve sorumluluk sınırlamalarını dengeli kurmak.

## Soğuk başlangıç (intake)
- Müvekkil beyanı veren (satıcı) mı, alan (alıcı) mı?
- Beyanlar imza ve/veya kapanış tarihinde tekrarlanacak mı?
- Disclosure letter (açıklama mektubu) hazırlanacak mı?
- Bilgi standardı (best knowledge / fairly disclosed) nasıl tanımlanacak?

## Denetim şeması
1. **Beyan kataloğu**: Kurumsal yetki, pay mülkiyeti ve takyidatsızlık, finansal tablolar, vergi, iş hukuku, fikri mülkiyet, sözleşmeler, dava, uyum, KVKK başlıklarında temel ve operasyonel beyanlar.
2. **Hukuki nitelik**: Türk hukukunda R&W, satımda ayıba karşı tekeffül (TBK m.219 vd.) ile zapttan sorumluluk (TBK m.214 vd.) mantığına benzer; sözleşmeyle bağımsız bir tazminat (indemnity) borcu olarak da kurulabilir.
3. **Disclosure (açıklama)**: Beyanlar disclosure letter ile sınırlandırılır; açıklanan hususlar ihlal sayılmaz. Genel ve özel açıklamalar ayrılır.
4. **İhlal ve tazminat**: İhlal halinde gerçek zarar TBK m.112 (gereği gibi ifa etmeme) çerçevesinde; hile varsa TBK m.36 ile iptal/tazminat hakları saklıdır ve sözleşmesel sınırlamalar hileyi kapsayamaz.
5. **Sınırlamalar**: Azami sorumluluk (cap), eşik (de minimis / basket), zaman sınırı (genel beyanlar için kısa, vergi/temel beyanlar için uzun), sandbagging düzenlemesi.
6. **İspat yükü**: İhlali ve zarar miktarını talep eden taraf ispatlar (HMK m.190).
7. **Ara sonuç**: Müvekkil satıcı ise sınırlamalar genişletilir; alıcı ise temel beyanlar sınırlama dışı bırakılır.

## Çıktı modülleri
- Beyan-tekeffül kataloğu taslağı
- Disclosure letter şablonu (genel + özel açıklamalar)
- Tazminat ve sınırlama klozları (cap/basket/süre)
- Risk dağılım tablosu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

