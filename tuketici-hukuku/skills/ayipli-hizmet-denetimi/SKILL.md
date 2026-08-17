---
argument-hint: ''
description: Bir hizmetin (tamir, kurs, sağlık dışı bakım, taşıma, dijital hizmet
  vb.) gereği gibi ifa edilmemesi halinde tüketicinin seçimlik haklarını ve sürelerini
  değerlendirmek gerektiğinde kullanılır.
name: ayipli-hizmet-denetimi
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ayıplı Hizmet Denetimi

## Görev
Sunulan hizmetin ayıplı olup olmadığını belirlemek, tüketicinin seçimlik haklarını (yeniden görme, indirim, dönme, onarım) altlamak ve hizmet ayıbına özgü ispat ve süre kurallarını uygulayarak çözüm yolunu belirlemek.

## Soğuk başlangıç (intake)
- Hizmet ne ve ne zaman ifa edildi; sözleşmede taahhüt edilen nitelik neydi?
- Eksiklik/kusur nedir; tüketici nasıl bir sonuç bekliyordu?
- Tüketici ne istiyor: hizmetin yeniden görülmesi, indirim, dönme, ek masrafların karşılanması?
- Zarar doğdu mu; hizmetin sonucu telafi edilebilir nitelikte mi?

## Denetim şeması
1. **Ayıplı hizmet (TKHK m.13):** Sözleşmede kararlaştırılan veya objektif olarak sahip olması gereken nitelikleri taşımayan, sağlayıcı tarafından reklam/vaat yoluyla bildirilen özellikleri içermeyen ya da eksik/kötü ifa edilen hizmet ayıplıdır.
2. **İspat (m.15 yollamasıyla m.10 kıyası):** Hizmetin ayıplı ifa edildiğine ilişkin ispatta, ifadan sonra makul sürede ortaya çıkan ayıplar bakımından sağlayıcının özen yükümü ve dosya delilleri (sözleşme, rapor, bilirkişi) tartılır.
3. **Seçimlik haklar (m.15):** Tüketici (a) hizmetin yeniden görülmesi, (b) ayıp oranında bedel indirimi, (c) ücretsiz onarım/eksikliğin giderilmesi, (d) sözleşmeden dönme haklarından birini seçebilir. Sağlayıcı bu talebi makul sürede ve tüketici için ciddi sorun çıkarmadan yerine getirmelidir. Ücretsiz onarım/yeniden görme orantısızsa diğer haklar gündeme gelir.
4. **Tazminat:** Seçimlik hakların yanında ayıbın sebep olduğu diğer zararlar genel hükümlere (TBK) göre talep edilebilir.
5. **Zamanaşımı (m.16):** Kural iki yıl; sağlayıcının ağır kusuru veya hilesi varsa süreyle sınırlı sorumluluktan yararlanamaz.
6. **Ara sonuç:** Talep süre içinde mi, hizmet ayıbı sabit mi, hangi seçimlik hak en uygun?

## Çıktı modülleri
- Hizmet ayıbı nitelendirmesi ve seçimlik hak önerisi.
- İspat ve delil ihtiyaç listesi (rapor, yazışma, ödeme belgesi).
- Sağlayıcıya talep yazısı taslağı.
- Yol haritası (hakem heyeti/mahkeme).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

