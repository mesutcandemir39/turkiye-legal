---
argument-hint: ''
description: Hangi yargı kolunda hangi dilekçe türünün yazılacağını saptamak, doğru
  iskeleti (HMK/İYUK/CMK) kurmak ve vakıa-hukuki sebep-talep sonucu omurgasını oturtmak
  gerektiğinde kullanılır.
name: layiha-mimarisi-ve-secim
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Layiha Mimarisi ve Dilekçe Türü Seçimi

## Görev
Somut talebe uygun yargı kolunu ve dilekçe türünü belirlemek; doğru biçim iskeletini seçip vakıa-hukuki sebep-talep sonucu omurgasını kurmak. Yanlış iskelet, baştan usulden ret veya hak kaybı doğurur; bu beceri tüm atölyenin giriş kapısıdır.

## Soğuk başlangıç (intake)
- Uyuşmazlık özel hukuk mu, idari mi, cezai mı? (taraflardan biri kamu idaresi mi?)
- İlk dilekçe mi, cevap/replik mi, yoksa kanun yolu (istinaf/temyiz) dilekçesi mi?
- Hak düşürücü süre veya dava açma süresi işliyor mu, son gün ne?
- Talep para alacağı mı, tespit mi, iptal mi, eda mı?

## Denetim şeması
1. Yargı kolu tespiti: Taraflardan biri idare ve uyuşmazlık idari işlem/eylemden doğuyorsa İYUK (2577) iskeleti. Suç isnadı varsa CMK (5271). Aksi halde HMK (6100). Karma durumlarda (ör. idari para cezasına itiraz) özel kanun yolunu kontrol edin (Kabahatler K. m.27 — sulh ceza hâkimliği).
2. Dilekçe türü: İlk dava (HMK m.119 / İYUK m.3), cevap (HMK m.126-129), replik-düplik (m.136), istinaf (HMK m.342 / İYUK m.45), temyiz (HMK m.361 / İYUK m.46).
3. İskelet seçimi: HMK m.119 zorunlu unsurları başlık olarak yerleştirin; idari dilekçede İYUK m.3 unsurları (idarenin işlemi, tarihi, tebliğ tarihi) eklenir.
4. Omurga: Vakıalar (numaralı, kronolojik) → her vakıaya delil → hukuki sebep (altlama) → talep sonucu. Ara sonuç: omurga eksiksizse türe özgü beceriye devredin.
5. İspat yükü ön kontrolü (HMK m.190): iddia eden ispatla yükümlüdür; vakıaları bu yüke göre seçin.

## Çıktı modülleri
- Yargı kolu + dilekçe türü kararı (gerekçeli, bir paragraf)
- Seçilen iskeletin başlık listesi (madde atıflı)
- Doldurulması gereken zorunlu unsur kontrol listesi
- İlgili türe özgü beceriye yönlendirme notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

