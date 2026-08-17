---
argument-hint: ''
description: Yatırımcı ve kurucular arasındaki yönetişim ve çıkış dengesini kuran
  pay sahipleri sözleşmesi (SHA) hazırlanır veya müzakere edilirken; veto, bilgi alma,
  sürükleme-birlikte satış, önalım gibi hükümler
name: pay-sahipleri-sozlesmesi-sha
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Pay Sahipleri Sözleşmesi (SHA) Kurgusu

## Görev
Kurucu-yatırımcı ilişkisinin yönetişim, kontrol, koruma ve çıkış mekanizmalarını SHA'da TBK serbestisi içinde kurgulamak; hangi hükmün esas sözleşmeye taşınması (ayni etki için) gerektiğini saptamak.

## Soğuk başlangıç (intake)
1. Taraflar ve pay oranları; kim çoğunluk, kim azınlık/yatırımcı?
2. İstenen mekanizmalar: veto/onay konuları, yönetim koltuğu, bilgi alma?
3. Çıkış hükümleri: drag-along, tag-along, önalım, IPO/satış senaryosu?
4. Vesting (kurucu ve çalışan) ve rekabet/devamlılık yükümlülüğü isteniyor mu?
5. İhtilaf çözümü: tahkim mi, mahkeme mi; uygulanacak hukuk?

## Denetim şeması
1. Geçerlilik temeli: SHA hükümleri taraflar arası borç sözleşmesidir (TBK m.26-27 serbestisi). Bunlar şirkete karşı doğrudan etki etmez; ayni etki (devir engeli, imtiyaz) için esas sözleşme/bağlam (TTK m.491-493, m.478-479) gerekir.
2. Yönetişim: Veto/olumlu oy konuları, yönetim kurulu temsili — oy sözleşmesi geçerli; ancak oy hakkının payla bütünlüğü (m.434) ve dürüstlük (TMK m.2) sınırı. Devredilemez YK yetkileri (m.375) sözleşmeyle kurucudan alınamaz.
3. Çıkış mekanizmaları: Drag-along (sürükleme), tag-along (birlikte satış), önalım — taraflar arası borç olarak geçerli; ihlalde cezai şart (TBK m.179) ve aynen ifa/tazminat. Payın üçüncü kişiye geçişini şirkete karşı engellemek için esas sözleşmesel bağlam (m.491-493) eklenmeli.
4. Vesting/ters vesting: Kurucu paylarının hak edilmesi; ayrılma halinde geri alım veya zorunlu satış — TBK serbestisi + esas sözleşmesel devir mekanizması ile kurulur.
5. Çıkmaz (deadlock): Eşit ortaklıkta tıkanma çözümü (shotgun/rus ruleti, üçüncü kişi, fesih); haklı sebeple fesih hakkı saklı (TTK m.531).
6. Uyum/çatışma: SHA-esas sözleşme çelişkisinde şirkete karşı esas sözleşme; taraflar arası SHA. Çatışmayı baştan haritala.
7. İspat/şekil: Yazılı; gerekirse imza onaylı. İhlalde def'i ve cezai şart kanıt zinciri.

## Çıktı modülleri
- SHA hüküm seti taslağı (veto/drag/tag/önalım/vesting + cezai şart).
- Esas sözleşmeye taşınması gereken hükümlerin listesi (ayni etki notu).
- SHA-esas sözleşme uyum/çatışma matrisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

