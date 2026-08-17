---
argument-hint: ''
description: İş kazası veya meslek hastalığı bildirimi, sürekli iş göremezlik gelirinin
  bağlanması, işverenin/üçüncü kişinin kusuru ve SGK rücu boyutu söz konusu olduğunda;
  hem sigortalı hem işveren cephesinden ku
name: is-kazasi-meslek-hastaligi
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İş Kazası ve Meslek Hastalığı

## Görev
Olayın iş kazası/meslek hastalığı niteliğini saptamak, sigortalıya sağlanacak edimleri ve işveren/üçüncü kişi sorumluluğu ile Kurumun rücu hakkını çözümlemek.

## Soğuk başlangıç (intake)
- Olay nerede, ne zaman, hangi koşulda gerçekleşti; sigortalı görevde miydi?
- SGK'ya iş kazası bildirimi yapıldı mı, ne zaman?
- Sürekli iş göremezlik derecesi (maluliyet oranı) tespit edildi mi?
- İşverenin İSG yükümlülüğü ihlali veya üçüncü kişi kusuru var mı?

## Denetim şeması
1. İş kazası tanımı — 5510 m.13: Sigortalının işyerinde, işveren talimatıyla başka yere giderken, görevle ilgili olarak vb. uğradığı olay. Tanıma giren bağlantı (illiyet) kurulur.
2. Meslek hastalığı — m.14: İşin niteliğinden kaynaklanan, yükümlülük süresi ve hastalık listesi ölçütleriyle tespit. SGK Yüksek Sağlık Kurulu/ATK raporu belirleyici.
3. Bildirim: İşveren iş kazasını m.13 ve İş Sağlığı ve Güvenliği Kanunu (6331 m.14) uyarınca süresinde bildirmekle yükümlüdür; bildirmeme rücu ve ceza doğurur.
4. Edimler: Geçici iş göremezlik ödeneği (m.18), sürekli iş göremezlik geliri (m.19), ölüm halinde hak sahiplerine gelir (m.20).
5. Sorumluluk ve rücu — m.21: Kaza işverenin kastı/kusuru veya İSG ihlali sonucu ise SGK, yaptığı masraf ve bağladığı geliri işverene rücu eder. Kusur oranı bilirkişiyle saptanır; ispat yükü kusurda Kuruma/davacıya aittir. Ara sonuç: maluliyet, edim ve rücu tutarı.

## Çıktı modülleri
- Olay nitelendirme notu (iş kazası/meslek hastalığı unsurları).
- Edim ve maluliyet özeti.
- İşverene karşı rücu/maddi-manevi tazminat değerlendirmesi (TBK m.49-55 ile bağlantı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

