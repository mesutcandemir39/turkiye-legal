---
argument-hint: ''
description: Ad üzerindeki hakka tecavüz, adın haksız kullanımı ya da haklı sebeple
  ad/soyad değiştirme veya nüfus kaydı düzeltme talebi gündeme geldiğinde kullanılır.
name: ad-soyad-degistirme
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Ad ve Soyadın Korunması ve Değiştirilmesi

## Görev
Ad üzerindeki hakkın korunmasını sağlamak (tecavüzün men'i/tespiti, tazminat) ya da haklı sebebe dayalı ad/soyad değiştirme veya nüfus kaydı düzeltme talebini doğru usul ve dayanakla kurmak.

## Soğuk başlangıç (intake)
- Talep koruma mı (başkası adımı haksız kullanıyor) yoksa değiştirme mi (kendi adımı değiştirmek istiyorum)?
- Değiştirme sebebi nedir: gülünç/incitici ad, fiilen kullanılan farklı ad, yabancı/yanlış yazım, dini/etnik aidiyet, cinsiyet, telaffuz güçlüğü?
- Adın kullanımından zarar/karışıklık doğuyor mu; somut örnek var mı?
- Nüfus kaydında maddi hata mı var (sehven yazım), yoksa irade ile değiştirme mi isteniyor?

## Denetim şeması
1. **Adın korunması** — TMK m.26: adının kullanılması çekişmeli olan kişi hakkının tespitini; adı haksız kullanılan kişi ise haksız kullanmanın önlenmesini, kusur varsa maddi-manevi tazminat ve kazancın iadesini isteyebilir. Tüzel kişinin adı/unvanı da kişilik hakkı kapsamında korunur.
2. **Ad değiştirme** — TMK m.27: haklı sebeplerin varlığında kişi, adının değiştirilmesini hâkimden isteyebilir; değişiklik nüfus siciline kaydolunur ve ilan edilir; değiştirmeden zarar gören bir yıl içinde dava açabilir. Haklı sebep takdiri hâkime aittir (gülünçlük, fiilî kullanım, aidiyet vb. yerleşik içtihatla kabul edilir).
3. **Görev ve usul** — Asliye hukuk mahkemesi görevlidir; ad değiştirme çekişmesiz yargıya yakın bir yapıda yürür (HMK m.382). Yetki: talep edenin yerleşim yeri (TMK m.19). Nüfus müdürlüğü hasım gösterilir.
4. **Nüfus kaydı düzeltme** — Maddi/sehven hatalarda 5490 sayılı Nüfus Hizmetleri Kanunu çerçevesinde idari düzeltme; çekişmeli/irade içeren değişiklikte mahkeme kararı gerekir.
5. **Soyadı** — Soyadı değişikliği de m.27 haklı sebep rejimine tabidir; aile soyadıyla bağ ve nüfus kaydının bütünlüğü gözetilir.

## Çıktı modülleri
- Talep türü ve dayanak (m.26 koruma / m.27 değiştirme) belirlemesi.
- Haklı sebep gerekçesi ve destekleyici delil listesi.
- Dilekçe iskeleti (görevli mahkeme, hasım nüfus müdürlüğü, talep sonucu).
- Yerleşik içtihat ilkesi atfı, künye `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

