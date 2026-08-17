---
argument-hint: ''
description: Bir edim ileride doğacak bir sebep için verildiği halde o sebep gerçekleşmediğinde
  veya başlangıçta var olan sebep sonradan ortadan kalktığında iadeyi belirlemek gerektiğinde
  kullanılır.
name: gerceklesmeyen-ve-sona-eren-sebep
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gerçekleşmeyen ve Sona Eren Sebep

## Görev
TBK m.77/2'nin diğer iki tipini denetlemek: gerçekleşmeyen sebep (condictio ob causam futuram) ve sona eren sebep (condictio ob causam finitam). Tipik örnekler: gerçekleşmeyen evlenme/sözleşme beklentisiyle yapılan kazandırmalar, geçersiz hale gelen veya bozulan ilişkide kalan edimler, dönmeyle (TBK m.125) tasfiye edilen edimler.

## Soğuk başlangıç (intake)
- Edim hangi ileriki sebep/amaç için verildi; o sebep gerçekleşti mi?
- Başlangıçta geçerli bir sebep var mıydı; sonradan hangi olayla ortadan kalktı?
- Sözleşmeden dönme, bozucu şart, fesih gibi bir tasfiye sebebi var mı?
- Karşı taraf edimi aldıktan sonra elden çıkardı mı; iyiniyetli mi?

## Denetim şeması
1. **Gerçekleşmeyen sebep.** Edim, ileride doğması beklenen bir sebep/amaç için verilmiş ama o amaç kesin olarak gerçekleşmemişse iade gerekir (m.77/2). Karşı tarafın amacın gerçekleşmesini bilerek engellemesi de iadeyi haklı kılar.
2. **Sona eren sebep.** Kazandırma anında geçerli olan sebep sonradan ortadan kalkarsa (bozucu şartın gerçekleşmesi, sözleşmenin geçmişe etkili sona ermesi), o ana kadarki edim sebepsiz hale gelir.
3. **Dönme ile yarışma/ayrım.** Sözleşmeden dönmede (TBK m.125/2) verilen edimlerin iadesi kural olarak dönmenin kendi tasfiye rejimine tâbidir; sebepsiz zenginleşme tamamlayıcı rol oynar. Hangi rejimin uygulanacağı önce belirlenir.
4. **İade kapsamı (m.79).** İyiniyetli zenginleşen yalnızca elinde kalan zenginleşme ölçüsünde; kötüniyetli olan veya iadeyi göze almalıydıysa tam iade ile sorumlu. Semere ve kullanım yararı iyiniyete göre eklenir.
5. **İspat.** Sebebin gerçekleşmediğini/sona erdiğini iade isteyen ispatlar; karşı taraf sebebin gerçekleştiğini veya kazandırmanın bağışlama amaçlı olduğunu ileri sürerse onu ispatlar.
6. **Ara sonuç.** Tip + iade kapsamı + faiz/semere başlangıcı + zamanaşımı (m.82, öğrenmeden 2 yıl) haritası çıkar.

## Çıktı modülleri
- Tip teşhisi ve tasfiye rejimi seçim notu (dönme mi, m.77 mi).
- İade kapsamı tablosu (iyiniyet ayrımıyla).
- İade talebi dava iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

