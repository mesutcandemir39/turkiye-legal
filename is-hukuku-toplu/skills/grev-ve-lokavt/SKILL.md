---
argument-hint: ''
description: Kanuni grev ve lokavt karar/uygulama usulunu, grev yasaklarini ve ertelemeyi,
  kanun disi grevin sonuclarini ele alir; grev karari alma, grev yasagi/erteleme veya
  kanun disi grev iddiasi durumlarinda k
name: grev-ve-lokavt
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


# Grev ve Lokavt Hukuku

## Görev
Kanuni grev/lokavt kararının alınması, uygulanması, yasak ve erteleme rejimi ile kanun dışı grevin hukuki sonuçlarını denetlemek. En yüksek riskli aşamadır; usul hatası fesih ve tazminat doğurur.

## Soğuk başlangıç (intake)
- Arabuluculuk tutanağı tutuldu mu, tarihi nedir?
- İşkolu/işyeri grev yasağı kapsamında mı (örn. can/mal güvenliği, bankacılık, kamu hizmeti)?
- Grev kararı alındı mı, ilan ve uygulama tarihleri nedir?
- Bir erteleme kararı söz konusu mu?

## Denetim şeması
1. **Kanuni grev şartı:** 6356 m.58-60 — grev ancak menfaat uyuşmazlığında, arabuluculuk aşaması tüketildikten ve uyuşmazlık tutanağı tebliğinden itibaren **60 gün** içinde alınan kararla, **6 işgünü** önce karşı tarafa bildirilerek uygulanabilir. Bu unsurlar yoksa grev kanun dışıdır.
2. **Lokavt:** 6356 m.60 — işverenin kanuni grev kararına karşı uygulayabileceği savunma aracı; benzer usul ve sürelere tabidir.
3. **Grev yasakları:** 6356 m.62 — can ve mal kurtarma, cenaze/mezarlık, şehir suyu-elektrik-gaz-petrol üretim/dağıtımı, bankacılık (sınırlı), hastaneler, itfaiye gibi işlerde/yerlerde grev ve lokavt yasaktır; bu uyuşmazlıklar **yüksek hakem kuruluna** gider (m.51).
4. **Grev erteleme:** 6356 m.63 — genel sağlığı veya millî güvenliği bozucu nitelikteki grev/lokavt, Cumhurbaşkanı kararıyla **60 gün** ertelenebilir; erteleme sonunda anlaşma yoksa uyuşmazlık YHK'ye gider.
5. **Kanun dışı grev sonuçları:** 6356 m.64-67 — kanun dışı grevde işveren, iş sözleşmelerini haklı nedenle feshedebilir; sendika ve işçiler zarardan sorumlu olabilir. Grev oylaması (m.61) yapılabileceği unutulmaz.

İspat: tutanak tarihleri, ilan ve bildirim belgeleri, oylama tutanağı belirleyicidir.

## Çıktı modülleri
- Grev/lokavt usul ve süre kontrol listesi (60 gün karar, 6 işgünü bildirim).
- Grev yasağı / erteleme değerlendirme notu.
- Kanun dışı grev risk ve sonuç analizi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

