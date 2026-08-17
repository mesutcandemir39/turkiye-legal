---
argument-hint: ''
description: TİTCK tarafından verilen uyarı, faaliyet durdurma, ruhsat askı/iptal
  ve idari para cezası gibi işlemlere karşı iptal davası ve yürütmenin durdurulması
  stratejisini kurmak için kullanılır.
name: titck-idari-yaptirim-dava
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# TİTCK İdari Yaptırımlarına Karşı Dava

## Görev
TİTCK’nın birel veya düzenleyici işlemine karşı idari yargıda iptal davasını, yürütmenin durdurulması talebini ve gerekçe stratejisini kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: uyarı, faaliyet/tanıtım durdurma, sertifika askısı, ruhsat iptali, idari para cezası, düzenleyici tebliğ/kılavuz mu?
- İşlemin tebliğ tarihi; dava açma süresi durumu?
- İşlemin gerekçesi ve dayanak norm nedir?
- Telafisi güç/imkânsız zarar doğuran etki var mı (tesis kapanması, listeden çıkma)?

## Denetim şeması
1. **İşlem niteliği.** Birel işlem mi düzenleyici işlem mi? Düzenleyici işlemde normlar hiyerarşisi ve süre (İYUK m.7) ayrı değerlendirilir; düzenleyici işlemin uygulanması üzerine de dava açılabilir.
2. **Unsur denetimi.** Yetki (TİTCK’nın 663 sayılı KHK’dan gelen yetkisi), şekil (gerekçe, savunma alma), sebep (denetim bulgusu/bilimsel değerlendirme), konu, maksat. Ara sonuç: hangi unsur sakat?
3. **Süre ve usul.** İYUK m.7 (60 gün); idari para cezasında özel kanun/5326 kontrolü; üst makama başvuru (İYUK m.11) süreyi durdurur. İspat: idare sebep unsurunu somut belgeyle; davacı sakatlığı ortaya koyar.
4. **Yürütmenin durdurulması.** İYUK m.27: açıkça hukuka aykırılık + telafisi güç/imkânsız zarar birlikte gösterilir; ilacın hayati önemi veya işletmenin kapanma riski somutlaştırılır.
5. **Ölçülülük ve eşitlik.** Takdire dayalı yaptırımda elverişlilik-gereklilik-orantılılık ve benzer olaylarla eşit muamele denetlenir; emsal idari işlem/karar karararama.danistay.gov.tr üzerinden araştırılır [DOĞRULANMADI].

## Çıktı modülleri
- İşlem niteliği ve süre tespiti.
- İptal + yürütmeyi durdurma dilekçesi iskeleti [doldurulacak].
- Unsur bazında hukuka aykırılık ve ölçülülük argüman listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

