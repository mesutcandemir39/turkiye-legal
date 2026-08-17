---
argument-hint: ''
description: Mahkeme ilamı veya ilam niteliğindeki belgeye dayalı takip yapmak, para
  dışı edimlerin (teslim, tahliye, çocuk teslimi) cebrî icrasını yürütmek ve icranın
  geri bırakılması ya da istinaf/temyizde tehir
name: ilamli-icra-ve-icranin-geri-birakilmasi
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İlamlı İcra ve İcranın Geri Bırakılması

## Görev
İlam veya ilam niteliğindeki belgeyle takip kurmak (m.24 vd.); konusu para, teminat, taşınır/taşınmaz teslimi, bir işin yapılması/yapılmaması veya tahliye olan edimleri icra etmek; borçlu lehine icranın geri bırakılması ve tehir-i icra yollarını yönetmek.

## Soğuk başlangıç (intake)
- Elde kesinleşmiş/kesinleşmemiş ilam mı, ilam niteliğinde belge mi (m.38) var?
- İlamın konusu nedir (para, teslim, tahliye, yapma/yapmama)?
- Kanun yolu (istinaf/temyiz) açık mı, tehir-i icra (m.36) gündemde mi?
- Borç icra emrinden sonra ödendi/itfa edildi mi (m.33)?

## Denetim şeması
1. **İcra emri (m.24-32)**: İlamlı takipte borçluya icra emri gönderilir; itiraz takibi durdurmaz. Para alacağında m.32, taşınır teslimi m.24, taşınmaz tahliye/teslimi m.26-28, çocuk teslimi (özel mevzuat/m.25 uygulaması), bir işin yapılması m.30, yapılmaması m.31.
2. **İlam niteliğinde belgeler (m.38)**: Mahkeme huzurunda yapılan sulh/kabul, kayıtsız şartsız para borcu ikrarını içeren düzenleme şeklindeki noter senetleri vb. ilam gibi icra edilir.
3. **İcranın geri bırakılması (m.33)**: Borçlu, icra emrinin tebliğinden sonra borcun itfa/imhal/zamanaşımı gibi sebeple sona erdiğini belgeyle ileri sürerse icra mahkemesinden geri bırakma ister. İlamların zamanaşımı için m.39'a (10 yıl) bakılır.
4. **Tehir-i icra (m.36)**: İstinaf/temyiz yoluna başvuran borçlu, teminat göstererek icranın geçici olarak durdurulmasını isteyebilir; süreler ve teminat oranı denetlenir.
5. **İspat yükü**: Geri bırakma talebinde borçlu, itfa/imhali nitelikli belgeyle ispatlar.
6. **Ara sonuç**: İcra emrinin uygunluğu, kanun yolu etkisi ve teminat planı belirlenir.

## Çıktı modülleri
- İlamlı takip talebi/icra emri taslağı.
- İcranın geri bırakılması veya tehir-i icra dilekçesi.
- Edim türüne göre fiilî icra adımları kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

