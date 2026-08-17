---
argument-hint: ''
description: E-ticaret sitesi veya platformunun müşteri verisi işleme, açık rıza,
  aydınlatma, çerez ve veri aktarımı yükümlülüklerinin KVKK uyumunun denetlenmesi
  gerektiğinde kullanılır.
name: e-ticaret-kvkk-veri
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


# E-Ticarette Kişisel Veri ve KVKK Uyumu

## Görev
E-ticaret faaliyetinde toplanan kişisel verilerin (üyelik, sipariş, ödeme, davranışsal/çerez verisi) 6698 sayılı KVKK'ya uygun işlenmesini denetlemek; ticari ileti onayı ile KVKK rızasının ayrıştırılmasını sağlamak.

## Soğuk başlangıç (intake)
- Hangi veri kategorileri işleniyor (kimlik, iletişim, ödeme, konum, çerez/davranış)?
- İşlemenin hukuki sebebi ne (sözleşmenin ifası, meşru menfaat, açık rıza)?
- Yurt dışına aktarım var mı (yurt dışı ödeme/bulut/pazarlama araçları)?
- Aydınlatma metni, çerez politikası ve VERBİS kaydı mevcut mu?

## Denetim şeması
1. Hukuki sebep (6698 m.5): sipariş/teslim için işleme çoğu kez sözleşmenin ifası (m.5/2-c) ya da meşru menfaate (m.5/2-f) dayanır; pazarlama/profilleme için kural olarak açık rıza gerekir. Rıza, hizmet şartına bağlanamaz.
2. Aydınlatma (6698 m.10): veri sorumlusu kimliği, işleme amaçları, aktarım, toplama yöntemi ve hakları içeren aydınlatma yapılır; ticari ileti onayından ayrı belgelenir.
3. Ticari ileti–KVKK ayrımı: 6563 ileti onayı ile KVKK açık rızası farklı hukuki kurumlardır; tek kutucukla birlikte alınması sakıncalıdır, ayrı ayrı ve özgür iradeyle alınmalıdır.
4. Aktarım (6698 m.9): yurt dışı aktarımda 2024 değişikliği sonrası yeterlilik kararı, uygun güvenceler (standart sözleşme/bağlayıcı kurallar) ya da istisna zemini aranır; standart sözleşme Kurula bildirilir.
5. Güvenlik ve ihlal (6698 m.12): teknik-idari tedbirler; veri ihlalinde Kurula ve ilgili kişiye makul sürede bildirim.
İspat yükü: rıza, aydınlatma ve tedbirlerin varlığını veri sorumlusu ispatlar.

## Çıktı modülleri
- Veri işleme envanteri ve hukuki sebep tablosu.
- Aydınlatma/açık rıza/çerez metni boşluk raporu.
- Aktarım ve ihlal müdahale notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

