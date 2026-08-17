---
argument-hint: ''
description: Marka tescil başvurusu, yayına itiraz, karara itiraz veya YİDK kararına
  karşı dava aşamalarında; idari sürecin süreleri ve usulünü m.11-m.20 ve m.172 üzerinden
  yönetmek için kullanılır.
name: turkpatent-basvuru-itiraz
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# TÜRKPATENT Başvuru, İtiraz ve YİDK Süreci

## Görev
Markanın TÜRKPATENT nezdindeki idari yaşam döngüsünü yönetmek: başvuru (m.11), şekli/mutlak inceleme, Bültende yayın, yayına itiraz (m.18), karara itiraz ve YİDK; YİDK nihai kararına karşı iptal davası (m.172/2). Süre disiplini bu alanda belirleyicidir; hak düşürücü süreler kaçırılırsa idari yol kapanır.

## Soğuk başlangıç (intake)
- Başvuru hangi aşamada (inceleme, yayın, itiraz, YİDK)?
- Hangi mal/hizmet sınıfları ve Bülten yayın tarihi nedir?
- İtiraz/karara itiraz için kalan süre ne kadar?
- Mutlak ret mi (re'sen), nispi sebep mi (itiraz üzerine) söz konusu?

## Denetim şeması
1. **Başvuru ve şekli inceleme (m.11-15).** Başvuru unsurları, sınıflandırma (Nice), başvuru tarihi ve rüçhan hakkı (m.12-13) kontrol edilir.
2. **Mutlak ret incelemesi (m.16).** TÜRKPATENT m.5 sebeplerini re'sen inceler; kısmî/tam ret kararı verir.
3. **Yayın ve itiraz (m.18).** Başvuru Bültende yayımlanır; ilgililer yayından itibaren iki ay içinde m.5-6 sebepleriyle itiraz eder. İtiraz süresi hak düşürücüdür.
4. **Kullanmama def'i (m.19/2).** İtiraz edilen, itiraz dayanağı markanın 5 yıllık kullanımının ispatını isteyebilir.
5. **Karara itiraz ve YİDK (m.20).** Markalar Dairesi kararına karşı iki ay içinde YİDK'ya itiraz; YİDK Kurum'un nihai kararını verir.
6. **YİDK kararına dava (m.172/2).** Nihai karar tebliğinden itibaren iki ay içinde Ankara FSHHM'de iptal davası açılır; bu süre hak düşürücüdür.

## Çıktı modülleri
- Aşama-süre takvimi (yayın, itiraz, YİDK, dava — tarih hesaplı).
- İtiraz/cevap dilekçesi iskeleti ve dayanak madde listesi.
- Süre kaçırma riski uyarı notu ve dava yolu kontrolü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

