---
argument-hint: ''
description: Siber olay veya bilişim ihtilafında müvekkili, yönetim kurulunu, çalışanları
  veya etkilenen ilgili kişileri hukuken doğru ama anlaşılır biçimde bilgilendirmek
  ve bildirim metinleri kurmak gerektiğinde
name: muvekkil-iletisim-bilgilendirme
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil ve Paydaş İletişimi

## Görev
Teknik ve hukuki açıdan karmaşık bir siber olayı, ilgili paydaşlara (müvekkil/yönetim, çalışanlar, etkilenen ilgili kişiler, düzenleyici) doğru, ölçülü ve anlaşılır biçimde aktaracak iletişim metinlerini kurmak.

## Soğuk başlangıç (intake)
1. Muhatap kim? (yönetim kurulu, müvekkil, çalışanlar, etkilenen müşteriler, basın?)
2. Hangi mesaj zorunlu, hangisi ihtiyari? (yasal bildirim mi, bilgilendirme mi?)
3. Hassasiyet düzeyi ne? (devam eden tehdit, soruşturma gizliliği, itibar?)
4. Hangi olgular kesin doğrulanmış, hangileri henüz belirsiz?

## Denetim şeması
1. **Mesaj-muhatap eşleştirmesi.** Her paydaşa içerik ve dil ayarlanır: yönetime risk/karar odaklı, çalışanlara talimat odaklı, ilgili kişilere KVKK m.12/5 bildirim içeriği (ihlalin niteliği, etkilenen veriler, önlemler, başvuru kanalları), düzenleyiciye resmi ve eksiksiz.
2. **Doğruluk ve ölçü.** Sadece doğrulanmış olgular paylaşılır; belirsizlikler abartılmadan/küçümsenmeden ifade edilir. Sorumluluk doğurabilecek peşin kabul ifadelerinden kaçınılır; aynı zamanda yanıltıcı/eksik bilgi yaptırım riski yaratır.
3. **Gizlilik ve ayrıcalık.** Soruşturma gizliliği (CMK), avukat-müvekkil gizliliği ve ticari sır gözetilir; iç hukuki değerlendirme notları ile dışa açık bildirimler ayrılır.
4. **Eylem yönlendirmesi.** İlgili kişilere somut koruyucu adımlar (şifre değişimi, kart bloke, dolandırıcılık uyarısı) ve başvuru kanalı sunulur; çalışanlara müdahale talimatı verilir.
5. **Ara sonuç.** Hangi metnin kime, hangi kanaldan, hangi zamanlamayla gideceği ve hukuki onay gereği belirlenir. İçtihat/karar atfı yapılacaksa künye doğrulanır; doğrulanmamışsa `[DOĞRULANMADI]` işaretlenir.

## Çıktı modülleri
- Paydaş-mesaj matrisi ve zamanlama.
- İlgili kişi bilgilendirme / çalışan talimatı / yönetim brifing metinleri.
- Sade dil özeti ve hukuki onay/uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

