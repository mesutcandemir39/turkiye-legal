---
argument-hint: ''
description: Bir işlemin veya yapının vergi riskini değerlendirmek, meşru vergi planlaması
  ile peçeleme/muvazaa sınırını çizmek ve dava-uzlaşma stratejisini önermek için kullanılır.
name: risk-strateji-ve-planlama
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Vergi Riski, Strateji ve Planlama

## Görev
Mevcut ya da planlanan bir işlemin vergisel riskini ölçmek, meşru planlama ile kanuna karşı hile (peçeleme/muvazaa) sınırını belirlemek ve uyuşmazlık halinde en uygun strateji yolunu önermek.

## Soğuk başlangıç (intake)
1. Değerlendirme geçmiş bir işleme mi (savunma) yoksa planlanan yapıya mı (önleyici) ilişkin?
2. İşlemin ekonomik amacı ve ticari gerekçesi nedir?
3. İlişkili kişiler/grup içi işlem veya yurt dışı unsur var mı?
4. Benzer işlemlerde idare görüşü/özelge veya yerleşik içtihat var mı?
5. Mükellefin risk iştahı ve nakit/teminat kapasitesi nedir?

## Denetim şeması
1. **Meşru planlama-peçeleme sınırı:** VUK m.3/B (gerçek mahiyet) ve ekonomik yaklaşım; vergiden kaçınma (kanunun tanıdığı seçenekleri kullanma) meşru, kanuna karşı hile/peçeleme (görünürdeki işlemle gerçeği gizleme) ise vergi ziyaı ve m.359 riski doğurur. Bu sınırı somut olaya göre çiz.
2. **İlişkili kişi riski:** KVK m.13 (transfer fiyatlandırması — emsallere uygunluk) ve KVK m.12 (örtülü sermaye); grup içi işlemde emsal ve belgelendirme yeterli mi?
3. **Belge ve şeklî uyum:** VUK m.227-242 belge düzeni; eksik belge hem KKEG hem özel usulsüzlük riskidir. İşlemin kâğıt zemini sağlam mı?
4. **Özelge ile koruma:** VUK m.369 ve m.413 — mükellefe verilmiş özelgeye uygun işlemde ceza kesilmez ve gecikme faizi hesaplanmaz; ancak özelge yalnızca muhatabını bağlar ve idareyi her zaman bağlamaz. Korumanın kapsamını gerçekçi değerlendir.
5. **Senaryo ve beklenen değer:** İhtilaf çıkma olasılığı × (vergi + ceza + faiz) ile uzlaşma/dava maliyetini karşılaştır; uzlaşma indirimi, dava kazanma olasılığı ve yürütmenin durması rejimini (İYUK m.27/4) hesaba kat. Ara sonuç: önerilen strateji (planı revize et / özelge iste / uzlaş / dava aç).
6. **Ceza yargısı eşiği:** Sahte belge ve hile unsuru varsa idari değil cezai (VUK m.359) risk öne çıkar; strateji bu eşiği gözeterek kurulur.

## Çıktı modülleri
- Risk haritası (kalem / olasılık / tutar etkisi / hukuki dayanak).
- Meşru planlama-peçeleme sınır notu.
- Strateji karşılaştırması (planı değiştir / özelge / uzlaşma / dava — beklenen değer).
- Önleyici aksiyon ve belgelendirme listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

