---
argument-hint: ''
description: Yabancının dosyasında izlenecek yol seçenekleri tartılacağında; sınır
  dışı/gözetim riski, başvuru-dava ardışıklığı ve en lehe statünün belirlenmesi gerektiğinde
  kullanılır.
name: risk-strateji
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
  - ad: Yabancılar ve Uluslararası Koruma Kanunu
    numara: '6458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Strateji

## Görev
Yabancının dosyasında mevcut riskleri (uzaklaştırma, gözetim, statü kaybı, yaptırım) haritalamak, seçenekleri olası sonuç ve sürelere göre tartmak, en lehe ve uygulanabilir yol haritasını kurmak.

## Soğuk başlangıç (intake)
1. Müvekkilin önceliği nedir (Türkiye'de kalış, çalışma, koruma, vatandaşlık, sınır dışını önleme)?
2. Aktif/potansiyel idari işlemler ve riskler nelerdir?
3. Zaman baskısı var mı (gözetim, yaklaşan süre, ailenin durumu)?
4. Geçmiş ihlal, giriş yasağı veya ceza kaydı var mı?

## Denetim şeması
1. **Risk envanteri**: Sınır dışı (YUKK m.54), gözetim (m.57), ikamet ret/iptal (m.33/50), izinsiz çalışma yaptırımı (6735 m.23), giriş yasağı (m.9), statü kaybı.
2. **Koruma kalkanları**: Geri gönderme yasağı (m.4/m.55), uluslararası/geçici koruma başvurusunun askıya alıcı etkisi, aile birliği ve çocuğun üstün yararı (AİHS m.8), sağlık durumu.
3. **Seçenek tartımı**: Her yol için (başvuru, idari itiraz, dava+YD, koruma başvurusu) başarı olasılığı, süre, askıya alıcı etki ve geri dönülemezlik karşılaştırılır. Statüler arası geçişte en aktif koruma sağlayan yol önceliklendirilir.
4. **Ardışıklık ve eşzamanlılık**: Örneğin sınır dışıya karşı dava açarken paralel koruma başvurusunun gözetim ve uzaklaştırmaya etkisi planlanır; çelişkili statü taleplerinden kaçınılır.
5. **Kötü senaryo planı**: Süre kaçarsa/dava reddedilirse alternatif (gönüllü dönüş, üçüncü ülke, yeniden başvuru) hazırlanır.
**Ara sonuç**: Önceliklendirilmiş, sürelere bağlanmış tek bir yol haritası ve yedek plan.

## Çıktı modülleri
- Risk haritası (risk, olasılık, etki, dayanak madde).
- Seçenek karşılaştırma tablosu ve tavsiye.
- Aşamalı eylem planı ve tetik tarihleri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

