---
argument-hint: ''
description: İdari işlem veya eylemden doğan zararın tazmini, eski hâle iade veya
  idarenin kusurlu/kusursuz sorumluluğunun tartışıldığı durumlarda kullanılır; kamulaştırmasız
  el atma, hizmet kusuru, sosyal risk gi
name: tam-yargi-davasi-tazminat
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tam Yargı Davası ve İdarenin Sorumluluğu

## Görev
İdari işlem veya eylemden doğan kişisel zararın tazminini, idarenin sorumluluk türünü (kusurlu/kusursuz), illiyet bağını ve zarar kalemlerini doğru kurgulayarak talep etmek.

## Soğuk başlangıç (intake)
- Zarar bir idari işlemden mi yoksa fiili bir eylemden mi doğdu?
- Eylem tarihinden bu yana ne kadar süre geçti (m.13 süreleri)?
- Zarar kalemleri neler: maddi (fiili zarar, yoksun kalınan kâr), manevi?
- İdarenin hizmeti kötü/geç/hiç işletilmesi söz konusu mu?

## Denetim şeması
1. **Ön başvuru şartı** (İYUK m.13): İdari eylemlerden doğan zararlarda dava açmadan önce eylemi öğrenme tarihinden itibaren **1 yıl** ve her hâlde eylem tarihinden itibaren **5 yıl** içinde ilgili idareye başvuru zorunludur. İdari işlemden doğan tam yargı davasında ise m.7/m.12 süreleri uygulanır.
2. **Sorumluluk türü**:
   - **Hizmet kusuru** (kusurlu sorumluluk): Hizmetin kötü, geç veya hiç işlememesi. Kusur idareye izafe edilir; kişiselleştirme aranmaz.
   - **Kusursuz sorumluluk**: Tehlike (riskli faaliyet) ilkesi ve fedakârlığın denkleştirilmesi (kamu külfetleri karşısında eşitlik) ilkeleri. Terör/sosyal risk zararlarında sosyal risk ilkesi.
3. **İlliyet bağı**: İdari faaliyet ile zarar arasında uygun nedensellik aranır. Mücbir sebep, beklenmeyen hâl, zarar görenin/üçüncü kişinin ağır kusuru illiyeti kesebilir veya tazminatta indirim sebebi olabilir.
4. **Zararın ispatı ve hesabı**: Zarar gerçek, kesin ve idari faaliyetle illiyetli olmalı. Maddi tazminatta fiili zarar ve yoksun kalınan kazanç; bedensel zararda işgücü kaybı, destekten yoksun kalma; manevi tazminatta takdiri ölçütler. İspat yükü kural olarak zarar görende; resen araştırma ilkesi geçerlidir (İYUK m.20).
5. **Ara sonuç**: Faiz başlangıcı (başvuru/dava tarihi) ve faiz türü ayrıca belirlenir; ıslah ile talep artırımı mümkündür (İYUK m.16/4).

## Çıktı modülleri
- Sorumluluk türü ve illiyet analizi notu
- Zarar kalemleri tablosu (maddi/manevi, dayanak)
- Ön başvuru ve dava süresi takvimi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

