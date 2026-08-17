---
argument-hint: ''
description: Dava öncesi ihtar çekmek, ihlali durdurma ve lisanslama çözümü için müzakere
  yürütmek ya da gelen ihtarnameye yanıt vermek gerektiğinde; tebligatlı ihtar ve
  uzlaşma stratejisini kurmak için kullanılır
name: ihtarname-uzlasma-iletisim
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtarname, Müzakere ve Karşı Taraf İletişimi

## Görev
İhlali durdurmaya yönelik ihtarname hazırlamak, sonradan lisanslama/uzlaşma müzakeresini yürütmek veya gelen ihtara hukuki ve stratejik yanıt üretmek.

## Soğuk başlangıç (intake)
- Hangi taraftayız (hak sahibi mi, ihlal iddia edilen mi)?
- Hedef ihlalin durması mı, geçmiş kullanım için bedel mi, lisanslama mı?
- Karşı tarafla ticari ilişki sürdürülecek mi?
- Süre/zamanaşımı veya delil kaybı baskısı var mı?

## Denetim şeması
1. Konum tespiti: Hak sahibi tarafında ihlalin hak ve kapsamı (m.20-25) sabitlenir; iddia edilen taraf ise savunma (izin, istisna m.30-40, eser niteliği yokluğu) önceden değerlendirilir.
2. İhtar amacı ve içeriği: İhtarname ihlalin durdurulmasını, nüshaların toplatılmasını ve makul süre talep eder; temerrüt ve faiz başlangıcı için tarih sabitlenir. Noter/KEP ile gönderim ispat değeri sağlar (TBK m.117 temerrüt; tebligat ispatı).
3. Aşırı talepten kaçınma: m.68 üç kat bedel caydırıcı bir koz olsa da müzakerede orantılı, somut emsale dayalı talep güveni artırır; mesnetsiz tehdit karşı tarafa koz verir.
4. Uzlaşma seçenekleri: İhlalin durması + geriye dönük lisans bedeli + ileriye dönük lisans; manevi hak ihlalinde ad belirtilmesi/düzeltme. Anlaşma metni mali hak boyutuyla m.52 yazılı şekle uygun düzenlenir.
5. Gelen ihtara yanıt: Süre tuzaklarından kaçın; ikrar doğuran ifadelerden sakın; eser/sahiplik ve izin/istisna savunmasını ölçülü biçimde bildir, gerekiyorsa ek süre/uzlaşma çağrısı yap.
6. Ara sonuç: Strateji (sert ihtar / müzakere / savunma), mesaj çerçevesi ve sonraki adım takvimi belirlenir.

İspat yükü: ihtar ve içeriğinin tebliği gönderene; izin/istisna savunması iddia edene aittir.

## Çıktı modülleri
- İhtarname taslağı (talep, süre, dayanak, temerrüt notu).
- Müzakere/uzlaşma strateji notu ve sulh metni iskeleti.
- Gelen ihtara yanıt taslağı ve risk uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

