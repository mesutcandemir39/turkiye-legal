---
argument-hint: ''
description: Hakem heyetinin oluşumu, tahkim yargılamasının yürütülmesi, süreler ve
  geçici hukuki koruma gibi tahkim sürecinin işleyişini planlamak veya yönetmek gerektiğinde
  kullanılır.
name: tahkim-yargilamasi-usul
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


# Tahkim Yargılaması Usulü

## Görev
Tahkim sürecini başlatmaktan hakem kararına kadar usul adımlarını, süreleri ve risk
noktalarını yönetmek; hakem atama, davanın açılması, delil sunumu ve geçici koruma
talepleri için yol haritası çıkarmak.

## Soğuk başlangıç (intake)
1. Tahkim iç tahkim (HMK) mi milletlerarası (MTK) mi, kurumsal mı ad hoc mı?
2. Hakem sayısı ve atama usulü anlaşmada nasıl belirlenmiş?
3. Tahkim süresi başladı mı, kararın verilmesi için süre işliyor mu?
4. Geçici tedbir/ihtiyati haciz ihtiyacı var mı?

## Denetim şeması
1. **Hakem sayısı ve atama**: **HMK m.415-417** / **MTK m.7** — sayı tek olmalı;
   belirlenmemişse hakem sayısı ve atama mahkeme veya kurum eliyle tamamlanır. Hakemin
   tarafsızlık/bağımsızlık açıklaması ve **ret sebepleri** (**HMK m.417**, **MTK m.7/C-D**)
   denetlenir.
2. **Davanın açılması ve dilekçeler**: Tahkim davası, talep tarihiyle açılır; iddia ve
   savunma dilekçeleri, deliller hakem heyetinin belirlediği takvime göre sunulur
   (**HMK m.426-428**, **MTK m.10**).
3. **Tahkim süresi**: İç tahkimde kural olarak **1 yıl** (**HMK m.427**), MTK'da **1 yıl**
   (**MTK m.10/B**); taraf anlaşması veya mahkeme kararıyla uzatılabilir. Süre aşımı iptal
   sebebidir; bu yüzden takvim sıkı tutulur.
4. **Geçici hukuki koruma**: Hakem heyeti ihtiyati tedbire karar verebilir ama cebri icra
   gerektiren tedbirler için mahkeme yetkilidir (**HMK m.414**, **MTK m.6**). Mahkemeden
   tedbir istemek tahkim iradesinden vazgeçme sayılmaz.
5. **Ara sonuç**: Usul takvimi, hakem heyeti durumu ve açık eksikler listesi.

## Çıktı modülleri
- Tahkim usul takvimi (atama, dilekçeler, duruşma, karar süresi).
- Hakem atama/ret dilekçesi taslağı.
- Geçici hukuki koruma başvuru notu (yetkili merci ayrımıyla).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

