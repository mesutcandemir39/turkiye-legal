---
argument-hint: ''
description: İmar hukukunun kavram haritası ve planlama kademeleri sorulduğunda; emsal-TAKS-KAKS-çekme
  mesafesi, çevre düzeni-nazım-uygulama planı zinciri, idari-adli yargı ayrımı ve
  hangi işlemin hangi rejime tab
name: temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Planlama Hiyerarşisi

## Görev
İmar dosyasının doğru çerçevelenmesi için kavramsal altyapıyı kurmak: planlama kademelerini, yapılaşma parametrelerini ve uyuşmazlığın hangi yargı koluna ait olduğunu belirlemek.

## Soğuk başlangıç (intake)
- İhtilaf hangi işlemden çıkıyor: imar planı/değişikliği mi, ruhsat mı, yıkım/ceza mı, kamulaştırma mı?
- Taşınmazın imar durumu nedir (ada/parsel, mevcut plan ölçeği, fonksiyon)?
- İşlemi tesis eden idare hangisi (belediye, büyükşehir, bakanlık)?
- Elinizde plan paftası, imar durum belgesi, ruhsat veya tebligat var mı?

## Denetim şeması
1. **Planlama hiyerarşisi (3194 m.6-8)**: Çevre düzeni planı (1/100.000-1/25.000) → nazım imar planı (1/5000) → uygulama imar planı (1/1000). Alt ölçekli plan üst ölçeğe ve şehircilik ilkelerine, kamu yararına, planlama esaslarına aykırı olamaz. Aykırılık iptal sebebidir.
2. **Yapılaşma parametreleri**: TAKS (taban alanı kat sayısı), KAKS/emsal (kat alanı kat sayısı), çekme mesafeleri, Hmax, ada/parsel bazında yapılaşma; Planlı Alanlar İmar Yönetmeliği'ndeki tanımlarla okunur. Plan notları parametre kadar bağlayıcıdır.
3. **Yargı kolu ayrımı**: Plan, ruhsat, yıkım, encümen para cezası → **idari yargı (iptal/tam yargı)**. Kamulaştırma bedel tespiti ve kamulaştırmasız el atma bedeli, kat karşılığı inşaat ve taşınmaz satış uyuşmazlıkları → **adli yargı**. Yanlış yargı kolu = görev yönünden ret riski.
4. **İşlem tipi-rejim eşleştirmesi**: Her işlemin dayanağı kademe ve mevzuat maddesi ile bağlanır (ör. yıkım → m.32; para cezası → m.42; DOP → m.18).
5. **Ara sonuç**: Uyuşmazlığın türü, yargı kolu, görevli mahkeme ve dayanak normlar bir cümlede sabitlenir; sonraki beceri buradan beslenir.

## Çıktı modülleri
- Kavram-parametre sözlüğü (emsal/TAKS/KAKS/çekme/Hmax tanımlı).
- Planlama hiyerarşisi şeması ve somut dosyadaki kademe konumu.
- Yargı kolu ve görevli mahkeme tespit notu.
- Bir sonraki adıma yönlendirme (plan denetimi / ruhsat / yıkım-ceza / kamulaştırma).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

