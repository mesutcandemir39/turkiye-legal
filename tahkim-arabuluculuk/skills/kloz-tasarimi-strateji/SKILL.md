---
argument-hint: ''
description: Bir sözleşmeye tahkim veya arabuluculuk klozu yerleştirirken forum, dil,
  yer, kurum ve çok kademeli uyuşmazlık çözüm zinciri kurmak; uyuşmazlık öncesi strateji
  belirlemek gerektiğinde kullanılır.
name: kloz-tasarimi-strateji
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kloz Tasarımı ve Forum Stratejisi

## Görev
Sözleşme müzakeresinde uyuşmazlık çözüm mimarisini kurmak: tahkim mi devlet yargısı mı,
çok kademeli (müzakere-arabuluculuk-tahkim) zincir mi; yer, dil, kurum ve uygulanacak
hukuk seçimini stratejik olarak belirlemek.

## Soğuk başlangıç (intake)
1. Sözleşme yerli mi sınır ötesi mi, taraflar ve ifa yeri nerede?
2. Uyuşmazlık değeri ve niteliği (gizlilik, teknik bilirkişi, hız ihtiyacı) nedir?
3. İcra/tenfiz nerede aranacak (karşı tarafın malvarlığı nerede)?
4. Çok kademeli çözüm (önce arabuluculuk, sonra tahkim) isteniyor mu?

## Denetim şeması
1. **Forum seçimi**: Yabancılık unsuru ve tenfiz ihtiyacı varsa tahkim (**New York
   Sözleşmesi** sayesinde tenfiz kolaylığı) tercih edilir; tamamen yerli ve düşük değerli
   uyuşmazlıkta devlet yargısı daha ekonomik olabilir. Elverişlilik **HMK m.408** süzgeci.
2. **Kloz unsurları**: Tahkim klozunda **tahkim yeri, dil, hakem sayısı, kurum kuralları**
   (ör. ISTAC, ICC, ITOTAM) ve esasa uygulanacak hukuk açıkça belirlenir; yazılılık
   (**HMK m.412**, **MTK m.4**) sağlanır. Eksik/çelişkili kloz patolojiktir.
3. **Çok kademeli (multi-tier) zincir**: Önce zorunlu müzakere/arabuluculuk, sonra tahkim
   öngörülebilir; her kademenin **süresi ve geçiş şartı** somut yazılmalı, aksi halde
   tahkime erişim tartışmaya açılır. Dava şartı arabuluculuk kapsamındaki uyuşmazlıklarda
   yasal zorunluluk ayrıca gözetilir.
4. **Tenfiz odaklı tasarım**: Hakem kararının icra edileceği ülkenin rejimi (kamu düzeni,
   elverişlilik) baştan değerlendirilir; karşı tarafın malvarlığının bulunduğu yer
   belirleyicidir.
5. **Ara sonuç**: Önerilen forum, kloz iskeleti ve strateji gerekçesi.

## Çıktı modülleri
- Forum karşılaştırma tablosu (tahkim/arabuluculuk/devlet yargısı; maliyet-hız-tenfiz).
- Tahkim ve/veya çok kademeli kloz taslağı ([doldurulacak] yer, dil, kurum, hukuk).
- Tenfiz/strateji risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

