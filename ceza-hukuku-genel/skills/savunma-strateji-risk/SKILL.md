---
argument-hint: ''
description: Bir ceza isnadında savunma hattını kurmak, beraat-indirim-düşme seçeneklerini
  tartmak ve müvekkile gerçekçi risk haritası sunmak gerektiğinde kullanılır.
name: savunma-strateji-risk
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


# Savunma Stratejisi ve Risk Değerlendirmesi

## Görev
Şüpheli/sanık vekilinin gözünden savunma hattını kurmak; suç teorisi katmanlarındaki zayıf noktaları savunma argümanına çevirmek ve müvekkile gerçekçi risk-seçenek haritası sunmak.

## Soğuk başlangıç (intake)
- İsnat ve sevk maddesi nedir; dosyadaki temel deliller hangileri?
- Müvekkilin hedefi nedir (beraat, en az ceza, hızlı kapanış)?
- Şikâyet, uzlaştırma, önödeme gibi düşme yolları açık mı?
- Sanığın geçmişi ve duruşmadaki tutumu nasıl olacak?

## Denetim şeması
1. **Tipiklik saldırısı:** Maddi unsur eksikliği (netice/nedensellik kopukluğu), manevi unsur eksikliği (kast yokluğu, taksir lehine niteleme) argümanları üretilir. Ara sonuç: tipiklik tartışılabilir mi?
2. **Hukuka aykırılık savunması:** Meşru savunma, rıza, hak kullanma (m.24-27) sebeplerinin şartları somut delille kurgulanır.
3. **Kusurluluk savunması:** Haksız tahrik (m.29), hata (m.30), cebir-zorunluluk (m.28, m.25/2), yaş/akıl (m.31-32) ve buna bağlı rapor talepleri.
4. **Niteleme ve içtima lehine argüman:** Daha hafif suça niteleme, teşebbüs/gönüllü vazgeçme (m.35-36), zincirleme yerine tek suç ya da tersi yönünde lehe değerlendirme.
5. **Düşme/sönme yolları:** Zamanaşımı (m.66), şikâyet süresi (m.73), uzlaştırma (CMK m.253), önödeme (m.75), şikâyetten vazgeçme; ardından yaptırım aşamasında m.62, m.50, m.51, HAGB (CMK m.231) lehine talepler.
6. **Risk tartımı:** Her seçeneğin olasılık ve ceza sonucu, in dubio pro reo ve ispat yükü dikkate alınarak tartılır.

## Çıktı modülleri
- Katman bazlı savunma argümanı matrisi (güç/zayıflık).
- Düşme/indirim yolları kontrol listesi ve süre takvimi.
- Müvekkile sade dilli risk-seçenek haritası.
- Delil talebi ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

