---
argument-hint: ''
description: Bir kanun, kararname veya idari işlemin bir temel hakka müdahalesinin
  Anayasa m.13 ölçütlerine uygun olup olmadığını adım adım test etmek; kanunilik,
  meşru amaç, demokratik gereklilik ve ölçülülük ana
name: temel-hak-sinirlama-testi
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


# Temel Hak Sınırlama Testi (m.13)

## Görev
Bir devlet tasarrufunun temel hakka müdahalesini Anayasa m.13'ün beş ölçütüyle (kanunilik, sınırlama sebebine bağlılık, demokratik toplum düzeninin gerekleri, ölçülülük, hakkın özü) sistematik biçimde denetlemek ve sonucu gerekçeli bir değerlendirmeye bağlamak.

## Soğuk başlangıç (intake)
1. Hangi temel hak müdahaleye uğradı (ör. ifade m.26, mülkiyet m.35, toplantı m.34)?
2. Müdahale hangi tasarrufla yapıldı — kanun, CB kararnamesi, yönetmelik, idari işlem?
3. Müdahalenin dayandığı amaç/sebep (kamu düzeni, başkalarının hakları, milli güvenlik vb.) ne?
4. Daha hafif bir önlemle aynı amaca ulaşmak mümkün müydü?

## Denetim şeması
1. **Koruma alanı ve müdahale.** Önce hakkın kapsamını ve müdahalenin varlığını saptayın. Müdahale yoksa test sona erer.
2. **Kanunilik.** Müdahale erişilebilir, belirli ve öngörülebilir bir **kanunla** öngörülmüş mü? (m.13). Yönetmelikle hak sınırlaması kural olarak yetersizdir. Ara sonuç: kanuni dayanak var mı?
3. **Meşru amaç / sınırlama sebebine bağlılık.** İlgili hakkın kendi maddesindeki özel sınırlama sebebine dayanıyor mu? (ör. m.26/2'deki sebepler). Genel sınırlama yasağı: sebep dışına çıkılamaz.
4. **Demokratik toplum düzeninin gerekleri.** Müdahale zorlayıcı bir toplumsal ihtiyaca karşılık geliyor mu? AİHS m.8-11 ve m.90/son üzerinden AİHM ölçütleriyle besleyin.
5. **Ölçülülük.** Üç alt ilke: (a) elverişlilik — önlem amaca ulaştırıyor mu; (b) gereklilik — daha az sınırlayıcı bir araç var mı; (c) orantılılık — yarar/zarar dengesi. Ara sonuç: en az birinde elenirse müdahale ölçüsüzdür.
6. **Hakkın özü.** Sınırlama hakkı kullanılamaz hale getiriyor mu? Öze dokunma tek başına aykırılık sebebidir.
İspat: müdahalenin varlığını başvurucu, meşruiyetini ve gerekliliğini kamu makamı ortaya koyar. İlke düzeyinde AYM ölçülülük içtihadına atıf yapın ve künyeyi `[DOĞRULANMADI]` işaretleyin (kararlarbilgibankasi.anayasa.gov.tr).

## Çıktı modülleri
- Adım adım m.13 test tablosu (her ölçüt: karşılandı/karşılanmadı + gerekçe).
- Zayıf halka tespiti ve aykırılık/ihlal sonucu.
- Norm denetimi veya bireysel başvuru dilekçesine taşınacak gerekçe paragrafları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

