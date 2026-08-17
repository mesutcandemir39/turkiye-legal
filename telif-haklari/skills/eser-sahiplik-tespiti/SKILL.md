---
argument-hint: ''
description: Bir fikir veya sanat ürününün FSEK anlamında eser olup olmadığını, türünü
  ve hak sahibinin kim olduğunu belirlemek gerektiğinde; korumanın eşiğini, hususiyet
  ölçütünü ve sahiplik karinelerini değerlen
name: eser-sahiplik-tespiti
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eser Niteliği ve Sahipliğin Tespiti

## Görev
Somut ürünün FSEK m.1/B ve m.2-6 anlamında korunan bir eser olup olmadığını, hangi türe girdiğini ve hak sahibinin kim olduğunu tespit etmek; aktif husumetin temelini kurmak.

## Soğuk başlangıç (intake)
- Ürün nedir (yazılım, fotoğraf, müzik, logo, makale, mimari proje, veri tabanı)?
- Kim, ne zaman, hangi koşullarda (hizmet/sipariş/serbest) meydana getirdi?
- Birden çok kişi katkı verdi mi; iş sözleşmesi/eser sözleşmesi var mı?
- Daha önce kamuya açıklanmış/yayımlanmış mı; üzerinde isim/işaret var mı?

## Denetim şeması
1. Tür eşleştirme: Ürün FSEK m.2 (ilim-edebiyat, yazılım dâhil), m.3 (musiki), m.4 (güzel sanat), m.5 (sinema) veya m.6 (işlenme/derleme) sayımına giriyor mu? Numerus clausus geçerlidir; sayıma girmeyen ürün eser olarak korunmaz.
2. Hususiyet (sübjektif unsur): Ürün "sahibinin hususiyetini" taşıyor mu (m.1/B-a)? Salt emek/yatırım yetmez; bağımsız yaratıcı seçim aranır. Fikirler, yöntemler, veriler tek başına korunmaz — koruma ifade biçimine bağlıdır.
3. Şekil verme/algılanabilirlik: Düşünce, dış dünyada algılanabilir biçime kavuşmuş mu? Sırf zihindeki tasarım korunmaz.
4. Sahiplik: Kural olarak eseri meydana getiren gerçek kişi sahiptir (m.8). İştirak hâlinde (ayrılmaz bütün) m.9; müşterek eserde m.10. Sahiplik karinesi: nüsha üzerindeki ad veya umuma arzdaki açıklama (m.11-12). Çalışan/memur eserinde mali hak kullanımı kural olarak işverene aittir (m.18/2), aksi sözleşme saklıdır.
5. Ara sonuç: Eser + tür + sahip belirlenir; eser değilse koruma reddi, sınai hak (6769 SMK) veya haksız rekabet (TTK m.54 vd.) alternatifi değerlendirilir.

İspat yükü: eser ve sahiplik iddiasını ileri sürende (HMK m.190); karine lehine olan tarafın işi kolaylaşır.

## Çıktı modülleri
- Eser/sahiplik analiz notu (tür, hususiyet gerekçesi, sahip ve dayanak madde).
- Sahiplik karinesi ve aktif husumet değerlendirmesi.
- Eser sayılmama hâlinde alternatif koruma yolları listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

