---
argument-hint: ''
description: Tapu, nüfus, ticaret sicili gibi resmî sicillere veya resmî senetlere
  dayanılan ya da bunların içeriğine itiraz edilen durumlarda; resmî belgenin ispat
  gücünü ve aksinin nasıl ispatlanacağını belirlem
name: resmi-belge-ve-sicile-guven-tmk-7
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Resmî Belgelerin İspat Gücü ve Sicile Güven (TMK m.7)

## Görev
Resmî sicil ve resmî senetlerin TMK m.7 uyarınca sahip olduğu ispat karinesini, bu karinenin kapsamını ve aksinin nasıl ispatlanacağını belirlemek; resmî belgeyle sicile güven ilkesi arasındaki bağı kurmak.

## Soğuk başlangıç (intake)
- Hangi resmî belge/sicil söz konusu (tapu kaydı, nüfus kaydı, ticaret sicili, resmî senet)?
- Karine, belgenin *hangi içeriğine* ilişkin (belgeyi düzenleyen memurun huzurunda olup bittiğini tespit ettiği olgular mı, beyanların doğruluğu mu)?
- Belgenin içeriğine itiraz mı ediliyor, yoksa sahteliği mi iddia ediliyor?
- Üçüncü kişinin sicile/belgeye iyiniyetle güveni var mı (TMK m.1023, m.3)?

## Denetim şeması
1. **Karine** — TMK m.7: resmî sicil ve senetler, belgeledikleri olguların doğruluğuna kanıt oluşturur; bunların içeriğinin doğru olmadığının ispatı, kanunlarda başka bir hüküm olmadıkça herhangi bir şekle bağlı değildir.
2. **Karinenin kapsamı** — Resmî belgenin güçlü ispat değeri, memurun *kendi tespit ve işlemlerine* ilişkin kısmıdır. Tarafların memura yaptığı beyanların maddî doğruluğu bu güçlü karineye dahil değildir; bunlar aksi serbestçe ispatlanabilen kısımdır.
3. **Aksini ispat** — İçeriğin doğru olmadığı, kanun başka şekil aramıyorsa serbest delille ispatlanır. Sahtelik iddiası ise ayrı bir rejime (HMK senedin sahteliği, ceza boyutu) tabidir.
4. **Sicile güven köprüsü** — Tapu siciline iyiniyetle güvenerek ayni hak kazanan üçüncü kişinin kazanımı korunur (TMK m.1023); yolsuz tescile rağmen iyiniyetli üçüncü kişi m.3 + m.1023 ile korunabilir. Bu, m.7 karinesinin maddi hukuktaki uzantısıdır.
5. **İspat yükü etkisi** — m.7, lehine karine olan tarafı ispat yükünden kurtarır; içeriğin yanlışlığını ileri süren aksini ispatla yükümlüdür (TMK m.6 ile bağ).
6. **Sınır** — Karine, belgenin geçerli ve usulüne uygun düzenlenmiş olmasını varsayar; yetkisiz makam/usulsüzlük karineyi zayıflatır.

## Çıktı modülleri
- Resmî belge/sicil türü ve karine kapsamı tespiti.
- Güçlü karine kısmı / serbest ispata açık kısım ayrımı.
- Aksini ispat yolu ve yükü.
- Sicile güven (m.1023/m.3) bağı + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

