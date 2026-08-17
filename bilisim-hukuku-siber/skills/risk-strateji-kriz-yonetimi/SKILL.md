---
argument-hint: ''
description: Bir siber olay veya bilişim hukuku ihtilafında ceza-idari-tazminat risklerini
  bütünsel tartmak, kurum/müvekkil için en iyi-en kötü senaryoyu ve eylem stratejisini
  belirlemek gerektiğinde kullanılır.
name: risk-strateji-kriz-yonetimi
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk, Strateji ve Kriz Yönetimi

## Görev
Çok katmanlı bir bilişim/siber olayda riskleri tartmak, senaryoları çıkarmak ve müvekkil/kurum için tutarlı bir hukuki strateji ile kriz yönetim planı kurmak.

## Soğuk başlangıç (intake)
1. Kurumun/müvekkilin pozisyonu ne? (mağdur, sorumlu, hem mağdur hem sorumlu?)
2. En kritik risk ne? (ceza, idari para cezası, tazminat, itibar, operasyon kesintisi?)
3. Karşı taraf/düzenleyici aktif mi? (savcılık, KVKK, müşteri talepleri?)
4. Zaman baskısı ve kaynak kısıtı ne düzeyde?

## Denetim şeması
1. **Risk envanteri.** Üç eksende risk çıkarılır: ceza (TCK m.243-245, m.135-140 maruziyeti), idari (KVKK m.18 para cezası, sektörel yaptırım), özel hukuk (TBK m.49/m.112 tazminat, toplu talep riski). Her risk olasılık ve etki ile derecelendirilir.
2. **Pozisyon analizi.** Kurum aynı anda mağdur (saldırıya uğrayan) ve potansiyel sorumlu (tedbirsizlik) olabilir; bu ikili konum stratejiyi belirler. Suç duyurusu seçeneği ile sorumluluk savunması çelişmemelidir.
3. **Senaryo çıkarma.** En iyi/orta/en kötü senaryolar; her birinde olasılık, mali etki, süre ve karşı hamle. Delil durumu ve ispat yükü dağılımı (KVKK'da tedbir ispatı kurumda; cezada iddia makamında) senaryoları belirler.
4. **Strateji tercihi.** Erken bildirim ve iş birliği (yaptırım hafifletici), uzlaşma/sulh, savunma hattı, eş zamanlı yargı yolları koordinasyonu; itibar/iletişim ile hukuki adımların uyumu. Ölçülülük: aşırı reaksiyon yeni risk doğurmamalı.
5. **Ara sonuç.** Önceliklendirilmiş aksiyon listesi, sorumlu kişiler ve karar noktaları net bir kriz planına bağlanır.

## Çıktı modülleri
- Risk matrisi (eksen, olasılık, etki, öncelik).
- Senaryo tablosu (en iyi/orta/en kötü + aksiyon).
- Kriz yönetim planı ve karar/iletişim notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

