---
argument-hint: ''
description: Kullanıcı dava açmanın maliyetini (harç, gider avansı, delil avansı),
  tutarın nasıl belirlendiğini veya ödeme gücü yoksa adli yardımdan nasıl yararlanacağını
  öğrenmek istediğinde kullanılır.
name: harc-gider-ve-adli-yardim
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


# Harç, Gider Avansı ve Adli Yardım

## Görev
Dava açma maliyetini öngörmek; harç ve avansları doğru yatırmak; ödeme gücü yetersizse adli yardım yolunu açmak.

## Soğuk başlangıç (intake)
- Davanın türü ve talep tutarı (değeri) nedir?
- Kaç tanık, kaç davalı ve tebligat söz konusu?
- Bilirkişi/keşif gerekecek mi?
- Maddi durumunuz harçları karşılamaya yeterli mi?
- İhtiyaç durumunuzu gösteren belge (gelir, mal varlığı) var mı?

## Denetim şeması
1. **Harçlar (492 sayılı Harçlar Kanunu):** Başvurma harcı (maktu) ve karar-ilam harcı alınır. Konusu para olan davalarda karar-ilam harcı nispîdir (talep edilen değer üzerinden); dörtte biri peşin yatırılır, kalanı karar sonunda. Maktu harçlı işler de vardır. Güncel tarife yıllık güncellenir — **[DOĞRULANMADI]**.
2. **Gider avansı (HMK m.120):** Tebligat, müzekkere, tanık gibi yargılama giderleri için mahkemenin belirlediği avans peşin yatırılır; yatırılmazsa dava işleme alınmaz/usulden reddedilebilir. Miktar yıllık tarifeyle belirlenir.
3. **Delil avansı (HMK m.324):** Bilirkişi/keşif gibi delil için ilgili taraf ayrıca avans yatırır; yatırmazsa o delile dayanmaktan vazgeçmiş sayılır.
4. **Adli yardım (HMK m.334-340):** Yargılama giderlerini kısmen/tamamen karşılayamayacak ve davası açıkça dayanaktan yoksun olmayan kişi adli yardım talep edebilir; kabulde harç ve avanslardan geçici muafiyet sağlanır (m.335). Talep, asıl davanın açılacağı mahkemeye yapılır (m.336) ve ihtiyaç belgelenir.
5. **Kazanma halinde iade:** Yargılama giderleri kural olarak haksız çıkan tarafa yüklenir (HMK m.326); kazanan, yatırdığı harç ve gideri karşı taraftan tahsil edebilir.
6. **Ara sonuç:** Harç + avans hesabı yapılır; ödeme gücü yoksa adli yardım dilekçesi öne alınır.

## Çıktı modülleri
- Tahmini maliyet tablosu (başvurma harcı, peşin karar-ilam harcı, gider/delil avansı) — güncel tarife **[DOĞRULANMADI]** notuyla.
- Adli yardım talep dilekçesi taslağı ve gereken belgeler listesi.
- Kazanma halinde gider tahsili notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

