---
argument-hint: ''
description: Dava ve ceza zamanaşımı sürelerini, şikâyete bağlı suçlarda süre ve usulü,
  önödeme ve uzlaştırmayı hesaplamak ve dava engellerini denetlemek gerektiğinde kullanılır.
name: zamanasimi-sikayet-dava-engelleri
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Zamanaşımı, Şikâyet ve Dava Engelleri

## Görev
Bir ceza dosyasında dava açma/yürütme engellerini denetlemek: dava ve ceza zamanaşımı, şikâyet süresi, önödeme ve uzlaştırma kurumlarını hesaplamak.

## Soğuk başlangıç (intake)
- Suçun yasal cezasının üst sınırı nedir (zamanaşımı buna göre belirlenir)?
- Suç tarihi ve varsa son kesen işlem tarihi nedir?
- Suç şikâyete bağlı mı; mağdur faili ve fiili ne zaman öğrendi?
- Suç önödeme veya uzlaştırma kapsamında mı?

## Denetim şeması
1. **Dava zamanaşımı süreleri (m.66):** Cezanın üst sınırına göre kademeli süreler (örn. 5 yıldan az hapiste 8 yıl, 5-20 yıl arası fiillerde artan süreler); süre suçun işlendiği günden işler (m.66/6). Çocuklarda süreler indirilir.
2. **Kesen ve durduran nedenler (m.67):** İfade alma, tutuklama, iddianame, mahkûmiyet kararı gibi işlemler süreyi keser; kesilmeyle yeniden başlar fakat uzatılmış süreyi (yarısından fazla) geçemez. Ara sonuç: en son hangi işlem kesti?
3. **Ceza zamanaşımı (m.68-69):** Kesinleşmiş cezanın infaz edilememesi süreleri; ceza türü ve miktarına göre.
4. **Şikâyet (m.73):** Şikâyete bağlı suçlarda mağdur fiili ve faili öğrenmesinden itibaren altı ay içinde şikâyet etmelidir; süre geçerse kovuşturma yapılamaz. Şikâyetten vazgeçme davayı/cezayı düşürür.
5. **Önödeme (m.75):** Yalnızca adli para cezası veya üst sınırı belirli hapsi gerektiren suçlarda; belirlenen miktarın ödenmesiyle kamu davası açılmaz/düşer.
6. **Uzlaştırma (CMK m.253):** Kapsamdaki suçlarda uzlaştırma zorunlu ön koşuldur; uzlaşma kovuşturmaya yer olmadığına ya da düşmeye yol açar. Ara sonuç: dosya uzlaştırma kapsamında mı?

## Çıktı modülleri
- Zamanaşımı hesap tablosu (başlangıç, kesen işlemler, son tarih).
- Şikâyet süresi ve usul kontrolü.
- Önödeme/uzlaştırma uygunluk notu.
- Dava engeli sonucu ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

