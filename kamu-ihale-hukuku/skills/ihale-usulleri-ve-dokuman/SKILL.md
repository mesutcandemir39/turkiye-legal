---
argument-hint: ''
description: Açık/belli istekliler/pazarlık/doğrudan temin usulünün doğru seçilip
  seçilmediğini ve idari şartname, teknik şartname, sözleşme tasarısı ile zeyilnamelerin
  hukuka aykırılığını incelemek gerektiğinde k
name: ihale-usulleri-ve-dokuman
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhale Usulleri ve İhale Dokümanı Denetimi

## Görev
Seçilen ihale usulünün kanuna uygunluğunu ve ihale dokümanının (idari/teknik şartname, sözleşme tasarısı, zeyilname) rekabeti ve eşit muameleyi zedeleyip zedelemediğini denetlemek.

## Soğuk başlangıç (intake)
1. Hangi usul uygulanmış; gerekçesi ihale onay belgesinde nasıl açıklanmış?
2. Teknik şartnamede belirli marka/model/menşe işaret ediliyor mu (m.12)?
3. Yeterlik kriterleri işin niteliğiyle orantılı mı yoksa rekabeti daraltıyor mu?
4. Zeyilname ile esaslı değişiklik yapılıp süre uzatımı verilmiş mi (m.29)?

## Denetim şeması
1. **Usul seçimi:** Açık ihale ve belli istekliler arasında ihale asıldır (m.18-20). Pazarlık (m.21) ve doğrudan temin (m.22) ancak kanunda sayılan hallerle sınırlıdır; gerekçe denetlenir. Doğrudan temin bir ihale usulü değildir, m.5 ilanı/teminat şartı aranmaz ama keyfî kullanım hukuka aykırıdır.
2. **Teknik şartname (m.12):** Rekabeti engelleyecek şekilde belirli marka, patent, menşe, kaynak gösterilemez; zorunluysa "veya dengi" ibaresi aranır. Ölçülebilir, objektif kriter şartı.
3. **İdari şartname/yeterlik:** Yeterlik kriterleri (m.10) işin niteliği ve büyüklüğüyle orantılı olmalı; aşırı/gereksiz kriter rekabet ihlali sayılır.
4. **Zeyilname (m.29):** Dokümanda esaslı değişiklik zeyilname ile ve son teklif gününden makul süre önce yapılır; gerekirse teklif süresi uzatılır. Süre verilmemesi iptal sebebidir.
5. **Ara sonuç:** Dokümana yönelik aykırılık varsa süresi içinde (ihale tarihinden 3 iş günü öncesine kadar doküman içeriğine itiraz) şikâyet yoluna gidilir; süre kaçırılmışsa esas iddia konsorbe olur.

İspat yükü: Doküman aykırılığını iddia eden istekli, somut maddeyi ve rekabete etkisini gösterir; idare orantılılık gerekçesini ortaya koyar.

## Çıktı modülleri
- Usul seçim gerekçesi değerlendirme notu.
- Şartname madde-bazlı aykırılık tablosu (madde / aykırılık / dayanak / öneri).
- Zeyilname/süre uzatımı kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

