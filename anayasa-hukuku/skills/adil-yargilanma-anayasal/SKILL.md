---
argument-hint: ''
description: Bir yargılamada adil yargılanma hakkının (m.36) veya suç-ceza güvencelerinin
  (m.38) ihlal edilip edilmediğini anayasal düzeyde değerlendirmek; mahkemeye erişim,
  makul süre, silahların eşitliği ve masu
name: adil-yargilanma-anayasal
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Adil Yargılanma ve Hak Arama (Anayasal Boyut)

## Görev
Hak arama hürriyeti ve adil yargılanma hakkını (Anayasa m.36, AİHS m.6) ile suç ve cezalara ilişkin güvenceleri (m.38) anayasal düzeyde denetlemek; özellikle bireysel başvuruda en sık görülen bu ihlal alanını sistematik incelemek.

## Soğuk başlangıç (intake)
1. Yargılama türü ne (hukuk, ceza, idari) ve şikâyet hangi aşamadan kaynaklanıyor?
2. Sorun mahkemeye erişim, makul süre, gerekçeli karar, silahların eşitliği, yoksa karine ihlali mi?
3. Ceza yargılamasında masumiyet karinesi, savunma hakkı veya kanunilik mi tartışılıyor?
4. İhlal kesinleşmiş bir kararla mı ortaya çıktı (bireysel başvuru eşiği için)?

## Denetim şeması
1. **Uygulanabilirlik.** m.36/AİHS m.6 kapsamına giren bir "uyuşmazlık" (medeni hak/yükümlülük veya cezai suçlama) var mı? Ara sonuç: kapsam dışıysa adil yargılanma güvencesi devreye girmez.
2. **Mahkemeye erişim.** Harç, süre, dava şartı engelleri hakkın özünü zedeleyecek ölçüde ağır mı, meşru amaca ve orantıya uygun mu?
3. **Bağımsız ve tarafsız mahkeme.** Kuruluş, atama ve görünürdeki tarafsızlık ölçütleri (m.138-140 yargı bağımsızlığı) sağlanmış mı?
4. **Usuli güvenceler.** Silahların eşitliği, çelişmeli yargılama, gerekçeli karar hakkı, makul sürede yargılanma ve delillere erişim ayrı ayrı denetlenir.
5. **Ceza güvenceleri (m.38).** Suç ve cezada kanunilik, aleyhe geçmişe yürümezlik, masumiyet karinesi, kendini suçlamama; ceza yargılamasında hukuka aykırı delil yasağı (m.38/6).
6. **Bütünsel adillik.** Tek bir eksiklik değil, yargılamanın bütünü adil olup olmadığı değerlendirilir.
İspat: ihlali başvurucu somutlaştırır; usule uygunluğu kamu makamı temellendirir. AYM bireysel başvuru ve AİHM m.6 içtihadına ilke düzeyinde atıf yapın; künyeyi `[DOĞRULANMADI]` işaretleyin (kararlarbilgibankasi.anayasa.gov.tr, hudoc.echr.coe.int).

## Çıktı modülleri
- İhlal alt başlıklarının (erişim, süre, gerekçe, eşitlik, karine) kontrol listesi.
- Her güvence için tespit + gerekçe.
- Bireysel başvuru dilekçesine taşınacak adil yargılanma gerekçesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

