---
argument-hint: ''
description: Aydınlatma metni hazırlanırken, mevcut metnin KVKK m.10 ve Tebliğ'e uygunluğu
  denetlenirken veya aydınlatmanın açık rızadan ayrı tutulması gerektiğinde kullanılır.
name: aydinlatma-yukumlulugu
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


# Aydınlatma Yükümlülüğü ve Metin Tasarımı

## Görev
KVKK m.10 ve Aydınlatma Yükümlülüğünün Yerine Getirilmesinde Uyulacak Usul ve Esaslar Hakkında Tebliğ uyarınca aydınlatma metni üretmek veya mevcut metni denetlemek; aydınlatmayı açık rızadan ve diğer belgelerden ayrı, doğru zamanlamayla kurmak.

## Soğuk başlangıç (intake)
1. Aydınlatma hangi kanaldan, hangi anda yapılacak (web formu, işe alım, sözleşme imzası, çağrı merkezi)?
2. Hangi veri kategorileri ve işleme amaçları söz konusu?
3. Aktarım var mı; varsa kime ve hangi amaçla?
4. Aynı süreçte açık rıza da alınacak mı (ayrı belge gerekir)?

## Denetim şeması
1. **Zorunlu içerik — m.10/1**: (a) veri sorumlusunun ve varsa temsilcisinin kimliği, (b) işleme amacı, (c) aktarılabileceği alıcı/alıcı grupları ve amacı, (ç) toplama yöntemi ve hukuki sebebi, (d) m.11'deki haklar. Tebliğ bunların somut ve açık biçimde sayılmasını ister; "vb.", "gerektiğinde" gibi muğlak ifadeler eksiklik sayılır.
2. **Zamanlama**: Aydınlatma, verinin elde edilmesi sırasında yapılır; sonradan yapılan aydınlatma yükümlülüğü ihlal eder.
3. **Açık rızadan ayrılık**: Tebliğ m.5 gereği aydınlatma ile açık rıza tek metinde/tek onayda birleştirilemez; aydınlatma rıza şartına bağlanamaz (aydınlatma her hâlde zorunludur, rıza ise koşullu).
4. **Hukuki sebebin doğru gösterimi**: Metinde m.5/m.6'daki sebep, genel "açık rıza" ifadesiyle değil, işleme bazında gösterilmelidir.
5. **Ara sonuç**: Eksik veya geç aydınlatma m.18/1-a kapsamında idari para cezası riskidir; metin her işleme amacına göre güncellenmelidir.

İspat yükü: Aydınlatmanın usulüne uygun ve zamanında yapıldığını veri sorumlusu ispatlar; bu nedenle kayıt/onay logu tutulmalıdır.

## Çıktı modülleri
- m.10 unsurlarına göre yapılandırılmış aydınlatma metni taslağı ([doldurulacak] yer tutucularıyla).
- Aydınlatma-açık rıza ayrımı kontrol listesi.
- Kanal bazlı aydınlatma matrisi (web, işe alım, müşteri, ziyaretçi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

