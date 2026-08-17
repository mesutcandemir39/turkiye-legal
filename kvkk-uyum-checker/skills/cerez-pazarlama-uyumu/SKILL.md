---
argument-hint: ''
description: Web sitesi çerezleri, çerez aydınlatması ve ticari elektronik ileti (İYS)
  süreçlerinin KVKK ve ilgili mevzuata uygunluğu denetlenirken kullanılır.
name: cerez-pazarlama-uyumu
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


# Çerez ve Pazarlama Uyumu Denetimi

## Görev
İki yüksek görünürlüklü uyum alanını denetlemek: (1) web sitesi/uygulama çerezlerinin ve çerez aydınlatmasının KVKK m.5/m.10 ve Kurul Çerez Rehberi'ne uygunluğu; (2) ticari elektronik ileti gönderiminin 6563 sayılı Kanun ve İYS (İleti Yönetim Sistemi) düzeninde olup olmadığı.

## Soğuk başlangıç (intake)
1. Sitede hangi çerezler var (zorunlu, analitik, pazarlama, üçüncü taraf)?
2. Çerez aydınlatma/rıza arayüzü var mı; ön işaretli kutu veya "kabul et" zorlaması var mı?
3. Pazarlama iletisi (SMS, e-posta, arama) gönderiliyor mu; alıcı onayı nasıl alındı?
4. İYS kaydı ve onay yönetimi yapılıyor mu?

## Denetim şeması
1. **Çerez tasnifi**: Zorunlu (işlevsel) çerezler için rıza aranmaz; analitik ve pazarlama/üçüncü taraf çerezler için açık rıza ve aydınlatma gerekir (Kurul Çerez Rehberi). Tüm çerezleri tek "kabul" altında toplayan banner kırmızı bulgudur.
2. **Rıza geçerliliği (m.3/1-a)**: Çerez rızası özgür, belirli ve bilgilendirilmiş olmalı; ön işaretli kutu, "kabul etmeden devam edemezsin" (cookie wall) ve reddi zorlaştıran tasarım geçersizdir.
3. **Aydınlatma (m.10)**: Çerez politikası; çerez türü, amacı, süresi, üçüncü taraf alıcıları ve hakların kullanımını içermeli.
4. **Ticari elektronik ileti (6563)**: İleti için önceden onay esastır (esnaf/tacir istisnaları ve mevcut müşteri sınırlı istisnası ayrı değerlendirilir); her iletide kolay ret (opt-out) imkânı bulunmalı.
5. **İYS kontrolü**: Onaylar İYS'ye yüklenmeli ve ret talepleri İYS üzerinden işlenmeli; İYS dışı gönderim yaptırım riskidir.
6. **Ara sonuç**: Çerez ihlali KVKK m.18, ileti ihlali 6563 idari para cezası kapsamındadır; iki rejim paralel işler.

İspat yükü: Çerez rızasının ve ileti onayının geçerli alındığını veri sorumlusu/gönderen kayıt ve İYS verisiyle ispatlar.

## Çıktı modülleri
- Çerez envanteri ve tasnif tablosu (zorunlu/rızaya tabi).
- Çerez banner ve politika uygunluk bulgu listesi.
- İYS onay/ret yönetimi ve ticari ileti uygunluk raporu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

