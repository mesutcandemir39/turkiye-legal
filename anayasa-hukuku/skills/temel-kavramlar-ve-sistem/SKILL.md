---
argument-hint: ''
description: Anayasa hukukunun temel kavramlarını, normlar hiyerarşisini ve 1982 Anayasası
  sistematiğini netleştirmek; bir uyuşmazlığın hangi anayasal başlığa ve denetim yoluna
  oturduğunu konumlandırmak gerektiğin
name: temel-kavramlar-ve-sistem
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Anayasal Sistematik

## Görev
Kullanıcının önündeki sorunu anayasal sistematiğe oturtmak: normlar hiyerarşisini, anayasanın üstünlüğünü (m.11), temel hak rejimini (m.12-74) ve organ yapısını (yasama-yürütme-yargı) doğru çerçeveye yerleştirip uygun denetim yoluna yönlendirmek.

## Soğuk başlangıç (intake)
1. Sorun bir norma mı (kanun, CB kararnamesi, yönetmelik) yoksa bireysel bir işleme/yargı kararına mı dayanıyor?
2. Hangi temel hak veya anayasal ilke (eşitlik, ifade, mülkiyet, adil yargılanma) zedeleniyor?
3. Taraf kim — birey mi, kamu organı mı, organlar arası yetki sorunu mu?
4. Hedef ne: norm denetimi, bireysel başvuru, yoksa danışma niteliğinde değerlendirme mi?

## Denetim şeması
1. **Normun yerini belirle.** Anayasa (m.11 üstünlük) > kanun/CB kararnamesi (m.104) > yönetmelik (m.124) > bireysel işlem. CB kararnamesi ile kanun çatışmasında kanun esas alınır (m.104/17).
2. **Hak/ilke katmanı.** İlgili Anayasa maddesini tespit et; m.90/son uyarınca AİHS'teki karşılığını köprüle. Ara sonuç: koruma alanı içinde miyiz?
3. **Sınırlama rejimi.** Bir hakka müdahale varsa m.13 süzgeci devreye girer (kanunilik, meşru amaç, demokratik toplumda gereklilik, ölçülülük, hakkın özü). Eşitlik iddiasında m.10: karşılaştırılabilir durum + farklı muamele + haklı sebep yokluğu.
4. **Yetki/usul katmanı.** Organlar arası ilişkide görev, şekil ve yöntem (yasama m.87-89, yürütme m.104-105, yargı bağımsızlığı m.138-140) ayrıca denetlenir.
5. **Denetim yolunu seç.** Soyut/somut norm denetimi (m.150-152), bireysel başvuru (m.148/3, 6216), idari yargı (m.125) ya da olağan yargı. İspat yükü, hak iddiası ileri süren tarafta; müdahalenin meşruiyetini ise müdahale eden kamu makamı temellendirir.

## Çıktı modülleri
- Sorunun anayasal nitelendirmesi ve uygulanacak madde haritası.
- Uygun denetim yolu ve ön koşulların (süre, sıfat, başvuru yolu tüketme) kısa kontrol listesi.
- Bir sonraki uzman beceriye yönlendirme (ör. sınırlama testi, eşitlik, bireysel başvuru).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

