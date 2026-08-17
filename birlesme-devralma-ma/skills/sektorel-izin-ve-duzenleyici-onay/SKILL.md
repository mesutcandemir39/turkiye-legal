---
argument-hint: ''
description: Düzenlenmiş sektörlerde (bankacılık, enerji, sigorta, telekom, sermaye
  piyasası) pay devrinin gerektirdiği ön izinleri, halka açık hedeflerde çağrı yükümlülüğünü
  ve KAP açıklamalarını belirlemek için
name: sektorel-izin-ve-duzenleyici-onay
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sektörel İzin ve Düzenleyici Onaylar

## Görev
Hedef şirketin faaliyet alanına göre devrin tabi olduğu düzenleyici ön izinleri ve halka açık hedeflerde sermaye piyasası yükümlülüklerini saptamak ve takvimlendirmek.

## Soğuk başlangıç (intake)
- Hedef düzenlenmiş bir sektörde mi (banka, enerji, sigorta, telekom)?
- Hedef halka açık ortaklık mı; eşik aşan pay devri var mı?
- Yabancı yatırımcı söz konusu mu (özel kısıtlı sektörler)?
- İşlem kamuya açıklanacak mı, ne zaman?

## Denetim şeması
1. **Bankacılık**: 5411 sayılı Kanun — bankada belirli eşikleri aşan pay devri **BDDK iznine** tabidir; izinsiz devir oy hakkını askıya alabilir.
2. **Enerji**: 6446 sayılı Kanun ve EPDK düzenlemeleri — lisans sahibi tüzel kişide kontrol/pay değişikliği EPDK onayına tabi olabilir.
3. **Sigorta ve diğer**: İlgili düzenleyicinin (Sigortacılık ve Özel Emeklilik Düzenleme ve Denetleme Kurumu vb.) pay devri onayı.
4. **Sermaye piyasası (halka açık hedef)**: 6362 sayılı SPK — yönetim kontrolünü sağlayan pay edinimi **zorunlu çağrıyı** (pay alım teklifi) tetikleyebilir; KAP'ta özel durum açıklaması ve içeriden öğrenenlerin ticareti yasağı (SPK m.106) gözetilir.
5. **Telekom**: BTK yetkilendirme rejimi kapsamında kontrol değişikliği bildirimi/onayı.
6. **Askı etkisi**: Ön izin alınmadan kapanış, oy hakkının kullanılamaması veya idari yaptırım doğurabilir → izin CP olarak kurgulanır.
7. **İspat/dayanak**: Düzenleyici izin yazısı kapanış belgesidir; güncel mevzuat metni teyit edilir `[DOĞRULANMADI]`.

## Çıktı modülleri
- Sektörel izin matrisi (düzenleyici, eşik, süre)
- Çağrı yükümlülüğü değerlendirme notu (halka açık hedef)
- KAP açıklama takvimi
- Düzenleyici başvuru dosyası kontrol listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

