---
argument-hint: ''
description: Bir ceza dosyasındaki delilleri suç unsurları bakımından tartmak, delil
  yasaklarını kontrol etmek ve hukuki nitelendirmenin delil durumuyla uyumunu denetlemek
  gerektiğinde kullanılır.
name: ispat-delil-degerlendirme
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Suç Vasfı Değerlendirmesi

## Görev
Dosyadaki delilleri her bir suç unsuru (tipiklik, kast, nitelikli hal) bakımından eşleştirmek, hukuka aykırı delilleri ayıklamak ve isnadın delil durumuyla örtüşüp örtüşmediğini değerlendirmek.

## Soğuk başlangıç (intake)
- İsnat edilen suç ve hangi unsurların ispatı tartışmalı?
- Dosyada hangi deliller var (beyan, görüntü/ses kaydı, dijital veri, bilirkişi raporu, fizik delil)?
- Deliller hukuka uygun yöntemle (arama-el koyma, iletişimin denetlenmesi) mı elde edildi?
- Tek delil mağdur/müşteki beyanı mı, yoksa beyanı destekleyen yan deliller var mı?

## Denetim şeması
1. Unsur-delil eşlemesi: Her suç unsuru için (fiil, netice, nedensellik, kast, nitelikli hal) dosyadaki hangi delilin onu ispatladığını yaz. İspatsız kalan unsur, beraat veya vasıf değişikliği gerektirir.
2. Delil yasakları: Hukuka aykırı yöntemle elde edilen deliller hükme esas alınamaz (Anayasa m.38/6; CMK m.206/2-a, m.217/2, m.230/1). Aramada usulsüzlük, hukuka aykırı iletişim tespiti veya işkence/baskıyla alınan ifade bu kapsamdadır.
3. Beyan delillerinin değerlendirilmesi: Mağdur/tanık beyanlarının istikrarı, çelişkileri, menfaat ilişkisi ve yan delillerle desteklenip desteklenmediği. Tek beyana dayalı mahkûmiyetin sınırları için ilkesel Yargıtay içtihadına atıf (karararama.yargitay.gov.tr; künye `[DOĞRULANMADI]`).
4. Bilirkişi ve teknik deliller: İğfal kabiliyeti, yaralanma derecesi, dijital iz analizi gibi teknik konularda raporun dayanağı ve metodolojisi denetlenir; çelişki halinde ek rapor/yeni bilirkişi talep edilir.
5. Şüpheden sanık yararlanır (in dubio pro reo): Unsurlardan biri makul şüphe düzeyinde dahi ispatlanamıyorsa, lehe yorum ve beraat değerlendirmesi yapılır. Vasıf değişikliği (örn. yağmadan hırsızlığa, nitelikli halden basit hale) gündeme gelebilir.
6. Ara sonuç: İspatlanan/ispatlanamayan unsurlar listesi + ayıklanması gereken deliller + olası suç vasfı ve beklenen sonuç (mahkûmiyet/beraat/vasıf değişikliği).

## Çıktı modülleri
- Unsur-delil eşleme tablosu (unsur, dayanak delil, güç derecesi).
- Delil yasağı/itiraz noktaları listesi (madde atıflı).
- Suç vasfı ve sonuç senaryosu değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

