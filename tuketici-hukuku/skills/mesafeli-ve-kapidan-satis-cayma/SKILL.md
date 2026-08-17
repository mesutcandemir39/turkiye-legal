---
argument-hint: ''
description: İnternetten, telefonla veya iş yeri dışında kurulan sözleşmelerde tüketicinin
  cayma hakkını, 14 günlük süreyi, istisnaları ve iade/geri ödeme yükümlülüklerini
  değerlendirmek gerektiğinde kullanılır.
name: mesafeli-ve-kapidan-satis-cayma
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mesafeli ve Kapıdan Satış — Cayma Hakkı

## Görev
İnternet, telefon, posta gibi uzaktan iletişim araçlarıyla (mesafeli) ya da iş yeri dışında (kapıdan) kurulan sözleşmelerde tüketicinin cayma hakkını altlamak; ön bilgilendirme yükümlülüğünü, sürenin başlangıcını, istisnaları ve karşılıklı iade borçlarını belirlemek.

## Soğuk başlangıç (intake)
- Sözleşme nasıl kuruldu (internet sitesi, telefon, kapıda, fuar)?
- Mal mı hizmet mi; teslim/ifa ne zaman gerçekleşti?
- Tüketiciye ön bilgilendirme ve cayma formu verildi mi?
- Tüketici ne zaman cayma iradesini bildirdi ya da bildirmek istiyor?

## Denetim şeması
1. **Nitelendirme:** Mesafeli sözleşme (TKHK m.48) tarafların fiziksel karşı karşıya gelmeksizin uzaktan iletişim araçlarıyla kurduğu sözleşmedir; iş yeri dışında sözleşme (m.47) satıcının olağan iş yeri dışında kurulur. Her ikisinde de cayma rejimi uygulanır.
2. **Ön bilgilendirme:** Satıcı/sağlayıcı, cayma hakkı ve şartları dahil zorunlu bilgileri Yönetmeliğe uygun vermek zorundadır. Bilgilendirme eksikse cayma süresi uzar (kural olarak bir yıl uzayabilir; eksik gideren bildirimden itibaren 14 gün işler).
3. **Cayma süresi:** Kural 14 gün. Mallarda süre teslim günü, hizmetlerde sözleşme günü esas alınarak başlar; tüketici gerekçe göstermeden ve cezai şart ödemeden cayabilir (m.48/4).
4. **İstisnalar (Yönetmelik):** Tüketicinin istekleri doğrultusunda kişiselleştirilen mallar, çabuk bozulan/son kullanma tarihi geçebilecek ürünler, açılınca iadesi sağlık/hijyen açısından uygun olmayan ürünler, dijital içerik (ifaya başlanmışsa) ve benzeri hallerde cayma hakkı yoktur; bu istisna somut olaya uygulanmalıdır.
5. **İade ve geri ödeme:** Cayma bildiriminin ulaşmasından itibaren satıcı 14 gün içinde tüm ödemeleri iade eder; tüketici malı 10 gün içinde geri gönderir. İade masrafına ilişkin bilgilendirme yoksa masraf satıcıya aittir.
6. **Ara sonuç:** Cayma süresi içinde mi, istisna kapsamında mı, geri ödeme yükümlülüğü doğdu mu?

## Çıktı modülleri
- Cayma hakkı değerlendirme notu (süre, istisna).
- Cayma bildirimi taslağı.
- Geri ödeme/iade takvimi.
- Bilgilendirme eksikliğine dayalı argüman seti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

