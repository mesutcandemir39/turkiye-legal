---
argument-hint: ''
description: Bono ve poliçenin zorunlu şekil şartlarını, eksiklik sonuçlarını ve poliçeye
  özgü kabul/keşide ilişkilerini denetlemek; senedin kambiyo vasfını taşıyıp taşımadığını
  belirlerken kullanılır.
name: bono-police-unsurlar
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


# Bono ve Poliçe Unsurları

## Görev
Bono (emre muharrer senet) veya poliçenin zorunlu unsurlarını madde madde denetlemek, eksikliklerin kambiyo vasfına etkisini saptamak ve poliçede kabul ilişkisini çözümlemek.

## Soğuk başlangıç (intake)
- Senet "bono/emre muharrer senet" mi yoksa üç taraflı "poliçe" mi?
- Bedel, vade, lehtar, tanzim yeri-tarihi ve imza tam mı?
- Poliçede muhatap kabul etmiş mi; kabul kaydı var mı?
- Senet matbu form mu, beyaz/açık düzenleme şüphesi var mı?

## Denetim şeması
1. Bono şekil şartları: TTK m.776 — "bono/emre muharrer senet" ibaresi, kayıtsız şartsız belirli bedel ödeme vaadi, vade, ödeme yeri, lehtar, tanzim yeri-tarihi, düzenleyen imzası. Eksiklikte m.777 yorum kuralları (vade yoksa görüldüğünde, ödeme yeri yoksa tanzim yeri, tanzim yeri yoksa düzenleyen ad yanı). İmza ve bedel telafi edilemez; bunların yokluğu vasfı düşürür.
2. Poliçe şekil şartları: TTK m.671 — "poliçe" kelimesi, ödeme emri, muhatap, lehtar, vade, ödeme/keşide yeri-tarihi, keşideci imzası; eksiklik m.672.
3. Bono-poliçe yollaması: bonoya ciro, vade, ödeme, başvurma, protesto, zamanaşımı bakımından poliçe hükümleri uygulanır (TTK m.778).
4. Poliçede kabul: muhatap kabulle (m.691 vd.) asıl borçlu olur; kabul etmezse hamil vadeden önce başvurabilir (m.713). Bonoda düzenleyen, poliçede kabul eden gibi sorumludur (m.778/son).
5. Beyaz senet: açık atılan imzayla verilen senet anlaşmaya aykırı doldurulmuşsa def'i m.680; iyiniyetli hamile karşı ileri sürülemez.
6. Ara sonuç: tüm zorunlu unsurlar tamamsa senet kambiyo vasfını taşır ve kambiyo takibine elverişlidir; değilse adi yazılı delil olarak kalır.

## Çıktı modülleri
- Unsur denetim cetveli (madde-madde var/yok + dayanak).
- Eksikliğin telafi edilebilirliği ve sonuç değerlendirmesi.
- Gerekiyorsa beyaz senet/anlaşmaya aykırı doldurma savunma notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

