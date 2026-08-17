---
argument-hint: ''
description: Sebepsiz zenginleşmenin dört unsurunu (zenginleşme, fakirleşme, illiyet,
  haklı sebebin yokluğu) somut olaya adım adım uygulamak ve talebin doğup doğmadığını
  test etmek gerektiğinde kullanılır.
name: sartlar-ve-denetim-semasi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Unsurlar ve Ana Denetim Şeması

## Görev
TBK m.77/1 unsurlarını somut olaya altlayarak iade alacağının doğup doğmadığını denetlemek; "haklı sebep" kavramını ve illiyet bağını uygulamalı olarak çözmek. Bu, alanın çekirdek denetimidir.

## Soğuk başlangıç (intake)
- Zenginleşen tarafın malvarlığında ne arttı veya hangi gider/borçtan kurtuldu?
- Fakirleşen tarafta karşılık gelen azalma nedir; emek mi, mal mı, para mı?
- Kayma neye dayanıyordu; o sebep baştan yok mu, geçersiz mi, sonradan mı düştü?
- Tarafların iyiniyet/kötüniyet durumu ve kazanımın hâlâ mevcut olup olmadığı?

## Denetim şeması
1. **Zenginleşme (m.77/1).** Malvarlığında olumlu (yeni değer girişi) veya olumsuz (borçtan/giderden kurtulma) artış. Hizmet/kullanım gibi maddi olmayan yararlar da zenginleşmedir; ölçüsü tasarruf edilen masraf veya rayiç karşılıktır.
2. **Fakirleşme.** Karşı tarafın malvarlığından veya emeğinden bir değer çıkmış olmalı. Bazı müdahale hallerinde fakirleşme aranmaz veya kazanç ölçü alınır; bu nokta tartışmalıdır ve somut talebe göre belirlenir.
3. **İlliyet bağı.** Zenginleşme ile fakirleşme aynı olgudan kaynaklanmalı (doğrudan kayma). Dolaylı kazanımlarda (üçlü ilişkiler) talep yönü dikkatle belirlenir; kural olarak kendi sözleşme ilişkisi içinde iade istenir.
4. **Haklı sebebin yokluğu.** Kayma; geçerli bir sözleşme, kanun hükmü, mahkeme kararı veya bağışlama iradesi gibi hukuken onaylanan bir temele dayanmıyorsa "sebepsiz"dir. Haklı sebep başlangıçta yok (geçersiz), hiç gerçekleşmeyecek (gerçekleşmeyen) veya sonradan ortadan kalkmış (sona eren) olabilir.
5. **İspat yükü (TMK m.6, m.78).** İade isteyen; zenginleşmeyi, kendi kazandırmasını ve sebebin bulunmadığını/geçersizliğini ispatlar. Borçlanmadığı halde ödeyen, m.78 uyarınca yanılarak (hata ile) ödediğini de ortaya koymalıdır.
6. **Ara sonuç.** Dört unsur sağlanıyorsa iade borcu doğar; sağlanmıyorsa (ör. geçerli bağışlama, ifa edilmiş geçerli sözleşme) talep reddedilir. İade kapsamı için m.79 (iyiniyet ayrımı) bir sonraki adımdır.

## Çıktı modülleri
- Unsur-unsur altlama tablosu (var/yok + dayanak).
- Haklı sebep analizi notu.
- İlliyet/üçlü ilişki şeması (gerekiyorsa).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

