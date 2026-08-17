---
argument-hint: ''
description: Zenginleşenin neyi, ne ölçüde geri vereceğini, semere ve faizin nasıl
  hesaplanacağını ve kazanımın elden çıkması halinde sorumluluğun değişip değişmediğini
  belirlemek gerektiğinde kullanılır.
name: iade-kapsami-ve-iyiniyet
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İadenin Kapsamı ve İyiniyet/Kötüniyet Ayrımı

## Görev
İade borcunun kapsamını TBK m.79 ekseninde belirlemek: iyiniyetli zenginleşenin "elde kalan zenginleşme" ile, kötüniyetli olanın tam iade ile sorumluluğunu ayırmak; semere, kullanım yararı ve faizi doğru hesaplamak. Bu beceri davanın miktarını belirler.

## Soğuk başlangıç (intake)
- İade konusu ne; aynen iade mümkün mü yoksa değer iadesi mi gerekiyor?
- Zenginleşen, kazanımı aldığında sebepsizliği biliyor muydu, bilmeli miydi?
- Kazanım kısmen/tamamen elden çıktı mı; nasıl (tüketim, devir, kayıp)?
- Kazanımdan semere/gelir elde edildi mi; kullanım yararı söz konusu mu?

## Denetim şeması
1. **Kural: elde kalan zenginleşme (m.79/1).** İyiniyetli zenginleşen, geri verme isteminden önce elinden çıkardığı ölçüde iadeyle yükümlü değildir; yalnızca hâlâ malvarlığında bulunan zenginleşmeyi iade eder.
2. **İstisna: kötüniyet/öngörü (m.79/2).** Zenginleşen, elden çıkarmada iyiniyetli değilse veya iadeyi (geri vermek zorunda kalacağını) hesaba katması gerekiyorduysa, elden çıkmış olsa bile tam değerden sorumludur.
3. **Aynen mi değer mi iade.** Mümkünse aynen iade; mümkün değilse (tüketilmiş, devredilmiş, türü gereği) rayiç değer üzerinden değer iadesi. Kullanım ve hizmet yararı rayiç karşılık (tasarruf edilen masraf) ile ölçülür.
4. **Semere ve faiz.** İyiniyetli zenginleşen toplanan semereleri ve kullanma karşılığını sınırlı verir; kötüniyetli olan elde ettiği ve elde edebileceği tüm semere/faizden sorumlu. Para borcunda temerrüt faizi başlangıcı (TBK m.117 ihtar / dava tarihi) ayrıca belirlenir.
5. **İspat yükü.** Zenginleşmenin elden çıktığını ve kendi iyiniyetini zenginleşen ispatlar (m.79/1); kötüniyet/öngörü iddiasını iade isteyen ileri sürer.
6. **Ara sonuç.** İade miktarı = aynen iade veya değer + semere/faiz; iyiniyet ayrımına göre net rakam ve faiz başlangıç tarihi çıkarılır. Giderler m.80 ile mahsup edilir.

## Çıktı modülleri
- İade miktarı hesap tablosu (anapara + semere + faiz).
- İyiniyet/kötüniyet değerlendirme notu (m.79/2 ölçütleri).
- Aynen/değer iade kararı gerekçesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

