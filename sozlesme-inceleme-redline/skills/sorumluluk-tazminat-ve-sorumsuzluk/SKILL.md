---
argument-hint: ''
description: Sorumluluk sınırlaması, tazminat tavanı, sorumsuzluk anlaşması ve dolaylı
  zarar dışlama gibi maddelerin geçerliliğini ve dengesini incelemek gerektiğinde
  kullanılır.
name: sorumluluk-tazminat-ve-sorumsuzluk
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sorumluluk, Tazminat ve Sorumsuzluk Kaydı Denetimi

## Görev
Sorumluluk sınırlaması, tazminat tavanı, sorumsuzluk anlaşması, dolaylı zarar dışlama ve tazminat (indemnity) kayıtlarını geçerlilik ve denge yönünden denetlemek; geçersiz olanları ve müvekkili koruyacak lafzı belirlemek.

## Soğuk başlangıç (intake)
- Sözleşmede sorumluluğu sınırlayan/kaldıran kayıt var mı; kimin lehine?
- Edim uzmanlık/ruhsat gerektiren bir hizmet mi (TBK m.115/f.3)?
- Tazminat tavanı, dolaylı/netice zararı dışlama, kâr kaybı dışlama kayıtları var mı?
- Yardımcı kişi/alt yüklenici kullanılıyor mu (TBK m.116)?

## Denetim şeması
1. **Sorumsuzluk yasağı**: TBK m.115/f.1-2 — borçlunun ağır kusurundan (kast/ağır ihmal) sorumlu olmayacağına ilişkin anlaşma **kesin geçersiz**. m.115/f.3 — uzmanlık gerektiren, kanun/yetkili makam izniyle yürütülen faaliyette hafif kusur sorumsuzluğu da geçersiz.
2. **Yardımcı kişi**: TBK m.116/f.2 — yardımcı kişinin fiilinden doğan sorumluluğun önceden kaldırılması anlaşması geçerli olabilir; ancak izne tabi/uzmanlık faaliyetinde sınırlanamaz.
3. **Tazminat tavanı (cap)**: Cap kural olarak geçerli ama ağır kusuru kapsayamaz; "tüm hâller dahil" tavan kasıt/ağır kusura karşı işlemez. Sigorta limitiyle uyumu kontrol edilir.
4. **Dolaylı zarar/kâr kaybı dışlama**: TBK'da menfi/müspet zarar ayrımı (m.112 vd.); "kâr kaybı talep edilemez" kaydı müvekkil lehineyse korunur, aleyhineyse istisna (ağır kusur) eklenir.
5. **İndemnity (zarar tazmin taahhüdü)**: Kapsam, tetikleyici, tavan, süre ve "third-party claim" prosedürü netleştirilir; tek taraflı/sınırsız indemnity pazarlığa çekilir.
6. **İspat yükü**: Kusursuzluğunu borçlu ispatlar (TBK m.112). Sorumsuzluk kaydının geçersizliği hâkimce resen dikkate alınır.

## Çıktı modülleri
- Geçerli/geçersiz sorumsuzluk kayıtları tablosu (madde atfıyla).
- Dengeli tavan ve istisna lafzı önerisi (ağır kusur/kasıt hariç).
- İndemnity prosedürü ve sigorta uyumu notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

