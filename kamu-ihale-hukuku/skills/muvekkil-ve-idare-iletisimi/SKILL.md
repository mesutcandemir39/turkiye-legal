---
argument-hint: ''
description: İstekli müvekkile süreci sade anlatmak, idareye/KİK'e yazılacak resmi
  yazıların tonunu ve içeriğini kurmak veya bilgi/belge talep yazıları hazırlamak
  gerektiğinde kullanılacak iletişim becerisidir.
name: muvekkil-ve-idare-iletisimi
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil ve İdare İletişimi

## Görev
İhale sürecinin teknik ve süre-yoğun adımlarını müvekkile anlaşılır biçimde aktarmak; idareye, KİK'e ve ilgili mercilere gönderilecek resmi yazışmaları doğru ton ve içerikle hazırlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim: müvekkil (istekli/idare), karşı idare, KİK?
2. İletişimin amacı: bilgilendirme, bilgi/belge talebi, şikâyet, savunma?
3. Süre baskısı var mı; yazının resmî kayda girmesi mi gerekiyor?
4. Hangi hukuki sonuç hedefleniyor (süre koruma, delil temini, uzlaşma)?

## Denetim şeması
1. **Müvekkil bilgilendirmesi:** Sürecin nerede olduğu, atılacak adım, hak düşürücü süreler ve olası sonuçlar sade dille; teknik terim açıklanarak aktarılır. Gerçekçi beklenti yönetimi yapılır, kesin sonuç vaadinden kaçınılır.
2. **İdareye yazışma (şikâyet/talep):** Saydamlık ilkesi (m.5) çerçevesinde bilgi/belge talebi; şikâyet dilekçesinde işlem, tarih, hukuki aykırılık ve talep açık biçimde, m.55'e uygun olarak yazılır. Resmî kayıt/tebliğ tarihi delil değeri taşır.
3. **KİK'e yazışma:** İtirazen şikâyet dilekçesi m.56'ya uygun; başvuru ehliyeti, süre, iddia ve dayanak somut belgeyle bağlanır, başvuru bedeli dekontu eklenir.
4. **Ton ve üslup:** Resmî, ölçülü, kişiselleştirmeden uzak; iddialar belgeye dayandırılır, suçlayıcı/abartılı dil kullanılmaz.
5. **Ara sonuç:** Her yazışma için muhatap, kanal (EKAP/yazılı), kayıt yöntemi ve süre etkisi belirlenir.

İspat yükü: Yazışmanın gönderim/tebliğ tarihi mutlaka kayda bağlanır.

## Çıktı modülleri
- Müvekkile durum özeti (sade dil) ve adım listesi.
- İdareye/KİK'e resmi yazı taslağı (talep + dayanak + ek).
- Yazışma kayıt ve süre etkisi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

