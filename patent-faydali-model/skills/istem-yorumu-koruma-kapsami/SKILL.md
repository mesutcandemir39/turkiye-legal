---
argument-hint: ''
description: Patentin koruma kapsamının ne olduğu, bir ürün/usulün istemlerin içine
  girip girmediği, eşdeğerlerin değerlendirilmesi gerektiğinde kullanılır; tecavüz
  ve hükümsüzlük analizinin teknik çekirdeğidir.
name: istem-yorumu-koruma-kapsami
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İstem Yorumu ve Koruma Kapsamı

## Görev
İstemleri SMK m.89 uyarınca yorumlayarak patentin koruma kapsamını netleştirmek; incelenen ürün/usulün istemlere literal veya eşdeğerler yoluyla girip girmediğini saptamak.

## Soğuk başlangıç (intake)
1. Bağımsız ve bağımlı istemler neler; metin elde mi?
2. İhtilaflı ürün/usulün teknik özellikleri nedir?
3. İnceleme/itiraz sürecinde istemler daraltıldı mı (dosya geçmişi)?
4. Tarifname ve resimler hangi yorumu destekliyor?

## Denetim şeması
1. **Koruma kapsamının kaynağı (SMK m.89/1).** Koruma istemlerle belirlenir; tarifname ve resimler istemlerin yorumunda kullanılır. İstem dışı, yalnızca tarifnamede yer alan özellik kapsam dışıdır.
2. **İstem ayrıştırması.** Bağımsız istemi özellik kümelerine (öğelere) böl. Bağımlı istemler bağımsız isteme ek özellik getirir; tecavüz için kural olarak bağımsız istemin tüm öğeleri karşılanmalı (öğelerin tümü kuralı).
3. **Literal kapsam.** İhtilaflı ürün/usul, bağımsız istemin her bir öğesini birebir taşıyor mu? Bir öğe eksikse literal tecavüz yok.
4. **Eşdeğerler (SMK m.89/5).** İstemde yazılı öğenin yerine, aynı işlevi esas itibarıyla aynı şekilde gören ve aynı sonucu doğuran eşdeğer öğe konulmuşsa kapsam genişler. Eşdeğer değerlendirmesi başvuru/rüçhan tarihindeki uzmana göre yapılır.
5. **Dosya geçmişiyle sınırlama.** İnceleme/itirazda istemden vazgeçilen unsur sonradan eşdeğer yoluyla geri alınamaz (beyan/sınırlama tutarlılığı). Ara sonuç: kapsam içi mi dışı mı?

## Çıktı modülleri
- Bağımsız istem öğe-öğe haritası.
- Literal kapsam karşılaştırma tablosu (öğe / ürün-usul / eşleşti mi).
- Eşdeğer değerlendirme notu.
- Koruma kapsamı sınırı ve dosya geçmişi uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

