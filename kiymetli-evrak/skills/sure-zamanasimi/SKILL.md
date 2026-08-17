---
argument-hint: ''
description: İbraz, protesto, başvurma ve kambiyo zamanaşımı sürelerini hesaplamak
  ve takvimlemek; hak kaybı riskini değerlendirirken ve sebep alacağına geçiş gerektiğinde
  kullanılır.
name: sure-zamanasimi
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Çek Kanunu
    numara: '5941'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı

## Görev
Kambiyo senedine ilişkin tüm süreleri (ibraz, protesto, başvurma, zamanaşımı) doğru başlangıç anından hesaplamak, hak düşümü ve zamanaşımı risklerini saptamak ve gerektiğinde sebep alacağına geçişi planlamak.

## Soğuk başlangıç (intake)
- Senet tipi nedir (çek/bono/poliçe) ve vade/keşide tarihi nedir?
- İbraz, protesto ve karşılıksız işlem tarihleri nedir?
- Talep kime yöneliyor (asıl borçlu / ciranta / avalist) — süreler buna göre değişir.
- Zamanaşımını kesen/durduran işlem (takip, dava, ikrar) var mı?

## Denetim şeması
1. Çek ibraz süreleri: aynı yerde 10 gün, farklı yerde 1 ay (TTK m.796); sürede ibraz başvurma hakkı ve karşılıksız işlemi için şarttır.
2. Çek zamanaşımı: TTK m.808 — kural olarak 3 yıl (hamilin müracaat borçlularına ve borçluların birbirine karşı süreleri fıkralara göre); başlangıç ibraz süresinin bitiminden işler.
3. Poliçe/bono zamanaşımı: TTK m.749 — kabul edene/asıl borçluya karşı vadeden itibaren 3 yıl; hamilin cirantalar ve düzenleyene karşı protesto/vade tarihinden 1 yıl; cirantanın cirantaya/düzenleyene rücuu, senedi ödediği veya dava edildiği tarihten 6 ay.
4. Protesto/başvurma süreleri: ödememe protestosu ve başvurma süreleri (TTK m.714, m.722) tutulmazsa cirantalara müracaat hakkı düşer (m.730).
5. Kesme/durma: zamanaşımı dava açılması, takip, ödeme emri tebliği, borcun ikrarı gibi sebeplerle kesilir; kesilme yalnızca işlemin yöneldiği borçluya etki eder.
6. Ara sonuç — sebep alacağı: kambiyo zamanaşımı dolsa veya hak düşse bile temel ilişkiden doğan alacak (TBK genel zamanaşımı, kural 10 yıl, TBK m.146; bazı ilişkilerde 5 yıl m.147) ve sebepsiz zenginleşme talebi (TTK m.732) ayrıca değerlendirilir.

## Çıktı modülleri
- Süre/zamanaşımı takvim tablosu (her borçlu için ayrı).
- Hak düşümü/zamanaşımı risk uyarısı.
- Sebep alacağına geçiş notu (dayanak + zamanaşımı).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

