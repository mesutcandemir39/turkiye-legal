---
argument-hint: ''
description: Bilişim/siber bir olayın hangi hukuk katmanlarına (ceza, KVKK, 5651,
  tazminat) dokunduğunu çözmek, kavramları yerli yerine oturtmak ve doğru başlığa
  yönlendirmek gerektiğinde kullanılır.
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


# Bilişim Hukukunun Temel Kavramları ve Sistematiği

## Görev
Bilişim/siber bir vakıayı doğru hukuki katmanlara ayırmak; bilişim sistemi, veri, içerik/yer/erişim sağlayıcı, dijital delil gibi temel kavramları tanımlayıp olayı isabetli alt-becerilere yönlendirmek.

## Soğuk başlangıç (intake)
1. Olay ne? (yetkisiz erişim, veri sızıntısı, dolandırıcılık, içerik ihlali, sistem kesintisi?)
2. Etkilenen ne? (bilişim sistemi mi, kişisel veri mi, banka/kart verisi mi, itibar/içerik mi?)
3. Taraf kim? (mağdur birey, kurum/veri sorumlusu, hizmet sağlayıcı, şüpheli?)
4. Beklenti? (şikâyet/ceza, uyum/idari savunma, tazminat, içerik kaldırma?)

## Denetim şeması
1. **Katman tespiti.** Olayı üç eksende sorgula: cezai (TCK m.243-245, m.135-140, m.158/1-f), idari/düzenleyici (KVKK m.12; 5651 m.8-9; BTK), özel hukuk (TBK m.49 vd. haksız fiil; sözleşmesel sorumluluk). Bir olay birden çok eksende sonuç doğurabilir.
2. **Bilişim sistemi kavramı.** TCK uygulamasında bilişim sistemi, verileri toplayıp işleyen manyetik/elektronik her türlü sistemdir; cep telefonu, sunucu, bulut hesabı dahil. Fiilin bir bilişim sistemi üzerinde gerçekleşip gerçekleşmediği tipikliğin ön şartıdır.
3. **Veri ayrımı.** Kişisel veri (KVKK/TCK m.135-140) ile sistem verisi (TCK m.244) ayrılır; banka/kredi kartı verisi için özel norm TCK m.245 önceliklidir.
4. **Sağlayıcı kavramı.** 5651 kapsamında içerik, yer, erişim ve toplu kullanım sağlayıcı ayrımı sorumluluk rejimini belirler; doğru sıfat saptanmadan tedbir/sorumluluk tartışılamaz.
5. **Ara sonuç.** Hangi katmanların devrede olduğu ve hangi alt-becerinin (suçlar, ihlal müdahalesi, dijital delil, sorumluluk, içerik kaldırma) öncelikli olacağı belirlenir. İspat yükü her katmanda ayrıdır: cezada iddia makamında, idari uyumda veri sorumlusunda (KVKK m.12 tedbirlerini aldığını ispat), tazminatta zarar görende.

## Çıktı modülleri
- Katman haritası (ceza / KVKK / 5651 / tazminat) ve öncelik sırası.
- Kavram tablosu: etkilenen sistem, veri türü, taraf sıfatları.
- Yönlendirme notu: hangi alt-beceriyle devam edileceği ve ilk aksiyonlar.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

