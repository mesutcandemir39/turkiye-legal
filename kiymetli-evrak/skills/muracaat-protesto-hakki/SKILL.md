---
argument-hint: ''
description: Ödememe/kabul etmeme halinde başvurma hakkının doğumu, protesto zorunluluğu
  ve başvurma bedelinin kapsamını incelemek; cirantalara ve avalistlere rücu imkânı
  değerlendirilirken kullanılır.
name: muracaat-protesto-hakki
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
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müracaat Hakkı ve Protesto

## Görev
Senedin ödenmemesi veya kabul edilmemesi halinde hamilin başvurma (müracaat) hakkını, bu hakkın korunması için gereken protesto/işlemleri ve başvurma bedelinin kapsamını belirlemek.

## Soğuk başlangıç (intake)
- Senet vadesinde ibraz edildi mi; ödenmedi mi, kabul mü edilmedi?
- Protesto çekildi mi (ödememe/kabul etmeme protestosu) ya da "protestosuz/masrafsız" kaydı var mı?
- Hamil hangi borçlulara (düzenleyen, cirantalar, avalistler) başvurmak istiyor?
- İbraz ve protesto süreleri tutuldu mu?

## Denetim şeması
1. Başvurma hakkının doğumu: vadede ödememe ya da vadeden önce kabul etmeme/ödememe ihtimali (iflas, ödemelerin tatili) hallerinde hamil cirantalara, düzenleyene ve diğer borçlulara başvurabilir (TTK m.713).
2. Protesto şartı: kural olarak başvurma hakkı, ödememe/kabul etmeme protestosunun süresinde düzenlenmesine bağlıdır (TTK m.714, m.722). Protesto noter aracılığıyla yapılır.
3. Muafiyet: "masrafsız/protestosuz iadesi" kaydı protesto zorunluluğunu kaldırır ama ibraz ve süre yükümlülüğünü kaldırmaz (TTK m.722).
4. İhbar: hamil, ödememe/kabul etmemeyi kendinden önceki borçluya süresinde ihbar eder (m.723); ihmal tazminat sorumluluğu doğurabilir, hakkı düşürmez.
5. Başvurma bedeli: hamil senet bedeli, işlemiş faiz, protesto ve ihbar masrafları ile komisyonu isteyebilir (TTK m.725); ödeyen ciranta kendinden öncekilerden m.726 kapsamında talep eder.
6. Ara sonuç: süre/protesto yükümlülükleri yerine getirilmemişse cirantalara ve onların avalistlerine başvurma hakkı düşer (m.730); ancak asıl borçluya (kabul eden/düzenleyen) karşı hak, zamanaşımına dek korunur.

## Çıktı modülleri
- Müracaat hakkı kontrol listesi (ibraz + protesto + süre).
- Başvurma bedeli hesap kalemleri tablosu (bedel/faiz/masraf [doldurulacak]).
- Protesto/ihbar taslağı veya hak düşümü savunma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

