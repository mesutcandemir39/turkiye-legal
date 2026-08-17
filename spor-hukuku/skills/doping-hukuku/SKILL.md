---
argument-hint: ''
description: Doping ihlali isnadı, numune süreci, yaptırım veya itiraz konularını
  WADA Kodu ve ilgili federasyon talimatı çerçevesinde değerlendirmek gerektiğinde
  kullanın.
name: doping-hukuku
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Doping Hukuku ve Yaptırım Süreci

## Görev
Bir doping ihlali isnadını WADA Kodu, ulusal doping talimatı ve uluslararası federasyon kuralları çerçevesinde değerlendirmek; numune ve usul güvencelerini denetlemek; savunma ya da yaptırıma itiraz stratejisi hazırlamaktır.

## Soğuk başlangıç (intake)
1. İhlal türü nedir: yasaklı madde bulgusu, numune vermekten kaçınma, bulunulabilirlik (whereabouts) ihlali?
2. Numune hangi tarihte alındı ve A/B numune süreci nasıl işledi?
3. Madde, yasaklılar listesinde hangi kategoride (her zaman/yarışma içi)?
4. Sporcunun açıklaması ve olası kaynak (kontaminasyon, tıbbi kullanım) nedir?
5. Tedavi amaçlı kullanım izni (TUE) var mı?

## Denetim şeması
1. **Norm zemini**: WADA Kodu ve Yasaklılar Listesi, ulusal doping kontrol talimatı ve ilgili uluslararası federasyon kuralları birlikte uygulanır; sıkı (objektif) sorumluluk ilkesi esastır.
2. **Usul güvenceleri**: Numune alma zinciri (chain of custody), A ve B numune analizi, laboratuvar akreditasyonu ve bildirim usulü denetlenir; usul ihlali sonucu etkileyebilir.
3. **Kusur değerlendirmesi**: Sıkı sorumlulukta varlık ispatı yeterlidir; ancak yaptırımın süresi sporcunun kusur derecesine (kasıtlı/kasıtsız, ağır/hafif kusur, hiç kusur yokluğu) göre indirilebilir veya kaldırılabilir.
4. **TUE ve kontaminasyon**: Geçerli tedavi amaçlı kullanım izni veya kanıtlanmış kontaminasyon savunması yaptırımı etkiler; ispat yükü sporcudadır.
5. **Yaptırım ve itiraz**: Müsabakadan men süresi, sonuçların iptali; karara karşı federasyon tahkimi ve milletlerarası boyutta **CAS** yolu, süreler kontrol edilir.
6. **Ara sonuç**: İhlalin sübutu, kusur derecesi ve indirim/itiraz şansı belirlenir.

## Çıktı modülleri
- Usul ve numune zinciri denetim listesi
- Savunma/itiraz dilekçesi iskeleti
- Kusur ve indirim argümanları
- CAS/tahkim süre notu `[DOĞRULANMADI]`



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

