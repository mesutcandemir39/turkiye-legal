---
argument-hint: ''
description: Belirli bir modern kuruma (mülkiyet, zilyetlik, sözleşme tipleri, temsil,
  ayni-şahsi hak) ilişkin Roma karşılığını ve dönüşümünü eşleştiren hızlı soykütüğü
  çıkarımı; doktrin notu veya ders materyali h
name: kavram-kokeni-haritasi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Modern Kavramların Roma Soykütüğü

## Görev
Yürürlükteki Türk hukukundaki tekil bir kurumun Roma karşılığını, Latince adıyla ve dönüşüm çizgisiyle eşleştirerek hızlı bir soykütüğü kartı üretmek.

## Soğuk başlangıç (intake)
- Hangi kurum (mülkiyet, zilyetlik, kazandırıcı zamanaşımı, satış, kira, vekâlet, temsil, kefalet)?
- Latince terim ve kaynak fragman gerekli mi?
- Çıktı ders notu mu, mütalaa eki mi, akademik metin mi?

## Denetim şeması
1. Modern kurumu ve madde dayanağını sabitle (ör. mülkiyet TMK m.683; zilyetlik TMK m.973; kazandırıcı zamanaşımı TMK m.712-713; satış TBK m.207; kira TBK m.299; vekâlet TBK m.502; temsil TBK m.40).
2. Roma karşılığını eşleştir ve Latince adını ver:
   - Mülkiyet → dominium / proprietas; ayni dava → rei vindicatio.
   - Zilyetlik → possessio; possessio civilis / naturalis ayrımı.
   - Kazandırıcı zamanaşımı → usucapio (ve longi temporis praescriptio).
   - Satış → emptio venditio (consensu doğan).
   - Kira/hizmet/eser → locatio conductio (rei/operarum/operis).
   - Vekâlet → mandatum; ortaklık → societas.
   - Kefalet → fideiussio; rehin → pignus/hypotheca.
   - Temsil → Roma'da doğrudan temsil ilkesel olarak yoktu; bu farkı vurgula (modern doğrudan temsil sonraki bir gelişmedir).
3. Unsur karşılaştırması yap: Roma kurumunun şartları ile modern maddenin şartlarını yan yana koy; eklenen/çıkarılan unsuru işaretle (ör. usucapio'da iyiniyet ve haklı sebep — TMK m.712 olağan zamanaşımındaki iyiniyet ve tapu kaydı şartlarıyla kıyasla).
4. Maxim bağla (varsa, doğru Latince): nemo plus iuris ad alium transferre potest quam ipse haberet (ayni hak devri sınırı); res perit domino (hasara katlanma); prior tempore potior iure (önceki tarihli hakkın üstünlüğü). Maximin yürürlükteki maddenin yorumuna katkısını yaz, hükmün yerine koyma.
5. Ara sonuç: soykütüğü kartını netleştir; varsa anlam kayması notunu ekle.

İspat/dayanak: modern norm madde ile; Roma kurumu fragman/maxim ile; doktrin [DOĞRULANMADI].

## Çıktı modülleri
- Soykütüğü kartı: modern kurum + madde / Roma adı (Latince) / kaynak / dönüşüm notu.
- Unsur karşılaştırma tablosu.
- İlgili Latince maxim ve doğru çevirisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

