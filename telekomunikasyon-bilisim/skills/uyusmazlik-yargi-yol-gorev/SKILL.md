---
argument-hint: ''
description: Bir telekom veya internet uyuşmazlığında idari yargı mı, sulh ceza hâkimliği
  mi, adli/tüketici yargısı mı yoksa BTK başvurusu mu gerektiği, görevli merci ve
  süre belirsiz olduğunda kullanılır.
name: uyusmazlik-yargi-yol-gorev
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
  - ad: Telekomunikasyon Kanunu
    numara: '5809'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Telekom-Bilişim Uyuşmazlıklarında Yargı Yolu ve Görev-Yetki

## Görev
Uyuşmazlığı doğru yola (idari yargı, sulh ceza hâkimliği, adli/tüketici yargısı, BTK idari başvuru) yönlendirmek; görevli/yetkili mercii, başvuru/dava süresini ve acil koruma ihtiyacını net biçimde tespit etmek.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı: BTK işlemi mi, 5651 içerik tedbiri mi, abonelik/sözleşme mi, veri/gizlilik mi?
2. Müvekkilin sıfatı ve karşı taraf kim (işletmeci, BTK, içerik sahibi, abone)?
3. Tebliğ/öğrenme tarihi nedir; süre işliyor mu?
4. Acil koruma (yürütmenin durdurulması/ihtiyati tedbir/erişim kararı) ihtiyacı var mı?

## Denetim şeması
1. **Yol ayrımı**: BTK düzenleyici/yaptırım işlemi → idari yargı (İYUK). 5651 m.8/8A/9/9A erişim engelleme-içerik çıkarma → sulh ceza hâkimliği (CMK m.267 itiraz). Abonelik/hizmet özel hukuk → adli yargı; gerçek kişi tüketici ise 6502 tüketici hakem heyeti/mahkemesi. Veri ihlali → KVKK Kurulu ve sonrasında idari yargı. Ara sonuç: hangi yol.
2. **İdari yargı**: İYUK m.2 iptal/tam yargı; m.7 süre (kural 60 gün, özel kanun süresi varsa o); m.27 yürütmenin durdurulması (telafisi güç zarar + açık hukuka aykırılık). Görevli yer kural olarak idare mahkemesi.
3. **Sulh ceza hâkimliği**: 5651 erişim engelleme/içerik çıkarma kararı ve itirazı; karar ve itiraz süreleri kısa olduğundan süre disiplini kritiktir.
4. **Adli/tüketici yargı**: Tüketici işleminde parasal sınıra göre hakem heyeti/tüketici mahkemesi; ticari nitelikte asliye ticaret/asliye hukuk; ihtiyati tedbir HMK m.389 vd.
5. **Süre disiplini**: İdari, ceza usulü ve özel hukuk sürelerinin ayrı işlediği; hak düşürücü süre/zamanaşımı karışıklığı en sık hatadır. Süre takvimi sabitlenmeden dilekçe yazılmaz.

## Çıktı modülleri
- Yol ve görevli/yetkili merci tespiti.
- Süre takvimi ve YD/itiraz/ihtiyati tedbir ihtiyaç notu.
- Yanlış mercie başvuru riski uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

