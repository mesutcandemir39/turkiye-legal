---
argument-hint: ''
description: Başvurunun komisyonca/bölümce kabul edilebilir bulunup bulunmayacağı,
  açıkça dayanaktan yoksunluk, önemli zarar ve diğer ret sebepleri değerlendirilirken;
  esasa geçmeden önceki eşiği geçmek için kulla
name: kabul-edilebilirlik-denetimi
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
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kabul Edilebilirlik Denetimi

## Görev
Başvurunun 6216 m.48 ve İçtüzük süzgeçlerinden geçip geçmeyeceğini önceden öngörmek; kabul edilemezlik risklerini tespit edip başvuruyu güçlendirmek veya gereksiz başvurudan caydırmak.

## Soğuk başlangıç (intake)
- Şikâyet konusu hangi anayasal hakka dayandırılıyor; açık bir anayasal mesele var mı?
- Başvurucunun katlandığı zarar önemli/anlamlı mı, yoksa önemsiz mi?
- Başvuru formundaki olay, deliller ve ihlal gerekçeleri tam mı?
- Daha önce aynı konuda AYM kararı var mı (mükerrerlik)?

## Denetim şeması
1. Anayasal/kişisel yetki — m.45-46: konu, kişi ve zaman bakımından yetki yeniden teyit edilir; eksikse usulden ret.
2. Açıkça dayanaktan yoksunluk — m.48/2: ihlal iddiası temellendirilmemişse, salt kanun yolu şikâyetiyse veya hak ihlali görünür biçimde yoksa başvuru reddedilir. Başvurucu, ihlali "ilk bakışta savunulabilir" (arguable) düzeyde ortaya koymalıdır.
3. Önemli zarar (anayasal önem) ölçütü — başvurucunun önemli bir zarara uğramadığı, anayasal ve kişisel önemi bulunmayan başvurular kabul edilemez bulunabilir; istisna, genel yarar veya ilkesel mesele varlığında değerlendirilir.
4. Mükerrerlik / derdestlik — daha önce esastan karara bağlanmış aynı başvuru veya başka uluslararası mercide derdest aynı şikâyet ret sebebidir.
5. Süre ve şekil — İçtüzük m.64'teki otuz günlük süre ve m.59 vd. başvuru formu şartları; eksiklik varsa giderme süresi tanınır, giderilmezse ret.

İspat yükü: kabul edilebilirlik eşiğini geçecek temellendirme başvurucudadır; AYM resen de inceler.

Ara sonuç: her ret sebebi için "geçti / riskli / geçemez" etiketi ve gerekçe çıkarılır.

## Çıktı modülleri
- Kabul edilebilirlik kontrol listesi (madde madde geçti/riskli/red).
- Açıkça dayanaktan yoksunluk riski analizi ve güçlendirme önerileri.
- Önemli zarar ve mükerrerlik notu.
- Eksiklik giderme uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

