---
argument-hint: ''
description: Bir birleşme, devralma, ortak girişim veya kontrol değişikliği işleminin
  Rekabet Kurulu iznine tabi olup olmadığını, bildirim eşiklerini ve esas inceleme
  riskini değerlendirmek istendiğinde kullanılır
name: birlesme-devralma-izni
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
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Birleşme ve Devralma İzni (m.7)

## Görev
İşlemin 4054 m.7 ve Birleşme/Devralma Tebliği (2010/4) kapsamında bildirime tabi bir yoğunlaşma oluşturup oluşturmadığını, ciro eşiklerini ve etkin rekabetin önemli ölçüde azalıp azalmayacağını değerlendirmek.

## Soğuk başlangıç (intake)
- İşlem türü: birleşme, hisse/varlık devri, ortak girişim kuruluşu?
- Kontrolde kalıcı değişiklik doğuyor mu (tek/ortak kontrol)?
- Tarafların Türkiye ve dünya ciroları yaklaşık ne düzeyde?
- Taraflar aynı pazarda rakip mi (yatay), tedarik zincirinde mi (dikey)?

## Denetim şeması
1. **Yoğunlaşma var mı (m.7, Tebliğ 2010/4)** — kontrolde kalıcı değişiklik gerekir. Geçici/finansal işlemler, grup içi yeniden yapılanmalar kural olarak yoğunlaşma sayılmaz. Tam işlevsel ortak girişimler bildirime tabidir.
2. **Bildirim eşikleri** — Tebliğ 2010/4'teki ciro eşiklerinin aşılıp aşılmadığı kontrol edilir (Türkiye ciroları ve taraf bazlı eşikler; teknoloji teşebbüsleri için özel eşik kuralı). **Eşik tutarları periyodik güncellendiğinden güncel Tebliğ metninden doğrulanır.**
3. **Zorunlu bildirim ve bekleme** — eşik aşılıyorsa işlem Kurul izni olmadan hukuken geçerlilik kazanmaz (m.7); izinden önce kapanış (gun-jumping) yaptırım riskidir.
4. **Esas inceleme** — etkin rekabetin özellikle hâkim durum yaratılması/güçlendirilmesi yoluyla önemli ölçüde azalıp azalmayacağı; yatay örtüşme, dikey/portföy etkileri, koordinasyon riski incelenir. HHI ve pazar payı eşikleri ön eleme aracıdır.
5. **Çözümler (taahhüt)** — rekabet endişesi varsa yapısal (elden çıkarma) veya davranışsal taahhütler sunulabilir; koşullu izin verilebilir.
6. **Ara sonuç** — bildirime tabi değil / koşulsuz izin beklenir / endişeli (taahhüt gerekli) / yasaklama riski şeklinde sonuçlandırılır.

## Çıktı modülleri
- Bildirim gerekliliği kararı ve eşik hesabı (güncel Tebliğ ile doğrulanacak).
- Yatay/dikey örtüşme ve risk haritası.
- Bildirim formu için bilgi/veri ihtiyaç listesi.
- Olası taahhüt senaryoları ve gun-jumping uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

