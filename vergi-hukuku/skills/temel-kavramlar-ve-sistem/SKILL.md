---
argument-hint: ''
description: Vergi türünü, mükellefiyeti, vergiyi doğuran olayı ve uygulanacak katmanı
  (maddi-usul-icra-yargı) belirlemek; bir vergi dosyasının haritasını çıkarmak gerektiğinde
  kullanılır.
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Vergilendirme Sistematiği

## Görev
Vergi uyuşmazlığının ya da danışmanlık sorusunun hangi vergi türüne, hangi mükellefiyete ve hangi hukuki katmana ait olduğunu belirleyip dosyanın yol haritasını kurmak. Bu beceri çoğu vergi işinin giriş süzgecidir.

## Soğuk başlangıç (intake)
1. Hangi vergi türü söz konusu (gelir, kurumlar, KDV, ÖTV, damga, MTV, emlak)?
2. Mükellef gerçek kişi mi, tüzel kişi mi; tam/dar mükellef mi?
3. Vergiyi doğuran olay hangi takvim yılında/dönemde gerçekleşti?
4. Elde bir idari işlem var mı (ihbarname, ödeme emri, ceza), tebliğ tarihi nedir?
5. Amaç tespit mi, savunma mı, planlama mı?

## Denetim şeması
1. **Verginin kanuniliği:** Anayasa m.73 — vergi ancak kanunla konur. Dayanak normu (GVK 193, KVK 5520, KDVK 3065, VUK 213) ve ilgili maddeyi tespit et.
2. **Vergiyi doğuran olay:** VUK m.19 uyarınca olayın vukuu/hukuki durumun tekemmülü anını belirle. Bu an hem zamanaşımının (VUK m.114) hem de uygulanacak oran/mevzuatın referansıdır.
3. **Mükellef ve vergi sorumlusu ayrımı:** VUK m.8 — mükellef vergi borcunu kendi malvarlığından ödeyen; sorumlu, kesip ödeyen (örn. stopaj/tevkifat). Muhatabı doğru belirle.
4. **Ekonomik yaklaşım:** VUK m.3/B — vergilendirmede olayların gerçek mahiyeti esastır; ispat, iktisadi-ticari icaplara uygunlukla değerlendirilir. Muvazaa/peçeleme iddiası burada doğar.
5. **Katman tayini:** Sorun matrah/oran ise maddi hukuk; tarh-tebliğ-ceza-süre ise VUK usul; tahsil-haciz-tecil ise AATUHK; iptal talebi ise İYUK vergi yargısı.
6. **Ara sonuç:** Vergi türü + mükellefiyet + doğuran olay yılı + katman + (varsa) işlem tipi ve tebliğ tarihi tek satırda sabitlenir.

## Çıktı modülleri
- Dosya künyesi tablosu (vergi türü, dönem, mükellef, tutar, işlem tipi, tebliğ tarihi).
- Uygulanacak norm zinciri (kanun > madde > tebliğ > özelge, bağlayıcılık notuyla).
- Katman ve sonraki adım yönlendirmesi (uzlaşma / dava / düzeltme / planlama).
- Açık belirsizlikler ve istenecek belge listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

