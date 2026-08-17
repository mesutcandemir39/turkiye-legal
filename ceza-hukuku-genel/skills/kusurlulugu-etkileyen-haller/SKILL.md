---
argument-hint: ''
description: Yaş küçüklüğü, akıl hastalığı, haksız tahrik, cebir-tehdit, zorunluluk
  ve hata gibi kusurluluğu etkileyen hâlleri ve sonuçlarını değerlendirmek gerektiğinde
  kullanılır.
name: kusurlulugu-etkileyen-haller
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kusurluluğu Kaldıran ve Azaltan Hâller

## Görev
Tipik ve hukuka aykırı bir fiilde failin kusurunun bulunup bulunmadığını; kusuru kaldıran ya da azaltan hâlleri (TCK m.28-34) ve sonuçlarını saptamak.

## Soğuk başlangıç (intake)
- Failin suç tarihindeki yaşı ve akli durumu nedir?
- Faili harekete geçiren haksız bir fiil/provokasyon var mıydı?
- Cebir, tehdit veya karşı konulamaz tehlike etkisi söz konusu muydu?
- Fail fiilin niteliğinde ya da hukuka uygunluk sebebinin şartlarında yanılmış mıydı?

## Denetim şeması
1. **Yaş küçüklüğü (m.31):** 0-12 yaş ceza sorumluluğu yok; 12-15 yaş için algılama/yönlendirme yeteneği araştırılır ve indirilir; 15-18 yaş için indirim uygulanır.
2. **Akıl hastalığı (m.32):** Algılama veya davranışlarını yönlendirme yeteneğini ortadan kaldıran akıl hastalığında ceza verilmez, güvenlik tedbiri uygulanır (m.57); kısmen azaltan hâlde indirimli ceza.
3. **Sağır ve dilsizlik (m.33), geçici nedenler/alkol-uyuşturucu (m.34):** Yaş gruplarına paralel rejim; iradi alınan alkol/uyuşturucunun etkisi kusuru kaldırmaz.
4. **Cebir, şiddet, tehdit (m.28) ve zorunluluk (m.25/2):** Karşı konulamaz cebir/ağır tehdit altında işlenen fiilde kusur bulunmaz; bu hâlde fiili icbar eden fail sayılır. Ara sonuç: irade tümüyle baskı altında mıydı?
5. **Haksız tahrik (m.29):** Haksız bir fiilin doğurduğu hiddet/şiddetli elem etkisiyle işlenen suçta ceza indirilir; tahrikin haksızlığı ve fiille orantısı denetlenir.
6. **Hata (m.30):** Maddi unsurlarda hata kastı kaldırır; hukuka uygunluk sebebinin maddi şartlarında kaçınılmaz hata kusuru kaldırır; haksızlık yanılgısı kaçınılmazsa ceza verilmez. Ara sonuç: hata kaçınılabilir miydi?

## Çıktı modülleri
- Hâl bazlı sonuç tablosu (cezasızlık / indirim / güvenlik tedbiri).
- Rapor ihtiyacı notu (ATK/sağlık kurulu, sosyal inceleme raporu).
- Tahrik/hata için olay-madde altlaması.
- Strateji ve eksik delil listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

