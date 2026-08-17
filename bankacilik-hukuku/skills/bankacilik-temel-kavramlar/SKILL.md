---
argument-hint: ''
description: Bankacılık uyuşmazlığının kamusal düzenleme katmanı mı yoksa banka-müşteri
  özel hukuk ilişkisi mi olduğunu ayırmak, uygulanacak kanunu (5411, TBK, TKHK, TTK)
  ve mahkeme/merci yolunu doğru seçmek gerek
name: bankacilik-temel-kavramlar
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


# Bankacılık Hukuku Temel Kavramlar ve Sistematik

## Görev
Önündeki bankacılık sorununun hangi hukuki katmana ve ilişki tipine ait olduğunu belirlemek, uygulanacak normu ve doğru merci/yargı yolunu sabitlemek. Bu, sonraki tüm denetimin altyapısıdır.

## Soğuk başlangıç (intake)
- Müvekkil hangi sıfatta: banka, kredi müşterisi, kefil, mevduat sahibi, kart hamili, tüketici mi?
- İlişki tipi nedir: kredi, mevduat/katılım fonu, teminat (kefalet/ipotek/rehin), havale/EFT, kiralık kasa, banka/kredi kartı?
- Müşteri tüketici mi (gerçek kişi, ticari/mesleki amaç dışı) yoksa ticari işletme mi? Bu, TKHK ile TTK rejimi arasında seçimi belirler.
- Sorun bir BDDK işlemi/yaptırımı mı (idari yargı), yoksa sözleşmesel/icrai uyuşmazlık mı (adli yargı)?

## Denetim şeması
1. **Katman ayrımı**: Düzenleyici-denetleyici sorun mu? Bankanın kuruluşu, faaliyet izni, sermaye yeterliliği, kredi sınırları (5411 m.48-54), banka sırrı yükümlülüğü (5411 m.73), TMSF/mevduat sigortası (5411 m.63) ve BDDK idari yaptırımları (5411 m.146 vd.) düzenleyici katmandır; bunlara karşı yol İYUK (2577) gereği idari yargıdır. Banka-müşteri sözleşmesi ise özel hukuk katmanıdır.
2. **İlişki tipini normla eşle**: Mevduat → TBK karz/usulsüz tevdi hükümleri ve 5411 m.60 fon kabul tekeli; kredi → genel kredi sözleşmesi (TBK genel hükümler) veya tüketici kredisi (TKHK m.22 vd.); teminat → kefalet (TBK m.581 vd.), ipotek/rehin (TMK/İİK); kart → 5464; çek → 5941 ve TTK.
3. **Tüketici/ticari süzgeci**: Karşı taraf tüketici ise TKHK m.5 haksız şart denetimi ve m.22 vd. emredici hükümleri devreye girer; uyuşmazlık tüketici hakem heyeti/tüketici mahkemesine gider. Ticari ise asliye ticaret mahkemesi görevli olup 7155 (TTK m.5/A) uyarınca dava şartı arabuluculuk uygulanır.
4. **Ara sonuç**: Uygulanacak kanun, görevli mahkeme/merci, zorunlu ön şart (arabuluculuk/hakem heyeti) ve ispat yükünün kimde olduğunu yaz. İspat yükü kural olarak iddia edene (TMK m.6, HMK m.190) aittir; banka kayıtlarının ibrazı bankadan istenir.
5. **İstisna kontrolü**: Karma sözleşmeler (örn. tüketici kefaleti) ve hem idari hem adli boyutu olan dosyalarda her iki yolu ayrı değerlendir.

## Çıktı modülleri
- İlişki-tipi ve uygulanacak-norm haritası (tablo).
- Görev-yetki ve zorunlu ön şart tespiti.
- Sonraki adım için doğru uzman beceriye yönlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

