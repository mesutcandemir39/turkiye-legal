---
argument-hint: ''
description: Kaybolan, çalınan veya yok olan kıymetli evrakın iptali davasını ve ödemeden
  men kararını yürütmek; senedi elinden çıkan hak sahibinin hakkını koruması gerektiğinde
  kullanılır.
name: senet-iptali-zayi
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


# Senedin Zıyaı ve İptali

## Görev
Elden çıkan (kayıp, çalıntı, yok olmuş) kıymetli evrakın iptali yoluyla hak sahibinin korunmasını sağlamak; ödemeden men tedbiri, ilan ve iptal kararı sürecini yürütmek.

## Soğuk başlangıç (intake)
- Senet hangi tip (çek, bono, poliçe, nama/hamiline) ve nasıl elden çıktı (kayıp/çalıntı/imha)?
- Senedi en son elinde bulunduran kim; senet içeriği (bedel, vade, taraflar) belgelenebiliyor mu?
- Senet henüz ödenmedi mi; muhatap/borçlu kim?
- Acil ödemeden men tedbiri gerekiyor mu?

## Denetim şeması
1. İptal kabiliyeti: kambiyo senetleri ve kıymetli evrak zıyaı halinde mahkemeden iptaline karar verilmesi istenebilir (TTK m.651 vd. genel; kambiyoda poliçe için m.757-765, çek için m.818 yollamasıyla uygulanır).
2. Yetkili/görevli mahkeme: kural olarak ödeme yeri veya senedin tedavül ettiği yer asliye ticaret mahkemesi; talep, senedi elinde bulunduranın bilinmemesi haliyle iptal davası olarak açılır.
3. Ödemeden men tedbiri: hak sahibinin istemi üzerine mahkeme borçluya/muhataba senet bedelini ödemekten men eden tedbir kararı verir (TTK m.758); böylece senet eline geçen üçüncü kişiye ödeme engellenir.
4. İlan ve süre: mahkeme, senedi getirmesi için hamile uygun süre vererek ilan yapar (m.759 vd.); süre içinde senet ibraz edilmezse iptaline karar verilir.
5. İptal kararının etkisi: iptal kararıyla hak sahibi, senet olmadan da hakkını borçludan talep edebilir veya yeni senet düzenlenmesini isteyebilir (m.763).
6. Ara sonuç: senet iyiniyetli üçüncü kişiye geçmişse onun korunan iktisabı (m.687) ile hak sahibinin iptal talebi karşı karşıya gelir; bu durumda iyiniyet ve devir zinciri ayrıca incelenir.

## Çıktı modülleri
- Ödemeden men tedbiri talepli iptal dilekçesi taslağı.
- Senet kimlik kartı (tip/bedel/vade/taraf [doldurulacak]).
- İlan ve süre takvimi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

