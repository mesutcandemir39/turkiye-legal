---
argument-hint: ''
description: Tüketici uyuşmazlığında ihtarname, hakem heyeti başvurusu, dava/itiraz
  dilekçesi veya cayma/fesih bildirimi taslağı üretmek gerektiğinde; layiha mimarisi
  ve yer tutucu disipliniyle kullanılır.
name: dilekce-ve-basvuru-taslagi
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe, Başvuru ve Sözleşme Taslakları

## Görev
Tüketici uyuşmazlığının gerektirdiği yazılı metni (ihtarname, hakem heyeti başvurusu, dava dilekçesi, hakem heyeti kararına itiraz, cayma/fesih bildirimi) usul kurallarına uygun, vakıa-hukuki sebep-talep mimarisiyle ve eksik bilgilerde yer tutucu disipliniyle üretmek.

## Soğuk başlangıç (intake)
- Hangi metin gerekiyor (ihtar, başvuru, dava, itiraz, bildirim)?
- Taraflar, talep konusu ve değeri nedir?
- Hangi maddi vakıalar ve deliller var; eksik bilgi hangileri?
- Hedeflenen sonuç (iade, onarım, fesih, tazminat) ne?

## Denetim şeması
1. **Metin türü seçimi:** Çözüm yoluna göre doğru belgeyi belirle — hakem heyeti başvurusu (m.66 usulü), tüketici mahkemesi dava dilekçesi (HMK m.119 zorunlu unsurları), hakem heyeti kararına itiraz dilekçesi (m.70, 15 gün), ihtarname (TBK m.117 temerrüt için) veya cayma/fesih bildirimi.
2. **Zorunlu unsurlar (HMK m.119):** Mahkeme, taraflar ve TC/adres, dava konusu, değer, açık vakıalar, dayanılan deliller, hukuki sebepler, açık talep sonucu ve imza. Eksik unsur ön incelemede tamamlattırılır; baştan eksiksiz yaz.
3. **Hukuki sebep altlaması:** Talebe göre TKHK madde grubunu doğru göster (ayıp m.11/15, haksız şart m.5, cayma m.48/24, abonelik m.52); tamamlayıcı olarak TBK/HMK maddelerini ekle.
4. **Talep sonucu netliği:** Eda talebini para/edim olarak somut yaz; faiz başlangıcı ve türünü (avans/yasal/ticari) belirt; fazlaya ilişkin haklar saklı tut.
5. **Yer tutucu disiplini:** Bilinmeyen tarih, tutar, ad için [doldurulacak: ...] biçiminde açık yer tutucu kullan; uydurma veri girme.
6. **Delil bağlama:** Her vakıayı ilgili delile bağla; delil listesini ayrı blokta ver.
7. **Ara sonuç:** Metin usulen eksiksiz mi, talep ve sebep tutarlı mı, yer tutucular işaretli mi?

## Çıktı modülleri
- Seçilen türde hazır taslak metin.
- Zorunlu unsur kontrol listesi.
- Delil dizini.
- Doldurulacak alanlar özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

