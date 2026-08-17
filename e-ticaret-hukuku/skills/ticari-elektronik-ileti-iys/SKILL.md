---
argument-hint: ''
description: SMS, e-posta veya arama yoluyla gönderilen ticari iletilerde onay, ret
  hakkı ve İleti Yönetim Sistemi (İYS) yükümlülüklerinin denetlenmesi ya da bir yaptırım/şikâyet
  savunması hazırlanması gerektiğind
name: ticari-elektronik-ileti-iys
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


# Ticari Elektronik İleti ve İYS Uyumu

## Görev
6563 m.6-7 ve Ticari Elektronik İleti Yönetmeliği kapsamında ticari iletilerin onay, içerik, ret hakkı ve İYS (İleti Yönetim Sistemi) yükümlülüklerine uygunluğunu denetlemek; aykırılık halinde yaptırım riskini veya savunmayı kurmak.

## Soğuk başlangıç (intake)
- İleti türü ne: SMS, e-posta, sesli arama, anlık mesaj?
- Alıcı tüketici mi tacir/esnaf mı? (tacirlere önceden onay gerekmeyebilir)
- Onay nasıl alındı, İYS'ye kayıtlı mı, tarih/kanal kaydı var mı?
- İletilerde gönderici kimliği ve kolay ret imkânı yer alıyor mu?

## Denetim şeması
1. Onay kuralı (6563 m.6): ticari elektronik ileti, alıcılardan önceden onay alınarak gönderilir. Onayın yazılı ya da her türlü elektronik iletişim araçlarıyla alınması mümkündür; ispat yükü hizmet sağlayıcıdadır.
2. Tacir/esnaf istisnası (m.6/3): alıcının tacir veya esnaf olması halinde önceden onay aranmaksızın ileti gönderilebilir; ancak ret hakkı saklıdır.
3. İçerik ve ret (6563 m.7): iletide hizmet sağlayıcının tanıtıcı bilgileri ile iletinin niteliği (tanıtım, kampanya vb.) yer alır; alıcı dilediğinde, ücretsiz ve kolayca reddedebilir; ret bildirimi alındığında 3 iş günü içinde ileti durdurulur.
4. İYS yükümlülüğü: onaylar ve ret bildirimleri İleti Yönetim Sistemi'ne kaydedilir; İYS'de kaydı olmayan onaya dayanılarak gönderim yapılamaz. İYS üzerinden alıcı onay/ret durumunu sorgulayabilir.
5. Yaptırım: aykırılıkta 6563 m.12 uyarınca idari para cezası uygulanır; abonelik/kişisel veri boyutu varsa KVKK ile yarışma değerlendirilir.
İspat yükü: onayın varlığı ve İYS kaydı sağlayıcıdadır; ret talebinin gereği gibi işlendiği belgelenir.

## Çıktı modülleri
- İleti uyum kontrol listesi (onay-içerik-ret-İYS).
- Şikâyet savunması veya aykırılık tespit notu.
- Onay metni ve ret mekanizması taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

