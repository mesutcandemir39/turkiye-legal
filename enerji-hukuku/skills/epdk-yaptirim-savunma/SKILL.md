---
argument-hint: ''
description: EPDK tarafından verilen idari para cezası, lisans iptali, faaliyet durdurma
  gibi yaptırımlara karşı savunma ve dava hazırlığı gerektiğinde; yaptırım soruşturması
  başladığında kullanılır.
name: epdk-yaptirim-savunma
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# EPDK İdari Yaptırımları ve Savunma

## Görev
EPDK kaynaklı idari yaptırımlara (para cezası, lisans iptali, faaliyet durdurma) karşı yazılı savunma, idari başvuru ve iptal davası stratejisini kurmak; usul ve esas sakatlıklarını tespit etmek.

## Soğuk başlangıç (intake)
1. Yaptırımın türü ve dayanağı (hangi madde/yönetmelik ihlali)?
2. Savunma istem yazısı/tebligat tarihi ve verilen süre nedir?
3. İhlal iddiasının somut konusu ve EPDK'nın delili nedir?
4. Daha önce ihtar/savunma alındı mı, tekerrür var mı?

## Denetim şeması
1. **Dayanak ve oran**: 6446 m.16 (elektrik) veya 4646 ilgili maddesi — yaptırım türü ve para cezası tutarının hesabı, üst sınır ve oransallık. Ara sonuç: uygulanan yaptırım türü/oranı dayanakla uyumlu mu.
2. **Usul denetimi**: Savunma hakkının tanınıp tanınmadığı, makul süre verilip verilmediği, gerekçe ve bilgi/belgeye erişim. Usul sakatlığı tek başına iptal sebebi olabilir (idari işlemde şekil/yetki unsuru).
3. **Esas denetimi**: İhlalin maddi olarak gerçekleşip gerçekleşmediği; teknik/lisans yükümlülüğünün ihlali iddiası karşı delil ve uzman raporuyla çürütülür. İspat yükü idarede; ancak müvekkil lehine vakıaları belgeleyin.
4. **Ölçülülük ve eşit muamele**: Benzer ihlallere uygulanan yaptırımlarla karşılaştırma; ağırlaştırıcı/hafifletici unsurlar.
5. **Dava yolu**: İdari yaptırım EPDK işlemi olduğundan İYUK m.7 (kural 60 gün) içinde iptal davası; m.27 yürütmenin durdurulması istemi para cezası tahsili/lisans iptali sonuçlarını dondurmak için kritik. Görevli yargı yeri idari yargıdır.

İlkesel içtihat için karararama.danistay.gov.tr (özellikle 13. Daire) taranır; künye [DOĞRULANMADI] işaretlenir, esas/karar no uydurulmaz.

## Çıktı modülleri
- EPDK savunma yazısı taslağı (usul + esas).
- İptal davası dilekçesi ve YD istemi iskeleti.
- Sakatlık ve karşı delil tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

