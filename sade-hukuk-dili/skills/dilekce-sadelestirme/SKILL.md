---
argument-hint: ''
description: Bir dava dilekçesini, cevap dilekçesini, istinaf/temyiz layihasını veya
  savunmayı müvekkilin anlayacağı sade Türkçeye çevirmek; talep sonucunu, vakıaları
  ve hukuki sebepleri yalın anlatmak gerektiğind
name: dilekce-sadelestirme
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


# Dilekçe ve Layiha Sadeleştirme

## Görev
Dava/cevap dilekçesi, replik-düplik, istinaf veya temyiz layihasını; vakıa-hukuki sebep-talep
sonucu mimarisini bozmadan, müvekkilin "bu dilekçede ne diyoruz, ne istiyoruz" sorusuna net
cevap verecek sade bir metne çevirmek.

## Soğuk başlangıç (intake)
1. Hangi dilekçe ve hangi taraf adına (davacı/davalı/sanık/müşteki)?
2. Yargı kolu nedir (HMK 6100, CMK 5271, İYUK 2577)?
3. Okuyucu müvekkil mi, yoksa hukukçu olmayan bir karar verici mi?
4. Vurgulanması istenen talep veya risk var mı?

## Denetim şeması
1. İSKELETİ ÇIKAR: Dilekçenin üç ana ekseni ayrıştırılır — vakıalar, hukuki sebepler, talep
   sonucu (HMK m.119 dava dilekçesinin zorunlu unsurları; cevap için m.129). Sade metin bu
   üçlüyü "neler oldu / hangi kurala dayanıyoruz / ne istiyoruz" başlıklarına oturtur.
2. TALEP SONUCUNU ÖNE AL: Hukukçu metni gerekçeyle başlatır; sade metin sonuçla (ne istiyoruz)
   başlar, gerekçeyi sonra verir. Talep sonucu birebir korunur, daraltılıp genişletilmez.
3. USULİ SÜZGEÇ (ispat/süre): İçinde süre bağlı bir işlem varsa (istinaf süresi HMK m.345 –
   iki hafta; temyiz HMK m.361 – iki hafta; cevap süresi m.127 – iki hafta) bu süreler takvim
   tarihiyle açıkça yazılır, çünkü müvekkil için kritik sonuçtur.
4. DELİL BAĞINI KORU: "Hangi iddiayı hangi delille gösteriyoruz" ilişkisi sadeleştirmede
   düşürülmez; ispat yükünün kimde olduğu yalın dille belirtilir.
5. ARA SONUÇ: Sade metin, dilekçenin talep sonucunu ve dayanağını eksiksiz yansıtıyor mu;
   hiçbir hukuki sebep veya delil atlanmış mı kontrol edilir.
6. İSTİSNA: Dilekçenin kendisi mahkemeye verilen bağlayıcı metindir; sade versiyon yalnızca
   müvekkili bilgilendirir, dosyaya sunulmaz.

## Çıktı modülleri
- "Bu dilekçede özetle" bölümü (3-5 cümle).
- Ne istiyoruz / Neden / Hangi delillerle tablosu.
- Kritik süreler ve sonraki adımlar (takvim tarihli).
- Korunan teknik terimler sözlüğü ve asıl dilekçeye yönlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

