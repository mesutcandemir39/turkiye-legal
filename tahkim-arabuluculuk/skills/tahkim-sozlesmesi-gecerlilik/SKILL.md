---
argument-hint: ''
description: Bir tahkim şartı veya tahkim sözleşmesinin geçerliliğini, kapsamını ve
  ayrılabilirliğini denetlemek; sözleşmeye tahkim klozu yazmak veya karşı tarafın
  tahkim itirazını değerlendirmek gerektiğinde kull
name: tahkim-sozlesmesi-gecerlilik
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


# Tahkim Sözleşmesi ve Geçerlilik Denetimi

## Görev
Tahkim iradesinin geçerli, yazılı ve kapsam bakımından yeterli olup olmadığını altlamak;
hem mevcut bir klozu denetlemek hem de yeni bir tahkim şartı kaleme almak. Geçersiz veya
patolojik kloz tüm tahkim sürecini riske atar.

## Soğuk başlangıç (intake)
1. Tahkim anlaşmasının metni nedir, asıl sözleşmenin içinde mi ayrı belge mi?
2. Yabancılık unsuru var mı (iç tahkim/MTK ayrımı için)?
3. Tahkim yeri, dili, hakem sayısı ve uygulanacak kurum kuralları belirlenmiş mi?
4. Karşı taraf tahkim itirazında mı bulunuyor yoksa tahkime mi gidiliyor?

## Denetim şeması
1. **Yazılılık**: İç tahkimde **HMK m.412/3**, MTK'da **MTK m.4/2** — yazılı şekil
   şarttır; tahkim şartı içeren belgeye atıf yapan sözleşme de geçerli sayılır.
2. **İrade ve elverişlilik**: Konunun tahkime elverişliliği (**HMK m.408** / **MTK m.1**)
   ve tarafların ehliyeti denetlenir; emredici alanlar dışlanır.
3. **Ayrılabilirlik (separability)**: Asıl sözleşmenin geçersizliği tahkim şartını
   kendiliğinden geçersiz kılmaz (**HMK m.412/4**, **MTK m.4/4**). Bu ilke ayrı altlanır.
4. **Yetki-yetki (competence-competence)**: Hakem kendi yetkisi hakkında karar verebilir
   (**HMK m.422**, **MTK m.7/H**). Mahkemeye tahkim itirazı **ilk itiraz** olarak ileri
   sürülür (**HMK m.116, m.413**).
5. **Patoloji kontrolü**: Belirsiz hakem atama usulü, çelişkili yetki klozları, geçersiz
   kurum atfı tespit edilir; ara sonuçta klozun ayakta kalıp kalmadığı belirtilir.

## Çıktı modülleri
- Geçerlilik denetim tablosu (yazılılık, elverişlilik, ayrılabilirlik, yetki).
- Önerilen/düzeltilmiş tahkim klozu taslağı (yer, dil, hakem sayısı, kurum kuralları
  ve [doldurulacak] yer tutucularıyla).
- Tahkim itirazı veya tahkime başvuru için strateji notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

