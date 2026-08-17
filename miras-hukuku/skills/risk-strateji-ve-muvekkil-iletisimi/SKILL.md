---
argument-hint: ''
description: Miras dosyasında dava açmadan önce başarı şansı, maliyet, süre ve sulh
  seçeneklerini tartmak; aile içi uyuşmazlıkta strateji belirlemek ve müvekkile sade,
  gerçekçi bilgilendirme yapmak gerektiğinde ku
name: risk-strateji-ve-muvekkil-iletisimi
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk, Strateji ve Müvekkil İletişimi

## Görev
Miras uyuşmazlığında dava/sulh kararını, başarı olasılığını, maliyet-süre dengesini ve aile dinamiklerini değerlendirip müvekkile anlaşılır bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin önceliği: maksimum pay mı, hız mı, ilişkiyi korumak mı?
- Karşı tarafla anlaşma ihtimali var mı? (aynı aile içi mi?)
- Eldeki delillerin gücü ve zayıf noktalar neler?
- Süre baskısı var mı? (ret 3 ay, tenkis 1 yıl gibi)
- Terekenin değeri dava maliyetini (harç, bilirkişi, vekâlet) karşılıyor mu?

## Denetim şeması
1. **Talep-delil-süre üçlüsünü tart:** Her talebin hukuki dayanağı (örn. tenkis m.560, muvazaa TBK m.19), ispat yükü ve hak düşürücü süre durumu netleştirilir; süresi kaçan talep elenir.
2. **Başarı olasılığı:** Delil gücü, yerleşik içtihat eğilimi (karararama.yargitay.gov.tr — künyeler doğrulanarak), karşı savunma senaryoları. Terditli kurgu (önce muvazaa, sonra tenkis) riski dağıtır.
3. **Maliyet-fayda:** Nispi harç (taşınmazda dava değeri üzerinden), bilirkişi ve keşif gideri, yargılama süresi (yıllarla ölçülen). Beklenen net kazanç ile karşılaştırılır.
4. **Alternatif çözüm:** Miras paylaşımı uyuşmazlıkları arabuluculuğa elverişlidir (HUAK m.1/2 kapsamı); aile içi onarıcı bir sulh çoğu zaman uzun davadan üstündür. Paylaşma sözleşmesi (m.676) ile çözüm değerlendirilir.
5. **İletişim disiplini:** Müvekkile süre riskleri yazılı bildirilir; gerçekçi olmayan beklenti düzeltilir; karar müvekkilindir, hukukçu seçenekleri ve olasılıkları sunar. Çıkar çatışması (birden çok mirasçının temsili) taranır.
6. **Ara sonuç:** önerilen strateji, alternatif senaryolar, müvekkil onayına sunulacak karar noktaları.

## Çıktı modülleri
- Risk haritası (talep / olasılık / maliyet / süre)
- Strateji notu (dava / sulh / terditli kurgu)
- Müvekkile sade dilde bilgilendirme metni
- Sulh/paylaşma teklifi taslağı ve müzakere notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

