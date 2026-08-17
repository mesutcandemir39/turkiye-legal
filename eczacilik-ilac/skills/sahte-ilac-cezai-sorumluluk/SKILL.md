---
argument-hint: ''
description: Sahte, taklit, kaçak veya bozulmuş ilaç, ruhsatsız ürün satışı ve sağlık
  için tehlikeli madde fiillerinde TCK ve 1262 sayılı Kanun kapsamında ceza sorumluluğunu
  değerlendirmek için kullanılır.
name: sahte-ilac-cezai-sorumluluk
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
  - ad: Hemşirelik Kanunu
    numara: '6197'
    tur: kanun
  - ad: Mimar ve Mühendisler Hakkında Kanun
    numara: '1262'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sahte ve Kaçak İlaç — Cezai Sorumluluk

## Görev
Sahte/taklit/kaçak/bozulmuş ilaç veya ruhsatsız ürün fiilinde uygulanacak ceza normunu belirlemek, unsurları ve isnadı denetlemek.

## Soğuk başlangıç (intake)
- Fiil: sahte/taklit ilaç imali mi, ruhsatsız müstahzar satışı mı, kaçak (gümrük dışı) ilaç mı, bozulmuş ilaç mı?
- Şüpheli sıfatı: üretici, ithalatçı, ecza deposu, eczacı, internet satıcısı?
- Ürün insan sağlığı için tehlike doğurdu mu; analiz/bilirkişi raporu var mı?
- Soruşturma aşaması: arama-el koyma, ifade, iddianame?

## Denetim şeması
1. **Norm seçimi.** Kişilerin hayatını ve sağlığını tehlikeye sokacak biçimde bozulmuş/değiştirilmiş/sahte ilaç → TCK m.187 (bozulmuş veya değiştirilmiş gıda/ilaç); ruhsatsız/taklit müstahzar → 1262 sayılı Kanun m.18-19 cezai hükümleri; kaçak ilaç → 5607 sayılı Kaçakçılıkla Mücadele Kanunu da gündeme gelir.
2. **Unsur denetimi.** Tipiklik (sahtelik/bozulma/ruhsatsızlık), kast (TCK m.21), fail sıfatı; ara sonuç: hangi norm hangi sıfata uyuyor, fikri içtima (TCK m.44) var mı?
3. **İspat ve delil.** Numune analiz raporu, TİTCK/ATK bilirkişi raporu, İTS/karekod kayıtları, ele geçen ürün-fatura zinciri. İspat yükü iddia makamında; lehe delil ve zincirdeki kopukluk savunma argümanı.
4. **İdari-cezai ayrım.** Aynı fiil hem TİTCK idari yaptırımı hem ceza soruşturması doğurabilir; non bis in idem ve idari/cezai sürecin ayrılığı değerlendirilir.
5. **Usul.** CMK çerçevesinde arama-el koymanın hukuka uygunluğu, delil yasakları, sağlık riski varsa bilirkişi zorunluluğu.

## Çıktı modülleri
- Norm-unsur eşleştirme tablosu.
- Savunma stratejisi ve delil itirazları notu.
- İdari-cezai sürecin eşgüdüm haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

