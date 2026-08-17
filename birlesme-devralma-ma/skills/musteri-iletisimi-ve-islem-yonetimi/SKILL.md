---
argument-hint: ''
description: M&A işleminin yol haritasını müvekkile sade biçimde anlatmak, riskleri
  ve karar noktalarını özetlemek, term sheet aşamasından kapanışa süreç ve sorumluluk
  dağılımını yönetmek için kullanılır.
name: musteri-iletisimi-ve-islem-yonetimi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil İletişimi ve İşlem Yönetimi

## Görev
İşlemi müvekkilin anlayacağı dille çerçevelemek, kritik karar noktalarını ve riskleri özetlemek, term sheet'ten kapanışa süreci ve görev dağılımını yönetmek.

## Soğuk başlangıç (intake)
- Müvekkilin işlemdeki önceliği ne (hız, fiyat, risk minimizasyonu)?
- Müvekkil M&A deneyimi olan kurumsal bir aktör mü, ilk kez mi?
- Karşı tarafın danışmanları ve müzakere üslubu nasıl?
- İşlem gizliliği ve kamuya açıklama hassasiyeti var mı?

## Denetim şeması
1. **Term sheet / niyet mektubu**: Bağlayıcı (gizlilik, münhasırlık) ve bağlayıcı olmayan hükümlerin ayrımı net yapılır; yanlış anlaşılma TBK m.1 anlamında erken bağlanma riski yaratır.
2. **Gizlilik (NDA)**: Bilgi paylaşımı öncesi gizlilik sözleşmesi ve veri odası kuralları.
3. **Süreç planı**: Signing → CP → closing → post-closing aşamaları, her aşamada müvekkilden beklenen kararlar ve onaylar.
4. **Risk iletişimi**: DD kırmızı bayrakları, indemnity sınırları ve earn-out belirsizlikleri sade dille; karar müvekkile bırakılır, hukuki sonuç açıklanır.
5. **Çıkar çatışması ve gizlilik**: Avukatlık Kanunu (1136) ve meslek kuralları çerçevesinde çatışma taraması ve sır saklama.
6. **İspat/kayıt hijyeni**: Önemli kararlar yazılı teyitle (e-posta/karar notu) belgelenir.
7. **Ara sonuç**: Müvekkile karar matrisi (seçenek, sonuç, öneri) sunulur.

## Çıktı modülleri
- İşlem yol haritası (sade dilli, aşamalı)
- Karar noktaları ve risk özeti (yönetici özeti)
- Term sheet bağlayıcılık ayrım notu
- Görev/sorumluluk dağılım tablosu (responsibility matrix)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

