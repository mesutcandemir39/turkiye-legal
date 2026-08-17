---
argument-hint: ''
description: Taşıma uyuşmazlığında dava/uzlaşma yolu seçimi, sorumluluk sınırının
  kalkma ihtimali, tahsil ve sigorta-rücu olasılıklarının tartılması ve müvekkile
  yön gösterilmesi gerektiğinde kullanılır.
name: risk-ve-strateji
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


# Risk Değerlendirmesi ve Strateji

## Görev
Taşıma uyuşmazlığında müvekkilin pozisyonunu (lehte/aleyhte) tartmak, sorumluluk sınırı ve tahsil riskini değerlendirip dava, uzlaşma veya sigorta yoluna ilişkin strateji önermek.

## Soğuk başlangıç (intake)
1. Müvekkil yük sahibi/sigortacı mı yoksa taşıyıcı/komisyoncu mu?
2. Talep tutarı sorumluluk sınırının (m.882/CMR m.23) üstünde mi?
3. Kasıt/pervasızlık (m.886 / CMR m.29) iddiasını destekleyen olgu var mı?
4. Geçerli nakliyat/CMR sigortası var mı; rücu zinciri ne?

## Denetim şeması
1. **Sorumluluk eksenli risk:** Olayın objektif sorumluluk (TTK m.875) kapsamına girip girmediği; kurtuluş sebeplerinin (m.876, m.878) güçlü olup olmadığı.
2. **Sınırın belirleyiciliği:** Talep, kg x 8,33 SDR sınırını aşıyorsa, m.886/CMR m.29 (kasıt-pervasızlık) ispatlanmadıkça aşkın kısım tahsil edilemez. Bu nedenle sınırın kalkması ihtimali dava değerini belirler.
3. **Sürelerin etkisi:** İhbar/rezerv ve 1/3 yıllık zamanaşımı (m.855/CMR m.32) — kaçırılmış süre aleyhe ağır risk; durdurma imkânları değerlendirilir.
4. **Tahsil/sigorta:** Taşıyıcının mali durumu, CMR/sorumluluk sigortası kapsamı; sigortacının halefiyetle rücu (TTK m.1472) hattı.
5. **Çözüm yolu seçimi:** Dava şartı arabuluculuğun zorunlu olduğu (TTK m.5/A) dikkate alınarak; tutar, kanıt gücü ve süre baskısına göre sulh/arabuluculuk veya dava önerisi.
6. **Senaryo analizi:** İyimser/kötümser/olası senaryolarda tahsil edilebilir tutar aralığı ve maliyet (harç, ekspertiz, vekâlet).
7. **Ara sonuç:** Önerilen yol, gerekçesi ve müvekkile sunulacak risk haritası.

## Çıktı modülleri
- Lehte/aleyhte olgu ve risk matrisi.
- Beklenen değer/senaryo tablosu (sınırlı vs. sınırsız sorumluluk).
- Strateji notu (arabuluculuk/sulh/dava) ve sonraki adım listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

