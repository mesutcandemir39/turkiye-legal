---
argument-hint: ''
description: İş davasında ispat yükünün dağılımı, bordro-puantaj değeri, tanık-yazılı
  delil dengesi ve ibranamenin geçerliliği tartışıldığında; hangi tarafın neyi ispatlayacağını
  ve belgelerin delil değerini sapta
name: ispat-delil-bordro-ibraname
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil, Bordro ve İbraname Denetimi

## Görev
İş uyuşmazlığında ispat yükünü doğru dağıtmak, bordro/puantaj/özlük dosyasının delil değerini belirlemek ve ibranamenin TBK m.420 geçerliliğini denetlemek.

## Soğuk başlangıç (intake)
1. İhtilaflı vakıalar neler (ücret miktarı, fazla çalışma, fesih sebebi, izin)?
2. İmzalı bordro, banka kaydı, puantaj/PDKS, özlük dosyası mevcut mu?
3. Tanık var mı; tanıklar dönem ve mesai düzenini biliyor mu?
4. İbraname imzalanmış mı; tarihi ve içeriği nedir?

## Denetim şeması
1. **İspat yükü temeli (HMK m.190; TMK m.6):** İddia eden ispatla yükümlüdür. İş hukukunda kayıt tutma işverende olduğundan kayıt ibraz edilmemesi işveren aleyhine değerlendirilebilir.
2. **Fesih sebebinin ispatı:** Geçerli/haklı feshi işveren ispatlar (m.20/2). İşçi savunmasının alınmaması ve yazılı-gerekçeli fesih yapılmaması işveren aleyhinedir.
3. **Bordro değeri:** İmzalı ve ihtirazi kayıtsız bordroda tahakkuk eden kalemler (fazla çalışma, tatil) kural olarak ödenmiş sayılır; aksini işçi ancak **yazılı delille** çürütebilir. Tahakkuk yoksa veya bordro imzasızsa o dönem işçi lehine tanıkla ispata açıktır.
4. **Fazla çalışma/tatil:** Kural olarak işçi ispatlar; yazılı delil yoksa tanıkla ispat mümkün. Uzun dönemli ve fiziken kesintisiz çalışma iddialarında hakkaniyet/takdiri indirim uygulanır.
5. **Ücret miktarı:** Çekişmeliyse meslek kuruluşu/sendika emsal ücret araştırması delil olur.
6. **İbraname (TBK m.420):** Geçerlilik için ibra (a) yazılı, (b) sözleşme sona erdikten en az **1 ay** sonra düzenlenmiş, (c) alacak türü ve miktarı açıkça belirtilmiş, (d) ödeme banka/eksiksiz yapılmış olmalı. Eksikse ibra geçersiz; miktar içeren ama tam ödeme içermeyen belge **makbuz** hükmündedir ve kısmi ödeme olarak değerlendirilir.

## Çıktı modülleri
- Vakıa bazında ispat yükü tablosu.
- Belge delil değeri değerlendirmesi (bordro/puantaj/özlük).
- İbraname geçerlilik denetimi sonucu.
- Delil tamamlama ve celp/keşif/bilirkişi talep listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

