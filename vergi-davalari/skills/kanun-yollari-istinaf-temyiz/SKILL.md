---
argument-hint: ''
description: Vergi mahkemesi kararına karşı bölge idare mahkemesine istinaf ve Danıştaya
  temyiz başvurularının kesinlik sınırlarını, sürelerini ve başvuru sebeplerini belirlemek
  için kullanılır.
name: kanun-yollari-istinaf-temyiz
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kanun Yolları (İstinaf ve Temyiz)

## Görev
Vergi mahkemesi kararına karşı hangi kanun yolunun açık olduğunu (istinaf/temyiz/kesinlik) belirlemek; başvuru süresini, parasal sınırları ve bozma-kaldırma sebeplerini doğru kurgulamak.

## Soğuk başlangıç (intake)
1. Vergi mahkemesi kararı lehe mi aleyhe mi; karar size ne zaman tebliğ edildi?
2. Uyuşmazlığın parasal değeri (vergi aslı + ceza) ne kadar?
3. Karar tek hâkimle mi kurul halinde mi verildi?
4. İtiraz edilecek husus maddi vakıa mı yoksa hukuki yorum/usul mü?

## Denetim şeması
1. **İstinaf yolu.** İYUK m.45 — vergi mahkemesi kararlarına karşı kararın tebliğinden itibaren 30 gün içinde bölge idare mahkemesine istinaf; belirli parasal sınırın altındaki davalarda karar kesin (sınır her yıl yeniden değerleme oranıyla güncellenir, **güncel tutar teyit edilmeli**).
2. **İstinaf incelemesi.** BİM hem maddi olay hem hukuki denetim yapar; gerektiğinde yeniden karar verir (m.45/4-5). İstinaf sebepleri (eksik inceleme, delil değerlendirme hatası, hukuka aykırılık) ayrı başlıklanır.
3. **Temyiz yolu.** İYUK m.46 — BİM kararlarına karşı, kanunda sayılan ve belirli parasal sınırı aşan davalarda kararın tebliğinden itibaren 30 gün içinde Danıştaya temyiz; çoğu uyuşmazlıkta istinaf kararı kesindir, yalnızca sınır üstü ve sayılı hallerde temyiz açıktır (**sınır ve liste teyit edilmeli**).
4. **Temyiz sebepleri.** İYUK m.49 — görev-yetki, hukuka aykırılık, usul hükümlerine aykırılık. Danıştay bozma kararı verirse dosya BİM'e gönderilir.
5. **Yürürlük ve teminat.** Kanun yolu başvurusunun yürütmeye etkisi ve YD talebi ayrı değerlendirilir (İYUK m.27, m.52). Ara sonuç: kararın kesin olup olmadığı, açıksa hangi merciye hangi sürede başvurulacağı netleştirilir.

## Çıktı modülleri
- Kanun yolu haritası (kesinlik / istinaf / temyiz, parasal sınır uyarısı).
- İstinaf veya temyiz dilekçesi iskeleti (sebep başlıklarıyla).
- Süre ve YD talep notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

