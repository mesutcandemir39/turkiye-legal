---
argument-hint: ''
description: Yürürlükteki bir maddenin yorumunda TMK m.1 çerçevesinde tarihî ve sistematik
  argüman üretilecekse; bir hükmün kökeninin (İsviçre/Roma) bugünkü anlamı aydınlatmak
  için kullanılacağı durumlarda devreye
name: tarihsel-yorum-argumani
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


# Tarihsel-Sistematik Yorum Argümanı Üretimi

## Görev
Yürürlükteki bir Türk hükmünün yorumunda, kökenini (Roma/İsviçre/Pandekt) kullanarak TMK m.1 çerçevesinde tarihî ve sistematik yorum argümanı üretmek; bu argümanı yürürlükteki normun yerine değil, onun anlamını desteklemek için konumlamak.

## Soğuk başlangıç (intake)
- Hangi madde ve hangi yorum sorunu (lafzî belirsizlik, boşluk, çatışma)?
- Tarihî argüman lehte mi aleyhte mi kullanılacak?
- Karşı argüman (amaçsal/güncel yorum) da gerekiyor mu?

## Denetim şeması
1. Yorum sorununu çerçevele: TMK m.1 — kanun lafzıyla ve ruhuyla uygulanır; boşlukta hâkim örf-âdet, yoksa kendisi kural koyarmış gibi karar verir; yerleşik doktrin ve içtihattan yararlanır. Yorum yöntemini belirle: lafzî, sistematik, tarihî, amaçsal.
2. Tarihî kaynağı tespit et: maddenin İsviçre kaynağını (ZGB/OR) ve gerekiyorsa Roma kökünü resepsiyon zinciri yoluyla sapta. Kaynak normun lafzı/amacı ile Türk metni arasındaki farkı işaretle.
3. Tarihî argümanı kur: kanun koyucunun iktibasta korumak istediği amacı, kaynak hukuktaki yerleşik anlamı yürürlükteki maddenin yorumuna taşı. Roma kökeni varsa, kavramın klasik işlevini bugünkü anlamı aydınlatmak için kullan.
4. Sistematik argümanı ekle: maddenin TMK/TBK içindeki konumu, komşu hükümlerle (ör. genel-özel norm, TMK m.2-3 dürüstlük süzgeci) ilişkisini kur. lex specialis ve sistematik bütünlük argümanını uygula.
5. Sınır ve denge: tarihî argüman amaçsal/güncel yoruma feda edilebilir; kanun koyucunun iradesi ile bugünkü ihtiyaç çatışırsa, yürürlükteki amaçsal yorumun üstünlüğünü kabul et. Tarihî argüman destekleyicidir, belirleyici değil; bunu açıkça yaz.
6. Karşı argümanı tartı: tarihî yoruma karşı amaçsal/teleolojik itirazı kur ve hangisinin somut olayda baskın olduğunu gerekçelendir. Ara sonuç: yorum sonucunu ve tarihî argümanın ağırlığını netleştir.

İspat/dayanak: TMK m.1 ve ilgili madde ile; kaynak norm (ZGB/OR) ve Roma kökü fragman/künye ile [DOĞRULANMADI]; mahkeme tarihî-sistematik yorum kullanmışsa karararama.yargitay.gov.tr üzerinden doğrula, karar numarası uydurma.

## Çıktı modülleri
- Yorum argümanı bloğu: madde + sorun + tarihî kök + sistematik konum + sonuç.
- Karşı argüman ve tartı notu.
- Sınır uyarısı: tarihî argüman destekleyici, yürürlükteki norm belirleyici.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

