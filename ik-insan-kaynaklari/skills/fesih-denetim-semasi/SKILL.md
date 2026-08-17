---
argument-hint: ''
description: Bir işçinin iş sözleşmesinin feshi planlanıyor veya yapılmış feshin hukuka
  uygunluğu değerlendirilecekse, geçerli/haklı sebep, usul ve son çare ilkesini adım
  adım denetlemek için kullanılır.
name: fesih-denetim-semasi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Fesih Denetim Şeması (Geçerli ve Haklı Sebep)

## Görev
İşveren feshini, iş güvencesi rejimi içinde ayakta kalacak biçimde planlamak veya yapılmış bir feshin işe iade/usulsüzlük riskini ölçmek. Esas + usul + ispat üçlüsünü birlikte denetlemek.

## Soğuk başlangıç (intake)
1. İşyerinde 30+ işçi var mı, işçinin kıdemi 6 ayı geçti mi (iş güvencesi kapsamı)?
2. Fesih sebebi davranış mı, yetersizlik/performans mı, işletme gereği mi, yoksa ahlak ve iyiniyete aykırılık (m.25/II) mı?
3. Olaydan bu yana kaç gün geçti (6 işgünü/m.26)?
4. Yazılı bildirim ve savunma alındı mı, daha hafif tedbir mümkün müydü?

## Denetim şeması
1. **Güvence kapsamı (m.18)**: 30+ işçi, 6 ay kıdem, belirsiz süreli ve işveren vekili olmama → kapsamdaysa **geçerli sebep ve usul** zorunlu.
2. **Sebep tipi**: (a) Geçerli sebep (m.18) = yetersizlik/davranış/işletme gereği; (b) Haklı/derhal sebep (m.25) = sağlık, ahlak ve iyiniyete aykırılık, zorlayıcı sebep. Sebep gerçek, ciddi ve fesihle orantılı olmalı.
3. **Usul (m.19)**: Fesih **yazılı** ve **sebep açıkça** belirtilmeli; m.18 sebepli fesihte (ve içtihaden m.25/II davranışlarda) işçinin **savunması** alınmalı. Savunma alınmadan davranış sebepli fesih usulsüzdür.
4. **Süre (m.26)**: Ahlak ve iyiniyete aykırılık sebepleri, öğrenmeden itibaren **6 işgünü** ve her halde 1 yıl içinde kullanılmalı; geçmesi haklı feshi düşürür.
5. **Son çare (ultima ratio)**: Özellikle işletme gereği ve performansta uyarı/yer değişikliği/eğitim gibi daha hafif yol tüketilmeli (içtihat — `[DOĞRULANMADI]`, karararama.yargitay.gov.tr).
6. **İspat (m.20/2)**: Feshin geçerli/haklı sebebe dayandığını **işveren** ispatlar; eldeki tutanak/ihtar/savunma yeterli mi kontrol et.
7. **Ara sonuç**: Eksik usul → usulsüz/geçersiz fesih; işe iade + boşta geçen süre ücreti + işe başlatmama tazminatı riski.

## Çıktı modülleri
- Fesih risk değerlendirme tablosu (esas/usul/süre/ispat skoru).
- Eksik adım listesi ve giderme önerisi.
- Fesih bildirimi taslağı veya feshi erteleme/alternatif tedbir önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

