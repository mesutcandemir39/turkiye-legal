---
argument-hint: ''
description: Sermaye Piyasası Kurulu'nun idari para cezası, tedbir ve menfaat iadesi
  kararlarına karşı savunma, idari yargıda iptal davası ve yürütmenin durdurulması
  gerektiğinde kullanılır.
name: idari-yaptirim-ve-iptal-davasi
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# SPK İdari Yaptırımları ve İptal Davası

## Görev
Kurul'un idari yaptırım kararını (idari para cezası, tedbir, menfaat iadesi) SPK m.92-104 ve İYUK çerçevesinde denetlemek; iptal davası ve yürütmenin durdurulması stratejisini kurmak.

## Soğuk başlangıç (intake)
- Yaptırımın türü ve dayanağı: hangi SPK maddesi/tebliğ ihlali gerekçe gösterildi?
- Karar ne zaman tebliğ edildi; dava açma süresi işliyor mu?
- Savunma alındı mı, usule uygun bildirim yapıldı mı; menfaat iadesi (m.104) var mı?
- Müvekkil gerçek kişi yönetici mi, ihraççı/kurum mu?

## Denetim şeması
1. **Yaptırım türü ve dayanak:** Kararın idari para cezası (m.103), tedbir (m.96-99) veya menfaat iadesi (m.104) niteliği ve dayanak maddesi belirlenir; ölçülülük (Anayasa m.13) test edilir.
2. **Usul denetimi:** Kurul kararının yetki, şekil, sebep, konu, maksat unsurları (idari işlem unsurları); savunma hakkı tanınması ve gerekçe yeterliliği incelenir. Usul sakatlığı tek başına iptal sebebidir.
3. **Esas denetimi:** İhlal fiilinin sabit olup olmadığı, isnat ile delil arasındaki bağ, cezanın alt-üst sınır ve tekerrür uygulaması denetlenir; ispat yükü ihlali iddia eden idarededir.
4. **Yargı yolu ve süre:** İptal davası idari yargıda açılır (İYUK m.2, m.7); dava açma süresi tebliğden itibaren işler, hak düşürücüdür; yürütmenin durdurulması (İYUK m.27) telafisi güç zarar ve açık hukuka aykırılık koşullarıyla talep edilir. Ara sonuç: süre takvimi ve YD talebi netleşir.
5. **Cezai eksenle ilişki:** Aynı fiil için cezai süreç (m.106-107) ayrı yürür; idari ve cezai sonuçların birbirini etkilemesi değerlendirilir.

## Çıktı modülleri
- Yaptırım kararı unsur denetim tablosu
- İptal sebepleri (usul + esas) listesi
- Dava açma süresi ve YD takvimi
- İptal/iddia dilekçesi iskeleti ([doldurulacak] yer tutucularıyla)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

