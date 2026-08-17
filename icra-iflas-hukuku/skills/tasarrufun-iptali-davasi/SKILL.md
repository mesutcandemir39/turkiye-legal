---
argument-hint: ''
description: Borçlunun alacaklılardan mal kaçırmak için yaptığı (bağış, eşler arası
  devir, düşük bedelli satış gibi) tasarrufları iptal ettirmek gerektiğinde; aciz
  vesikası şartı, iptale tabi tasarruf türleri ve ü
name: tasarrufun-iptali-davasi
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tasarrufun İptali (İptal Davaları)

## Görev
Borçlunun alacaklıyı zarara uğratan tasarruflarını (m.277-284) iptal ettirerek haczi/satışı o mal üzerinde mümkün kılmak; iptal sebeplerini ve üçüncü kişinin iyiniyet durumunu denetlemek.

## Soğuk başlangıç (intake)
- Alacak için kesin/geçici aciz vesikası var mı (m.277, m.105)?
- İptali istenen tasarruf ne (bağış, satış, ipotek, ödeme)?
- Tasarruf borcun doğumundan sonra/şüphe döneminde mi yapıldı?
- Üçüncü kişi borçlunun yakını mı; iyiniyetli sayılabilir mi?

## Denetim şeması
1. **Dava şartı — aciz hali (m.277)**: İptal davası açabilmek için alacaklının elinde (geçici/kesin) aciz vesikası veya iflas bulunmalıdır. Bu, davanın ön şartıdır.
2. **İvazsız tasarruflar (m.278)**: Bağışlamalar ve bağışlama benzeri tasarruflar (ör. mutat dışı hediyeler, eşe/yakına düşük bedelli devirler) iflas/haciz tarihinden geriye doğru belirli süre içinde iptale tabidir.
3. **Acizden doğan iptal (m.279)**: Borçlunun mevcut borçları için olağandışı ödeme, teminat verme veya muaccel olmayan borcu ödeme gibi tasarrufları, alacaklıların durumunu bilen lehtara karşı iptal edilebilir.
4. **Zarar verme kastı (m.280)**: Borçlunun mallarını kaçırma kastıyla yaptığı, üçüncü kişinin bu kastı bildiği/bilmesi gerektiği tasarruflar iptale tabidir; yakınlar bakımından bilme karinesi vardır.
5. **İspat yükü ve sonuç (m.283)**: Alacaklı iptal sebebini ispatlar; dava kabul edilirse alacaklı o mal üzerinde haciz/satış isteyebilir, mülkiyet üçüncü kişide kalmaya devam eder. Zamanaşımı m.284 (5 yıl) denetlenir.
6. **Ara sonuç**: İptale en uygun sebep, davalı çevresi ve tahsil etkisi belirlenir.

## Çıktı modülleri
- Aciz vesikası ve şüphe dönemi kontrolü.
- İptal sebebi seçim notu (m.278/279/280).
- Dava dilekçesi iskeleti ve zamanaşımı takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

