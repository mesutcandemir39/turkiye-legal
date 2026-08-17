---
argument-hint: ''
description: Rapor içi çelişkileri, dosyadaki diğer deliller veya önceki raporlarla
  çelişkileri ve sorulduğu hâlde yanıtsız kalan hususları sistematik biçimde ortaya
  çıkarmak istendiğinde kullanılır.
name: celiski-eksiklik-tespiti
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Çelişki ve Eksiklik Tespiti

## Görev
Raporu hem kendi içinde hem dosyanın bütünüyle karşılaştırarak tutarsızlık ve boşlukları çıkarmak; bunları ek rapor veya yeni heyet talebine gerekçe yapmak.

## Soğuk başlangıç (intake)
- Dosyada birden fazla bilirkişi raporu/uzman mütalaası var mı?
- Rapor, kendi içinde farklı yerlerde farklı sayı/sonuç veriyor mu?
- Tanık beyanı, keşif tutanağı, belge gibi delillerle rapor çelişiyor mu?
- Hangi soru fiilen yanıtsız kalmış?

## Denetim şeması
1. **Rapor içi çelişki:** Gövde, tablo ve sonuç bölümleri arasındaki sayısal/mantıksal tutarsızlıklar işaretlenir. Aynı kalemin farklı yerlerde farklı çıkması denetlenebilirliği bozar (HMK m.279).
2. **Dosya delilleriyle çelişki:** Rapordaki kabuller; belge, tanık, keşif tutanağı ve kayıtlarla karşılaştırılır. Delille çelişen kabul, sonucu sakatlar; çelişki dosya sayfasıyla çıpalanır.
3. **Raporlar arası çelişki:** Birden fazla rapor varsa hangi noktada ayrıştıkları ve hangisinin dayanağının güçlü olduğu gösterilir; hâkim raporları serbestçe takdir eder (HMK m.282), bu yüzden çelişkinin giderilmesi istenir.
4. **Eksik yanıt:** Görevlendirme sorularından yanıtsız kalanlar listelenir (HMK m.273 ile bağ).
5. **Ara sonuç:** Giderilebilir çelişki/eksik → **ek rapor**; raporlar arası esaslı ve giderilemeyen çelişki → **yeni/üçüncü heyet** talebi (HMK m.281). Her çelişki "rapordaki ifade vs. çelişen kaynak" biçiminde karşılıklı sunulur.

## Çıktı modülleri
- Çelişki matrisi (rapordaki ifade / çelişen kaynak / sayfa / etki).
- Yanıtsız kalan görevlendirme sorularının listesi.
- Raporlar arası ayrışma haritası.
- Çelişki temelli itiraz ve talep paragrafı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

