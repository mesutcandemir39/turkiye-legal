---
argument-hint: ''
description: ÇED/izin iptali dava dilekçesi, idari para cezasına itiraz, çevresel
  tazminat dilekçesi, idareye başvuru ve çevresel taahhüt/uyum sözleşmesi taslaklarını
  üretmek gerektiğinde; vakıa-hukuki sebep-talep
name: dilekce-basvuru-taslaklari
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
  - ad: Çevre Kanunu
    numara: '2872'
    tur: kanun
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe, Başvuru ve Sözleşme Taslakları

## Görev
Çevresel uyuşmazlığa uygun dava dilekçesi, idari başvuru/itiraz ve sözleşme metinlerini doğru usul kalıbı ve madde dayanaklarıyla üretmek; eksik bilgileri [doldurulacak] yer tutucularıyla işaretlemek.

## Soğuk başlangıç (intake)
1. Hangi metin: iptal/tam yargı dilekçesi, idari para cezasına itiraz, tazminat dilekçesi, idareye başvuru, uyum/taahhüt sözleşmesi?
2. Taraflar, işlem/karar künyesi ve dayanak madde nedir?
3. Talep sonucu net mi (iptal, yürütmenin durdurulması, tazminat tutarı, el atmanın önlenmesi)?
4. Eldeki deliller (ÇED dosyası, ölçüm, tutanak, bilirkişi) nelerdir?

## Denetim şeması
1. **Usul kalıbını seç**: İdari dava → 2577 sayılı İYUK m.3 unsurları (taraflar, konu, sebepler, deliller, talep). Adli dava → 6100 sayılı HMK m.119 zorunlu unsurları. İdari para cezası itirazında görevli mercie göre dilekçe formatı belirlenir.
2. **Mimari**: Vakıa → hukuki sebep (somut madde: 2872 ilgili maddesi, ÇED/izin yönetmeliği, İYUK/HMK) → talep sonucu zinciri kurulur; her vakıa bir delile bağlanır.
3. **Acil talepler**: İdari dilekçede yürütmenin durdurulması (İYUK m.27), adli dilekçede ihtiyati tedbir (HMK m.389) ve delil tespiti gerekçeli olarak eklenir.
4. **Sözleşme metinleri**: Çevresel taahhüt, uyum yol haritası, atık devir/bertaraf veya saha rehabilitasyon sözleşmelerinde sorumluluk dağılımı, tazminat/cezai şart (TBK m.179) ve emredici çevre yükümlülüklerinin sözleşmeyle bertaraf edilemeyeceği gözetilir.
5. **İspat ve ara sonuç**: Delil dizini ve ispat yükü dağılımı dilekçede açıkça kurulur; içtihat atıfları yalnızca doğrulanmış künye ile, aksi halde [DOĞRULANMADI] işaretiyle eklenir.

## Çıktı modülleri
- Seçilen metin türüne uygun dilekçe/başvuru iskeleti
- Vakıa-hukuki sebep-talep tablosu ve delil dizini
- Acil talep (YD/ihtiyati tedbir) bölümü
- Sözleşme/taahhüt taslağı ve risk maddeleri ([doldurulacak] yer tutuculu)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

