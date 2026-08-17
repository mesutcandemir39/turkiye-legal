---
argument-hint: ''
description: Bankacılık uyuşmazlığında doğru mahkemeyi (asliye ticaret, tüketici,
  idare), zorunlu ön şartı (dava şartı arabuluculuk, tüketici hakem heyeti) ve yetkili
  yeri belirlemek, yanlış yol nedeniyle hak kayb
name: bankacilik-dava-gorev-yetki
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Bankacılık Uyuşmazlıklarında Görev, Yetki ve Yargı Yolu

## Görev
Bankacılık uyuşmazlığında görevli mahkemeyi, yetkili yeri, zorunlu ön şartları ve kanun yollarını doğru belirleyerek usul hatasından kaynaklanan hak kayıplarını önlemek.

## Soğuk başlangıç (intake)
- Taraflar: banka-tüketici, banka-tacir, banka-BDDK hangisi?
- Uyuşmazlık konusu ve tutarı nedir; tüketici hakem heyeti sınırı içinde mi?
- Sözleşmede yetki/tahkim şartı var mı; tüketici aleyhine yetki şartı geçerli mi?
- Dava mı, icra takibi mi, idari başvuru mu söz konusu?

## Denetim şeması
1. **Yargı kolu**: BDDK işlemleri ve düzenleyici uyuşmazlıklar idari yargıda (İYUK 2577); banka-müşteri sözleşmesel uyuşmazlıkları adli yargıda görülür.
2. **Görevli mahkeme**: Taraflar arasında ticari iş niteliğindeki uyuşmazlık asliye ticaret mahkemesinde (TTK m.4-5); tüketici işlemlerinde tüketici mahkemesinde, parasal sınır altında tüketici hakem heyetinde (TKHK m.66-70) görülür. Banka işlemleri tacir bakımından mutlak ticari iş sayılır (TTK m.3-4).
3. **Zorunlu ön şartlar**: Ticari davalarda konusu para alacağı/tazminat olan uyuşmazlıklarda TTK m.5/A dava şartı arabuluculuk; tüketici uyuşmazlıklarında 6325 sayılı HUAK m.18/B dava şartı arabuluculuk (parasal sınır üstü) ve tüketici hakem heyeti yolu kontrol edilir. Ön şart yerine getirilmeden açılan dava usulden reddedilir.
4. **Yetki**: Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davada ifa yeri (HMK m.10). Tüketici aleyhine yetki sözleşmesi geçersizdir; tüketici kendi yerleşim yeri mahkemesinde de dava açabilir.
5. **Kanun yolları**: İstinaf ve temyiz sınırları (HMK m.341, m.362) ile tüketici/ticari dava özellikleri kontrol edilir. Ara sonuç olarak görevli mahkeme, yetkili yer, ön şart ve süreleri net yaz.

## Çıktı modülleri
- Görev-yetki-ön şart karar tablosu.
- Yanlış yol riskine karşı uyarı notu.
- Süre ve kanun yolu takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

