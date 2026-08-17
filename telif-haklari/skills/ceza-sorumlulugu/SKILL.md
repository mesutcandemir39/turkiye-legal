---
argument-hint: ''
description: Eser, icra, fonogram veya yapım üzerindeki hakların ihlalinin suç oluşturup
  oluşturmadığını ve şikâyet sürecini değerlendirmek gerektiğinde; FSEK m.71-75 suç
  tiplerini, şikâyet şartını ve savunmayı ku
name: ceza-sorumlulugu
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Telif Hakkı İhlalinde Ceza Sorumluluğu

## Görev
İhlalin FSEK m.71 vd. anlamında suç oluşturup oluşturmadığını belirlemek, şikâyet sürecini ve cezai savunmayı kurmak.

## Soğuk başlangıç (intake)
- İhlal eylemi nedir (izinsiz çoğaltma, yayma, satışa arz, umuma iletim, ad belirtmeme)?
- Eylem ticari boyutta mı; kazanç/yayma var mı?
- Şikâyet süresi (fiilin ve failin öğrenilmesi) işledi mi?
- Hak sahibi/yetkili meslek birliği şikâyetçi mi?

## Denetim şeması
1. Suç tipi (m.71): Manevi, mali veya bağlantılı hakları ihlal eden eylemler — eseri izinsiz işleme/çoğaltma/yayma/temsil/umuma iletim, ad belirtmeme, eseri başkasının eseri gibi gösterme/intihal, korsanla mücadele kapsamı. Eylemin kanuni tarife birebir uyması (kanunilik, TCK m.2) aranır.
2. Manevi unsur: Kasıt aranır (TCK m.21); taksirle ihlal kural olarak cezalandırılmaz. Hata ve kusurluluk değerlendirilir (TCK m.30).
3. Hukuka uygunluk: Hak sahibinin izni, FSEK m.30-40 istisnaları (şahsen kullanma m.38, iktibas m.35, haber m.37) tipikliği veya hukuka aykırılığı kaldırabilir.
4. Şikâyet ve süre (m.75): Bu suçlar kural olarak şikâyete bağlıdır; şikâyet, fiil ve failin öğrenilmesinden itibaren işleyen süreye tabidir (TCK m.73 — altı ay). Yetkili şikâyetçi (hak sahibi/meslek birliği) ve şikâyetin geri alınması sonuçları değerlendirilir.
5. Görev ve uzlaşma: Fikri ve Sınai Haklar Ceza Mahkemesi (yoksa görevlendirilen ağır ceza/asliye ceza) görevlidir (m.76). Şikâyete bağlı suç olması nedeniyle uzlaştırma (CMK m.253) gündeme gelir.
6. Ara sonuç: Suç var/yok, şikâyet geçerliliği, savunma ekseni ve hukuk davasıyla koordinasyon belirlenir.

İspat yükü: ceza yargılamasında suçun ispatı iddia makamında; şüpheden sanık yararlanır. İzin/istisna savunması ileri sürülür ve değerlendirilir.

## Çıktı modülleri
- Suç tipi ve unsur analizi (m.71, kasıt, hukuka uygunluk).
- Şikâyet süresi ve yetkili şikâyetçi kontrolü.
- Şikâyet/şikâyetten vazgeçme veya savunma dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

