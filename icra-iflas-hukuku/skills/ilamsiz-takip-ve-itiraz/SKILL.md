---
argument-hint: ''
description: Genel haciz yoluyla ilamsız takip başlatmak, ödeme emrine itiraz etmek
  ya da gelen itiraza karşı strateji kurmak gerektiğinde; takip talebi, ödeme emri,
  itiraz türleri ve takibin durması-kesinleşmesi
name: ilamsiz-takip-ve-itiraz
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


# İlamsız Takip ve Ödeme Emrine İtiraz

## Görev
Para/teminat alacağı için genel haciz yoluyla ilamsız takip kurmak; ödeme emrine itirazı (borca, imzaya, kısmî) doğru şekilde yapmak veya karşılamak; takibin durma/kesinleşme mantığını yönetmek.

## Soğuk başlangıç (intake)
- Alacak likit mi, vade gelmiş mi, dayanak belge var mı?
- Ödeme emri tebliğ edildi mi, tarih nedir (7 günlük itiraz süresi)?
- İtiraz edilecekse borca mı, imzaya mı, faize/yetkiye mi itiraz var?
- Borçlu mal beyanında bulundu mu (m.74)?

## Denetim şeması
1. **Takip talebi (m.58)**: Tarafların kimliği, alacak miktarı, faiz başlangıcı, dayanağı ve takip yolu eksiksiz yazılır.
2. **Ödeme emri (m.60)**: Borçluya 7 gün içinde ödeme veya itiraz, aksi halde haciz ihtarı tebliğ edilir. Mal beyanı yükümlülüğü hatırlatılır.
3. **İtiraz (m.62)**: Borçlu 7 gün içinde icra dairesine itiraz eder; itiraz takibi **kendiliğinden durdurur** (m.66). İmzaya itiraz ayrıca ve açıkça belirtilmelidir (m.62/V); aksi halde imza kabul edilmiş sayılır. Yetkiye itiraz esasa itirazla birlikte yapılmalıdır.
4. **İtirazın sonucu**: İtiraz varsa alacaklı ya itirazın iptali davası (m.67, genel mahkeme, 1 yıl) ya itirazın kaldırılması (m.68 vd., icra mahkemesi, 6 ay) yolunu seçer. İtiraz yoksa takip kesinleşir, haciz istenebilir.
5. **İspat yükü**: Alacağın varlığını alacaklı ispatlar; borçlu ödeme/def'ileri belgeyle ileri sürer. İmzaya itirazda imzanın borçluya ait olduğunu alacaklı ispatlar.
6. **Ara sonuç**: Kesinleşme tarihi, haciz isteme süresi (m.78, talepten itibaren 1 yıl) ve sonraki adım belirlenir.

## Çıktı modülleri
- Takip talebi ve ödeme emri taslağı (yer tutucularla).
- İtiraz dilekçesi / itiraza karşı strateji notu.
- Süre ve kesinleşme takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

