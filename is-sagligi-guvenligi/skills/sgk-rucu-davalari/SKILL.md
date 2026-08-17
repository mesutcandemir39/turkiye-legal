---
argument-hint: ''
description: İş kazası veya meslek hastalığında SGK'nın yaptığı yardımları işverene
  rücu etmesini, kusur oranı ve peşin sermaye değeri hesabını değerlendirmek için
  kullanılır.
name: sgk-rucu-davalari
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# SGK Rücu Davaları

## Görev
İş kazası/meslek hastalığında SGK'nın sigortalıya veya hak sahiplerine yaptığı/yapacağı yardımları 5510 m.21 uyarınca kusurlu işverene (ve varsa üçüncü kişiye) rücuunu değerlendirmek; talep kapsamını ve savunmaları çıkarmak.

## Soğuk başlangıç (intake)
- SGK hangi yardımları yaptı/bağladı (geçici iş göremezlik, sürekli iş göremezlik geliri, ölüm geliri, cenaze/emzirme)?
- Kusur oranı tespiti var mı; işverenin İSG yükümlülük ihlali somutlaştı mı?
- Alt işveren-asıl işveren veya üçüncü kişi kusuru söz konusu mu?
- Bildirim yükümlülüğüne aykırılık (geç/eksik bildirim) iddiası var mı?

## Denetim şeması
1. **Rücunun şartı (5510 m.21/1):** İş kazası/meslek hastalığı, işverenin kasıt veya sigortalının sağlığını koruma ve İSG mevzuatına aykırı hareketi sonucu meydana gelmişse SGK, yaptığı/ileride yapacağı ödemeleri işverenden ister. Sorumluluk kusurla sınırlıdır; kusursuz işverene rücu edilmez.
2. **Üçüncü kişi sorumluluğu (m.21/4) ve bildirim aykırılığı (m.21/2):** Olay üçüncü kişi kusuruyla olduysa ona rücu; işveren bildirim yükümlülüğünü ihlal ettiyse bildirime kadarki ödemeler ayrıca işverene yüklenebilir.
3. **Kusur tespiti:** Mahkeme, dosyaya özgü bilirkişi/İSG raporuyla kusur dağılımını belirler; SGK talebi işverenin kusuru oranıyla sınırlıdır.
4. **Hesap:** Bağlanan gelirlerin ilk peşin sermaye değeri esas alınır; daha önce iş kazası tazminat davasında belirlenen kusur ve tavan (tazminat miktarı) ile bağlantı kurulur — SGK rücuu sigortalının işverenden isteyebileceği miktarı aşamaz (tavan/halefiyet ilkesi). **Ara sonuç:** Rücua konu kalemleri ve kusur oranını netleştir.
5. **Zamanaşımı:** Genel kurallar ve halefiyetin niteliğine göre; künye gerekiyorsa içtihadı karararama.yargitay.gov.tr'den `[DOĞRULANMADI]` olarak doğrula.

## Çıktı modülleri
- Rücua konu yardım kalemleri tablosu.
- Kusur oranı ve peşin sermaye değeri hesap notu.
- İşveren savunması (tavan, kusur, bildirim, üçüncü kişi) listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

