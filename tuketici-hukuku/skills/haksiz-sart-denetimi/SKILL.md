---
argument-hint: ''
description: Standart/matbu tüketici sözleşmelerinde müzakere edilmemiş, dengesizlik
  yaratan haksız şartları tespit etmek ve geçersizliğini ileri sürmek gerektiğinde;
  banka, abonelik, sigorta, üyelik sözleşmeleri
name: haksiz-sart-denetimi
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


# Haksız Şart Denetimi

## Görev
Tüketici sözleşmesindeki tek tek şartları haksız şart denetiminden geçirmek; müzakere edilmemiş, dürüstlük kuralına aykırı ve tüketici aleyhine dengesizlik yaratan şartların kesin hükümsüzlüğünü (yazılmamış sayılma) ortaya koymak ve sözleşmenin kalan kısmının akıbetini değerlendirmek.

## Soğuk başlangıç (intake)
- Sözleşme matbu/standart mı, şartlar tüketiciyle ayrı ayrı görüşüldü mü?
- İtiraz edilen şart hangisi (ücret, masraf, cezai şart, tek taraflı değişiklik, yetki)?
- Şart tüketici aleyhine nasıl bir dengesizlik yaratıyor?
- Şarta dayanılarak tüketiciden bir bedel tahsil edildi mi?

## Denetim şeması
1. **Kapsam (TKHK m.5/1):** Tüketiciyle müzakere edilmeden sözleşmeye konan, tarafların hak ve yükümlülüklerinde dürüstlük kuralına aykırı biçimde tüketici aleyhine dengesizliğe yol açan şart haksız şarttır.
2. **Müzakere edilmemiş olma karinesi (m.5/3):** Bir şartın önceden hazırlanması ve tüketicinin içeriğine etki edememesi (özellikle standart sözleşme) halinde, o şart müzakere edilmemiş sayılır; aksini, yani şartın ayrıca görüşüldüğünü ispat satıcı/sağlayıcıya düşer.
3. **Yaptırım (m.5/2):** Haksız şart kesin olarak hükümsüzdür; tüketici yönünden yazılmamış (bağlamayan) sayılır. Sözleşme, haksız şart olmadan da varlığını sürdürebiliyorsa diğer hükümlerle ayakta kalır (m.5/4).
4. **Şeffaflık ve yorum:** Şart açık ve anlaşılır olmalıdır; tereddüt halinde tüketici lehine yorumlanır (m.5/5 ve TBK m.23 ilkesi).
5. **İçerik denetimi örnekleri:** Tek taraflı ücret/faiz değiştirme yetkisi, orantısız cezai şart, ispat yükünü tüketiciye yükleyen kayıt, fahiş gecikme faizi, tüketiciyi belirli yetkili mahkemeye zorlayan kayıt tipik haksız şart adaylarıdır; her biri somut dengesizlik testinden geçirilir.
6. **Ara sonuç:** İtiraz edilen şart haksız mı, hangi ödemenin iadesi gündeme gelir, sözleşmenin kalanı ayakta kalır mı?

## Çıktı modülleri
- Şart şart haksızlık değerlendirme tablosu.
- İade edilecek bedel/masraf hesabı.
- Hükümsüzlük ve istirdat talebi argümanları.
- Sözleşmenin geçerli kalan kısmına ilişkin değerlendirme.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

