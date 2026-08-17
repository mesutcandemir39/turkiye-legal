---
argument-hint: ''
description: Bir veri ihlali (sızıntı, yetkisiz erişim, kayıp) yaşandığında ya da
  güvenlik tedbirleri denetlenirken; Kurul'a ve ilgili kişilere bildirim yükümlülüğü
  ve süreleri değerlendirilirken kullanılır.
name: veri-ihlali-bildirimi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Veri İhlali ve Güvenlik Yükümlülüğü

## Görev
KVKK m.12 kapsamında veri güvenliği tedbirlerini denetlemek ve bir veri ihlali gerçekleştiğinde Kurul'a ve ilgili kişilere bildirim sürecini, sürelerini ve içeriğini doğru yönetmek.

## Soğuk başlangıç (intake)
1. Ne oldu — yetkisiz erişim, sızıntı, kayıp, fidye yazılımı, yanlış alıcıya gönderim?
2. İhlal ne zaman, nasıl tespit edildi (tespit anı süreyi başlatır)?
3. Hangi kişi grupları ve veri kategorileri etkilendi, sayısı nedir?
4. Özel nitelikli veri veya finansal veri etkilendi mi (zarar riski yüksek olabilir)?

## Denetim şeması
1. **Güvenlik yükümlülüğü — m.12/1**: Veri sorumlusu, verinin hukuka aykırı işlenmesini ve erişilmesini önlemek, muhafazasını sağlamak için uygun teknik ve idari tedbirleri almak zorundadır. Kurul'un teknik-idari tedbirler rehberi ölçü alınır.
2. **Kurul'a bildirim — m.12/5**: İhlal öğrenildiği tarihten itibaren en kısa sürede ve 72 saat içinde Kurul'a bildirilir. Bildirim Kurul'un belirlediği form üzerinden yapılır; 72 saat aşılırsa gecikme gerekçesi açıklanır.
3. **İlgili kişiye bildirim**: İhlalden etkilenen kişiler de makul en kısa sürede bilgilendirilir; bu, ilgili kişilerin önlem almasını sağlamaya yöneliktir.
4. **İçerik**: Bildirimde ihlalin niteliği, etkilenen veri kategorileri ve kişi sayısı, olası sonuçlar, alınan/önerilen tedbirler ve irtibat bilgisi yer alır.
5. **Ara sonuç**: Bildirim yükümlülüğünün ihlali m.18 kapsamında ayrı bir yaptırım sebebidir; ihlal anından itibaren kanıt zinciri (loglar, müdahale kayıtları) korunmalıdır.

İspat yükü: Tedbirlerin alındığını ve bildirimin süresinde yapıldığını veri sorumlusu ispatlar; müdahale dokümantasyonu hem yaptırım hem tazminat davalarında belirleyicidir.

## Çıktı modülleri
- İhlal müdahale ve 72 saat takip cetveli.
- Kurul bildirim formu taslağı ([doldurulacak] alanlarla).
- İlgili kişi bilgilendirme metni ve etkilenen kayıt listesi şablonu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

