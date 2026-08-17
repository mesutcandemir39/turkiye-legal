---
argument-hint: ''
description: Dilekçenin sonuç kısmını infaz edilebilir biçimde yazmak; faiz türü ve
  başlangıcı, belirsiz alacak, terditli talep, harç ve vekâlet ücretini doğru kurmak
  gerektiğinde kullanılır.
name: talep-sonucu-faiz-gider
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Talep Sonucu, Faiz ve Yargılama Gideri

## Görev
Layihanın en kritik bölümü olan talep sonucunu, mahkemenin aynen hükmedebileceği ve infaz edilebileceği netlikte yazmak; faiz, gider ve vekâlet ücretini eksiksiz eklemek. Talep edilmeyen şeye hükmedilemez (HMK m.26 — taleple bağlılık).

## Soğuk başlangıç (intake)
- Talep miktarı belirli mi, belirsiz mi (HMK m.107)?
- Faiz türü ne: yasal mı, ticari/avans mı (3095 s.K., TBK m.88/120)?
- Faiz başlangıcı: temerrüt mü, dava/ihtar tarihi mi?
- Terditli/kademeli talep var mı?

## Denetim şeması
1. Talep türü: Eda, tespit, inşai ayrımını netleştirin; eda talebinde miktar ve para birimi açık olmalı.
2. Belirsiz alacak (HMK m.107): Miktar dava açılırken belirlenemiyorsa belirsiz alacak davası; asgari tutar ve fazlaya ilişkin hak saklı tutulur. Aksi halde kısmi dava (m.109) tercih edilir.
3. Faiz: Türünü ve başlangıcını ayrı belirtin. Temerrüt faizi başlangıcı TBK m.117 (temerrüt) ve m.120; oran 3095 s.K. (ticari işlerde avans faizi). Faiz talebi açıkça yazılmazsa hükmedilemez.
4. Yargılama gideri ve vekâlet ücreti (HMK m.323, m.326-330): Gider haksız çıkan tarafa yükletilir; vekâlet ücreti AAÜT'ye göre. Talep sonucuna açıkça ekleyin.
5. Terdit/kademe: Asıl ve yedek talebi (ör. öncelikle aynen ifa, olmazsa tazminat) açık ayırın; harç bu yapıya göre hesaplanır. Ara sonuç: her kalem yazılı ve dayanaklıysa sonuç bloğu kapanır.

## Çıktı modülleri
- Numaralı talep sonucu bloğu
- Faiz tablosu (tür, oran dayanağı, başlangıç)
- Belirsiz alacak/kısmi dava tercih notu
- Gider ve vekâlet ücreti talebi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

