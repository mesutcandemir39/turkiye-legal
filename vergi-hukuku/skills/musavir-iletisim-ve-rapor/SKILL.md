---
argument-hint: ''
description: Vergi konusundaki teknik analizi mükellefin/karar vericinin anlayacağı
  dilde sunmak, gerekçeli vergi mütalaası ve bilgilendirme yazısı üretmek için kullanılır.
name: musavir-iletisim-ve-rapor
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


# Müvekkil İletişimi ve Mütalaa Yazımı

## Görev
Vergi hukuku analizini mükellefe, mali müşavire veya şirket yönetimine açık, gerekçeli ve eyleme dönük biçimde aktarmak; hukuki mütalaa, bilgilendirme yazısı veya yönetim notu hazırlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim (bireysel mükellef, şirket yönetimi, mali müşavir, dava karşı tarafı)?
2. Çıktı türü nedir (mütalaa, bilgi notu, dava değerlendirmesi, e-posta özeti)?
3. Karar verici hangi soruya cevap arıyor (öde / dava aç / uzlaş / yapıyı değiştir)?
4. Teknik derinlik ne olmalı (özet mi, gerekçeli mütalaa mı)?
5. Tutar, ceza ve süre baskısı var mı?

## Denetim şeması
1. **Soru çerçeveleme:** Hukuki sorunu tek cümleyle sabitle (ör. "Re'sen tarhiyatın iptali şansı ve uzlaşma alternatifi"). Cevap bu soruya bağlı kalmalı.
2. **Olay tespiti:** Maddi vakıaları tarafsız ve tarihli biçimde özetle; ihtilaflı/belgesiz vakıaları ayrıca işaretle.
3. **Altlama:** İlgili normu (VUK/GVK/KVK/KDVK/İYUK/AATUHK ilgili maddesi) olaya uygula; karşı görüşü ve içtihadı dengeli ver. Doğrulanmamış karar künyesini `[DOĞRULANMADI]` ile işaretle; karararama.danistay.gov.tr kaynağını an.
4. **Sonuç ve gerekçe:** Net bir sonuç ver; tek seçenek dayatma, lehe-aleyhe ihtimalleri ve başarı olasılığını dürüstçe belirt (kesinlik vaadi verme).
5. **Sade dile çevirme:** Teknik terimi (re'sen tarh, ihtirazi kayıt, tevkifat) parantez içi kısa açıklamayla ver; karar vericinin yapması gerekeni madde madde yaz. Ara sonuç: muhatap "ne yapacağını" tereddütsüz anlar.
6. **Risk ve süre uyarısı:** Hak düşürücü süreyi ve sonraki kritik tarihi belgenin başında ve sonunda vurgula.

## Çıktı modülleri
- Yönetici özeti (soru – cevap – kritik tarih, 3-5 satır).
- Gerekçeli mütalaa gövdesi (olay / hukuki değerlendirme / sonuç).
- Aksiyon listesi (kim, neyi, hangi tarihe kadar).
- Sade dil eki ve istenecek belge/teyit listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

