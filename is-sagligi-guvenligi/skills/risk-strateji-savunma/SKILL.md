---
argument-hint: ''
description: İşveren veya çalışan tarafı için iş kazası ve uyum riskini değerlendirmek,
  savunma stratejisi ve sulh-uzlaşma seçeneklerini tartmak için kullanılır.
name: risk-strateji-savunma
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
  - ad: İş Sağlığı ve Güvenliği Kanunu
    numara: '6331'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Stratejisi ve Savunma Planlaması

## Görev
Tarafın konumuna göre (işveren savunması ya da çalışan/hak sahibi talebi) bütüncül risk değerlendirmesi yapmak; idari, tazminat, rücu ve ceza eksenlerini birlikte tartıp strateji ve sulh seçeneklerini önermek.

## Soğuk başlangıç (intake)
- Müvekkil sıfatı ve hedefi (riski sınırlamak / azami tazminat / cezadan kaçınmak)?
- Dört eksenden hangileri açık (idari ceza, tazminat, SGK rücuu, ceza)?
- Kusur oranı/bilirkişi tahmini ve karşı tarafın delil gücü ne?
- Sulh/uzlaşma için tarafların eğilimi ve ödeme kapasitesi var mı?

## Denetim şeması
1. **Çok eksenli risk haritası:** Aynı kaza dört ayrı sonuç doğurur — idari ceza (6331 m.26), işçi/hak sahibi tazminatı (TBK m.417), SGK rücuu (5510 m.21), ceza (TCK m.85-89). Bir eksendeki kusur tespiti diğerlerini güçlü biçimde etkiler; tek strateji tüm eksenleri gözetmeli.
2. **İşveren tarafı:** Önlem ve uyum belgeleriyle kusuru azaltma (önleme hiyerarşisi, eğitim, yazılı uyarı zinciri), müterafik/üçüncü kişi kusuru argümanı, idari cezada usul itirazı, ceza eksende bilinçli taksir-basit taksir ayrımı.
3. **Çalışan/hak sahibi tarafı:** Risk değerlendirmesi/eğitim eksikliği ve önleme hiyerarşisi ihlaliyle kusuru yükseltme, belirsiz alacakla tam talep, manevi tazminat ve destek kalemleri.
4. **Sulh-uzlaşma ekonomisi:** Ceza ekseninde uzlaşma kapsamı, tazminatta makbuz/ibraname riskleri (gerçek iradeyi yansıtmayan ibra geçersiz olabilir), maluliyetin kesinleşmemesi nedeniyle erken sulhün riski.
5. **Senaryo karşılaştırması:** En iyi/orta/en kötü senaryoda mali ve cezai sonuç. **Ara sonuç:** Önerilen strateji + gerekçe + sonraki adımları sırala.

## Çıktı modülleri
- Dört eksenli risk haritası ve etkileşim notu.
- Taraf bazlı argüman ve savunma listesi.
- Sulh/uzlaşma senaryo karşılaştırma tablosu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

