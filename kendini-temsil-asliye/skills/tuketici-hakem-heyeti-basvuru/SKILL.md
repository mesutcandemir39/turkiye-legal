---
argument-hint: ''
description: Tüketici sıfatıyla mal veya hizmet uyuşmazlığı yaşayan kişi ayıplı ürün,
  iade, abonelik, haksız şart veya cayma gibi konularda parasal sınır altı uyuşmazlık
  için hakem heyetine başvuracağında kullanıl
name: tuketici-hakem-heyeti-basvuru
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tüketici Hakem Heyeti Başvurusu

## Görev
Tüketici işleminden doğan, parasal sınır altındaki uyuşmazlık için tüketici hakem heyetine eksiksiz ve kabul edilebilir bir başvuru hazırlamak.

## Soğuk başlangıç (intake)
- Mal/hizmeti ticari amaç dışında, kişisel ihtiyaç için mi aldınız (tüketici sıfatı)?
- Satıcı/sağlayıcı kim, işlem tarihi ve tutarı nedir?
- Sorun ne (ayıp, iade reddi, haksız şart, abonelik, fazla tahsilat)?
- Satıcıya yazılı başvuru/şikâyet yaptınız mı, yanıt geldi mi?
- Elinizde fatura, sözleşme, mesaj/e-posta var mı?

## Denetim şeması
1. **Tüketici işlemi mi (6502 sayılı TKHK m.3):** Bir tarafın tüketici, diğerinin satıcı/sağlayıcı olduğu işlem olmalı. Ticari amaçlı alımlar tüketici korumasının dışındadır.
2. **Parasal sınır ve görev:** Sınır altı uyuşmazlıkta tüketici hakem heyetine başvuru **zorunludur**; sınır üstünde tüketici mahkemesi görevlidir. Güncel parasal sınır her yıl Ticaret Bakanlığı tebliğiyle güncellenir — **[DOĞRULANMADI]**, ezbere yazılmaz.
3. **Yetkili heyet:** Tüketicinin veya satıcının yerleşim yerindeki il/ilçe tüketici hakem heyeti. Tüketici kendi yerleşim yeri heyetine başvurabilir.
4. **Esas hak — örnek:** Ayıplı malda tüketicinin seçimlik hakları (6502 sayılı Kanun m.11): değişim, ücretsiz onarım, bedel indirimi, sözleşmeden dönme. Ayıp ihbarı ve zamanaşımı süreleri (kural olarak iki yıl, m.12) kontrol edilir.
5. **İspat:** Fatura, sözleşme, ayıbı gösteren fotoğraf/rapor, yazışmalar başvuruya eklenir. İspat yükü kural olarak iddia edende; ayıbın teslim anında varlığı karinesi tüketici lehinedir.
6. **Ara sonuç:** Sıfat + sınır altı + yetkili heyet + delil tamamsa başvuru yapılır. Heyet kararına karşı tüketici mahkemesinde itiraz süresi işler (karar tebliğinden itibaren 15 gün — **[DOĞRULANMADI]**).

## Çıktı modülleri
- Hakem heyeti başvuru dilekçesi taslağı ([doldurulacak] yer tutucularıyla).
- Delil/ek belge listesi.
- Karara itiraz yolu ve süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

