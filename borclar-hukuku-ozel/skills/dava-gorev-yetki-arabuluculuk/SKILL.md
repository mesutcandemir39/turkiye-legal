---
argument-hint: ''
description: Sözleşme uyuşmazlığında hangi mahkemenin görevli ve yetkili olduğunu,
  dava şartı arabuluculuğun zorunlu olup olmadığını ve usul rotasını belirlemek gerektiğinde
  kullanılır.
name: dava-gorev-yetki-arabuluculuk
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dava Yolu — Görev, Yetki ve Dava Şartı Arabuluculuk

## Görev
İsimli sözleşme uyuşmazlığında görevli ve yetkili mahkemeyi, dava şartı arabuluculuk zorunluluğunu ve dava açma rotasını belirlemek; yanlış mahkeme/eksik arabuluculuk dava şartı eksikliğiyle usulden ret riski doğurur.

## Soğuk başlangıç (intake)
- Uyuşmazlığın konusu ve tarafların sıfatı (tacir, tüketici, gerçek kişi)?
- Talep para alacağı mı, tahliye mi, tespit mi?
- Sözleşmede yetki/tahkim şartı var mı?
- Daha önce arabuluculuğa/hakem heyetine başvuruldu mu?

## Denetim şeması
1. **Görevli mahkeme.** Genel kural Asliye Hukuk (HMK m.2). İstisnalar: kira ilişkisinden doğan davalar ve sözleşme konusu değere bakılmaksızın Sulh Hukuk (HMK m.4); iki tarafın da tacir olduğu ticari işlerde Asliye Ticaret (TTK m.4-5); tüketici işlemlerinde Tüketici Mahkemesi (6502 m.73), belirli tutar altında Tüketici Hakem Heyeti zorunlu.
2. **Yetkili mahkeme.** Genel yetki davalının yerleşim yeri (HMK m.6); sözleşmeden doğan davalarda sözleşmenin ifa yeri de yetkili (HMK m.10). Taşınmaza ilişkin ayni uyuşmazlıkta taşınmazın yeri kesin yetkili (HMK m.12).
3. **Dava şartı arabuluculuk.** Ticari davalarda konusu para olan alacak/tazminat talepleri için TTK m.5/A uyarınca arabuluculuk dava şartı; tüketici uyuşmazlıklarında 6502 m.73/A; kira (m.4 kapsamı) uyuşmazlıkları için de dava şartı arabuluculuk (7445 ile genişletilen kapsam) kontrol edilir. Başvurulmadan açılan dava usulden reddedilir.
4. **Tüketici hakem heyeti eşiği.** Yıllık güncellenen parasal sınır altındaki tüketici uyuşmazlıklarında hakem heyetine başvuru zorunlu; karara karşı tüketici mahkemesine itiraz (`[doğrulanacak: güncel tutar]`).
5. **Tahkim/yetki sözleşmesi.** Geçerli tahkim şartı varsa mahkeme yetkisizdir; yetki sözleşmesi yalnızca tacir/kamu tüzel kişileri arasında geçerli (HMK m.17).
6. **Ara sonuç.** Görev + yetki + ön şart (arabuluculuk/hakem heyeti) zinciri; dava açma sırası ve süre. İspat/itiraz: görev kamu düzeninden resen; yetki itirazı ilk itiraz olarak süresinde ileri sürülür.

## Çıktı modülleri
- Görev-yetki-ön şart karar ağacı.
- Arabuluculuk başvuru ve son tutanak kontrol notu.
- Doğru mahkemeye dava açma yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

