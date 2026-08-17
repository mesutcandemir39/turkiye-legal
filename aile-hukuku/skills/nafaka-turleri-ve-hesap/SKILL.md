---
argument-hint: ''
description: Tedbir, yoksulluk ve iştirak nafakası taleplerinin türünü, şartlarını,
  miktarını ve süresini belirlemek; nafakanın artırımı, azaltımı veya kaldırılması
  davalarını kurgulamak gerektiğinde kullanılır.
name: nafaka-turleri-ve-hesap
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
  requires_human_review: true
  risk_level: high
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


# Nafaka Türleri, Şartları ve Hesap

## Görev
Talep edilen nafakayı doğru türe oturtmak (tedbir, yoksulluk, iştirak, yardım), şartlarını denetlemek ve tarafların mali gücüne göre hakkaniyete uygun miktar/süre kurgulamak.

## Soğuk başlangıç (intake)
1. Nafaka kimin için isteniyor: eş için mi, çocuk için mi, üstsoy-altsoy/kardeş için mi?
2. Dava sürüyor mu (tedbir nafakası), boşanma kesinleşti mi (yoksulluk/iştirak)?
3. Tarafların gelirleri, malvarlığı, çocuk sayısı ve özel ihtiyaçları neler?
4. Mevcut nafaka var mı; artırım, azaltım veya kaldırma mı isteniyor?

## Denetim şeması
1. **Tür ayrımı.** Yargılama süresince eş ve çocuk için **tedbir nafakası** (TMK m.169) talep edilir. Boşanma sonrası eş için **yoksulluk nafakası** (m.175): boşanmayla yoksulluğa düşecek taraf, kusuru daha ağır olmamak kaydıyla, süresiz olarak isteyebilir. Çocuk için **iştirak nafakası** (m.182, m.327-330): velayet kendisine verilmeyen taraf, çocuğun bakım-eğitim giderlerine gücü oranında katılır; ergin olana kadar (eğitimi sürüyorsa m.328/2 kapsamında uzayabilir). Akrabalar arası **yardım nafakası** (m.364).
2. **Şart denetimi.** Yoksulluk nafakasında: boşanma yüzünden yoksulluk + talep eden kusurun daha ağır olmaması + nafaka yükümlüsünün gücü. İştirak nafakasında kusur aranmaz; ölçüt çocuğun ihtiyacı ve ana-babanın mali gücüdür.
3. **Miktar/biçim.** Hâkim irat veya toptan ödemeye karar verebilir (m.176/1); irat şeklindeki nafaka ÜFE/uyarlama hükmüyle (m.176/4, m.331) artırılabilir. Yoksulluk nafakası, alacaklının yeniden evlenmesi, ölüm veya fiilen evli gibi yaşama halinde kendiliğinden/dava ile kalkar (m.176/3).
4. **Uyarlama davaları.** Tarafların mali durumunun değişmesi halinde artırım/azaltım/kaldırma (m.176/4, m.331); ispat yükü değişikliği iddia edende.
5. **Ara sonuç.** Tür + şart + miktar/süre + uyarlama imkânı raporlanır.

## Çıktı modülleri
- Nafaka türü-şart-süre tablosu ve hakkaniyet gerekçesi.
- Gelir-gider/ihtiyaç dökümü ile miktar önerisi aralığı.
- Artırım/azaltım/kaldırma dilekçesi için dayanak listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

