---
argument-hint: ''
description: İhlali durdurmak veya delilleri korumak için acil koruma tedbiri istenmesi
  gerektiğinde; FSEK m.77 ihtiyati tedbir, toplatma, el koyma ve HMK delil tespiti
  şartlarını ve dilekçesini hazırlamak için ku
name: ihtiyati-tedbir-delil-tespiti
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtiyati Tedbir ve Delil Tespiti

## Görev
Süregelen veya yakın tehlike arz eden ihlale karşı ihtiyati tedbir, toplatma/el koyma ve delil tespiti yollarını değerlendirmek, şartlarını test edip taslağını üretmek.

## Soğuk başlangıç (intake)
- İhlal halen sürüyor mu; gecikme telafisi güç zarar doğurur mu?
- Tedbir konusu nedir (satışın durdurulması, çoğaltma nüshalarına/araçlara el koyma, içeriğin kaldırılması)?
- Delil kaybolma riski var mı (çevrimiçi içerik, geçici ürün)?
- Yaklaşık ispat için hangi belgeler mevcut?

## Denetim şeması
1. Yaklaşık ispat (m.77, HMK m.390/3): Tedbir isteyen, hakkının ve ihlalin/ihlal tehlikesinin varlığını yaklaşık olarak ispatlar. FSEK m.77, esaslı zarar/ani tehlike hâlinde ihtiyati tedbir ve gümrükte/sınırda durdurma dâhil önlemleri öngörür.
2. Tedbir türü: Çoğaltılmış nüshalara, çoğaltmaya yarayan araçlara el koyma/imha veya satışın-yayımın durdurulması; çevrimiçi içerikte erişimin/kullanımın engellenmesi. Ölçülülük gözetilir (HMK m.391); en az müdahaleyle amaca ulaşan tedbir seçilir.
3. Teminat: Kural olarak teminat karşılığı verilir (HMK m.392); haklılığın yüksek olasılığı teminattan muafiyet gerekçesi olabilir.
4. Delil tespiti (HMK m.400-405): İleride ispatın zorlaşacağı hâllerde mevcut durumun (kod, nüsha, ekran görüntüsü, web arşivi) tespiti; bilirkişi ve keşifle desteklenir.
5. Usul ve süre: Dava açılmadan istenen tedbirde, kararın ardından iki hafta içinde esas dava açma yükümlülüğü (HMK m.397/1); aksi hâlde tedbir kalkar. İtiraz yolu (HMK m.394) hatırlanır.
6. Ara sonuç: Uygun tedbir türü, dayanağı, teminat ve süre takvimi belirlenir.

İspat yükü: yaklaşık ispat tedbir isteyene aittir; haksız tedbirden doğan zarardan sorumluluk (HMK m.399) hatırlatılır.

## Çıktı modülleri
- İhtiyati tedbir/delil tespiti dilekçe taslağı (yaklaşık ispat, tedbir türü, teminat).
- Süre takvimi (esas dava açma, itiraz).
- Toplatma/el koyma ve çevrimiçi içerik kaldırma seçenek notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

