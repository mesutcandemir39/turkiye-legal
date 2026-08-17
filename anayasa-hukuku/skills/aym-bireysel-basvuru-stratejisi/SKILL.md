---
argument-hint: ''
description: Bir temel hak ihlali iddiasının Anayasa Mahkemesine bireysel başvuru
  yoluyla taşınıp taşınamayacağını ve kabul edilebilirlik şartlarını değerlendirmek;
  başvuru yollarının tüketilmesi, süre ve konu yön
name: aym-bireysel-basvuru-stratejisi
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
  version: 0.1.0
user-invocable: true
---


# AYM Bireysel Başvuru Stratejisi

## Görev
Anayasa ve AİHS ortak koruması altındaki bir temel hakkın kamu gücü işlemiyle ihlal edildiği iddiasını, Anayasa m.148/3 ve 6216 sayılı Kanun çerçevesinde bireysel başvuruya hazırlamak; kabul edilebilirlik eşiklerini önceden test etmek.

## Soğuk başlangıç (intake)
1. İhlal hangi temel haktan kaynaklanıyor ve hem Anayasa hem AİHS kapsamında mı (ortak koruma alanı)?
2. İhlali doğuran kesinleşmiş işlem/karar hangisi ve ne zaman tebliğ edildi?
3. Olağan kanun yolları (istinaf, temyiz, gerekirse karar düzeltme) tüketildi mi?
4. İhlalden doğan güncel ve kişisel bir mağduriyet var mı?

## Denetim şeması
1. **Konu bakımından yetki.** Hak hem Anayasa hem AİHS (ve ek protokoller) kapsamında ortak korunan bir hak olmalı (m.148/3, 6216 m.45). Yasama işlemleri ve düzenleyici işlemler doğrudan başvuru konusu olamaz; idari/yargısal uygulama işlemi aranır.
2. **Kişi bakımından yetki.** Başvurucu güncel ve kişisel olarak, doğrudan etkilenen mağdur olmalı (6216 m.46). Kamu tüzel kişileri başvuramaz.
3. **Başvuru yollarının tüketilmesi.** İhlali gidermeye elverişli tüm olağan idari ve yargısal yollar tüketilmelidir (6216 m.45/2). Ara sonuç: tüketilmemişse başvuru reddedilir.
4. **Süre.** Başvuru yollarının tüketildiği, yoksa ihlalin öğrenildiği tarihten itibaren **otuz gün** içinde yapılır (6216 m.47/5). Mazeret rejimi sınırlıdır.
5. **Kabul edilebilirlik.** Açıkça dayanaktan yoksunluk, anayasal ve kişisel önemden yoksunluk (önemli zarar yokluğu) elemeleri uygulanır. Esasta ihlal tespit edilirse AYM ihlali ve sonuçlarını giderme yolunu (yeniden yargılama, tazminat) gösterir.
6. **AİHM ile ilişki.** AYM, iç hukukta etkili başvuru yolu olarak görülür; AİHM'e gitmeden önce kural olarak tüketilmesi gereken bir aşamadır.
Künye verirken başvuru numarası ve karar tarihini `[DOĞRULANMADI]` işaretleyin; kaynak kararlarbilgibankasi.anayasa.gov.tr.

## Çıktı modülleri
- Kabul edilebilirlik ön testi (yetki, tüketme, süre, mağdur sıfatı) tablosu.
- İhlal iddiasının hak bazlı gerekçesi ve talep edilecek giderim (yeniden yargılama/tazminat).
- Süre takvimi ve eksik belge listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

