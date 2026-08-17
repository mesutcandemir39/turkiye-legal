---
argument-hint: ''
description: SGK'ya idari başvuru/itiraz, iş mahkemesinde dava ve cevap dilekçeleri
  ile gelir testi/idari para cezası itiraz metinlerinin taslağı hazırlanması gerektiğinde
  kullanılır.
name: basvuru-dilekce-ve-itiraz
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Başvuru, Dilekçe ve İtiraz Taslağı

## Görev
Sosyal güvenlik uyuşmazlığına uygun idari başvuru, itiraz ve yargı dilekçelerini doğru yapı ve dayanaklarla taslaklamak; yer tutucu disiplinini korumak.

## Soğuk başlangıç (intake)
- Hangi belge gerekiyor: SGK'ya itiraz, dava dilekçesi, cevap, gelir testi/idari para cezası itirazı mı?
- Taraflar ve statüleri kim (sigortalı, işveren, SGK, hak sahipleri)?
- Talep sonucu net mi (tespit, iptal, aylık bağlanması, alacak)?
- İdari aşama tamamlandı mı; tebliğ ve süre durumu nedir?

## Denetim şeması
1. Tür seçimi: İdari aşamada SGK'ya itiraz/başvuru (5510 m.101); yargıda iş mahkemesinde dava (7036 m.5). Yanlış mercie verilen dilekçe usul riski yaratır.
2. İskelet — HMK m.119: Dava dilekçesinde mahkeme, taraflar, konu, vakıalar, hukuki sebepler, deliller ve talep sonucu eksiksiz yer alır; cevapta HMK m.129 unsurları.
3. Dayanak yerleştirme: İlgili 5510 maddeleri (statüye/uyuşmazlığa göre m.4, m.13, m.21, m.28, m.41, m.60, m.80, m.86, m.93) ve usul (7036, HMK) doğru atıfla bağlanır.
4. Delil bağlama: Her vakıaya delil iliştirilir; SGK'dan getirtilecek belgeler ve tanıklar dilekçede gösterilir.
5. Yer tutucu disiplini: Bilinmeyen tarih/tutar/ad alanları `[doldurulacak]` ile işaretlenir; uydurma rakam/künye girilmez. Ara sonuç: gönderime hazır taslak iskeleti.

## Çıktı modülleri
- Seçilen tür için dilekçe/itiraz iskeleti.
- Dayanak madde ve delil bloğu.
- `[doldurulacak]` alan listesi ve ek belge kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

