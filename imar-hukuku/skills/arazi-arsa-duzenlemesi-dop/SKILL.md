---
argument-hint: ''
description: İmar uygulaması, parselasyon, düzenleme ortaklık payı (DOP) kesintisi,
  dağıtım ve tahsis işlemlerine itiraz veya iptal davası gündeme geldiğinde; eşit/eşdeğer
  dağıtım ilkesi ve DOP oranı sorulduğunda
name: arazi-arsa-duzenlemesi-dop
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Arazi ve Arsa Düzenlemesi (m.18 / DOP)

## Görev
İmar uygulaması (parselasyon) ve DOP işlemlerinin hukuka uygunluğunu denetlemek; eşit dağıtım ve kamu payı dengesini kontrol ederek iptal davasını kurmak.

## Soğuk başlangıç (intake)
- Uygulama hangi imar planına dayanıyor, encümen/onay kararı tarihi ne?
- Müvekkilin eski parseli ile tahsis edilen yeni parsel(ler) neler?
- DOP oranı kaç, hangi kamu tesisleri için kesildi?
- Dağıtımda değer kaybı, başka bölgeye tahsis veya eşitsizlik var mı?

## Denetim şeması
1. **Uygulamanın dayanağı (3194 m.18)**: Düzenlemenin **onaylı uygulama imar planına** dayanması zorunludur; plansız m.18 uygulaması yapılamaz. Plan-uygulama bağı ilk denetim noktasıdır.
2. **DOP kesintisi**: Düzenlemeye giren taşınmazlardan, düzenleme ile oluşan değer artışı karşılığında ve **kanunda belirlenen üst oran** dahilinde, bedelsiz olarak düzenleme ortaklık payı kesilir; DOP yalnızca m.18'de sayılan kamusal hizmet alanları için kullanılabilir. Oranın ve kullanım amacının yasallığı denetlenir.
3. **Eşit/eşdeğer dağıtım ilkesi**: Maliklerin yeni parsellere mümkün olduğunca **eski parseline yakın ve eşdeğer** biçimde tahsisi esastır; başka bölgeye savrulma, değer kaybı, hisseli hale getirme eşitlik denetiminden geçirilir.
4. **Mükerrer DOP yasağı**: Aynı taşınmazdan ikinci kez DOP kesilemez (daha önce kesinti yapılmışsa); bu husus tapu kaydı ve önceki uygulamalarla doğrulanır.
5. **İspat ve bilirkişi**: Harita mühendisi/şehir plancısı bilirkişi, dağıtım cetvelleri, parselasyon paftaları, değerleme; ispat yükü idarenin işlemin hukuka uygunluğunu, davacının somut zararını göstermesi şeklinde paylaşılır.
6. **Süre ve ara sonuç**: Parselasyon işlemi ilan edilir; İYUK m.7'de 60 günde iptal davası açılır. DOP oranı, dağıtım veya plan-uygulama bağı sakatsa iptal + gerekirse YD. İlkesel Danıştay atfı `[DOĞRULANMADI]`.

## Çıktı modülleri
- DOP oranı ve kullanım amacı denetim notu.
- Eski-yeni parsel eşdeğerlik karşılaştırması.
- Mükerrer DOP/değer kaybı kontrol listesi.
- Parselasyon iptali dilekçe iskeleti ve bilirkişi soruları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

