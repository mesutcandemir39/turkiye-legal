---
argument-hint: ''
description: Suçun tamamlanmadığı, icra hareketlerine başlanıp netice gerçekleşmediği
  durumlarda teşebbüs ile gönüllü vazgeçme ayrımını ve ceza sonuçlarını belirlemek
  gerektiğinde kullanılır.
name: tesebbus-gonullu-vazgecme
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
  version: 0.1.0
user-invocable: true
---


# Teşebbüs ve Gönüllü Vazgeçme

## Görev
İcra hareketlerine başlanmış fakat netice gerçekleşmemiş suçlarda teşebbüs (TCK m.35), gönüllü vazgeçme (m.36) ve elverişsiz teşebbüs ayrımlarını yapıp ceza sonucunu belirlemek.

## Soğuk başlangıç (intake)
- Hazırlık hareketleri mi yapıldı, yoksa icraya başlandı mı?
- Suç neden tamamlanmadı; failin elinde olmayan bir engel mi araya girdi?
- Fail kendi iradesiyle mi durdu, yoksa dış etkenle mi engellendi?
- Kullanılan araç/yöntem neticeyi gerçekleştirmeye elverişli miydi?

## Denetim şeması
1. **İcraya başlama eşiği (m.35/1):** Failin elverişli araçlarla doğrudan doğruya icraya başlaması gerekir; hazırlık hareketleri kural olarak cezalandırılmaz. Ara sonuç: eşik aşıldı mı?
2. **Tamamlanamama nedeni:** Suç, failin elinde olmayan nedenlerle tamamlanamadıysa teşebbüs gündeme gelir.
3. **Teşebbüste ceza (m.35/2):** Meydana gelen zarar/tehlikenin ağırlığına göre cezada indirim; ağırlaştırılmış müebbet/müebbet hapsi gerektiren suçlarda kademeli indirim öngörülür.
4. **Gönüllü vazgeçme (m.36):** Fail icra hareketlerinden gönüllü vazgeçer ya da neticeyi kendi çabasıyla önlerse, teşebbüsten cezalandırılmaz; yalnız o ana kadarki hareketler bağımsız bir suç oluşturuyorsa o suçtan sorumlu olur. Ara sonuç: durma gönüllü mü, dış engel mi?
5. **Elverişsiz teşebbüs / işlenemez suç:** Araç ya da konu neticeyi doğurmaya mutlak elverişsizse cezalandırılabilirlik tartışılır; somut tehlike ölçütü değerlendirilir.
6. **İçtima ile ilişki:** Tamamlanan başka bir suç varsa ayrıca değerlendirilir.

## Çıktı modülleri
- Hazırlık/icra/teşebbüs/gönüllü vazgeçme aşama haritası.
- İndirim oranı ve hesap notu.
- Gönüllü vazgeçme savunması taslağı (somut argümanlarla).
- Eksik vakıa ve `[DOĞRULANMADI]` içtihat listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

