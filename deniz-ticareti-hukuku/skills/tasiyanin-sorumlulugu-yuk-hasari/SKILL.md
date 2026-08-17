---
argument-hint: ''
description: Taşınan yükün ziyaa uğraması, hasar görmesi veya gecikmesi nedeniyle
  taşıyana karşı talep ya da savunma hazırlanırken; sorumluluğun şartlarını, kurtuluş
  hallerini, sorumluluk sınırını ve ihbar yükümlü
name: tasiyanin-sorumlulugu-yuk-hasari
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
  version: 0.1.0
user-invocable: true
---


# Taşıyanın Sorumluluğu ve Yük Ziya/Hasarı

## Görev
Yükün ziya, hasar veya gecikmesinden doğan zararda taşıyanın sorumlu tutulup tutulamayacağını belirlemek; kurtuluş hallerini ve sorumluluk sınırını uygulamak; ihbar ve protesto sürelerinin korunup korunmadığını denetlemek.

## Soğuk başlangıç (intake)
- Yük tamamen mi kayıp, kısmen mi hasarlı, yoksa gecikmeli mi teslim edildi?
- Hasar yükleme öncesi, taşıma sırasında mı yoksa boşaltma sonrası mı gerçekleşti?
- Teslimde sörvey/ekspertiz yapıldı mı; ziya-hasar ihbarı süresinde yapıldı mı?
- Yükün cinsi, koli/birim sayısı ve brüt ağırlığı (sorumluluk sınırı hesabı için)?

## Denetim şeması
1. **Sorumluluğun temeli**: Taşıyan, yükü teslim aldığı andan teslim edinceye kadar ziya ve hasardan kural olarak sorumludur (TTK m.1178 vd.); kusur karinesine dayanan bir sorumluluktur.
2. **Denize elverişlilik**: Zararın gemi denize/yola/yüke elverişsizliğinden doğduğu iddiasında taşıyanın gereken özeni gösterdiğini ispatı (TTK m.1141, m.1180); özen gösterilmemişse kurtuluş yoktur.
3. **Kurtuluş halleri (istisnalar)**: Teknik kusur/yangın gibi kanunda sayılan sorumluluktan kurtuluş sebeplerini (TTK m.1180-1182 çerçevesinde) ve bunların ispat yükünü değerlendir; navlun sözleşmesindeki sorumsuzluk kayıtlarının emredici sınırlar karşısında geçerliliğini denetle.
4. **Sorumluluk sınırı**: Tazminat, koli/birim başına veya kilogram başına hesaplanan tutarla sınırlıdır (TTK m.1186 — Lahey-Visby esaslı SDR sınırı); konteyner içeriğinin konişmentoda dökümüne göre birim sayısının nasıl belirleneceğini hesapla. Taşıyanın kasdı/pervasızlığı sınırı kaldırır.
5. **İhbar ve ara sonuç**: Açık hasarda teslim anında, gizli hasarda kanunda öngörülen süre içinde ihbar yapılmazsa karine taşıyan lehine işler. Eşyaya ilişkin taleplerde **bir yıllık** zamanaşımını (TTK m.1188) hesapla. Çıktıda sorumluluk-kurtuluş-sınır zincirini sıralı sonuçla.

## Çıktı modülleri
- Sorumluluk/kurtuluş değerlendirme tablosu
- Sorumluluk sınırı hesap taslağı (birim ve kilogram)
- İhbar/zamanaşımı kontrol listesi ve talep/savunma stratejisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

