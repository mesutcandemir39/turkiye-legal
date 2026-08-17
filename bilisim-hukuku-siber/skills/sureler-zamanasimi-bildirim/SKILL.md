---
argument-hint: ''
description: Bilişim/siber uyuşmazlıkta ceza zamanaşımı, dava açma süreleri, KVKK
  ihlal bildirim süresi ve başvuru sürelerini hesaplamak ve hak kaybını önleyecek
  takvim kurmak gerektiğinde kullanılır.
name: sureler-zamanasimi-bildirim
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve Bildirim Takvimi

## Görev
Olaya bağlı tüm süreleri (bildirim, şikâyet, dava, zamanaşımı) tespit edip hak düşürücü kayıpları önleyecek bir takvim kurmak.

## Soğuk başlangıç (intake)
1. Olay/öğrenme tarihi ve fark edilme anı ne?
2. Hangi süreçler söz konusu? (ceza, KVKK bildirim, tazminat, idari dava?)
3. Şikâyete bağlı suç var mı, fail/zarar biliniyor mu?
4. Bir tebligat/karar var mı, tarihi ne?

## Denetim şeması
1. **KVKK ihlal bildirimi.** Veri ihlalinde Kurula bildirim, öğrenmeden itibaren Kurul uygulaması gereği **72 saat** içinde yapılır; ilgili kişilere de makul en kısa sürede bildirilir. Gecikme ayrı bir yaptırım riskidir.
2. **Ceza zamanaşımı (TCK m.66-72).** Dava zamanaşımı suçun cezasının üst sınırına göre belirlenir (TCK m.66); bilişim suçlarının çoğunda 8 yıllık dilim devreye girer. Şikâyete bağlı suçlarda **6 aylık** şikâyet süresi (TCK m.73) failin ve fiilin öğrenilmesinden itibaren işler. Banka/kart suçları ve nitelikli haller resen takip edilir.
3. **Tazminat zamanaşımı.** Haksız fiilde zarar ve failin öğrenilmesinden itibaren **2 yıl** ve her halde fiilden itibaren **10 yıl** (TBK m.72); fiil aynı zamanda suçsa daha uzun ceza zamanaşımı uygulanır. Sözleşmesel taleplerde genel **10 yıl** (TBK m.146), özel hallerde **5 yıl** (TBK m.147).
4. **İdari/içerik süreleri.** KVKK Kurul kararına/idari yaptırıma karşı dava açma süresi (2577 İYUK m.7, kural 60 gün; idari para cezası niteliğine göre değerlendirilir). 5651 sulh ceza/BTK kararlarına itiraz CMK itiraz süresine (kural 7 gün) tabidir.
5. **Ara sonuç.** Her süre için başlangıç anı, uzunluk, son gün ve durma/kesilme halleri belirlenip tek takvimde toplanır. İspat açısından öğrenme tarihinin belgelenmesi önemlidir.

## Çıktı modülleri
- Süre takvimi tablosu (süreç, başlangıç, uzunluk, son gün, dayanak).
- Hak düşürücü riskler ve öncelikli aksiyonlar.
- Şikâyet/dava/itiraz için son tarih uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

