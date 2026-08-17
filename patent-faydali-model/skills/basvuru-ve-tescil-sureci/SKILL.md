---
argument-hint: ''
description: TPMK nezdinde patent veya faydalı model başvurusu hazırlanırken, inceleme/itiraz
  aşamaları yönetilirken ve rüçhan/dönüştürme kararları verilirken kullanılır; başvuru
  stratejisi ve süreç yönetimi için
name: basvuru-ve-tescil-sureci
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Patent/Faydalı Model Başvuru ve Tescil Süreci

## Görev
TPMK başvuru dosyasının unsurlarını (SMK m.90-92) hazırlamak, araştırma-inceleme-itiraz aşamalarını yönetmek, rüçhan ve faydalı modele dönüştürme kararlarını planlamak.

## Soğuk başlangıç (intake)
1. Buluş için patent mi faydalı model mi hedefleniyor; teknik alan ne?
2. Yurt dışı öncelik (rüçhan) var mı; PCT/EPC yolu düşünülüyor mu?
3. Tarifname, istemler, özet ve resimler hazır mı; istem stratejisi belirlendi mi?
4. Kamuya açıklama riski/zaman baskısı var mı (grace period)?

## Denetim şeması
1. **Başvuru unsurları (SMK m.90-92).** Başvuru dilekçesi, tarifname, bir veya birden çok istem, özet, gerektiğinde resimler. Başvuru tarihinin kesinleşmesi için asgari unsurlar (m.90) tamam mı? Buluş bütünlüğü (tek genel buluş düşüncesi) sağlanmış mı?
2. **Rüçhan (SMK m.93-94).** Paris Sözleşmesi rüçhanı ilk başvurudan itibaren 12 ay; rüçhan belgesi süresinde sunulmalı. Tarih, yenilik değerlendirmesinin referansını belirler.
3. **Araştırma ve inceleme (patent).** Araştırma raporu talebi, yayım, üçüncü kişi görüşü, esaslı inceleme; patent verme kararı esaslı incelemeye tabidir (SMK m.96-98). Süreleri ve ücretleri takip et.
4. **İtiraz (SMK m.99).** Patentin verilmesi kararına karşı yayımdan itibaren altı ay içinde itiraz; YİDD (Yeniden İnceleme ve Değerlendirme Dairesi) kararı, ardından FSHM'de iptal davası.
5. **Faydalı model özellikleri (SMK m.143-144).** Esaslı inceleme zorunlu değildir ama araştırma raporu düzenlenir; buluş basamağı aranmaz. Patent-faydalı model arası dönüştürme imkânını (m.144) süre koşuluyla değerlendir.

## Çıktı modülleri
- Başvuru unsurları kontrol listesi ve eksik uyarısı.
- Rüçhan ve süre takvimi.
- Araştırma-inceleme-itiraz yol haritası.
- Patent/faydalı model ve dönüştürme strateji notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

