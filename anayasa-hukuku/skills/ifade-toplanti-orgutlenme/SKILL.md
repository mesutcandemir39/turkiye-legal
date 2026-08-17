---
argument-hint: ''
description: İfade özgürlüğü, basın, toplantı-gösteri ve dernek-sendika gibi iletişim
  ve örgütlenme özgürlüklerine yönelik bir müdahalenin anayasaya uygunluğunu değerlendirmek;
  bu çekirdek demokratik haklara ilişk
name: ifade-toplanti-orgutlenme
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


# İfade, Toplantı ve Örgütlenme Özgürlükleri

## Görev
İfade (m.25-26), basın (m.28), toplantı ve gösteri yürüyüşü (m.34) ile dernek/sendika kurma (m.33, m.51) özgürlüklerine yönelik müdahaleleri anayasal ve AİHS standartlarıyla denetlemek; demokratik toplumda bu hakların ayrıcalıklı korumasını gözetmek.

## Soğuk başlangıç (intake)
1. Müdahale hangi özgürlüğe yönelik — ifade/basın, toplantı, yoksa örgütlenme mi?
2. Tasarruf türü ne: ceza yaptırımı, idari yasak/dağıtma, erişim engeli, fesih kararı?
3. İçerik siyasi tartışma, gazetecilik, sanatsal ifade gibi yüksek korumalı bir alanda mı?
4. Şiddete çağrı veya nefret söylemi unsuru ileri sürülüyor mu?

## Denetim şeması
1. **Hakkın belirlenmesi.** İlgili maddeyi (m.26 ifade, m.28 basın, m.34 toplantı, m.33/51 örgütlenme) ve AİHS karşılığını (m.10, m.11) m.90/son üzerinden köprüleyin.
2. **Müdahale tespiti.** Yaptırım, önleme, dağıtma, kapatma/fesih veya caydırıcı (chilling) etki müdahale sayılır.
3. **m.13 + özel sınırlama sebepleri.** İfadede m.26/2 sebepleri, toplantıda m.34, örgütlenmede ilgili maddelerin özel sebepleri. Kanunilik → meşru amaç → demokratik gereklilik → ölçülülük sırasıyla işletilir.
4. **Yüksek koruma kademesi.** Siyasi ifade, kamu yararını ilgilendiren gazetecilik ve seçilmişlerin ifadesi geniş korunur; bu alanlarda gereklilik eşiği yükselir, müdahalenin gerekçesi ağırlaşır.
5. **Şiddet/nefret sınırı.** Şiddete açık çağrı, nefret söylemi ve başkalarının haklarına somut tehdit korumadan çıkabilir; ancak bu istisna dar yorumlanır ve somut delil ister. Ara sonuç: salt rahatsız edici/şok edici içerik sınırlama sebebi değildir.
6. **Önleyici tedbir denetimi.** Toplantının önceden yasaklanması veya yayının/erişimin engellenmesi en ağır müdahale türüdür; kategorik yasaklar ölçülülüğü kural olarak aşar.
AYM ve AİHM (ör. ifade özgürlüğü) içtihatlarına ilke düzeyinde atıf yapın; künyeyi `[DOĞRULANMADI]` işaretleyin (hudoc.echr.coe.int, kararlarbilgibankasi.anayasa.gov.tr).

## Çıktı modülleri
- Müdahale tipi ve uygulanan koruma kademesinin tespiti.
- m.13 testinin bu özgürlüğe özgü uygulanmış hali.
- Bireysel başvuru/iptal gerekçesi için ifade-toplantı odaklı paragraflar.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

