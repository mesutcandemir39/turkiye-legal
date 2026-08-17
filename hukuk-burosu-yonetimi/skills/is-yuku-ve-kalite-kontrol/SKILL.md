---
argument-hint: ''
description: Büroda dosyaların avukatlara dağıtımı, kapasite planlaması, iş yükü dengelemesi
  ve çıktı kalitesinin gözden geçirilmesi (peer review) süreçleri kurgulanırken kullanılır.
name: is-yuku-ve-kalite-kontrol
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İş Yükü Dağılımı ve Kalite Kontrol

## Görev
Dosya ve görevleri ekip içinde dengeli ve uzmanlığa uygun dağıtmak; kapasiteyi izlemek; çıktıların (dilekçe, sözleşme, mütalaa) büroyu terk etmeden önce kalite kontrolünden geçmesini sağlamak.

## Soğuk başlangıç (intake)
1. Ekipte kaç avukat/stajyer var, uzmanlık alanları ve mevcut yükleri ne?
2. Dağıtılacak iş(ler)in türü, aciliyeti ve karmaşıklık düzeyi nedir?
3. Yaklaşan kritik süreler ve duruşmalar hangi tarihlerde yoğunlaşıyor?
4. Kalite kontrol için mevcut bir gözden geçirme (review) akışı var mı?

## Denetim şeması
1. **Yetkinlik eşleştirmesi**: İş, uzmanlık ve deneyime göre atanır; karmaşık/yüksek riskli iş daha kıdemli avukata, çift kontrol gerektirenlere ikinci göz atanır (özen — TBK m.506).
2. **Kapasite ve süre dengesi**: Mevcut yük ve yaklaşan süreler birlikte değerlendirilir; süre çakışmaları görünür kılınır, darboğaz tarihleri için erken müdahale planlanır.
3. **Çıkar çatışması teyidi**: Atama öncesi ilgili avukatın o işte çatışması olmadığı doğrulanır (1136 m.38).
4. **Kalite kontrol katmanı**: Her büro-dışı çıktı için kontrol listesi — doğru taraf/mahkeme, talep sonucu vakıalarla uyumlu mu, süre içinde mi, madde atıfları teyit edildi mi, gizli/yanlış bilgi sızıyor mu.
5. **Sorumluluk izi**: Hazırlayan ve gözden geçiren ayrı kaydedilir; revizyon notları saklanır.
6. **Ara sonuç**: Uygun atama + kapasite teyidi + tamamlanmış kalite kontrolü ile iş "teslime hazır" sayılır.

## Çıktı modülleri
- İş yükü/atama tablosu (avukat, dosya, aciliyet, kapasite durumu).
- Yaklaşan süre/duruşma yoğunluk takvimi.
- Çıktı kalite kontrol listesi (dilekçe/sözleşme/mütalaa için).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

