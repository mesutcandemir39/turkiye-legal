---
argument-hint: ''
description: Baro tarafından CMK kapsamında zorunlu müdafi/vekil görevlendirmesi,
  adli yardım bürosu atamaları, bu görevlerin reddi ve ücretlendirilmesi söz konusu
  olduğunda kullanılır.
name: cmk-adli-yardim-zorunlu-mudafi
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# CMK Müdafiliği, Adli Yardım ve Zorunlu Görevlendirmeler

## Görev
Baro üzerinden yapılan zorunlu müdafi/vekil ve adli yardım görevlendirmelerinin
yükümlülüklerini, reddi mümkün halleri ve ücret-rücu düzenini belirlemek.

## Soğuk başlangıç (intake)
1. Görevlendirme CMK zorunlu müdafilik mi, adli yardım vekilliği mi?
2. Görevi reddetmek için haklı/kanuni sebep var mı (çıkar çatışması, mazeret)?
3. Görev kapsamı hangi aşamayı içeriyor (soruşturma, kovuşturma, kanun yolu)?
4. Ücret CMK tarifesinden mi, adli yardımdan mı talep edilecek?

## Denetim şeması
1. **Görevin kaynağı.** Zorunlu müdafilik CMK m.150 (zorunlu hallerde müdafi tayini) ve
   m.156 (mağdur/vekil) ile baro tarafından atama yoluyla doğar; adli yardım Av. K. m.176-181
   kapsamında baro adli yardım bürosunca yürütülür. Atanan avukat görevi kabul ile yükümlüdür.
2. **Reddedilebilir haller.** Çıkar çatışması (Av. K. m.38), kabul edilemeyecek mazeret veya
   yasal engel halinde görev baroya iade/itiraz yoluyla bırakılabilir; keyfi ret disiplin
   suçudur. Ara sonuç: ret sebebi m.38/mazeret kalıbına uyuyor mu?
3. **Özen yükümü aynıdır.** Zorunlu/ücretsiz görevde de özen, sır ve sadakat yükümü serbest
   vekâletteki ile aynıdır (Av. K. m.34, m.36); savunmanın etkinliği esastır.
4. **Ücret ve giderler.** CMK görevlerinde ücret, ilgili CMK ücret tarifesinden Hazine/baro
   eliyle ödenir; adli yardımda ödeme Av. K. m.180 çerçevesinde yapılır. Davanın kazanılması
   halinde karşı taraftan tahsil ve rücu (Av. K. m.181) gözetilir.
5. **Sona erme.** Vekille temsil veya görevin kalkması halinde görevlendirme sona erer;
   dosya ve bilgi devri yapılır.

## Çıktı modülleri
- Görevin kabul/ret değerlendirmesi ve dayanağı.
- Aşama bazlı yükümlülük ve ücret özeti (CMK / adli yardım ayrımı).
- Görev iadesi/itiraz veya ücret talep dilekçesi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

