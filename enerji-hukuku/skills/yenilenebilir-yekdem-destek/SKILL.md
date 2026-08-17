---
argument-hint: ''
description: YEK belgesi, YEKDEM kapsamında fiyat garantisi, yerli katkı ilavesi,
  destek süresi ve YEKA yarışmaları gibi yenilenebilir destek konuları ele alındığında
  ve destekten yararlanma uyuşmazlıklarında kull
name: yenilenebilir-yekdem-destek
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


# Yenilenebilir Enerji ve YEKDEM Destek Mekanizması

## Görev
Yenilenebilir üretim tesisinin 5346 sayılı YEK Kanunu destek mekanizmasından (YEKDEM/YEK belgesi) yararlanma koşullarını, fiyat ve süre hesabını ve destek uyuşmazlıklarını çözümlemek.

## Soğuk başlangıç (intake)
1. Kaynak türü (rüzgâr, GES, HES, biyokütle, jeotermal) ve kapasite?
2. İşletmeye giriş/geçici kabul tarihi nedir?
3. YEK belgesi alındı mı; YEKDEM'e kayıtlı mı, hangi dönem?
4. Yerli aksam/katkı ilavesi talep ediliyor mu?

## Denetim şeması
1. **Kapsam**: 5346 — destekten yararlanacak kaynaklar ve YEK belgesinin alınması. Ara sonuç: kaynak ve tesis destek kapsamında mı.
2. **Fiyat ve süre**: 5346 ve eki I sayılı cetvel — kaynak bazlı taban fiyat ($/MWh); destek süresi kural olarak işletmeye giriş tarihinden itibaren on yıl. Olay tarihindeki cetvel ve kur/dönem uygulaması esastır (tarih kilidi).
3. **Yerli katkı ilavesi**: Yerli üretim aksam kullanımına bağlı ilave fiyat; aksamın yerlilik belgesi ve süre sınırı (kural olarak ilk beş yıl) ispatla aranır. İspat yükü üreticide.
4. **YEKDEM kayıt ve uzlaştırma**: EPİAŞ nezdinde YEKDEM kayıt başvurusu, son tarihler ve dönemsel beyan. Kayıt/süre kaçırılırsa o dönem destek dışı kalınır; bu, doğrudan alacak kaybı doğurur.
5. **YEKA modeli**: YEKA yarışmalarında fiyat ve yerli üretim taahhütleri sözleşmesel olup 5346 destek rejiminden ayrı; ihale şartnamesi ve sözleşme hükümleri esas alınır.

Uyuşmazlıkta EPİAŞ uzlaştırma verisi ve bilirkişi hesabı temel delildir; idari ret kararına karşı İYUK yolu, alacak için sözleşmesel/idari ayrımı yapılır.

## Çıktı modülleri
- Destek uygunluk ve fiyat/süre hesap notu.
- Yerli katkı belge kontrol listesi.
- YEKDEM kayıt/itiraz başvuru taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

