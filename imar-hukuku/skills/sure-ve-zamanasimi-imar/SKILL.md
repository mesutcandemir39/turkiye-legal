---
argument-hint: ''
description: İmar işlemlerine karşı dava açma süresi, askı-ilan ve itiraz sürelerinin
  hesabı ya da bir sürenin kaçırılıp kaçırılmadığı sorulduğunda; İYUK süreleri, üst
  makama başvuru ve sürenin başlangıcı tartışıl
name: sure-ve-zamanasimi-imar
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İmar Uyuşmazlıklarında Süre ve Hak Düşürücü Süreler

## Görev
İmar işlemine karşı dava ve başvuru sürelerini doğru hesaplamak; sürenin başlangıcını, durmasını ve kaçırma riskini ortaya koymak.

## Soğuk başlangıç (intake)
- İşlem türü ne (plan, ruhsat, yıkım, para cezası, parselasyon)?
- İşlem ne zaman tebliğ edildi/ilan edildi/öğrenildi?
- Askı ilanı veya üst makama başvuru yapıldı mı?
- Bugünün tarihi itibarıyla kalan süre nedir?

## Denetim şeması
1. **Genel dava süresi (İYUK m.7)**: İdari işlemlere karşı, yazılı bildirim/tebliğ tarihinden itibaren **60 gün** (Danıştay ve idare/vergi mahkemeleri için genel süre). Sürenin başlangıcı tebliğ, ilan veya muttali olma anına göre tespit edilir.
2. **Planlarda askı-itiraz**: Plan **1 ay askıda** kalır; askı süresi sonunda dava süresi başlar. Askı içinde idareye itiraz edilirse, itirazın reddi (açık/zımni) yeni 60 günlük süre açar (İYUK m.11 ile bağlantılı değerlendirme).
3. **Üst makama başvuru (İYUK m.11)**: Dava süresi içinde işlemin kaldırılması/değiştirilmesi için üst makama başvurulabilir; başvuru işlemekte olan süreyi durdurur, cevap (veya 30/60 günlük zımni ret) ile kalan süre işler. İmar para cezası ve bazı işlemlerde bu yol kullanılır.
4. **İşlem türüne özgü farklar**: Yıkım ve mühürlemede sürenin tebliğden işlemesi; parselasyonda ilan; kamulaştırma/acele kamulaştırmada 2942'deki özel süreler; el atma bedelinde zamanaşımı ayrı kurulur. Her işlem için doğru başlangıç saptanır.
5. **İspat**: Tebligat parçası, askı tutanağı, ilan metni, başvuru ve cevap yazıları süreyi ispatlayan belgelerdir; sürenin başlangıcı çekişmeliyse "öğrenme" anı tartışılır (ispat yükü iddia edene).
6. **Ara sonuç**: Net bir süre takvimi (başlangıç-durma-bitiş) çıkarılır; süre dolmuşsa istisnai yollar (zımni ret, yeni işlem, mücbir sebep) değerlendirilir. Süre kritikse ivedi dava + YD önerilir.

## Çıktı modülleri
- İşlem türüne göre süre tablosu (başlangıç-bitiş-kalan gün).
- Askı/itiraz/üst makam başvuru akış şeması.
- Süre durması/yenilenmesi notu.
- Kaçırılan süre için istisna değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

