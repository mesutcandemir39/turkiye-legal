---
argument-hint: ''
description: Yetki tespiti/itirazi, toplu gorusme cagri yazisi, uyusmazlik tutanagi,
  grev karari, YHK basvurusu ve sendikal tazminat davasi gibi toplu is hukuku belgelerinin
  taslaklarini uretir; bir belge kaleme a
name: dilekce-ve-basvuru-taslaklari
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
  - ad: Sendikalar ve Toplu İş Sözleşmesi Kanunu
    numara: '6356'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe, Tutanak ve Başvuru Taslakları

## Görev
Toplu iş hukukunun tipik belgelerini doğru madde dayanağı ve usul mimarisiyle taslaklamak. Boş bırakılması gereken her yer `[doldurulacak]` ile işaretlenir; uydurma bilgi konmaz.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor (çağrı, itiraz dilekçesi, grev kararı, dava dilekçesi, YHK başvurusu)?
- Taraflar, işkolu, düzey ve tarihler nedir?
- Mahkeme/Bakanlık/YHK gibi muhatap kim?
- Dayanılacak temel vakıalar ve talep nedir?

## Denetim şeması
1. **Belge türünü ve dayanağını eşle:** Yetki itirazı → 6356 m.43 + HMK genel dilekçe unsurları (HMK m.119). TİS yorum/sendikal tazminat davası → HMK m.119 dava dilekçesi (taraflar, vakıa, hukuki sebep, deliller, talep sonucu). Çağrı/tutanak → 6356 m.46-47.
2. **Görevli/yetkili mercii doğrula:** Dava ve yetki itirazı İş Mahkemesi (7036 m.5); yetki tespiti başvurusu Bakanlık; menfaat uyuşmazlığında arabuluculuk (m.50) ve YHK (m.51).
3. **İskelet kur:** Başlık ve muhatap; taraf/vekil bilgileri `[doldurulacak]`; konu; açıklamalar (vakıa kronolojisi + madde altlaması); hukuki sebepler (6356 ilgili maddeleri, HMK); deliller; talep sonucu; tarih-imza.
4. **Süre uyarısı ekle:** İlgili hak düşürücü süre (örn. 6 işgünü itiraz) belge başında not düşülür.
5. **Doğrulama:** Madde numaraları ve tarihler kontrol edilir; içtihat anılacaksa künye `[DOĞRULANMADI]` ve kaynak (karararama.yargitay.gov.tr) belirtilir.

Ara sonuç: Eksiksiz bir taslak + doldurulacak alan listesi + süre uyarısı.

## Çıktı modülleri
- İstenen belgenin tam taslağı (`[doldurulacak]` yer tutucularıyla).
- Dayanak madde ve görevli mercii notu.
- Doldurulacak alan ve ek/delil kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

