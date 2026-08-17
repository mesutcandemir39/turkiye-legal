---
argument-hint: ''
description: Bir davanın esastan görülmeden usulden reddedilip reddedilemeyeceğini,
  dava şartı eksikliği mi yoksa ilk itiraz mı söz konusu olduğunu tespit etmek; husumet,
  hukuki yarar, derdestlik, kesin hüküm, yet
name: dava-sartlari-ilk-itirazlar
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
  version: 0.1.0
user-invocable: true
---


# Dava Şartları ve İlk İtirazlar Denetimi

## Görev
Davanın esasa geçmeden önce aşması gereken eşikleri taramak; dava şartı (re'sen, her aşamada) ile ilk itiraz (süresinde ve ön incelemede) ayrımını net kurmak.

## Soğuk başlangıç (intake)
- Davalı/davacı taraf sıfatı (husumet) doğru mu?
- Aynı dava başka mahkemede derdest mi, kesin hüküm var mı?
- Yetki/tahkim itirazı geç kalmamış mı (cevap süresi içinde mi)?
- Dava şartı arabuluculuk gerekiyorsa son tutanak dosyada mı?

## Denetim şeması
1. **Dava şartları** (HMK m.114): yargı yolu, görev, taraf ve dava ehliyeti, davayı takip yetkisi, hukuki yarar (m.114/1-h), derdestlik (m.114/1-ı), kesin hüküm (m.114/1-i), gider avansı (m.114/1-g, m.120). Bunlar **re'sen** ve yargılamanın **her aşamasında** gözetilir (m.115). Eksiklik giderilebilir nitelikteyse süre verilir (m.115/2); değilse dava usulden reddedilir.
2. **İlk itirazlar** (m.116): kesin yetki dışındaki yetki itirazı, tahkim itirazı, iş bölümü (görev kalıntısı) itirazları. Bunlar **yalnızca cevap dilekçesinde** ve hepsi birlikte ileri sürülür (m.117); ön incelemede karara bağlanır. Süresinde ileri sürülmezse dinlenmez.
3. **Husumet (sıfat)**: Maddi hukuka ilişkin taraf sıfatı eksikliği dava şartı değil, esastan ret sebebidir; ancak ön incelemede erken teşhis hak kaybını önler.
4. **Hukuki yarar**: Eda davası açılabilecekken tespit davası açılması, muaccel olmayan alacak gibi hallerde yarar yokluğu usulden redde götürür.
5. **Dava şartı arabuluculuk**: Ticari (TTK m.5/A), iş, tüketici ve genişleyen kapsamda son tutanak yoksa dava usulden reddedilir; kapsam mevzuattan teyit edilir.

Ara sonuç: Her bir başlık için "var / yok / giderilebilir / itiraz süresi geçti" etiketi çıkar.

## Çıktı modülleri
- Dava şartı kontrol listesi (madde atıflı, durum etiketli).
- İlk itiraz değerlendirmesi (süre tutmuş mu, hangileri birlikte ileri sürülmüş).
- Usulden ret riski ve giderme yolu önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

