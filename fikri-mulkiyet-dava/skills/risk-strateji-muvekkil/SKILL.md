---
argument-hint: ''
description: Dava açmadan önce ihtarname/cease and desist, tedbir-esas-ceza yol seçimi,
  kazanma şansı ve maliyet değerlendirmesi ile müvekkile sade dilde risk haritası
  ve strateji önerisi sunmak gerektiğinde kulla
name: risk-strateji-muvekkil
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk, Strateji ve Müvekkil İletişimi

## Görev
Uyuşmazlığa girmeden önce hak sahibinin (veya tecavüzle suçlanan tarafın) stratejik konumunu değerlendirmek; ihtar, müzakere, tedbir, dava ve ceza seçenekleri arasında gerekçeli yol önermek ve müvekkile sade dilde aktarmak.

## Soğuk başlangıç (intake)
- Müvekkil hak sahibi mi, tecavüzle suçlanan taraf mı?
- Öncelik hızlı durdurma mı, tazminat mı, ticari ilişkiyi korumak mı?
- Karşı tarafın hükümsüzlük/kullanmama gibi karşı kozları var mı?
- Bütçe, zaman ve kamuoyu/itibar hassasiyeti nedir?

## Denetim şeması
1. Konum tespiti: Hakkın geçerliliği (sicil, kullanım kanıtı), tecavüzün gücü ve karşı tarafın olası savunmaları (kullanmama m.19, hükümsüzlük, önceki hak) birlikte tartılır; zayıf hak üzerine agresif dava tedbir tazminatı riski doğurur.
2. İhtar adımı: Çoğu olayda ihtarname/cease and desist ile durdurma ve müzakere denenir; ihtar, sonraki tedbir talebinde kötüniyeti ve devam eden tecavüzü belgeler. Ancak ihtar, karşı tarafa delil karartma fırsatı verebilir — gizli delil tespiti/tedbir önceliği değerlendirilir.
3. Yol seçimi: (a) sadece hukuk (tedbir+tecavüz+tazminat), (b) ceza eklemek (caydırıcılık, arama), (c) idari yol (hükümsüzlük/iptal için TÜRKPATENT/Ankara FSHM). Maliyet, süre ve kanıt gücü matrisi kurulur.
4. Karşı taraf temsili: Tecavüzle suçlanan müvekkilde önce hakkın geçerliliği ve kullanım kapsamı sorgulanır; hükümsüzlük/kullanmama def'i ile savunma kurgulanır, sulh seçeneği tartılır.
5. Müvekkil iletişimi: Olasılıklar yüzde kesinlik vaadi olmadan; en iyi/orta/kötü senaryo ve tahmini süre-maliyet sade dille sunulur. Karar müvekkilindir; yazılı bilgilendirme alınır.

## Çıktı modülleri
- Risk haritası (hak gücü / tecavüz gücü / karşı koz / senaryo).
- Yol seçimi karşılaştırma tablosu.
- Müvekkile sade dilde strateji notu ve ihtarname taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

