---
argument-hint: ''
description: Belirli bir hukuki ilkeyi veya güncel içtihat eğilimini bulmak gerektiğinde;
  resmî karar bankalarında ve mevzuat sisteminde etkili arama sorgusu kurmak ve sonuçları
  değerlendirmek için kullanılır.
name: kaynak-arama-sorgu-stratejisi
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Kaynak Arama ve Sorgu Stratejisi

## Görev
Aranan hukuki ilkeyi veya içtihat eğilimini resmî kaynaklarda verimli biçimde bulmak için arama sorgusu kurmak ve dönen sonuçları güvenilirlik/güncellik bakımından elemek.

## Soğuk başlangıç (intake)
- Aranan ilke nedir; hangi kanun maddesi etrafında dönüyor?
- Hangi yargı kolu/banka uygun (Yargıtay, Danıştay, AYM, AİHM)?
- Lehe karar mı, eğilim tespiti mi, karşı içtihat taraması mı amaç?
- Konunun teknik terimi/anahtar kelimesi ne?

## Denetim şeması
1. **Banka seçimi** — Adli/özel hukuk ve ceza: karararama.yargitay.gov.tr. İdari/vergi: karararama.danistay.gov.tr. Anayasal/temel hak: kararlarbilgibankasi.anayasa.gov.tr. AİHS: hudoc.echr.coe.int. Mevzuat: mevzuat.gov.tr.
2. **Sorgu kurma** — Hukuki terim + ilgili madde (örn. "ayıplı ifa" + "TBK 219") kombinlenir; çok genel terim çok sonuç, çok dar terim sıfır sonuç verir, kademeli daraltılır. Eş anlamlı/eski terim de denenir (örn. "müdahalenin meni" / "el atmanın önlenmesi").
3. **Tarih ve daire filtresi** — Güncellik için tarih aralığı; konu dairesini bilen ilgili daireyle filtreler (örn. ticari için 11. HD, iş için 9./22. HD eğilimi). Filtre, eğilimi daraltmak için araçtır, gerçeği saptırmak için değil.
4. **Sonuç eleme** — Dönen kararın vakıası eldeki olaya benziyor mu; ratio aranan ilkeyi gerçekten kuruyor mu? Benzemeyen karar emsal listesine alınmaz.
5. **Eğilim okuma** — Birden çok karar varsa istikrar ve tarih izlenir; daireler arası çelişki/İBK varlığı kontrol edilir; eğilim dürüstçe (lehe-aleyhe) özetlenir.
6. **Künye çıkarımı** — Bulunan kararın künyesi metinden aynen alınır; **arama yapılmadan/karar görülmeden künye yazılmaz.**

## Çıktı modülleri
- Banka + sorgu önerileri (kademeli).
- Filtre stratejisi (tarih/daire/terim).
- Bulunan kararların eleme tablosu (vakıa benzerliği).
- Eğilim özeti + doğrulanmış künyeler / `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

