---
argument-hint: ''
description: İnfaz hukukunun temel kavramlarını, kesinleşmiş ilamın infaz kabiliyetini,
  hapis ile adli para cezası infazı ayrımını ve infaz türlerinin sistematiğini netleştirmek
  gerektiğinde kullanılır.
name: infaz-temel-kavramlar
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İnfaz Hukuku Temel Kavramlar ve Sistematik

## Görev
Bir ceza ilamının infaz boyutunu sistematik biçimde çerçevelemek: hangi ceza türünün, hangi rejimle, hangi kanun maddesine göre infaz edileceğini ve infaz sürecinin haritasını çıkarmak.

## Soğuk başlangıç (intake)
- Elinde kesinleşmiş bir ilam var mı; kesinleşme tarihi nedir?
- Ceza türü ne: hapis mi, adli para cezası mı, güvenlik tedbiri mi?
- Suç tarihi ve suç tipi nedir (oranları etkiler)?
- Birden fazla ilam/içtima var mı; hükümlü tutuklu/firari mi?
- İlam infaza verilmiş mi, çağrı kâğıdı tebliğ edilmiş mi?

## Denetim şeması
1. İnfaz kabiliyeti: İnfaz yalnızca kesinleşmiş ve infaz edilebilir bir ilama dayanır (5275 m.4). Kesinleşmemiş veya HAGB'li (CMK m.231) bir hüküm doğrudan infaz edilmez; HAGB'de denetim süresi rejimi işler. Ara sonuç: ilam infaz kabiliyeti taşıyor mu?
2. Ceza türünü ayır:
   - Hapis cezası: 5275 m.19 vd. çağrı, m.14 açık/kapalı kurum rejimi.
   - Adli para cezası: 5275 m.106; ödenmezse hapse çevrilir, ancak kamuya yararlı işe çevirme ve taksitlendirme imkânları değerlendirilir.
   - Güvenlik tedbiri: TCK m.53 (hak yoksunlukları), m.54-55 (müsadere) infaz boyutu.
3. Rejim seçimi: kısa süreli hapis cezası ise TCK m.50 seçenek yaptırımları ve m.51 erteleme uygulanmış mı kontrol et; bunlar infaz tarzını kökten değiştirir.
4. İspat yükü: infaz lehine talepte (mahsup, denetimli serbestlik) dayanak belgeleri hükümlü tarafı sunar; infaz hesabı resen Cumhuriyet savcılığınca yapılır.
5. Ara sonuç: ceza türü + rejim + dayanak madde üçlüsü netleşince infaz takvimi kurulabilir.

## Çıktı modülleri
- İnfaz haritası tablosu (ceza türü, dayanak madde, rejim, sorumlu makam).
- Eksik belge ve doğrulanacak nokta listesi.
- Bir sonraki uzman beceriye yönlendirme (hesap, koşullu salıverilme, başvuru).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

