---
argument-hint: ''
description: Anonim şirkette pay ve pay senedi, nama/hamiline yazılı pay devri ve
  bağlam (TTK m.490-493), limited şirkette esas sermaye payı devri (m.595), imtiyaz
  ve pay sahipliği hakları konuları gündeme geldiği
name: pay-ve-pay-sahipligi-pay-devri
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
  version: 0.1.0
user-invocable: true
---


# Pay, Pay Sahipliği ve Pay Devri

## Görev
Payın hukuki niteliğini, devir usulünü ve geçerlilik şartlarını saptamak; pay sahipliği hak ve borçlarını, imtiyaz ve bağlam (devir sınırlaması) hükümlerini doğru uygulamak.

## Soğuk başlangıç (intake)
1. Şirket AŞ mi Ltd. mi; pay nama mı hamiline yazılı mı, senet bastırıldı mı?
2. Devir konusu pay üzerinde bağlam, imtiyaz veya rehin var mı?
3. Devir bedeli/ayni mi; devir sözleşmesi yazılı mı?
4. AŞ'de senetsiz pay devri mi (alacağın temliki) söz konusu?
5. Ltd.'de genel kurul onayı alındı mı, pay defterine işlendi mi?

## Denetim şeması
1. Pay senedi: AŞ nama/hamiline yazılı pay senetleri m.484-486; hamiline yazılı pay senedi devri MKK'ya bildirim + zilyetlik geçişi (m.489).
2. AŞ nama yazılı pay devri: ciro + zilyetlik geçişi (m.490/2); senetsiz payda alacağın devri hükümleri. Bağlam: esas sözleşmeyle devrin sınırlanması m.491-493; şirketin onaydan kaçınması ancak kanunda öngörülen önemli sebeplerle (m.493) ya da gerçek değerden devralma teklifiyle.
3. Ltd. pay devri: yazılı şekil + imzaların noter onayı + genel kurul onayı (m.595); aksi sözleşmede yoksa onay şarttır; ret için haklı sebep aranmaz ancak esas sözleşme düzenleyebilir. Devir pay defterine işlenir.
4. Pay sahipliği hakları: oy hakkı (m.434), bilgi alma-inceleme (m.437), kâr payı (m.507), rüçhan (m.461), tasfiye payı; oyda imtiyaz m.479; imtiyazlı pay sahipleri özel kurulu m.454.
5. Borçlar: sermaye koyma borcu (m.480 sınırı: tek borç ilkesi), temerrüt ve ıskat (m.482-483).
6. Geçiş/kayıt: Pay defteri (m.499); şirkete karşı pay sahipliği için kayıt önemlidir.
7. İspat: Devrin geçerli şekli ve onayı devralan tarafından; bağlam/önalım iddiası ileri sürence ispatlanır.

## Çıktı modülleri
- Pay devir sözleşmesi/temlik taslağı (şekil ve onay şartlı).
- Pay defteri kayıt ve bildirim adımları.
- Bağlam/imtiyaz analiz notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

