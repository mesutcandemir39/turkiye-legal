---
argument-hint: ''
description: İlk derece kararına karşı bölge idare mahkemesine istinaf veya Danıştay'a
  temyiz başvurusunun, parasal sınırların ve kesinlik kurallarının değerlendirilmesinde
  kullanılır; hangi karara hangi kanun yol
name: istinaf-temyiz-kanun-yollari
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İstinaf ve Temyiz Kanun Yolları

## Görev
İlk derece idari/vergi mahkemesi kararına karşı doğru kanun yolunu (istinaf/temyiz), süreyi ve kesinlik durumunu belirleyip başvuruyu kurgulamak.

## Soğuk başlangıç (intake)
- Karar idare/vergi mahkemesinin mi, BİM'in mi; ilk derece Danıştay mı?
- Uyuşmazlığın parasal değeri kesinlik/temyiz sınırının neresinde?
- Karar lehe mi aleyhe mi; hangi kısmı temyiz/istinaf edilecek?
- Kararın tebliğ tarihi nedir?

## Denetim şeması
1. **İstinaf** (İYUK m.45): İdare ve vergi mahkemelerinin nihai kararlarına karşı, kararın tebliğini izleyen günden itibaren **30 gün** içinde bölge idare mahkemesine (BİM) istinaf yolu açıktır. Konusu belirli bir parasal sınırın (yıllık yeniden değerleme ile güncellenen tutar — **[DOĞRULANMADI]**) altında kalan davalardaki kararlar kesindir, istinafa kapalıdır.
2. **İstinaf incelemesi**: BİM hem maddi olay hem hukuk yönünden inceleme yapar; gerekirse tahkikat yenileyip işin esası hakkında karar verir. BİM kararlarının bir kısmı kesindir.
3. **Temyiz** (İYUK m.46): BİM'in m.46'da sayılan kararlarına ve ilk derece olarak Danıştay'ca verilen kararlara karşı, tebliği izleyen günden itibaren **30 gün** içinde Danıştay'a temyiz yolu açıktır. Temyiz parasal sınırı yıllık güncellenir (**[DOĞRULANMADI]**).
4. **Temyiz sebepleri** (İYUK m.49): Görev-yetki dışında bir işe bakılması, hukuka aykırı karar verilmesi, usul hükümlerine uyulmaması gibi sebepler. Temyiz yalnızca hukukilik denetimidir; Danıştay maddi vakıa tahkikatı yapmaz, bozar veya onar.
5. **Kanun yararına temyiz**: Kesinleşmiş kararlar için Danıştay Başsavcısı tarafından (İYUK ilgili hükmü) sınırlı denetim; hüküm sonucu etkilenmez.
6. **Ara sonuç — yürütme**: İstinaf/temyiz başvurusu kural olarak kararın yürütmesini kendiliğinden durdurmaz; gerektiğinde YD talep edilir (İYUK m.52). Kararın düzeltilmesi yolu kaldırılmıştır.

## Çıktı modülleri
- Açık kanun yolu, süre ve mahkeme tespiti
- Parasal sınır/kesinlik değerlendirmesi ([DOĞRULANMADI] güncel tutar uyarısı)
- İstinaf/temyiz dilekçesi sebep iskeleti



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

