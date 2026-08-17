---
argument-hint: ''
description: Bankanın kuruluş/faaliyet izni, BDDK denetimi, idari para cezası, faaliyet
  kısıtlaması veya TMSF'ye devir gibi düzenleyici işlemleri değerlendirmek ve bunlara
  karşı idari yargı yolunu kurmak gerektiği
name: bddk-denetim-yaptirim
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
  - ad: Bankacılık Kanunu
    numara: '5411'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# BDDK Düzenlemesi, Denetimi ve İdari Yaptırımlar

## Görev
BDDK'nın düzenleyici/denetleyici işlemini (izin, tedbir, idari para cezası, faaliyet kısıtlaması, TMSF'ye devir) hukuka uygunluk yönünden değerlendirmek ve idari yargı yolunu kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: faaliyet izni başvurusu/reddi, uyarı/tedbir kararı, idari para cezası (5411 m.146 vd.), faaliyet kısıtlaması, faaliyet izninin kaldırılması (m.71) mı?
- İşlemin tebliğ tarihi ve dava açma süresi (İYUK m.7 — 60 gün) doluyor mu?
- Müvekkil banka mı, banka yöneticisi/ortağı mı, üçüncü kişi mi (ehliyet/menfaat)?
- İşlemin sebebi ve dayanağı (hangi 5411 hükmü) açık mı?

## Denetim şeması
1. **İşlem niteliği**: BDDK işlemi icrai bir idari işlemdir; iptal davasına konu olur. Unsur analizi yetki-şekil-sebep-konu-maksat (idari işlem unsurları) üzerinden yapılır.
2. **Dayanak ve ölçülülük**: İşlemin 5411'deki somut dayanağı (örn. kredi sınırı ihlali m.54, sermaye yeterliliği, sır ihlali) ve seçilen yaptırımın ölçülülüğü (Anayasa m.13) denetlenir. İdari para cezalarında 5411 m.146-153 çerçevesi ve usul güvenceleri (savunma alınması) aranır.
3. **Tedbir ve devir**: Faaliyet izninin kaldırılması (m.71) ve TMSF'ye devir ağır sonuçlu işlemlerdir; şartların gerçekleşip gerçekleşmediği ve usul güvenceleri sıkı denetlenir.
4. **Yargı yolu ve süre**: İptal/tam yargı davası İYUK 2577 uyarınca açılır; dava açma süresi kural olarak 60 gün (m.7), yürütmenin durdurulması (m.27) talep edilebilir. Görevli/yetkili mahkeme (Danıştay/idare mahkemesi) işlemin niteliğine göre belirlenir.
5. **İdari/adli ayrım**: Aynı fiil hem idari yaptırıma hem adli yaptırıma (örn. zimmet 5411 m.160) konu olabilir; her yol ayrı yürütülür. Ara sonuç olarak dava türü, süre, yürütmeyi durdurma gerekçesi ve iptal sebeplerini yaz. İçtihat için karararama.danistay.gov.tr esas alınır [DOĞRULANMADI].

## Çıktı modülleri
- İşlem hukuka uygunluk denetim tablosu (unsur unsur).
- İptal sebepleri ve yürütmeyi durdurma gerekçeleri.
- İdari dava dilekçesi iskeleti ve süre takvimi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

