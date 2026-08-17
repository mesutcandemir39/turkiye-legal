---
argument-hint: ''
description: Pazar yeri veya platform işleten ya da platformda satış yapan tarafın
  6563 m.9 kapsamındaki aracı sorumluluğu, uyar-kaldır ve ETAHS yükümlülüklerinin
  değerlendirilmesi gerektiğinde kullanılır.
name: araci-hizmet-saglayici-platform
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
  - ad: Elektronik Ticaretin Düzenlenmesi Hakkında Kanun
    numara: '6563'
    tur: kanun
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aracı Hizmet Sağlayıcı ve Platform Sorumluluğu

## Görev
Pazar yeri/platform (aracı hizmet sağlayıcı) ile platformda satış yapan hizmet sağlayıcı arasındaki sorumluluk dağılımını ve 7416 sayılı Kanunla gelen ETAHS yükümlülüklerini değerlendirmek.

## Soğuk başlangıç (intake)
- Müvekkil platform mu (ETAHS) yoksa platform satıcısı mı (ETHS)?
- Platformun yıllık net işlem hacmi ve işlem sayısı hangi eşik bandında?
- Uyuşmazlık konusu: üçüncü kişi içeriği/hak ihlali mi, reklam/indirim sınırı mı, ödeme/komisyon mu?
- Hak sahibinin bildirimi (uyar-kaldır) yapıldı mı?

## Denetim şeması
1. Genel kural (6563 m.9): aracı hizmet sağlayıcı, hizmet sunduğu içeriği kontrol etmek ve hukuka aykırılığı araştırmakla yükümlü değildir; kural olarak başkalarına ait içerikten sorumlu tutulmaz.
2. Uyar-kaldır: 5651 ve 6563 çerçevesinde hak ihlali iddiası usulüne uygun bildirildiğinde platform makul sürede gereğini yapmazsa sorumluluğu doğabilir; fikri mülkiyet ihlallerinde özel bildirim-kaldırma mekanizması işler.
3. ETAHS kademeli yükümlülükleri (7416 değişiklikleri): net işlem hacmine göre "elektronik ticaret aracı hizmet sağlayıcı", "büyük" ve "çok büyük" ETAHS kategorileri; reklam ve indirim bütçesi sınırları, kendi markalı ürün satış kısıtları, lisans alma ve lisans bedeli, veri taşınabilirliği ve eşit muamele yükümlülükleri devreye girer.
4. Sözleşmesel dağılım: ETAHS-ETHS arasındaki aracılık sözleşmesinde sorumluluk, komisyon, fikri haklar ve cezai şart denetlenir.
5. Yaptırım: 6563 m.12 idari para cezaları ve faaliyet durdurma/erişim engelleme riskleri.
İspat yükü: bildirimin usulüne uygunluğu hak sahibinde, gereğinin yapıldığı platformdadır.
Ara sonuç: kategori + tetiklenen yükümlülükler + sorumluluk eşiği.

## Çıktı modülleri
- ETAHS kategori ve yükümlülük haritası.
- Uyar-kaldır prosedürü ve cevap taslağı.
- Aracılık sözleşmesi risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

