---
argument-hint: ''
description: Sendika veya isveren tarafi icin toplu sureclerde hukuki ve operasyonel
  riskleri (yetki dususu, kanun disi grev, sendikal tazminat, idari para cezasi) tartip
  strateji onerir; bir pazarlik veya catisma
name: risk-ve-strateji-toplu-is
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Strateji

## Görev
Müvekkilin (sendika veya işveren) toplu süreçteki konumunu risk-fırsat ekseninde tartmak ve uygulanabilir bir strateji önermek. Hukuki doğruluğu ticari/operasyonel gerçeklerle buluşturur.

## Soğuk başlangıç (intake)
- Müvekkil hangi taraf; hedefi nedir (TİS imzası, grevi önleme, maliyet kontrolü)?
- Süreç hangi aşamada (yetki, görüşme, arabuluculuk, grev eşiği)?
- En kötü senaryo (grev, yetki düşmesi, ceza) müvekkil için ne anlama gelir?
- Müzakerede esneklik var mı; kırmızı çizgiler neler?

## Denetim şeması
1. **Yetki riski:** Baraj/çoğunluk tartışmalıysa yetki düşmesi (6356 m.41-44) ile süreç sıfırlanabilir; sendika için kayıt sağlamlaştırma, işveren için itiraz hakkı (m.43) değerlendirilir.
2. **Grev/lokavt riski:** Kanun dışı grev işveren için fesih ve tazminat fırsatı (m.64-67), sendika için ağır risktir; usul kusuru olasılığı baştan ölçülür. İşveren için grev yasağı/erteleme (m.62-63) argümanları haritalanır.
3. **Sendikal tazminat/idari ceza riski:** İşveren için sendikal ayrımcılık (m.25, en az bir yıllık ücret) ve 6356 m.78 idari para cezaları; süreç tasarımı bu riskleri minimize edecek şekilde kurgulanır.
4. **Müzakere kaldıracı:** Sendika açısından grev tehdidi/üye gücü; işveren açısından lokavt, faaliyet sürekliliği planı ve yüksek hakem yolu. Her kaldıracın hukuki sınırı belirtilir.
5. **Ara sonuç:** Senaryolar (anlaşma / arabuluculuk / grev / YHK) olasılık ve maliyetle tartılır; önerilen birincil ve yedek strateji yazılır.

İçtihat eğilimleri için Yargıtay kararları künye `[DOĞRULANMADI]` olarak anılır; uydurma numara verilmez.

## Çıktı modülleri
- Risk matrisi (olasılık × etki).
- Senaryo analizi ve önerilen strateji.
- Kırmızı çizgi / müzakere kaldıracı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

