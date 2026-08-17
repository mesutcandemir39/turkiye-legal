---
argument-hint: ''
description: Radyo, televizyon ve isteğe bağlı yayın hizmetlerinde yayın ilkelerine
  aykırılık, RTÜK idari para cezaları ve bu kararlara karşı idari dava yolu söz konusu
  olduğunda kullanılır.
name: rtuk-yayin-denetimi
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# RTÜK Yayın Denetimi ve İdari Yaptırımlar

## Görev
6112 sayılı Kanun kapsamında yayın hizmeti ilkelerine aykırılığı değerlendirmek, RTÜK idari yaptırımlarının hukuka uygunluğunu denetlemek ve idari dava yolunu kurgulamak.

## Soğuk başlangıç (intake)
1. Yayın hangi mecrada (TV/radyo/isteğe bağlı/internet yayını) çıktı?
2. İddia edilen ihlal hangi yayın ilkesine ilişkin (m.8)?
3. RTÜK kararı tebliğ edildi mi, tebliğ tarihi ne?
4. Müvekkil medya hizmet sağlayıcı mı, şikâyetçi izleyici mi?

## Denetim şeması
1. **Yayın ilkeleri (m.8)**: İnsan onuru, özel hayat, çocukların korunması, tarafsızlık ve doğruluk gibi ilkeler denetlenir. Aykırılık tespiti somut yayın içeriğiyle altlanmalıdır.
2. **Yaptırım rejimi (m.32)**: İhlalin ağırlığına göre uyarı, idari para cezası, program durdurma ve lisans iptaline kadar giden kademeli yaptırımlar uygulanır. Orantılılık ve tekerrür değerlendirilir.
3. **Düzeltme ve cevap (m.18)**: İşitsel-görsel yayında kişilik hakkı ihlaline karşı cevap-düzeltme yolu işler.
4. **Yargı yolu**: RTÜK kararı bir idari işlemdir; 2577 sayılı İYUK uyarınca iptal davası idari yargıda açılır. Dava süresi tebliğden itibaren altmış gündür (İYUK m.7); yürütmenin durdurulması talep edilebilir (İYUK m.27).
5. **Ara sonuç**: İşlemin yetki-şekil-sebep-konu-maksat unsurlarından biri sakatsa iptal; orantısız yaptırımda hukuka aykırılık doğar.

## Çıktı modülleri
- Yayın ilkesi-ihlal altlama tablosu
- İdari yaptırıma karşı iptal dava dilekçesi iskeleti (İYUK)
- Yürütmenin durdurulması talebi gerekçesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

