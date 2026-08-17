---
argument-hint: ''
description: Kuruluşun veri ihlali müdahale planının varlığı ve yeterliliği denetlenirken,
  72 saatlik Kurul bildirim ve ilgili kişi bilgilendirme süreçleri test edilirken
  kullanılır.
name: veri-ihlali-mudahale-hazirligi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Veri İhlali Müdahale Hazırlığı Denetimi

## Görev
KVKK m.12/5 kapsamında kuruluşun veri ihlaline hazırlığını denetlemek: müdahale planı, ekip ve roller, 72 saatlik Kurul bildirim akışı ve ilgili kişi bilgilendirme mekanizması mevcut ve işler mi? Bu beceri olay anına değil, olaya hazırlığa odaklanır.

## Soğuk başlangıç (intake)
1. Yazılı bir veri ihlali müdahale planı var mı; ekip ve roller (kim karar verir, kim bildirir) tanımlı mı?
2. İhlali tespit eden çalışanın bildirim yapacağı iç kanal belli mi?
3. Daha önce yaşanan ihlal var mı; nasıl yönetildi, kayıt tutuldu mu?
4. 72 saatlik süreyi takip edecek bir mekanizma/şablon hazır mı?

## Denetim şeması
1. **Plan varlığı (m.12)**: Yazılı müdahale planı, eskalasyon zinciri ve karar matrisi olmalı. Plan yoksa veya güncel değilse yüksek risk bulgusu.
2. **Tespit→bildirim akışı**: İhlalin öğrenildiği an süreyi başlatır. Kurul'a bildirim en kısa sürede ve en geç 72 saat içinde, Kurul'un belirlediği form üzerinden yapılır; 72 saat aşılırsa gecikme gerekçesi açıklanmalı. Bu akışın test edilebilir (tatbikatlı) olması beklenir.
3. **İlgili kişi bilgilendirme**: Etkilenen kişiler makul en kısa sürede bilgilendirilir; bilgilendirme metni şablonu hazır olmalı.
4. **Bildirim içeriği**: İhlalin niteliği, etkilenen veri kategorileri ve kişi sayısı, olası sonuçlar, alınan/önerilen tedbirler ve irtibat bilgisi. Eksik içerik ayrı yükümlülük ihlalidir.
5. **Kanıt zinciri**: Loglar ve müdahale kayıtlarının korunacağı düzen kurulmalı; bu kayıtlar hem yaptırım hem tazminat davasında belirleyicidir.
6. **Ara sonuç**: Hazırlıksızlık, ihlal anında 72 saatin aşılmasına ve m.18 ek yaptırımına yol açar.

İspat yükü: Bildirimin süresinde ve usulüne uygun yapıldığını/yapılacağını veri sorumlusu plan ve kayıtlarla ispatlar.

## Çıktı modülleri
- Veri ihlali müdahale planı uygunluk kontrol listesi.
- 72 saat takip cetveli ve Kurul bildirim formu taslağı ([doldurulacak]).
- İlgili kişi bilgilendirme metni şablonu ve eskalasyon karar matrisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

