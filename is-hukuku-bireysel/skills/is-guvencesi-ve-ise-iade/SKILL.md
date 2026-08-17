---
argument-hint: ''
description: İşçinin iş güvencesi kapsamında olup olmadığını ve işe iade davasının
  şartları, süresi, arabuluculuk ve sonuçlarını çözmek gerektiğinde; geçersiz feshe
  karşı işe iade ve boşta geçen süre/işe başlatmam
name: is-guvencesi-ve-ise-iade
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İş Güvencesi ve İşe İade Davası

## Görev
İş K. m.18-21 kapsamında iş güvencesi şartlarını denetlemek, işe iade sürecini (arabuluculuk + dava) kurmak ve geçersiz fesih sonuçlarını (işe başlatma ya da tazminat) hesaplamak.

## Soğuk başlangıç (intake)
1. İşyerinde kaç işçi çalışıyor; işverenin aynı işkolundaki diğer işyerleri var mı?
2. İşçinin kıdemi en az 6 ay mı; işveren vekili konumunda mı (m.18/son)?
3. Fesih bildirimi ne zaman tebliğ edildi?
4. Fesih yazılı ve gerekçeli mi?

## Denetim şeması
1. **Kapsam şartları (m.18):** Otuz veya daha fazla işçi, en az 6 ay kıdem, belirsiz süreli iş sözleşmesi. İşveren vekili ve yardımcıları (işletmenin bütününü sevk/yönetenler ile işyerinin tamamını yöneten ve işçi alıp çıkarma yetkisi olanlar) kapsam dışı. İşçi sayısı eşiği işverenin aynı işkolundaki tüm işyerleri birlikte sayılarak belirlenir.
2. **Geçerli sebep yokluğu:** Fesih geçerli sebebe dayanmıyorsa veya sebep ispatlanamıyorsa fesih geçersizdir. İspat yükü işverende (m.20/2).
3. **Süre ve usul:**
   - Arabuluculuğa başvuru: Fesih bildiriminin tebliğinden itibaren **bir ay** içinde arabulucuya başvuru zorunlu (dava şartı — 7036 m.3, m.11 atfı).
   - Anlaşamama tutanağından itibaren **iki hafta** içinde işe iade davası açılır.
4. **Hüküm (m.21):** Mahkeme feshin geçersizliğine karar verirse:
   - Boşta geçen süre ücreti: en çok **4 aya** kadar ücret ve haklar.
   - İşe başlatmama tazminatı: işçinin kıdemine göre **4-8 aylık** ücret (mahkeme takdir eder).
   - İşçi, kesinleşen kararın tebliğinden itibaren **10 işgünü** içinde işe başlamak için işverene başvurmalı; başvurmazsa fesih geçerli sayılır.
   - İşveren bir ay içinde işe başlatmazsa tazminat muaccel olur.

## Çıktı modülleri
- Kapsam şartları kontrol listesi (var/yok).
- Süre takvimi (1 ay arabuluculuk + 2 hafta dava + 10 işgünü başvuru).
- Olası hüküm: boşta geçen + başlatmama tazminatı tahmini aralığı.
- Stratejik not: işe iade mi, alacak davası mı tercih edilmeli.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

