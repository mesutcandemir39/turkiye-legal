---
argument-hint: ''
description: Sağlıkta klinik karar destek, bankacılıkta kredi skorlama, istihdamda
  işe alım eleme, sigortada fiyatlama veya kamuda otomatik işlem gibi yüksek etkili
  yapay zekâ kullanımlarında sektörel mevzuat ile
name: sektorel-yz-uygulama
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sektörel Yüksek Riskli Yapay Zekâ Uygulamaları

## Görev
Bireyin haklarını doğrudan etkileyen sektörel YZ kullanımlarında uygulanacak özel mevzuatı KVKK ile birlikte değerlendirip uyum ve sorumluluk şemasını çıkarmak.

## Soğuk başlangıç (intake)
1. Hangi sektör: sağlık, bankacılık/kredi, istihdam, sigorta, kamu idaresi, sermaye piyasası?
2. YZ kararı bireyi nasıl etkiliyor (kredi reddi, işe alım eleme, tanı önerisi, prim)?
3. Sektörel düzenleyici (BDDK, SGK, TİTCK, SPK, ilgili idare) onay/kayıt gerektiriyor mu?
4. Nihai kararı insan mı veriyor, sistem mi?

## Denetim şeması
1. **Sektör normu tespiti**: Sağlıkta hekimin özen ve aydınlatılmış onam yükümlülüğü (1219/3359, TBK vekâlet), klinik karar destek hekimin sorumluluğunu kaldırmaz; bankacılık/kredide 5411 ve düzenlemeleri; istihdamda 4857 ve eşit davranma; sigortada 5684/TTK; kamuda 2577 İYUK ve gerekçeli işlem. Ara sonuç: baskın sektörel norm.
2. **KVKK katmanı**: Her halde m.4-6 işleme şartı, m.10 aydınlatma ve m.11/1-g otomatik karar itirazı uygulanır; sağlık/biyometrik veride m.6 özel nitelikli rejim.
3. **İnsan denetimi**: Tanı, kredi reddi ve işe alım eleme gibi kararlarda anlamlı insan gözetimi hem sorumluluk hem KVKK açısından kritiktir; biçimsel onay yetmez.
4. **Ayrımcılık riski**: Modelin korunan özellikler üzerinden dolaylı ayrımcılık üretmesi eşitlik ilkesi ve m.4 doğruluk/hukuka uygunluk ihlali doğurabilir; istihdamda 4857 ayrımcılık tazminatı.
5. **Sorumluluk**: Hatalı sektörel kararda sektörel sorumluluk (ör. hekim/banka) ile YZ sağlayıcı sorumluluğu (bkz. sorumluluk becerisi) birlikte değerlendirilir.

İçtihat için karararama.yargitay.gov.tr ve karararama.danistay.gov.tr; künye [DOĞRULANMADI].

## Çıktı modülleri
- Sektör + KVKK çifte uyum tablosu.
- İnsan gözetimi ve ayrımcılık riski değerlendirmesi.
- Sektörel onay/kayıt yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

