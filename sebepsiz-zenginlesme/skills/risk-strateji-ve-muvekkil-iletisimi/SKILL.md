---
argument-hint: ''
description: Sebepsiz zenginleşme uyuşmazlığında dava/sulh seçeneklerini tartmak,
  kazanma olasılığı ve maliyet-fayda analizi yapmak ve müvekkile anlaşılır bir yol
  haritası sunmak gerektiğinde kullanılır.
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi, Strateji ve Müvekkil İletişimi

## Görev
İade uyuşmazlığında hukuki pozisyonu gerçekçi tartmak; talep seçimi, süre ve ispat zayıflıklarını öne koymak; dava/sulh/ihtar seçeneklerini maliyet-fayda ekseninde değerlendirip müvekkile sade ve dürüst bir yol haritası sunmak.

## Soğuk başlangıç (intake)
- Müvekkilin hedefi ne (parayı geri almak, aynen iade, ilişkiyi tasfiye etmek)?
- Eldeki delillerin gücü ve karşı tarafın muhtemel savunması (bağışlama, geçerli sebep, zamanaşımı)?
- Zaman baskısı (yaklaşan iki/on yıllık süre)?
- Risk iştahı ve bütçe (harç, vekâlet ücreti, bilirkişi)?

## Denetim şeması
1. **Pozisyon analizi.** Dört unsuru (m.77) ve seçilen tipi delil gücüyle altla; en zayıf halkayı belirle. Tipik zayıflıklar: haklı sebebin yokluğunun ispatı, yanılarak ödemenin (m.78) ispatı, öğrenme tarihinin (m.82) belirsizliği, karşı tarafın bağışlama savunması.
2. **Talep ve süre stratejisi.** Yarışan talep (istihkak/sözleşme/haksız fiil) varsa süre ve miktar avantajına göre birincil talebi, sebepsiz zenginleşmeyi yedek (terditli) kur. Zamanaşımı yakınsa derhal kesen işlem (dava/takip) planla.
3. **Senaryo matrisi.** En iyi/orta/en kötü sonuç; kazanma olasılığı kaba bant (yüksek/orta/düşük) olarak verilir, kesin oran vaadinden kaçınılır. Karşı tarafın m.79 (elden çıkma) ve m.81 (ahlaka aykırılık) savunmaları değerlendirilir.
4. **Maliyet-fayda.** Tahmini harç/giderler, yargılama süresi (istinaf/temyiz dahil), tahsil kabiliyeti (karşı tarafın ödeme gücü). İade miktarı ölçü olduğundan, faiz ve semere kalemleriyle gerçek getiri hesaplanır.
5. **Strateji seçimi.** İhtar → (gerekirse) arabuluculuk → dava sıralaması; ihtiyati haciz (İİK m.257) gereği değerlendirilir; sulh için makul aralık ve kozlar (zamanaşımı riski, ispat zorluğu) belirlenir.
6. **Müvekkil iletişimi.** Sonuç sade Türkçe ile; seçeneklerin artı/eksisi, önerilen adım ve varsayımlar/`[DOĞRULANMADI]` veriler açıkça yazılır. Kesin kazanç taahhüdü verilmez. Ara sonuç: önerilen yol + gerekçe + sonraki adım listesi.

## Çıktı modülleri
- Risk haritası (unsur-delil-zayıflık tablosu).
- Senaryo ve maliyet-fayda özeti.
- Müvekkile sade bilgilendirme notu ve aksiyon planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

