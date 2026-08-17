---
argument-hint: ''
description: Borçlunun borcunu zamanında ifa etmemesi, temerrüt faizi, gecikme tazminatı
  ve karşılıklı sözleşmelerde dönme/aynen ifa/tazminat seçeneklerinin değerlendirilmesi
  gerektiğinde kullanılır.
name: borclu-temerrudu
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


# Borçlu Temerrüdü ve Seçimlik Haklar

## Görev
Borçlunun temerrüde düşüp düşmediğini, ihtar ve süre şartlarını, temerrüt faizini ve karşılıklı sözleşmelerde alacaklının seçimlik haklarını belirlemek.

## Soğuk başlangıç (intake)
- Borç muaccel mi; alacaklı borçluyu ihtar etti mi?
- Sözleşmede kesin vade var mı (ihtar gereksiz hâl)?
- Edim para borcu mu; faiz oranı kararlaştırıldı mı?
- Alacaklı aynen ifada mı ısrar ediyor, yoksa dönme/fesih mi istiyor?

## Denetim şeması
1. Temerrüt şartları: TBK m.117 — muaccel borç + alacaklının ihtarı. İhtar gerekmeyen hâller (m.117/f.2): kesin vade kararlaştırılmış, ihtarın faydasızlığı, borçlunun ifadan kaçınacağını bildirmesi, haksız fiil/sebepsiz zenginleşme bazı hâlleri.
2. Genel sonuçlar: m.118 — borçlu beklenmedik hâlden de sorumlu olur (sorumluluğun ağırlaşması). Gecikme tazminatı.
3. Para borçlarında: m.120 — temerrüt faizi; sözleşmede oran yoksa 3095 s.K. uygulanır. Aşkın zarar (munzam zarar) m.122; ticari işlerde TTK m.8-9 faiz rejimi.
4. Karşılıklı borç yükleyen sözleşmelerde seçimlik haklar: m.123-126 — alacaklı uygun süre verir (m.123; gereksiz olduğu hâller m.124). Süre sonunda: ya aynen ifa + gecikme tazminatı, ya ifadan vazgeçip müspet zarar (olumlu zarar) tazmini, ya da sözleşmeden dönüp menfi zarar (olumsuz zarar) tazmini (m.125). Sürekli edimli sözleşmelerde dönme yerine fesih (m.126).
5. Müspet/menfi zarar ayrımı: Dönmede menfi zarar (sözleşme hiç yapılmasaydı durumu), ifadan vazgeçmede müspet zarar (sözleşme ifa edilseydi durumu).
6. İspat yükü: Temerrüdü ve zararı alacaklı; kusursuzluğu ve mücbir sebebi borçlu ispatlar.

## Çıktı modülleri
- Temerrüt oluşum analizi (ihtar/kesin vade kontrolü).
- Süre verme ihtarnamesi taslağı iskeleti.
- Seçimlik hak ve zarar kalemleri (müspet/menfi) tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

