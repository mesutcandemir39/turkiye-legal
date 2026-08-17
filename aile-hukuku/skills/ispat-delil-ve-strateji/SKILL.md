---
argument-hint: ''
description: Aile davalarında kusurun, gelir-malvarlığının veya soybağının ispatı,
  delil toplama ve kabul edilebilirliği, gizlilik ve hukuka aykırı delil sorunları
  ile genel dava stratejisi gerektiğinde kullanılır
name: ispat-delil-ve-strateji
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Dava Stratejisi

## Görev
Aile hukuku uyuşmazlığında ispat yükünü dağıtmak, her vakıa için uygun ve kabul edilebilir delili belirlemek, hukuka aykırı delil ve gizlilik risklerini yönetmek ve genel stratejiyi kurmak.

## Soğuk başlangıç (intake)
1. İspatlanacak çekişmeli vakıalar neler (kusur, gelir, katkı, soybağı, yoksulluk)?
2. Eldeki deliller hangileri ve nasıl elde edildi (kayıt, mesaj, tanık, kamera)?
3. Karşı tarafın olası savunması ve karşı delilleri ne olabilir?
4. Müvekkilin kırmızı çizgileri ve önceliği (çocuk mu, para mı, hız mı) nedir?

## Denetim şeması
1. **İspat yükü.** Kanunun aksini öngörmedikçe, iddia eden ispatla yükümlüdür (TMK m.6, HMK m.190). Kusura dayalı talepte kusuru iddia eden; katılma alacağında malın edinilmiş olmadığını iddia eden ispatlar (TMK m.222 karinesi: aksi ispatlanamayan mal edinilmiş sayılır).
2. **Delil eşleştirme.** Kusur: tanık (HMK m.240 vd.), mesaj/yazışma, kamera, sosyal medya, ceza/koruma dosyası. Gelir-malvarlığı: SGK/işyeri kaydı, banka hareketleri, tapu-trafik kaydı, vergi beyanı; mahkemeden müzekkere ile celp. Soybağı: DNA tespiti (m.284, hâkim re'sen). Yoksulluk: ekonomik-sosyal durum araştırması. Çocuk: pedagog/uzman raporu, idrak çağında çocuğun dinlenmesi.
3. **Kabul edilebilirlik ve gizlilik.** Hukuka aykırı yolla elde edilen delil kural olarak değerlendirilemez (HMK m.189/2; AY m.38/6). Karşı eşin telefonuna izinsiz erişim, gizli ses/görüntü kaydı TCK m.132-134 ve m.135 vd. kapsamında suç oluşturabilir; bu deliller hem reddedilebilir hem müvekkili ceza riskine sokar — uyarı şart. Yargıtay uygulamasında "tesadüfen/aynı konutta" elde edilen bazı kayıtların değerlendirildiği istisnalar ilkesel olarak anlatılır, somut karar künyesi `[DOĞRULANMADI]` (karararama.yargitay.gov.tr).
4. **Strateji.** Önce tür/sebep seçimi, sonra delil yeterliliği; zayıf kusur dosyasında genel sebep (m.166) tercih edilir; tasfiye için mal kaçırma riskine karşı ihtiyati tedbir/haciz öngörülür; çocuk önceliğinde uzlaşma ve uzman desteği değerlendirilir.
5. **Ara sonuç.** Vakıa-delil-ispat yükü matrisi + risk uyarıları + strateji önerisi.

## Çıktı modülleri
- İspat planı tablosu (vakıa / ispat yükü / delil / temin yolu).
- Hukuka aykırı delil ve ceza riski uyarı notu.
- Strateji ve müzekkere/tedbir talep listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

