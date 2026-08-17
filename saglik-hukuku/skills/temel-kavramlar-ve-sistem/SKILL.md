---
argument-hint: ''
description: Sağlık hukukunda ilk vasıflandırma için kullanılır; hekim-hasta ilişkisinin
  sözleşmesel mi idari mi olduğunu, hangi sorumluluk rejiminin ve yargı kolunun devreye
  gireceğini belirler.
name: temel-kavramlar-ve-sistem
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
  - ad: Banka Muhasebe Sistemi Hakkında Kanun
    numara: '1219'
    tur: kanun
  - ad: Gayrimenkul Ek Vergisi Hakkında Kanun
    numara: '3359'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Olayın hangi sorumluluk eksenine ve yargı koluna düştüğünü baştan doğru saptamak. Yanlış vasıflandırma görev-yetki, zamanaşımı ve ispat yükünü baştan bozar.

## Soğuk başlangıç (intake)
1. Müdahale nerede yapıldı: kamu hastanesi mi, özel hastane mi, muayenehane mi?
2. Talep eden hasta/yakını mı, hekim/hastane mi, sigorta mı?
3. Olay teşhis/tedavi/ameliyat/ilaç/onam hangi aşamada?
4. Zarar ne (ölüm, yaralanma, kalıcı sakatlık, sadece manevi)?
5. Olay tarihi ve dava/şikâyet açılmış mı?

## Denetim şeması
1. **İlişkinin niteliği**: Özel hastane/muayenehane ise ilişki kural olarak TBK m.502 vd. vekâlet sözleşmesidir; estetik/protez gibi sonucun vaat edildiği işlerde eser sözleşmesi (TBK m.470 vd.) tartışılır. Kamu hastanesinde ilişki idaridir; sorumluluk hizmet kusuruna dayanır.
2. **Yargı kolu**: Özel sağlık kuruluşu → adli yargı (tüketici/asliye hukuk). Kamu hastanesi → idari yargı, tam yargı davası (İYUK m.12-13). Hekime karşı kişisel dava 3359 Ek m.18 nedeniyle kural olarak idareye yöneltilir; rücu ayrı işler.
3. **Sorumluluk ekseni**: Hukuki (sözleşme TBK m.112 / haksız fiil TBK m.49), cezai (TCK m.85-89 taksir), idari/disiplin (1219, 663 KHK). Eksenler birikebilir.
4. **Özen ölçütü**: Hekim sonucu değil tıbbın gereği özeni borçlanır (TBK m.506/f.3 — benzer uzmandan beklenen özen). Ara sonuç: kusur var mı sorusuna geçilir.
5. **İspat yükü**: Kusuru kural olarak davacı ispatlar; aydınlatma ve onamın varlığını ise hekim/hastane ispatlar (TMK m.6 istisnası).

## Çıktı modülleri
- İlişki ve yargı kolu tespiti tablosu
- Uygulanacak sorumluluk eksenleri listesi
- Bir sonraki adım önerisi (hangi alt-beceriye geçilecek)
- Belirsizlik/eksik bilgi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

