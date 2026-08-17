---
argument-hint: ''
description: Zarar bir çalışanın, hayvanın, yapının veya tehlikeli bir işletmenin
  faaliyetinden doğduğunda; failin kusuru ispatlanamasa bile sorumluluk kurulabilecek
  objektif sorumluluk normunu belirlemek için kul
name: kusursuz-sorumluluk-halleri
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


# Kusursuz (Objektif) Sorumluluk Halleri

## Görev
Olaya uyan objektif sorumluluk normunu seçmek (hakkaniyet m.65, adam çalıştıran m.66, hayvan m.67-68, yapı maliki m.69-70, tehlike m.71) ve bu normun şartları ile kurtuluş imkânını denetlemek. Kusur aranmadığından dava, zarar görenin lehine ispat kolaylığı sağlar.

## Soğuk başlangıç (intake)
- Zarar kimin/neyin faaliyetinden doğdu (çalışan, hayvan, bina/eser, tehlikeli işletme)?
- Sorumlu sıfatı kimde (işveren, hayvan bulunduran, yapı maliki, işletme sahibi)?
- Failin kusuru ispatlanabilir mi, yoksa objektif sorumluluk mu daha güçlü?
- Özel kanun rejimi var mı (KTK işleteni m.85, ürün, çevre)?

## Denetim şeması
1. **Adam çalıştıranın sorumluluğu (m.66).** İşveren, çalışanın işin görülmesi sırasında üçüncü kişiye verdiği zarardan kusursuz sorumludur. Kurtuluş kanıtı: işveren seçim, talimat, gözetim ve organizasyonda gerekli özeni gösterdiğini ispatlarsa sorumluluktan kurtulabilir.
2. **Hayvan bulunduranın sorumluluğu (m.67-68).** Hayvanın verdiği zarardan bulunduran sorumludur; gerekli özeni gösterdiğini ispatlarsa kurtulur. Alıkoyma hakkı m.68'de düzenlidir.
3. **Yapı malikinin sorumluluğu (m.69-70).** Bir binanın/yapı eserinin yapım bozukluğu veya bakım eksikliğinden doğan zarardan malik kusursuz sorumludur; intifa/kira hakkı sahibine rücu mümkündür.
4. **Tehlike sorumluluğu (m.71).** Önemli ölçüde tehlike arz eden işletmenin faaliyetinden doğan zarardan işletme sahibi ve işleten kusursuz/kurtuluşsuz sorumludur; tipik tehlike gerçekleşmişse sorumluluk kaçınılmazdır.
5. **Hakkaniyet sorumluluğu (m.65).** Ayırt etme gücü bulunmayanın verdiği zararda hakkaniyet gerektiriyorsa tazminata hükmedilebilir.
6. **Ara sonuç ve rücu.** İlliyet ve sorumlu sıfatı zarar görence; kurtuluş kanıtı sorumluca ispatlanır. Birden çok sorumlu varsa müteselsil sorumluluk (m.61) ve iç ilişkide rücu (m.62) belirlenir.

## Çıktı modülleri
- Norm seçim notu (uygulanacak madde + sorumlu sıfatı).
- Kurtuluş kanıtı/şart kontrol listesi.
- Müteselsil sorumluluk ve rücu haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

