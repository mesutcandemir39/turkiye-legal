---
argument-hint: ''
description: İmar dosyasında dava açmadan önce kazanım şansı, idari çözüm, maliyet
  ve geri dönülemez risklerin tartılması; müvekkile sade dilde durum, seçenek ve beklenti
  yönetimi sunulması gerektiğinde kullanılır
name: risk-strateji-ve-muvekkil-iletisimi
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Haritası, Strateji ve Müvekkil İletişimi

## Görev
İmar uyuşmazlığında hukuki yolların kazanım olasılığını, maliyetini ve riskini tartmak; müvekkile anlaşılır bir strateji ve beklenti çerçevesi sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin asıl amacı ne (yapıyı korumak, tazminat, inşaata devam, süre kazanmak)?
- Geri dönülemez bir adım var mı (yıkım yakın mı, inşaat ilerliyor mu)?
- İdari çözüm/uzlaşma (ruhsata bağlama, aykırılığı giderme, YKB) mümkün mü?
- Maliyet, süre ve itibar açısından kısıtlar neler?

## Denetim şeması
1. **Hedef ve seçenek ayrımı**: Müvekkilin gerçek menfaati ile hukuki araç eşleştirilir: iptal davası, tam yargı (tazminat), idari başvuru/uzlaşma, aykırılığı giderme, Yapı Kayıt Belgesi değerlendirmesi. Her seçeneğin sonucu ayrı yazılır.
2. **Kazanım olasılığı**: İşlemin unsur sakatlığı (yetki-şekil-sebep-konu-maksat), üst plana/yönetmeliğe aykırılık ve içtihat eğilimi tartılarak güçlü/zayıf/belirsiz olarak derecelendirilir; belirsizlik açıkça belirtilir, garanti verilmez.
3. **Geri dönülemez risk**: Yıkım, satış, inşaatın ilerlemesi gibi telafisi imkânsız sonuçlar varsa, **yürütmenin durdurulması (İYUK m.27)** ve ivedi başvuru önceliklendirilir; zamanlama riski en kritik kalemdir.
4. **Maliyet-fayda**: Harç, bilirkişi-keşif gideri, vekâlet ücreti, süre (idari yargıda istinaf/temyiz dahil yıllar) ile beklenen kazanım karşılaştırılır; uzlaşma/idari çözüm maliyet avantajıyla sunulur.
5. **Müvekkil iletişimi (sade dil)**: Teknik kavramlar (emsal, DOP, mühürleme, YD) yalın anlatılır; "kesin kazanırız" yerine olasılık, süre ve maliyet dürüstçe aktarılır; kararı müvekkilin vermesi sağlanır.
6. **Ara sonuç**: Önerilen yol, gerekçesi, alternatifleri, ilk 30 günde atılacak adımlar ve süre uyarıları tek sayfalık karar notuna bağlanır.

## Çıktı modülleri
- Risk haritası (seçenek × olasılık × maliyet × süre).
- Geri dönülemez risk ve ivedilik uyarısı.
- Müvekkile sade dilde durum/strateji notu.
- İlk adımlar ve süre takvimi (eylem planı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

