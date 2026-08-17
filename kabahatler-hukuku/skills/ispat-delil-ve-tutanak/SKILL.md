---
argument-hint: ''
description: İdari yaptırıma dayanak tutanak, cihaz/kayıt ve tespitlerin ispat değerini
  değerlendirmek, ispat yükünü dağıtmak ve çürütücü delil stratejisi kurmak gerektiğinde
  kullanılır.
name: ispat-delil-ve-tutanak
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Tutanak Denetimi

## Görev
Kabahatin sübutunu sağlayan delilleri (tutanak, ölçüm cihazı, kamera/ses kaydı, tanık) ispat değeri açısından denetlemek ve çürütücü delil stratejisi kurmak.

## Soğuk başlangıç (intake)
- Kabahat hangi delille tespit edilmiş (tutanak, mobese, hız/emisyon cihazı, numune)?
- Tutanağı kim, hangi yetkiyle, nasıl düzenlemiş; imza/tanık var mı?
- Ölçüm cihazının kalibrasyon/muayene belgesi mevcut mu?
- İlgili kişiye tespit anında bildirim/savunma imkânı tanınmış mı?

## Denetim şeması
1. **İspat yükü:** Kabahatin gerçekleştiğini ispat kural olarak **idareye** düşer. İdare somut, doğrulanabilir delil sunmalıdır; soyut tespit yetersizdir.
2. **Tutanağın değeri:** Usulüne uygun düzenlenmiş tutanak güçlü bir delildir ancak kesin (mutlak) delil değildir; aksi her türlü delille ispatlanabilir. Tutanağın yer-zaman-fiil-tespit yöntemi yönünden çelişki ve eksikliklerini tara.
3. **Teknik tespitler:** Hız/emisyon/gürültü ölçümü, kantar vb. cihazların yetkili kurumca kalibre/muayene edilmiş olması; ölçüm koşullarının kurallara uygunluğu denetlenir. Kalibrasyonsuz/usulsüz ölçüm ispat değerini düşürür.
4. **Hukuka aykırı delil:** Hukuka aykırı yolla elde edilen delilin değerlendirme dışı bırakılması ilkesi (genel ispat hukuku ve Anayasa m.38/6) kabahatler bakımından da gözetilir.
5. **Çürütücü delil:** Tanık, karşı belge, bilirkişi/teknik rapor ve keşif talepleriyle idarenin delilini sars. Başvuruda delillerini açıkça göster.
6. **Ara sonuç:** İspat yükü dengesini değerlendir — idare sübutu sağlayamıyorsa kabahat sabit sayılmaz ve ceza kaldırılır.

## Çıktı modülleri
- Delil-tespit eleştiri tablosu (her delil için zayıf nokta).
- Çürütücü delil listesi ve talep dilekçesi taslağı.
- İspat yükü değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

