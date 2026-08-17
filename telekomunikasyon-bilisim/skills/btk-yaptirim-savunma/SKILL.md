---
argument-hint: ''
description: BTK tarafından verilen idari para cezası, yetkilendirme iptali, faaliyet
  durdurma gibi yaptırımlara ve bant genişliği daraltma kararlarına karşı savunma
  ve iptal davası hazırlığı gerektiğinde kullanıl
name: btk-yaptirim-savunma
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


# BTK İdari Yaptırımları ve Savunma

## Görev
BTK kaynaklı idari yaptırımlara (para cezası, yetkilendirme iptali, faaliyet durdurma, sosyal ağ tedbirleri) karşı yazılı savunma, idari başvuru ve iptal davası stratejisini kurmak; usul ve esas sakatlıklarını tespit etmek.

## Soğuk başlangıç (intake)
1. Yaptırımın türü ve dayanağı (5809/5651 hangi madde, hangi yönetmelik ihlali)?
2. Savunma istem yazısı/tebligat tarihi ve verilen süre nedir?
3. İhlal iddiasının somut konusu ve BTK'nın delili nedir?
4. Daha önce ihtar/savunma alındı mı, tekerrür/kademeli yaptırım var mı?

## Denetim şeması
1. **Dayanak ve oran**: 5809 m.60-63 (elektronik haberleşme yaptırımları) veya 5651 ilgili hükümleri — yaptırım türü, para cezasının hesap usulü, üst sınır ve oransallık. Ara sonuç: uygulanan yaptırım türü/oranı dayanakla uyumlu mu.
2. **Usul denetimi**: Savunma hakkının tanınması, makul süre, gerekçe ve bilgi/belgeye erişim; idari işlemde yetki ve şekil unsuru. Usul sakatlığı tek başına iptal sebebi olabilir.
3. **Esas denetimi**: İhlalin maddi olarak gerçekleşip gerçekleşmediği; teknik/yükümlülük ihlali iddiası karşı delil ve uzman raporuyla çürütülür. İhlali idare ispatlar; ancak müvekkil lehine vakıaları (uyum, mücbir sebep) belgeleyin.
4. **Ölçülülük ve eşit muamele**: Kademeli yaptırımda (özellikle sosyal ağ rejiminde reklam yasağı/bant daraltma) ölçülülük, benzer ihlallere uygulanan yaptırımlarla karşılaştırma ve ifade özgürlüğü etkisi.
5. **Dava yolu**: BTK yaptırımı idari işlem olduğundan İYUK m.7 (kural 60 gün) içinde iptal davası; m.27 yürütmenin durdurulması istemi tahsil/iptal/erişim kısıtı sonuçlarını dondurmak için kritik. Görevli yargı yeri idari yargıdır.

İlkesel içtihat için karararama.danistay.gov.tr (özellikle 13. Daire), temel hak boyutunda kararlarbilgibankasi.anayasa.gov.tr taranır; künye [DOĞRULANMADI] işaretlenir, esas/karar no uydurulmaz.

## Çıktı modülleri
- BTK savunma yazısı taslağı (usul + esas).
- İptal davası dilekçesi ve YD istemi iskeleti.
- Sakatlık ve karşı delil tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

