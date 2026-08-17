---
argument-hint: ''
description: Önaraştırma, yerinde inceleme, soruşturma açılması, savunma yazıları
  ve sözlü savunma gibi Rekabet Kurulu önündeki idari süreçte hak ve süreleri yönetmek
  istendiğinde kullanılır.
name: sorusturma-usulu-savunma
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


# Rekabet Kurulu Soruşturma Usulü ve Savunma

## Görev
4054 m.40-55 çerçevesinde Rekabet Kurumu/Kurulu önündeki sürecin aşamalarını, teşebbüsün usuli haklarını ve savunma stratejisini yönetmek; yerinde inceleme ve bilgi taleplerine hukuka uygun yanıt vermek.

## Soğuk başlangıç (intake)
- Süreç hangi aşamada: önaraştırma, yerinde inceleme yapıldı mı, soruşturma açıldı mı, soruşturma raporu tebliğ edildi mi?
- Teşebbüse tebliğ edilen belge ve tanınan süre nedir?
- Yerinde incelemede zorluk çıkarma/engelleme riski oluştu mu?
- Pişmanlık veya uzlaşma yolu gündemde mi?

## Denetim şeması
1. **Önaraştırma (m.40)** — Kurum şikâyet/resen bilgiyle önaraştırma yapar; bu aşamada henüz taraf savunması zorunlu değildir, ancak işbirliği tonu önemlidir.
2. **Yerinde inceleme (m.15)** — Kurum yetkilileri defter, belge ve elektronik kayıtları inceleyebilir; engelleme/yanlış-eksik bilgi nispi para cezası ve ihlal karinesini güçlendirme riski doğurur (m.16). Yasal sınırlar ve mesleki sır savunması dikkatle yönetilir.
3. **Soruşturma açılması (m.41)** — Kurul soruşturma açarsa teşebbüse bildirilir; ilk yazılı savunma için süre tanınır.
4. **Savunma hakkı ve dosyaya erişim (m.43-44)** — soruşturma raporu tebliğinden sonra yazılı savunma; eşit silah ilkesi gereği iddia ve delillere erişim sağlanır. Süreler hak düşürücüdür; kaçırılması savunmasız kalma sonucunu doğurabilir.
5. **Sözlü savunma toplantısı (m.46)** — talep hâlinde yapılır; iddialar ve savunmalar Kurul önünde tartışılır.
6. **Nihai karar ve yaptırım (m.16, m.52)** — ihlal tespiti hâlinde ciro üzerinden idari para cezası; kararın gerekçesiyle tebliği. Pişmanlık (kartelde) ve Uzlaşma Yönetmeliği kapsamında indirim/erken bitirme imkânları değerlendirilir.

## Çıktı modülleri
- Süreç aşaması ve süre takvimi (hak düşürücü tarihler işaretli).
- Yerinde inceleme yanıt protokolü ve sır savunması notu.
- Yazılı/sözlü savunma iskeleti ve argüman önceliklendirme.
- Pişmanlık/uzlaşma fizibilite değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

