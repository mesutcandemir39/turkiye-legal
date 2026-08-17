---
argument-hint: ''
description: İzinsiz kullanım, taklit, iltibas veya benzer işaretle marka hakkına
  saldırı söz konusuysa; m.29 tecavüz hallerini ve m.149-150 dava taleplerini denetlemek
  için kullanılır.
name: marka-tecavuzu-ve-onleme
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


# Marka Hakkına Tecavüz ve Önleme

## Görev
Tescilli marka hakkına yönelik saldırıyı SMK m.29 (tecavüz sayılan haller) ve m.7 (yasaklama yetkisi) çerçevesinde tespit etmek; m.149-150 kapsamında tecavüzün önlenmesi/durdurulması/kaldırılması ve sonuçlarının giderilmesi taleplerini kurmak.

## Soğuk başlangıç (intake)
- Marka tescilli mi; tecavüz iddiası hangi mal/hizmette?
- Karşı tarafın kullanımı aynı işaret-aynı mal mı, benzer mi (iltibas)?
- Karşı tarafın kendi tescili/önceki hakkı/dürüst kullanım savunması var mı?
- Tecavüz devam ediyor mu (tedbir aciliyeti)?

## Denetim şeması
1. **Hakkın varlığı.** Geçerli ve devam eden marka tescili; kapsamı (mal/hizmet ve işaret) m.7'ye göre belirlenir.
2. **Tecavüz halleri (m.29).** İzinsiz kullanım (m.7 ihlali); markayı taklit; tecavüz yoluyla kullanılan ürünleri satma/dağıtma/ticari amaçla elde bulundurma; izinsiz lisans/devir. Marka sahibinin izninin yokluğu esastır.
3. **İltibas ve karıştırılma.** Aynı işaret-aynı mal doğrudan; benzer işaret-benzer mal hâlinde karıştırılma ihtimali (m.7/2) aranır.
4. **Savunmalar.** Karşı tarafın geçerli tescili (tescilli markanın kullanımı tek başına savunma değildir; hükümsüzlük gündeme gelir), dürüst kullanım (m.7/5), hakkın tüketilmesi (m.152), önceye dayalı hak.
5. **Talepler (m.149).** Tecavüzün tespiti, men'i (önlenmesi), ref'i (giderilmesi), ürünlere el konulması/imhası, üretim araçlarına el konulması, kararın ilanı; ayrıca tazminat (ayrı şema).
6. **İhtiyati tedbir (m.159).** Tecavüzün durdurulması/önlenmesi için yargılama öncesi/sırasında tedbir; teminat ve aciliyet değerlendirilir.

## Çıktı modülleri
- Tecavüz hali-madde eşleştirmesi ve delil listesi.
- Talepler kataloğu (tespit/men/ref/imha/ilan).
- İhtiyati tedbir gerekçe taslağı; ihtarname iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

