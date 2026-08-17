---
argument-hint: ''
description: İş ilişkisinde ihtarname, haklı/geçerli fesih bildirimi, savunma istem
  yazısı, iş sözleşmesi veya ibraname taslağı hazırlanması gerektiğinde; usule uygun,
  gerekçeli ve yer tutuculu taslak metin üretme
name: belge-taslak-ihtar-fesih-sozlesme
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Belge ve Taslak Üretimi — İhtar, Fesih, Sözleşme, Savunma

## Görev
İş ilişkisinde usule uygun belge taslakları üretmek: fesih bildirimi, savunma istem yazısı, ihtarname, iş sözleşmesi, ibraname. Yer tutucu disipliniyle, eksik bilgiyi [doldurulacak] olarak işaretleyerek.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor; taraf hangisi (işçi/işveren)?
2. Belgenin hukuki amacı ve dayandığı sebep nedir (örn. m.25/II fesih)?
3. Tarih, ücret, sicil gibi değişken veriler elde var mı?
4. Tebligat usulü nasıl yapılacak (noter/iadeli taahhütlü/KEP)?

## Denetim şeması
1. **Fesih bildirimi (m.19):** Yazılı olmalı, fesih sebebi açık ve kesin gösterilmeli, m.25/II hariç davranış/verimsizlikte önceden savunma alınmalı. Bildirimde dayanılan vakıa, tarih, hukuki sebep (m.25/II-... vb.) ve ekler belirtilir. Sonradan başka sebep eklenemeyeceği için sebep tam yazılır.
2. **Savunma istem yazısı:** İşçiye isnat edilen somut olay, yer-zaman, makul savunma süresi ve cevap usulü açıkça belirtilir; aksi halde fesih usulsüz olur.
3. **İhtarname (işçi tarafı):** Ödenmeyen ücret/fazla çalışma için temerrüde düşürme; muacceliyet, talep edilen tutar/dönem, ödeme süresi ve aksi halde m.24/II haklı fesih ihtarı içerir. Faiz başlangıcı için önemlidir.
4. **İş sözleşmesi taslağı:** Taraflar, işin tanımı, ücret ve ekler, süre/tür, deneme süresi (m.15), çalışma süresi, rekabet yasağı (TBK m.444 sınırları — süre/yer/konu) ve gizlilik; emredici hükümlere aykırı (örn. fazla çalışma ücretini tamamen dışlayan) lafızdan kaçınılır.
5. **İbraname taslağı (TBK m.420):** Fesihten 1 ay sonrasına tarihli, kalem ve miktar açık, ödeme banka üzerinden; aksi halde geçersizlik/makbuz riski not düşülür.
6. **Tebligat:** İspat değeri için noter veya KEP önerilir.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık, gövde, talep, ekler, imza bloğu).
- Kullanılan madde dayanakları listesi.
- [doldurulacak] yer tutucu envanteri.
- Tebligat ve saklama önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

