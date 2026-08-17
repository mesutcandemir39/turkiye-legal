---
argument-hint: ''
description: Bir teklifin değerlendirme dışı bırakılması, ihale dışı bırakma veya
  yeterlik belgelerinin (iş deneyim, mali yeterlik, geçici teminat) eksikliği tartışıldığında
  başvurulacak değerlendirme denetimi bec
name: yeterlik-ve-teklif-degerlendirme
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yeterlik ve Teklif Değerlendirme

## Görev
Tekliflerin değerlendirilmesinde isteklinin yeterlik kriterlerini sağlayıp sağlamadığını, değerlendirme dışı bırakma veya ihale dışı bırakma kararının hukuka uygunluğunu denetlemek.

## Soğuk başlangıç (intake)
1. Hangi belge eksik/uygunsuz görülerek teklif değerlendirme dışı bırakıldı?
2. Eksiklik bilgi tamamlatma kapsamında mı, yoksa esasa ilişkin mi (m.37)?
3. İş deneyim belgesi, mali yeterlik oranları, geçici teminat uygun mu (m.10, m.33-34)?
4. İhale dışı bırakma sebebi (m.10 son fıkra) somut belgeyle mi dayandırıldı?

## Denetim şeması
1. **Geçici teminat (m.33-34):** Teklif edilen bedelin %3'ünden az olmamak üzere; uygun olmayan/eksik teminat değerlendirme dışı bırakma sebebidir, tamamlatılamaz.
2. **Yeterlik kriterleri (m.10):** Ekonomik-mali yeterlik (banka referansı, bilanço/iş hacmi oranları) ve mesleki-teknik yeterlik (iş deneyim belgesi, kapasite, kalite belgeleri) sağlanmalı. İş deneyim oranları işin türüne göre (yapımda asgari oranlar) kontrol edilir.
3. **İhale dışı bırakma (m.10 son fıkra):** İflas, tasfiye, vergi/SGK borcu, m.17 yasak fiil, ihale tarihinden önceki belirli süre içinde mahkûmiyet gibi durumlar somut belgeyle ortaya konur.
4. **Bilgi/belge tamamlatma (m.37, ilgili Yönetmelik):** Teklifin esasını değiştirmeyen, sunulan belgelerdeki bilgi eksiklikleri tamamlatılabilir; teklif fiyatını veya teklifin esasını etkileyen eksiklik tamamlatılamaz, bu ayrım iptal davalarının düğüm noktasıdır.
5. **Eşit muamele:** Bir istekliye tanınan tamamlatma imkânı diğerine de tanınmalıdır (m.5). Çelişkili uygulama iptal sebebidir.
6. **Ara sonuç:** Karar hukuka aykırıysa kesinleşen ihale kararının bildiriminden itibaren 10 gün içinde şikâyet edilir.

İspat yükü: Yeterliğini iddia eden istekli belgeyi sunmuş olmalı; idare ret sebebini gerekçeli açıklar.

## Çıktı modülleri
- Belge bazlı yeterlik kontrol tablosu.
- Tamamlatılabilir/tamamlatılamaz ayrım analizi.
- Eşit muamele karşılaştırma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

