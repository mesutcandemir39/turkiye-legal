---
argument-hint: ''
description: Kendisine dava açılmış ve cevap dilekçesi vermesi gereken davalı, itirazlarını
  ve karşı delillerini düzenlemek istediğinde veya zamanaşımı, yetki, takas gibi savunmaları
  ileri sürmek istediğinde kulla
name: cevap-dilekcesi-ve-savunma
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


# Cevap Dilekçesi ve Savunma Hazırlama

## Görev
Davalı tarafın süresinde, eksiksiz ve stratejik bir cevap dilekçesi vermesini sağlamak; itiraz ve def'ileri doğru sırayla ileri sürmek.

## Soğuk başlangıç (intake)
- Dava dilekçesi/tebligat size ne zaman tebliğ edildi (süre için kritik)?
- İddiaların hangisini kabul, hangisini inkâr ediyorsunuz?
- Yetki/görev itirazınız var mı?
- Alacak zamanaşımına uğramış olabilir mi?
- Karşı alacağınız (takas) veya karşı dava talebiniz var mı?

## Denetim şeması
1. **Süre:** Cevap dilekçesi, dava dilekçesinin tebliğinden itibaren kural olarak iki hafta içinde verilir (HMK m.127); basit yargılamada da iki hafta (m.317). Süre içinde verilmezse davacının dilekçesindeki vakıaları inkâr etmiş sayılır (m.128); ek süre talep edilebilir.
2. **İlk itirazlar (HMK m.116, 117):** Kesin yetki dışındaki yetki itirazı, tahkim itirazı, iş bölümü gibi itirazlar **cevap dilekçesinde birlikte** ileri sürülür; sonradan ileri sürülemez.
3. **Maddi savunma:** Vakıaların açıkça kabul/inkârı; inkâr edilen her vakıa için karşı delil (m.129). Susulan vakıa ikrar sayılabilir.
4. **Def'iler:** Zamanaşımı def'i talep edilmedikçe hâkim re'sen dikkate almaz — mutlaka açıkça ileri sürülür. Takas, ödemezlik def'i (TBK m.97) gibi savunmalar bu aşamada belirtilir.
5. **Karşı dava:** Şartları varsa (HMK m.132-134) cevap dilekçesiyle birlikte açılır.
6. **Ara sonuç:** Süre + ilk itirazlar + maddi inkâr + def'iler eksiksizse savunma tamamdır; basit yargılamada savunmanın genişletilmesi de sınırlıdır (m.319).

## Çıktı modülleri
- Cevap dilekçesi taslağı (itiraz/def'i/karşı delil bölümleriyle).
- Süre uyarısı ve kalan gün hesabı.
- Zamanaşımı/takas kontrol notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

