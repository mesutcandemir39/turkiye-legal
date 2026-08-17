---
argument-hint: ''
description: İdari uyuşmazlıkta kazanma ihtimalini, süre/yargı yolu risklerini, idari
  ve adli yol seçeneklerini ve müzakere/uzlaşma imkânlarını tartmak için kullanılır;
  dava açma kararı verilmeden önce bütünsel de
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Risk Değerlendirmesi ve Dava Stratejisi

## Görev
Dosyayı bütünsel değerlendirip dava açma/açmama, hangi yolu izleme ve idare ile müzakere kararını risk temelli vermek; müvekkile gerçekçi bir tablo sunmak.

## Soğuk başlangıç (intake)
1. Müvekkilin asıl hedefi nedir (işlemin iptali mi, tazminat mı, süre kazanmak mı)?
2. En kritik risk hangisi (süre, ehliyet, yargı yolu, esasın zayıflığı)?
3. İdareyle uzlaşma/işlemin geri alınması imkânı var mı?
4. Zaman ve maliyet baskısı ne düzeyde?

## Denetim şeması
1. **Eşik (kabul edilebilirlik) riskleri.** Önce süre, ehliyet-menfaat, görev-yetki ve zorunlu ön başvuru (m.11/m.13) eşiklerini denetle; biri kapalıysa esas tartışması anlamsızdır.
2. **Esasın gücü.** Beş unsur denetiminden çıkan aykırılıkları "güçlü / tartışmalı / zayıf" olarak derecelendir; idarenin re'sen araştırmada savunmasını öngör.
3. **Yürütmenin durdurulması ihtimali.** m.27 çifte koşulu karşılanıyor mu; YD alınamazsa işlem icra edilir ve zarar büyür mü?
4. **Alternatif yollar.** İYUK m.11 ile işlemin idarece geri alınması/düzeltilmesi, üst makama başvuru, bilgi edinme (4982) ile belge toplama, uzlaşma (vergi alanında) gibi dava dışı seçenekler.
5. **Maliyet-fayda.** Yargılama süresi, harç/masraf, vekâlet ücreti riski, icranın geri dönülebilirliği ve müvekkilin hedefi birlikte tartılır.
6. **İçtihat eğilimi.** Benzer uyuşmazlıkta Danıştay/İDDK eğilimini araştır ve künyeyi `[DOĞRULANMADI]` işaretle (karararama.danistay.gov.tr).
7. **Ara sonuç.** Tavsiye edilen yol (dava/başvuru/uzlaşma) + gerekçe + en büyük üç risk ve azaltma önerisi.

## Çıktı modülleri
- Eşik riskleri kontrol listesi (süre/ehliyet/görev/ön başvuru).
- Esas gücü derecelendirme tablosu.
- Yol seçenekleri karşılaştırması (dava/başvuru/uzlaşma).
- Müvekkile sunulacak risk özeti ve tavsiye.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

