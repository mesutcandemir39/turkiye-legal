---
argument-hint: ''
description: Buluşun patent mi faydalı model mi olarak korunacağı, ulusal/EPC/PCT
  rejimi, koruma süresi ve uygulanacak normun belirlenmesi gerektiğinde; uyuşmazlığı
  doğru rejime oturtmak için ilk başvurulacak bece
name: temel-kavramlar-ve-sistem
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


# Patent ve Faydalı Model Temel Kavramları ve Sistematik

## Görev
Önündeki teknik korumayı doğru rejime oturtmak: patent mi faydalı model mi, ulusal mı EPC/PCT yoluyla mı geldiği, koruma süresi ve uygulanacak normu (SMK Dördüncü Kitap, SMK Yönetmeliği, EPC/PCT) belirleyip uyuşmazlığın iskeletini kurmak.

## Soğuk başlangıç (intake)
1. Korunan/korunacak konu nedir: ürün mü usul mü; teknik alan ne?
2. Patent mi faydalı model mi; belge verildi mi, başvuru hangi aşamada?
3. Hak ulusal başvurudan mı, PCT ulusal aşamasından mı, yoksa Türkiye'de validasyonlu Avrupa patentinden mi doğuyor?
4. Başvuru/rüçhan tarihi ve kalan koruma süresi nedir?

## Denetim şeması
1. **Rejim tespiti.** Patent SMK m.82 vd. (20 yıl, m.101); faydalı model SMK m.142-145 (10 yıl). Faydalı modelde buluş basamağı aranmaz (m.142/1), ancak usuller, kimyasal/biyolojik maddeler ve eczacılık ürünleri faydalı modelle korunamaz (m.142/3). Ara sonuç: hangi rejim?
2. **Hak kaynağı.** Ulusal patent TPMK; PCT başvurusunun ulusal aşaması; Avrupa patenti EPC m.65 uyarınca çeviri/validasyon ile Türkiye'de ulusal patent hükmü doğurur. Validasyon ve yıllık ücret durumunu sicilden teyit et.
3. **Koruma kapsamının kaynağı.** Koruma istemlerle belirlenir (SMK m.89); tarifname ve resimler yorumda kullanılır. Bağımsız/bağımlı istem ayrımını çıkar.
4. **Süre ve ayakta kalma.** Patent 20, faydalı model 10 yıl; koruma yıllık ücretlerin ödenmesine bağlıdır (SMK m.101). Ödenmeyen ücret hakkı düşürür; ek süre/telafi imkânını kontrol et.
5. **Norm seçimi.** Maddi şartlarda SMK m.82-83; usulde SMK Yönetmeliği; çatışmada özel düzenleme genel kuralı önceler.

## Çıktı modülleri
- Rejim ve uygulanacak norm haritası (patent/faydalı model; ulusal/EPC/PCT).
- Hak kaynağı ve sicil durumu özeti.
- Koruma süresi ve yıllık ücret takvimi uyarısı.
- İstem yapısı (bağımsız/bağımlı) ilk dökümü.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

