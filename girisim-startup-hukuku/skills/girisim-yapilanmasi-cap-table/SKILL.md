---
argument-hint: ''
description: Bir girişimin şirket tipini (AŞ tercihi), ortaklık yapısını, pay defteri
  ve cap table mantığını, hangi yatırım aşamasında olduğunu ve uygulanacak çerçeveyi
  ayırt etmek için kullanılır; sonraki tüm yat
name: girisim-yapilanmasi-cap-table
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Girişim Yapılanması ve Cap Table Temeli

## Görev
Girişimi doğru şirket tipi, doğru ortaklık yapısı ve okunabilir bir cap table üzerine oturtmak; yatırım aşamasını teşhis edip hangi alt-beceriye geçileceğini belirlemek.

## Soğuk başlangıç (intake)
1. Şirket tipi nedir (AŞ / Ltd. / henüz kurulmadı) ve neden?
2. Hangi aşamadasınız: kuruluş, pre-seed, seed, Seri A+ veya çıkış?
3. Mevcut pay dağılımı, kurucu sayısı ve varsa opsiyon havuzu nedir?
4. Kim temsil ediliyor: girişimci/kurucular mı, yatırımcı mı?
5. Yurtdışı holding (ör. flip) düşünülüyor mu; yoksa tamamen Türkiye mi?

## Denetim şeması
1. Tip tercihi: Yatırım alacak girişim kural olarak AŞ (TTK m.329 vd.) olmalı; imtiyazlı pay (m.478-479), kayıtlı sermaye (m.460) ve ESOP esnekliği AŞ'de mümkün. Ltd. ise tür değiştirme TTK m.180-190 ile AŞ'ye dönüştürülür.
2. Kuruluş/sermaye: Asgari ve kayıtlı sermaye TTK m.332 — güncel tutarı olay tarihinden teyit et; tek ortakla AŞ kurulabilir (m.338).
3. Cap table mantığı: Pay defteri (TTK m.499) gerçeği; cap table yönetsel araç. Tam sulandırılmış (fully diluted) tabloda mevcut paylar + tahsis edilmiş/edilmemiş opsiyon havuzu + dönüştürülebilir enstrümanların (SAFE/nota) dönüşüm etkisi gösterilir.
4. Rüçhan ve sulandırma: Her bedelli artırımda rüçhan hakkı m.461; yatırımcı girişi için bu hak yönetilir (mevcut ortakların oran kaybı = sulandırma).
5. Aşama tayini ve yönlendirme: term sheet → enstrüman (SAFE/nota/equity) → SHA/esas sözleşme → ESOP → çıkış. İlgili alt-beceriye geç.
6. İspat/şekil: Pay sahipliği şirkete karşı pay defteri kaydıyla; devir geçerliliği m.490 şekline tabi.

## Çıktı modülleri
- Aşama ve tip teşhis tablosu (madde atıflı).
- Mevcut ve tam sulandırılmış cap table iskeleti (yer tutuculu).
- Hangi alt-beceriye geçileceğini gösteren yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

