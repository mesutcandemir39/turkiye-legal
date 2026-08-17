---
argument-hint: ''
description: Toplu is uyusmazliklarinda ispat yukunu ve delil araclarini (uyelik kayitlari,
  iskolu istatistikleri, tutanaklar, tanik) planlar; sendikal neden, baraj/coklugu
  veya grev usulunun ispati gerektiginde k
name: ispat-ve-delil-toplu-is
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat ve Delil Stratejisi

## Görev
Toplu iş uyuşmazlığının türüne göre ispat yükünü doğru dağıtmak ve delil mimarisini kurmak. Sendikal neden, baraj/çoğunluk ve grev usulü farklı delil setleri ister.

## Soğuk başlangıç (intake)
- İspatlanacak ana vakıa nedir (sendikal neden / çoğunluk / grev usulü / TİS ihlali)?
- Elde hangi belgeler var (üyelik kaydı, bordro, tutanak, yazışma)?
- Tanık var mı; resmî kayıt erişimi mümkün mü?
- Karşı tarafın elindeki belgeler neler?

## Denetim şeması
1. **Sendikal neden ispatı:** 6356 m.25/7-8 — işçi, sendikal nedeni kuvvetle muhtemel kılan olguları (üyelik/çekilme tarihi, fesihle zaman yakınlığı, eşit durumdaki üye olmayanların korunması) gösterir; ardından geçerli/haklı neden ispatı işverene geçer. Delil: e-Devlet üyelik kaydı, fesih yazısı, karşılaştırmalı işten çıkarma listesi, tanık.
2. **Baraj/çoğunluk ispatı:** Yetki uyuşmazlığında Bakanlık işkolu istatistik tebliğleri, e-Devlet üyelik kayıtları, sendika ve işyeri işçi listeleri esastır (6356 m.41-43). Sayısal tespit belgeye dayanır; tanıkla çoğunluk ispatı kural olarak yetersizdir.
3. **Grev usulü ispatı:** Tutanak tarihleri, çağrı/bildirim yazıları, grev oylaması tutanağı (m.61), erteleme kararı; kanuni/kanun dışı grev ayrımı tarih ve belge ile kurulur.
4. **TİS ihlali ispatı:** Yürürlükteki TİS metni, ödeme/bordro kayıtları, işveren uygulamaları; normatif hükmün ihlali belge üzerinden gösterilir.
5. **Ara sonuç:** Her vakıa için ispat yükü sahibi ve asgari delil seti belirlenir; eksik deliller için celp/müzekkere planı yapılır (Bakanlık, SGK, banka kayıtları).

İspat yükü kuralı her zaman önce iddiacıda, kanunun yer değiştirdiği hallerde (m.25) işverende.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa – yük sahibi – delil).
- Delil toplama ve celp planı.
- Eksik/çelişki listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

