---
argument-hint: ''
description: Beşeri tıbbi ürün ruhsat başvurusu, varyasyon, ruhsat red/askı/iptali
  ve veri/dosya gizliliği konularında ruhsatlandırma yönetmeliği şartlarını denetlemek
  gerektiğinde kullanılır.
name: ilac-ruhsatlandirma
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Beşeri Tıbbi Ürün Ruhsatlandırma

## Görev
Bir beşeri tıbbi ürünün ruhsat başvurusu, varyasyonu veya ruhsat işlemine (red, askıya alma, iptal) karşı süreci Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği çerçevesinde değerlendirmek.

## Soğuk başlangıç (intake)
- Ürün orijinal mi, jenerik (eşdeğer) mi, biyobenzer mi; başvuru türü nedir?
- Hangi aşama: dosya değerlendirme, eksiklik yazısı, ruhsat reddi, askı, iptal, varyasyon reddi?
- TİTCK’nın gerekçesi nedir (etkililik/güvenlilik, GMP, dosya eksikliği, ruhsat sahibinin yükümlülüğü)?
- İşlemin tebliğ tarihi ve süre durumu?

## Denetim şeması
1. **Dayanak.** Beşeri Tıbbi Ürünler Ruhsatlandırma Yönetmeliği (RG 11.12.2021) ve 1262 sayılı Kanun m.1 vd. (ruhsatsız müstahzar yasağı); TİTCK’nın yetkisi 663 sayılı KHK’ya dayanır.
2. **Başvuru unsurları.** CTD formatında kalite, klinik, klinik-dışı modüller; jenerikte biyoeşdeğerlik ve referans ürünle kıyas; GMP uygunluğu. Ara sonuç: dosya tam mı, eksiklik yazısına süresinde cevap verildi mi?
3. **İdari işlem denetimi.** Ruhsat reddi/askısı/iptali idari işlemdir; yetki-şekil-sebep-konu-maksat yönünden incelenir. Sebep unsuru (bilimsel değerlendirme) teknik takdire dayanır; ancak takdir yetkisi ölçülülük ve eşitlikle sınırlıdır. İspat: idare sebebi (örn. güvenlilik sinyali) somut göstermelidir.
4. **Yargı yolu ve süre.** İptal davası Danıştay/idare mahkemesi; İYUK m.7 ile 60 gün; ivedi durumlarda yürütmenin durdurulması (İYUK m.27) — telafisi güç zarar ve açık hukuka aykırılık birlikte gösterilir.
5. **Veri ve dosya korunması.** Ruhsat dosyasındaki gizli bilgilerin korunması; jenerik başvurularda veri münhasıriyeti süreleri yönetmelik ve ilgili düzenlemelerden teyit edilir.

## Çıktı modülleri
- Başvuru/varyasyon eksiklik kontrol listesi.
- Ruhsat işlemine karşı iptal + yürütmeyi durdurma dilekçe iskeleti [doldurulacak].
- Bilimsel-teknik itiraz için bilirkişi/uzman görüşü planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

