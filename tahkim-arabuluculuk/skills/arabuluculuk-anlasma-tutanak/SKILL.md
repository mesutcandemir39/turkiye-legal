---
argument-hint: ''
description: Arabuluculuk sonunda düzenlenen anlaşma belgesi veya son tutanağı kaleme
  almak, denetlemek ve icra edilebilirliğini sağlamak gerektiğinde kullanılır.
name: arabuluculuk-anlasma-tutanak
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Arabuluculuk Anlaşma Belgesi ve Tutanak

## Görev
Arabuluculuk sürecinin yazılı çıktısını (anlaşma belgesi veya son tutanak) hukuken sağlam,
icra edilebilir ve ileride uyuşmazlık doğurmayacak şekilde hazırlamak veya denetlemek.

## Soğuk başlangıç (intake)
1. Süreç anlaşma ile mi anlaşmama ile mi sonuçlandı, kısmi anlaşma var mı?
2. Anlaşma konuları neler, edimler somut ve infazı kabil mi?
3. Taraflar avukatla mı temsil edildi (icra edilebilirlik şerhi etkisi)?
4. Belge dava şartı arabuluculuk sonucu mu, sonraki dava açma süresine etkisi ne?

## Denetim şeması
1. **Belge türü**: Anlaşma sağlandıysa **anlaşma belgesi**; sağlanamadıysa **son tutanak**
   (**HUAK m.17, m.18**). Son tutanağa anlaşılan/anlaşılamayan hususlar açıkça yazılır.
2. **İçerik sağlamlığı**: Taraflar, uyuşmazlık konusu, üzerinde anlaşılan edimler, ödeme
   takvimi, ferağ/feragat kapsamı açık ve infaza elverişli olmalı. Belirsiz edim icra
   sorunudur.
3. **İcra edilebilirlik**: Taraflar **ve avukatları ile arabulucunun** birlikte imzaladığı
   anlaşma belgesi **icra edilebilirlik şerhi niteliğinde** olup ilam hükmündedir
   (**HUAK m.18/4**). Avukatla imzalanmadıysa **sulh hukuk mahkemesinden** şerh alınır.
4. **Anlaşılan konunun davaya kapanması**: Anlaşılan hususlar yönünden taraflar dava
   açamaz; bu, belgenin kesin etkisidir. Anlaşılamayan kısım için dava şartı sürer.
5. **Ara sonuç**: Belgenin icra edilebilirliği, açık riskler ve düzeltme önerileri.

## Çıktı modülleri
- Anlaşma belgesi / son tutanak taslağı (taraf, edim, takvim, imza bölümleriyle).
- İcra edilebilirlik kontrol listesi (avukat imzası vs. mahkeme şerhi ayrımı).
- Edim infaz riski notu (belirsiz/asimetrik ifadelerin işaretlenmesi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

