---
argument-hint: ''
description: Kuruluşun ilgili kişi başvurularını karşılama prosedürünün m.13 ve Başvuru
  Tebliği'ne uygunluğu, 30 günlük yanıt süresine riayet ve şikâyete geçiş riski denetlenirken
  kullanılır.
name: ilgili-kisi-basvuru-sureci-denetimi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İlgili Kişi Başvuru Süreci Denetimi

## Görev
Kuruluşun m.11 haklarına dayanan başvuruları nasıl karşıladığını denetlemek: başvuru kanalları, kimlik doğrulama, 30 günlük yanıt süresi, gerekçeli ret usulü ve Kurul'a şikâyete geçişin önlenmesi açısından sürecin sağlamlığını ölçmek.

## Soğuk başlangıç (intake)
1. İlgili kişi başvurusu için ilan edilmiş bir kanal/form var mı (web, KEP, yazılı)?
2. Gelen başvuruyu kim alıyor, kim yanıtlıyor; sorumlu birim belli mi?
3. Başvuru–yanıt süreleri kayıt altında mı; geçmişte süre aşımı yaşandı mı?
4. Ret kararları gerekçelendiriliyor mu?

## Denetim şeması
1. **Kanal ve usul (m.13, Başvuru Tebliği)**: Başvuru yazılı veya Kurul'un belirlediği yöntemlerle (KEP, güvenli elektronik imza, kayıtlı e-posta vb.) yapılır; kuruluş bu kanalları ilan etmiş ve işler tutmuş olmalı.
2. **Kimlik doğrulama**: Başvuranın ilgili kişi olduğunun doğrulanması gerekir; aşırı bilgi talebi ise ölçülülük ihlali olur — denge denetlenir.
3. **Yanıt süresi**: Talep en kısa sürede ve en geç 30 gün içinde sonuçlandırılır. İşlemin maliyeti varsa Kurul tarifesi uygulanır; süre aşımı doğrudan şikâyet ve yaptırım riskidir.
4. **Gerekçeli ret**: Ret kararı gerekçesiz olamaz; m.11 haklarından hangisinin neden reddedildiği açıklanmalı.
5. **Şikâyete geçiş (m.14)**: Ret, eksik yanıt veya 30 günde yanıtsızlık halinde ilgili kişi, öğrenmeden itibaren 30 ve her hâlde başvurudan itibaren 60 gün içinde Kurul'a şikâyet edebilir. Veri sorumlusuna başvuru, şikâyet için zorunlu ön şarttır.
6. **Ara sonuç**: Süresinde, gerekçeli ve kayıtlı yanıt, hem şikâyeti hem yaptırımı önler.

İspat yükü: Başvurunun süresinde ve gereği gibi yanıtlandığını veri sorumlusu yanıt kayıtlarıyla ispatlar.

## Çıktı modülleri
- Başvuru süreci uygunluk kontrol listesi ve süre takip cetveli.
- Standart başvuru formu ve gerekçeli yanıt (kabul/ret) şablonları.
- Süre aşımı/şikâyet riski uyarı raporu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

