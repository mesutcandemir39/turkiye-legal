---
argument-hint: ''
description: İYUK'a uygun vergi dava dilekçesi, cevaba cevap ve istinaf-temyiz dilekçelerinin
  yapısını kurup talep sonucunu asıl-ceza-faiz ekseninde doğru formüle etmek için
  kullanılır.
name: dava-dilekcesi-ve-layihalar
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi Dava Dilekçesi ve Layihalar

## Görev
İYUK biçim ve içerik kurallarına uygun dava dilekçesi ve sonraki layihaları (cevaba cevap, istinaf, temyiz) üretmek; vakıa-hukuki sebep-talep sonucu mimarisini vergi uyuşmazlığına özgü olarak kurmak.

## Soğuk başlangıç (intake)
1. Dava konusu işlem ve tarafları kim (mükellef / vergi dairesi başkanlığı veya defterdarlık)?
2. İşlemin türü, tarihi ve tebliğ tarihi; talep edilen iptal kapsamı (asıl / ceza / faiz)?
3. YD talebi olacak mı; teminat gösterilecek mi?
4. Dayanak deliller neler (ihbarname, inceleme raporu, defterler, ödeme belgeleri)?

## Denetim şeması
1. **Biçim unsurları.** İYUK m.3 — dilekçede tarafların ad-unvan ve adresleri, dava konusu işlem ve tebliğ tarihi, olaylar, hukuki sebepler, talep sonucu ve varsa YD talebi yer alır. İYUK m.5 — her işlem için ayrı dava kuralı ve istisnaları (bağlantı) gözetilir.
2. **Husumet.** Dava, işlemi tesis eden idareye (ilgili Vergi Dairesi Başkanlığı / Defterdarlık) yöneltilir; doğru hasım belirlenir.
3. **Talep sonucu.** Vergi aslı, vergi ziyaı cezası, usulsüzlük cezası ve gecikme faizi/zammı ayrı kalemler halinde, tutar belirtilerek iptal talep edilir; kısmi iptal hedefleniyorsa miktar netleştirilir.
4. **Hukuki sebepler.** Her iptal sebebi ilgili madde ile altlanır (örn. re'sen tarh sebebinin yokluğu — VUK m.30; cezada kat hatası — VUK m.344; zamanaşımı — VUK m.114). İçtihat ilkesel atıfla anılır, künye `[DOĞRULANMADI]` bırakılır.
5. **Süre ve harç.** İYUK m.7/m.58 süresine uygunluk dilekçe başında teyit edilir; harç ve posta gideri ile dilekçe ekleri (tebliğ alındısı, işlem örneği) listelenir. Yer tutucular `[doldurulacak]` biçiminde işaretlenir. Ara sonuç: dilekçenin reddini doğuracak şekil eksiği (İYUK m.15 ret sebepleri) kalmadığı kontrol edilir.
6. **Layiha zinciri.** Cevap dilekçesine karşı ikinci dilekçe (cevaba cevap) ve idarenin ikinci cevabı; istinaf (m.45) ve temyiz (m.46) dilekçelerinde bozma/kaldırma sebepleri ayrı başlıklanır.

## Çıktı modülleri
- Vergi dava dilekçesi tam iskeleti (başlık → vakıa → hukuki sebep → talep sonucu → YD → ekler).
- Talep sonucu kalem tablosu (asıl/ceza/faiz, tutar).
- İstinaf/temyiz dilekçesi şablonu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

