---
argument-hint: ''
description: Çevresel uyuşmazlıkta idari yargı ile adli yargı arasındaki yol ayrımını,
  görevli ve yetkili mahkemeyi, dava türünü (iptal, tam yargı, tazminat) ve menfaat/dava
  ehliyetini belirlemek gerektiğinde; yan
name: usul-gorev-yetki
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yargı Yolu, Görev ve Yetki

## Görev
Çevresel uyuşmazlığı doğru yargı koluna ve mahkemeye yönlendirmek; dava türünü, menfaat/ehliyet şartını ve yetkili yeri belirleyerek usul kaynaklı ret riskini ortadan kaldırmak.

## Soğuk başlangıç (intake)
1. Uyuşmazlığın kaynağı idari işlem mi (ÇED/izin/yaptırım), yoksa kirleten ile zarar gören arasındaki özel ilişki mi?
2. Talep iptal mi, tam yargı (idare aleyhine tazminat) mı, özel hukuk tazminatı/el atma mı?
3. Davacının menfaat/dava ehliyeti var mı (yöre halkı, dernek, komşu)?
4. İdari işlemde tebliğ/ilan tarihi ve süre durumu nedir?

## Denetim şeması
1. **Yol ayrımı**: İdari işlem ve idarenin sorumluluğu → idari yargı (2577 sayılı İYUK). Kirleten ile zarar gören arasındaki tazminat/el atma → adli yargı (asliye hukuk). İdari para cezasında görev yolu, dayanak kanuna göre idare mahkemesi veya 5326 m.27 uyarınca sulh ceza hâkimliği olabilir; mutlaka madde düzeyinde teyit et.
2. **Dava türü**: İdari işlemin hukuka aykırılığı → iptal davası (İYUK m.2/1-a). İdarenin kusurlu/kusursuz eylem ve işlemlerinden doğan zarar → tam yargı davası (İYUK m.2/1-b).
3. **Dava şartları**: İdari yargıda menfaat (sübjektif ehliyet) aranır; çevresel davalarda yöre halkı ve çevre derneklerinin menfaat bağı genişçe yorumlanır — bu noktada ilkesel içtihat için karararama.danistay.gov.tr taranır, künye [DOĞRULANMADI] işaretlenir.
4. **Süre ve yetki**: İptal/tam yargıda kural süre 60 gün (İYUK m.7); yetkili idare mahkemesi işlemi yapan idarenin/uyuşmazlık konusu taşınmazın yeridir (İYUK m.34-36). Adli yargıda yetki haksız fiilin işlendiği/zararın doğduğu yer (HMK) kuralına göre belirlenir.
5. **Ara sonuç**: Yol, mahkeme, dava türü, ehliyet ve süre tek tabloda sabitlenir; tereddütte idari merci tecavüzü ve görevsizlik riski not edilir.

## Çıktı modülleri
- Yargı yolu ve görev/yetki tablosu
- Dava türü ve talep eşleştirmesi
- Menfaat/ehliyet değerlendirmesi
- Süre ve yetkili yer notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

