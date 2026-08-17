---
argument-hint: ''
description: Taşınmazın kamulaştırılması, kamulaştırmasız el atma, acele kamulaştırma
  ve kamulaştırma bedelinin tespiti süreçlerini değerlendirmek için kullanılır; idarenin
  mülkiyete müdahalesi söz konusuysa başvu
name: kamulastirma
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kamulaştırma ve Bedel Davaları

## Görev
Kamulaştırma işleminin hukuka uygunluğunu, bedel tespiti sürecini ve kamulaştırmasız el atma hallerini değerlendirmek; mülkiyet hakkı (Anayasa m.35, m.46) ile kamu yararı dengesini kurmak.

## Soğuk başlangıç (intake)
1. Usulüne uygun kamulaştırma kararı ve kamu yararı kararı var mı?
2. Süreç hangi aşamada (kıymet takdiri, uzlaşma, bedel tespiti/tescil davası, acele kamulaştırma)?
3. Fiilen el atılmış ama kamulaştırma yapılmamış mı (kamulaştırmasız el atma)?
4. Tebliğ ve süreler korunmuş mu?

## Denetim şeması
1. **Dayanak ve kamu yararı.** Anayasa m.46 ve 2942 sayılı Kamulaştırma Kanunu. Kamu yararı kararı, onay ve kıymet takdiri usulüne uygun mu? Kamu yararı yoksa veya amaç dışıysa iptal yolu (idari yargı) açık.
2. **Bedel tespiti ve tescil.** Uzlaşma sağlanamazsa idare, asliye hukuk mahkemesinde bedel tespiti ve tescil davası açar (2942 m.10). Bedel **gerçek karşılık** olmalı; değerleme bilirkişi ile yapılır; bedel artırımı talep edilebilir.
3. **İki yargı yolu ayrımı.** Kamulaştırma **işleminin iptali** idari yargıda; **bedel** uyuşmazlığı adli yargıda (asliye hukuk) görülür. Bu ayrımı baştan kur.
4. **Acele kamulaştırma.** 2942 m.27: acele el koyma kararı ve bilirkişi bedeli; sonradan esas bedel davası. Acelelik koşullarının denetimi.
5. **Kamulaştırmasız el atma.** Fiili el atma → adli yargıda tazminat (bedel) davası; hukuki el atma (imar kısıtlaması) → idari yargı. Süreç ve yargı yolu seçimi kritik.
6. **İspat.** Taşınmazın niteliği, emsal, değer artırıcı unsurlar; değerleme raporuna gerekçeli itiraz.
7. **Ara sonuç.** Hedef iptal mi, bedel mi, kamulaştırmasız el atma tazminatı mı; yargı yolu ve mahkeme.

## Çıktı modülleri
- Yargı yolu ayrımı tablosu (iptal/bedel/el atma).
- Süreç aşaması ve eksik işlem listesi.
- Bedele/değerleme raporuna itiraz notu.
- İlgili dava dilekçesi için iskelet.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

