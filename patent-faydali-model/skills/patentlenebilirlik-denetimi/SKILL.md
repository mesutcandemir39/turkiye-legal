---
argument-hint: ''
description: Bir buluşun yenilik, buluş basamağı ve sanayiye uygulanabilirlik şartlarını
  taşıyıp taşımadığı; patentlenebilir konu olup olmadığı tartışıldığında kullanılır;
  başvuru stratejisi ve hükümsüzlük analizi
name: patentlenebilirlik-denetimi
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Patentlenebilirlik Denetim Şeması

## Görev
Buluşun SMK m.82-83 patentlenebilirlik şartlarını (yenilik, buluş basamağı, sanayiye uygulanabilirlik) ve konu istisnalarını adım adım denetleyerek belge alabilirlik/ayakta kalabilirlik değerlendirmesi yapmak.

## Soğuk başlangıç (intake)
1. Buluşun çözdüğü teknik sorun ve teknik çözüm (istemler) nedir?
2. Başvuru/rüçhan tarihi ne; bu tarihten önce kamuya açıklama (sergi, yayın, satış, sunum) oldu mu?
3. En yakın bilinen teknik (prior art) ve fark nedir; araştırma raporu var mı?
4. Konu yazılım, iş yöntemi, tedavi usulü gibi istisnaya girer mi?

## Denetim şeması
1. **Konu denetimi.** SMK m.82/2-3: keşif, teori, matematiksel yöntem, estetik yaratma, iş yöntemi, bilgisayar programı "bu unsurlara ilişkin olduğu ölçüde" patentlenemez; m.82/3 kamu düzeni/ahlak, bitki-hayvan çeşitleri, insan/hayvan tedavi ve teşhis usulleri. Teknik katkı varsa istisna aşılabilir. Ara sonuç: konu patentlenebilir mi?
2. **Yenilik (SMK m.83/1-2).** Tekniğin bilinen durumu, başvuru/rüçhan tarihinden önce dünyada yazılı/sözlü/kullanım yoluyla erişilebilir kılınan her şeydir. Tek bir önceki belge istemin tüm özelliklerini içeriyorsa yenilik yok. Buluş sahibinin önceki açıklaması için m.84 grace period (12 ay) kontrol et.
3. **Buluş basamağı (SMK m.83/4).** İlgili alanda uzman kişiye göre tekniğin bilinen durumundan aşikâr çıkarılamama. Problem-çözüm yaklaşımı: en yakın teknik → objektif teknik problem → çözüm aşikâr mı? Faydalı modelde bu şart aranmaz.
4. **Sanayiye uygulanabilirlik (SMK m.83/6).** Tarım dahil sanayide üretilebilir/kullanılabilir olma.
5. **Yeterli açıklama (SMK m.92/4).** Tarifname, uzmanın buluşu uygulayabileceği açıklıkta olmalı; aksi halde belge alınsa da hükümsüzlük sebebi (m.138/1-b).

## Çıktı modülleri
- Şart şart patentlenebilirlik değerlendirmesi (geçti/geçmedi gerekçeli).
- Prior art - istem eşleştirme tablosu (yenilik/buluş basamağı için).
- Konu istisnası ve grace period notu.
- Belge alabilirlik / hükümsüzlük riski skoru.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

