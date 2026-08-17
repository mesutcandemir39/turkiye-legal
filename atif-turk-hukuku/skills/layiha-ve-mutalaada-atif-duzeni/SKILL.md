---
argument-hint: ''
description: Dava dilekçesi, cevap, istinaf/temyiz layihası veya hukuki mütalaa yazılırken;
  mevzuat-içtihat-doktrin atıflarının metin içi yerleşimini ve hukuki sebep bildirimini
  düzenlemek için kullanılır.
name: layiha-ve-mutalaada-atif-duzeni
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Layiha ve Mütalaada Atıf Düzeni

## Görev
Bir layiha veya mütalaada atıfları, usul kurallarına ve okunabilirliğe uygun biçimde yerleştirmek; hukuki sebebi doğru bildirmek ve dayanakları izlenebilir kılmak.

## Soğuk başlangıç (intake)
- Belge türü: dava dilekçesi, cevap, replik/düplik, istinaf, temyiz, mütalaa mı?
- Yargı kolu hangisi (HMK, CMK, İYUK)?
- Talep sonucu hangi norma dayanıyor; hukuki sebepler listesi hazır mı?
- Atıf yoğunluğu metni boğuyor mu?

## Denetim şeması
1. **Hukuki sebep bildirimi** — HMK m.119/1-(g): dava dilekçesinde dayanılan hukuki sebepler gösterilir (hâkimin hukuku resen uygulaması saklı — iura novit curia). Mevzuat madde/fıkra ile bildirilir; eksik/yanlış hukuki niteleme tek başına hak kaybı doğurmaz ama atıf disiplinli olmalı.
2. **Vakıa-delil-hukuk ayrımı** — Vakıalar (HMK m.119/1-(e)) ayrı, deliller (m.119/1-(f)) vakıaya bağlı, hukuki sebepler ayrı bölümde; atıf yalnızca hukuk kısmında yoğunlaşır, vakıaya delil gösterilir.
3. **Atıf yerleşimi** — Mevzuat metin içinde "(TBK m.49)" parantezi ile; içtihat ana metinde ilke + künye, yoğunsa dipnotta; doktrin destekleyici olarak ölçülü kullanılır. Layiha içtihat yığını değil, argüman taşır.
4. **İçtihat seçimi** — Lehe ve güncel, mümkünse İBK/HGK; tek daire kararı "yerleşik" diye sunulmaz. Aleyhe yerleşik içtihat varsa öngörülüp karşılanır.
5. **Mütalaada katman dürüstlüğü** — Mütalaa kesinlik derecesini dürüstçe yansıtır ("kuvvetle muhtemel / tartışmalı"); bağlayıcı kural ile yazar görüşü ayrılır; risk açıkça yazılır.
6. **Doğrulama işaretleri** — Teyit edilmemiş künyeler `[DOĞRULANMADI]`, eksik bilgi `[doldurulacak]`; taslak bu işaretlerle teslim edilebilir, sahte numarayla değil.

## Çıktı modülleri
- Belgenin hukuki sebepler bölümü taslağı (madde atıflı).
- İçtihat yerleşim planı (ana metin/dipnot).
- Atıf yoğunluğu/okunabilirlik notu.
- `[DOĞRULANMADI]` / `[doldurulacak]` işaret listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

