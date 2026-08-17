---
argument-hint: ''
description: Tarife/uzlaştırma alacağı, lisans yükümlülüğü ihlali, üretim/tüketim
  verisi, EPC ayıp ve gecikme gibi konularda hangi delilin nasıl elde edileceği ve
  değerlendirileceği belirlenirken kullanılır.
name: enerji-ispat-delil
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Enerji Uyuşmazlıklarında İspat ve Delil

## Görev
Enerji dosyasında ispat yükünü doğru dağıtmak; teknik/sayısal delili (ölçüm, uzlaştırma, EPDK kaydı) hukuken kullanılabilir biçimde toplamak ve bilirkişi incelemesine hazırlamak.

## Soğuk başlangıç (intake)
1. İspatı gereken vakıa nedir (bedel, ihlal, üretim miktarı, ayıp, gecikme)?
2. Mevcut belgeler hangileri (lisans, sözleşme, fatura, ölçüm verisi)?
3. Veri EPİAŞ/EPDK/dağıtım şirketinde mi; erişim yetkisi var mı?
4. Teknik konu bilirkişi gerektiriyor mu?

## Denetim şeması
1. **İspat yükü**: TMK m.6 — iddia eden ispatla yükümlü. İdari yaptırımda ihlali idare ispatlar; ancak müvekkil lehine vakıalar (uyum, mücbir sebep) müvekkilce belgelenir.
2. **Belge delili**: Lisans/önlisans, bağlantı ve sistem kullanım anlaşmaları, PPA/EPC, EPDK Kurul kararları ve yazışmaları öncelikli yazılı delildir (HMK m.199 vd.); ticari defterler TTK m.64 ve HMK kapsamında değerlendirilir.
3. **Teknik/sayısal veri**: Sayaç ve ölçüm verisi, EPİAŞ uzlaştırma ve PTF/SMF verileri, üretim raporları; bunların resmî kayıttan temini ve dönem bütünlüğü doğrulanır. Eksik dönem hesabı çürütür.
4. **Bilirkişi**: Tarife/uzlaştırma hesabı, üretim kaybı, EPC performans/ayıp gibi konularda HMK m.266 vd. bilirkişi; rapor metodolojisi ve dayanak verisi denetlenir, çelişki için ek rapor istenir.
5. **Delil tespiti ve sunum**: Acil hallerde HMK m.400 vd. delil tespiti; idari yargıda re'sen araştırma ilkesi gözetilerek eksik belgenin mahkemece getirtilmesi talep edilir.

## Çıktı modülleri
- İspat yükü ve delil planı tablosu (vakıa/delil/kaynak).
- Veri temin ve müzekkere talep listesi.
- Bilirkişiye sorulacak teknik sorular taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

