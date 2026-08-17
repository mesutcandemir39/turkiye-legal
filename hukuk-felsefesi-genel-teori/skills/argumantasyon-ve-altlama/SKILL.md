---
argument-hint: ''
description: Soyut bir norm ile somut olayı gerekçeli biçimde bağlamak (altlama/subsumption),
  tümdengelimli hukuki kıyas kurmak, argüman türlerini sıralamak ve bir mütalaa/dilekçenin
  mantıksal iskeletini denetleme
name: argumantasyon-ve-altlama
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Hukuki Argümantasyon ve Altlama Tekniği

## Görev
Hukuki kıyas (büyük önerme: norm; küçük önerme: olay; sonuç) ile altlamayı kurallı biçimde
kurmak; argüman türlerini sıralamak ve bir hukuki metnin gerekçe iskeletini denetlemek. Bu
beceri, mütalaa ve dilekçe üretiminin mantıksal omurgasıdır.

## Soğuk başlangıç (intake)
- Uygulanacak norm(lar) net mi; metni ve koşul unsurları çıkarıldı mı?
- Olayın hangi vakıaları sabit, hangileri çekişmeli/ispatı gerekli?
- Talep sonucu ne; hangi norm bu sonucu üretiyor?
- Karşı argüman(lar) tahmin edilebiliyor mu?

## Denetim şeması
1. **Büyük önermeyi kur.** Uygulanacak normun koşul unsurlarını (tatbik şartları) ve hukuki
   sonucunu ayrıştır; belirsiz/yorum gerektiren unsur varsa önce yorum becerisiyle anlamlandır.
   Norm metni ve madde atfı açıkça verilir.
2. **Küçük önermeyi (olayı) çıkar.** Somut vakıaları normun her koşul unsuruna tek tek
   eşle (altlama). Eşlenemeyen unsur varsa o talep çöker; ispatı gereken vakıayı işaretle
   (TMK m.6; HMK m.190 ispat yükü).
3. **Sonucu türet.** Tüm koşullar gerçekleşmişse hukuki sonuç doğar; kısmen gerçekleşmişse
   kısmî sonuç/terditli talep kurulur. Ara sonuç: norm + olay → talep sonucu bağı kanıtlanır.
4. **Argüman türlerini diz.** Lafzî, sistematik, amaçsal, tarihsel argümanlar; kıyas,
   a fortiori, a contrario; otorite argümanı (içtihat/doktrin) ve sonuç argümanı (consequentialist)
   sırasıyla güçlendirilir. Otorite argümanında karar künyesi doğrulanmadıkça [DOĞRULANMADI]
   konur; uydurma künye yasaktır.
5. **Çürütme testi.** Karşı argümanı en güçlü hâliyle kur ve cevapla (steel-man); altlamada
   zayıf halkayı (genellikle çekişmeli vakıa veya belirsiz koşul unsuru) açıkça işaretle.

## Çıktı modülleri
- Kıyas iskeleti (büyük önerme / küçük önerme / sonuç).
- Altlama tablosu (koşul unsuru ↔ vakıa ↔ ispat durumu).
- Argüman sıralaması (güçten zayıfa) ve karşı argümana cevap.
- Zayıf halka / ispat boşluğu uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

