---
argument-hint: ''
description: Mesafeli satış sözleşmesi, ön bilgilendirme formu, üyelik/kullanım koşulları,
  aracılık sözleşmesi veya açık rıza/onay metni gibi e-ticaret belgelerinin hazırlanması
  ya da revize edilmesi gerektiğinde
name: e-ticaret-sozlesme-taslagi
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


# E-Ticaret Sözleşme ve Metin Taslakları

## Görev
E-ticaret faaliyetinin ihtiyaç duyduğu belgeleri (mesafeli satış sözleşmesi, ön bilgilendirme formu, kullanım koşulları, aracılık sözleşmesi, ileti onayı, aydınlatma metni) mevzuata uygun ve [doldurulacak] yer tutucularıyla üretmek.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor; taraflar B2C mi B2B mi?
- Müvekkil hizmet sağlayıcı mı, aracı platform mu?
- Konu mal mı hizmet mi dijital içerik mi (cayma istisnaları)?
- Ödeme, teslim, iade ve uyuşmazlık çözüm tercihi nedir?

## Denetim şeması
1. Zorunlu içerik eşlemesi: mesafeli satış sözleşmesi ve ön bilgilendirme formu için 6502 m.48 ve Mesafeli Sözleşmeler Yönetmeliği'nin asgari içerik listesi (taraflar, mal/hizmet nitelikleri, toplam fiyat, ödeme/teslim, cayma hakkı ve istisnaları, şikâyet mercii) madde madde doldurulur.
2. 6563 uyumu: kullanım koşullarına bilgi verme (m.3), sözleşme öncesi teknik adımlar ve hata düzeltme (m.4), sipariş teyidi (m.5) hükümleri işlenir.
3. Emredici sınır denetimi: tüketici aleyhine, cayma hakkını kaldıran veya hakem heyeti/mahkeme yolunu engelleyen haksız şartlar (6502 m.5) elenir; aracılık sözleşmesinde ETAHS yükümlülükleriyle çelişen kayıtlar düzeltilir.
4. KVKK/ileti metinleri: açık rıza ve aydınlatma ayrı belgelenir; ticari ileti onayı İYS uyumlu kurgulanır.
5. Uyuşmazlık ve yürürlük: yetki/tahkim, uygulanacak hukuk, yürürlük ve değişiklik bildirimi maddeleri eklenir; tüketici sözleşmelerinde zorunlu yargı yolu saklı tutulur.
İspat ve saklama: sözleşme/onayın kalıcı veri saklayıcısında tutulması ve erişilebilirliği sağlanır.

## Çıktı modülleri
- Belge taslağı ([doldurulacak] alanlarla).
- Zorunlu içerik kontrol listesi.
- Haksız/eksik şart revizyon notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

