---
argument-hint: ''
description: 4054 m.16 uyarınca ciro üzerinden idari para cezası riskini hesaplamak,
  ağırlaştırıcı/hafifletici unsurları belirlemek ve pişmanlık ya da uzlaşma yoluyla
  indirim stratejisi kurmak istendiğinde kullanı
name: idari-para-cezasi-hesabi
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İdari Para Cezası ve Pişmanlık-Uzlaşma

## Görev
Rekabet ihlalinde 4054 m.16 ve Ceza Yönetmeliği çerçevesinde olası para cezasını öngörmek; ağırlaştırıcı/hafifletici sebepleri haritalamak; pişmanlık (kartel) ve uzlaşma yollarıyla cezayı azaltma stratejisi geliştirmek.

## Soğuk başlangıç (intake)
- İhlal türü: kartel mi, diğer m.4 ihlali mi, m.6 kötüye kullanma mı, izinsiz birleşme/yanlış bilgi mi?
- Teşebbüsün ihlal yılına ilişkin yıllık gayri safi geliri (ciro) yaklaşık ne düzeyde?
- İhlal süresi ve tekerrür durumu nedir?
- İşbirliği/pişmanlık başvurusu yapılabilir mi; deliller ne durumda?

## Denetim şeması
1. **Ceza türü (m.16)** — esas para cezası kural olarak teşebbüsün bir önceki yıl gayri safi gelirleri üzerinden orana göre belirlenir (üst sınır kanunda öngörülmüştür). Ayrıca yerinde incelemeyi engelleme, yanlış/yanıltıcı bilgi, izinsiz birleşme gibi durumlarda nispi/özel cezalar gündeme gelir.
2. **Temel oran ve ağırlık** — Ceza Yönetmeliği uyarınca ihlalin türü (kartel daha ağır), süresi, pazar etkisi temel oranı belirler; süre uzadıkça artış uygulanır.
3. **Ağırlaştırıcı sebepler** — tekerrür, soruşturmaya yardımcı olmama, ihlale devam, zorlayıcı/teşvik edici (elebaşı) rol.
4. **Hafifletici sebepler** — soruşturmaya yardım, ihlale son verme, kusurun azlığı, devlet teşvikiyle hareket, ihlalde sınırlı rol.
5. **Pişmanlık (Kartel Yönetmeliği)** — yalnızca kartellerde; ilk başvurana ve delil sunana tam muafiyet, sonrakilere kademeli indirim. Başvuru sırası ve delil kalitesi belirleyicidir.
6. **Uzlaşma (Uzlaşma Yönetmeliği)** — ihlalin kabulü karşılığında belirli oranda indirim ve sürecin kısaltılması; pişmanlıkla birlikte kullanılabilir.
7. **Ara sonuç** — ceza aralığı tahmini, en uygun indirim yolu (pişmanlık/uzlaşma) ve net beklenen yaptırım senaryosu.

## Çıktı modülleri
- Ceza aralığı tahmini (ciro tabanı + ağırlık + süre + sebepler).
- Ağırlaştırıcı/hafifletici sebep envanteri.
- Pişmanlık vs. uzlaşma karar matrisi ve zamanlama uyarısı.
- Özel hukuk tazminat (m.57-58) yansıma riski notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

