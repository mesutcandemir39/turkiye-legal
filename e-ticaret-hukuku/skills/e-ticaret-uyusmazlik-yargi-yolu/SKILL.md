---
argument-hint: ''
description: E-ticaret uyuşmazlığında hangi merciye başvurulacağını (Tüketici Hakem
  Heyeti, tüketici mahkemesi, asliye ticaret, idari yargı, KVKK Kurulu) ve görev-yetki
  kurallarını belirlemek gerektiğinde kullanıl
name: e-ticaret-uyusmazlik-yargi-yolu
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
  - ad: Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
    numara: '6563'
    tur: kanun
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Uyuşmazlık Çözümü ve Görev-Yetki

## Görev
E-ticaret uyuşmazlığının niteliğine göre doğru çözüm merciini ve görev-yetki kurallarını belirlemek; gerekli ön şartları (dava şartı arabuluculuk, parasal sınır) tespit etmek.

## Soğuk başlangıç (intake)
- Taraflar tüketici-satıcı mı, iki tacir mi, vatandaş-idare mi?
- Uyuşmazlık değeri yaklaşık ne kadar?
- Konu sözleşme/iade mi, ticari ileti yaptırımı mı, veri ihlali mi, içerik mi?
- Daha önce bir başvuru/şikâyet yapıldı mı?

## Denetim şeması
1. Tüketici uyuşmazlıkları (6502): tüketici işlemlerinde parasal sınır altındaki uyuşmazlıklar Tüketici Hakem Heyeti'ne (zorunlu), üzeri Tüketici Mahkemesi'ne gider; sınır her yıl güncellenir. Tüketici davalarında dava şartı arabuluculuk öngörülen hallerde uygulanır.
2. Ticari uyuşmazlıklar (B2B): tacirler arası e-ticaret sözleşmeleri ve haksız rekabet (TTK m.54-55) Asliye Ticaret Mahkemesi'nde; ticari davalarda dava şartı arabuluculuk (TTK m.5/A) uygulanır.
3. İdari yaptırım: 6563 m.12 idari para cezalarına ve Bakanlık işlemlerine karşı 2577 sayılı İYUK kapsamında idari yargı (idare mahkemesi); süre ve dava şartlarına dikkat edilir.
4. Kişisel veri: KVKK ihlallerinde ilgili kişi başvurusu ve KVK Kurulu şikâyeti (6698 m.13-15); Kurul kararına karşı idari yargı yolu açıktır.
5. İçerik/erişim: 5651 kapsamında erişim engelleme ve içerik kaldırma talepleri Sulh Ceza Hâkimliği veya ilgili usule göre yürütülür.
Yetki: HMK genel yetki kuralları + tüketici lehine yerleşim yeri mahkemesi seçeneği; sözleşmedeki yetki şartının tüketiciye karşı geçerliliği denetlenir.
Ara sonuç: mercii + ön şart + süre listesi.

## Çıktı modülleri
- Görev-yetki ve mercii kararı tablosu.
- Dava şartı (arabuluculuk/parasal sınır) kontrolü.
- Başvuru sırası ve süre takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

