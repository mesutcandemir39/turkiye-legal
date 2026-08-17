---
argument-hint: ''
description: Borçlu, alacaklı veya komiser perspektifinden konkordato stratejisini
  belirlemek, risk haritası çıkarmak ve taraflarla iletişim metinlerini hazırlamak
  gerektiğinde kullanılır.
name: risk-strateji-ve-iletisim
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


# Risk, Strateji ve Taraf İletişimi

## Görev
Tarafın konumuna göre strateji kurmak: borçlu için sürecin başarısını ve yöneticilerin sorumluluk riskini yönetmek; alacaklı için tahsil/itiraz stratejisi; komiser/alacaklılar kurulu için denetim stratejisi. Risk haritası ve iletişim metinleri üretmek.

## Soğuk başlangıç (intake)
- Müvekkilin konumu: borçlu, alacaklı, komiser/kurul üyesi mi?
- Hedef: sürecin başarısı, alacağın korunması yoksa süreçten çıkış mı?
- Yöneticilerin kişisel sorumluluk riski (TTK m.553, vergi/SGK) gündemde mi?
- Karşı tarafla müzakere/yazışma ihtiyacı var mı?

## Denetim şeması
1. **Konum analizi.** Borçlu tarafında: konkordatonun reddi halinde iflas riski (m.308/son), yönetici sorumluluğu (TTK m.553), kamu borçlarından (vergi/SGK) şahsi sorumluluk (VUK m.10, 6183 s.K. mük. m.35) değerlendirilir.
2. **Alacaklı stratejisi.** Alacağı kaydettirme, çekişmeli alacak iddiası, çoğunluk hesabındaki ağırlık, rehin/imtiyaz konumunu güçlendirme; tasdike/projeye itiraz (m.304) hakkı denetlenir.
3. **Risk haritası.** Olasılık ve etki ekseninde: tasdik edilmeme, mühletin kaldırılması (m.292), iptal/fesih (m.308/e), kamu borcu yaptırımları, sözleşmesel temerrüt etkileri sıralanır. İspat zafiyetleri işaretlenir.
4. **İletişim metinleri.** Müvekkile sade dilde durum/seçenek notu; karşı tarafa müzakere veya itiraz yazısı; komisere/mahkemeye sunum dili. Gizlilik ve avukatlık sır saklama (Av.K. m.36) gözetilir.
5. **Ara sonuç.** Önerilen strateji (sürdür/itiraz et/çık), gerekçesi ve sonraki somut adımlar belirlenir.

## Çıktı modülleri
- Konuma özgü strateji notu.
- Risk haritası (olasılık-etki matrisi).
- Müvekkil bilgilendirme metni (sade dil).
- Karşı tarafa/komisere yazı taslağı (yer tutuculu).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

