---
argument-hint: ''
description: Tüketici kredisi, konut finansmanı ve bağlı kredilerde sözleşme şartlarını,
  cayma hakkını, erken ödeme indirimini, masraf/ücret iadesini ve temerrüt sonuçlarını
  değerlendirmek gerektiğinde kullanılır.
name: tuketici-kredisi-konut-finansmani
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


# Tüketici Kredisi ve Konut Finansmanı

## Görev
Tüketici kredisi ve konut finansmanı sözleşmelerini TKHK rejimine göre denetlemek; cayma, erken ödeme indirimi, haksız masraf/ücret iadesi, bağlı kredi sonuçları ve temerrüt halinde muacceliyet kurallarını altlamak.

## Soğuk başlangıç (intake)
- Kredi türü ne (ihtiyaç/tüketici, konut finansmanı, bağlı kredi)?
- Sözleşme tarihi, tutar, faiz ve tahsil edilen masraflar neler?
- Tüketici cayma, erken ödeme, masraf iadesi ya da temerrüze itiraz mı istiyor?
- Kredi bir mal/hizmet alımıyla bağlantılı mı (bağlı kredi)?

## Denetim şeması
1. **Sözleşme şartı (TKHK m.22-23):** Tüketici kredisi sözleşmesi yazılı şekilde kurulur; zorunlu unsurları içermeyen sözleşmenin geçersizliği tüketici aleyhine ileri sürülemez. Tüketicinin imzaladığı nüshanın verilmesi zorunludur.
2. **Cayma (m.24):** Tüketici 14 gün içinde gerekçe göstermeden krediden cayabilir; anaparayı ve tahakkuk eden faizi azami 30 gün içinde geri öder.
3. **Erken ödeme (m.27):** Tüketici borcun tamamını veya bir kısmını erken ödeyebilir; bu halde gerekli faiz ve komisyon indirimi yapılır.
4. **Masraf/ücret denetimi (m.4, m.5):** Tüketiciden alınan ve sözleşmede açıkça öngörülmeyen ya da hizmet karşılığı olmayan masraf/ücretler haksızdır; iadeye konu olur. Dosya masrafı, hesap işletim ücreti gibi kalemler somut olarak denetlenir.
5. **Bağlı kredi (m.30):** Kredi belirli bir mal/hizmet alımı için verilmişse ve mal/hizmet hiç ya da gereği gibi teslim edilmezse, tüketici satıcı ve kredi veren karşısında haklarını kullanabilir; bağlı kredide kredi veren de sorumluluk üstlenir.
6. **Konut finansmanı (m.32-35) ve temerrüt:** Konut finansmanında muacceliyet için kanunda öngörülen ardışık taksit ve ihtar koşulları (m.34) aranır; bu koşullar oluşmadan tüm borç muaccel kılınamaz.
7. **Ara sonuç:** Hangi hak süre içinde, hangi masraf iadesi mümkün, temerrüt usulüne uygun mu?

## Çıktı modülleri
- Masraf/ücret iade hesabı.
- Cayma veya erken ödeme bildirimi taslağı.
- Bağlı kredi sorumluluk analizi.
- Temerrüt/muacceliyet itiraz argümanları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

