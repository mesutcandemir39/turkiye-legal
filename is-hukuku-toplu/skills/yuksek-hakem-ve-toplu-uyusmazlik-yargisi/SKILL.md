---
argument-hint: ''
description: Grev yasagi veya erteleme hallerinde Yuksek Hakem Kuruluna basvuruyu,
  kurulun TIS yerine gecen kararini ve toplu hak uyusmazliklarinin yargi yolunu ele
  alir; YHK sureci veya TIS yorum davasi gerektigi
name: yuksek-hakem-ve-toplu-uyusmazlik-yargisi
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


# Yüksek Hakem Kurulu ve Toplu Uyuşmazlık Yargısı

## Görev
Grevin yasak veya ertelenmiş olduğu menfaat uyuşmazlıklarında Yüksek Hakem Kurulu (YHK) yolunu, kurulun TİS hükmündeki kararını ve toplu hak uyuşmazlıklarının yargısal çözümünü yönetmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık grev yasağı kapsamında mı veya erteleme mi yapıldı?
- Arabuluculuk/erteleme süreci tamamlandı mı?
- Sorun yeni TİS şartı mı (menfaat) yoksa mevcut TİS yorumu mu (hak)?
- Tarafların YHK'ye başvuru iradesi/zorunluluğu var mı?

## Denetim şeması
1. **YHK'ye başvuru halleri:** 6356 m.51 — grev ve lokavtın yasak olduğu uyuşmazlıklarda, arabuluculukta anlaşma sağlanamazsa taraflardan biri YHK'ye başvurur; grevin ertelendiği ve erteleme sonunda anlaşma olmayan hallerde de YHK devreye girer (m.63 yollamasıyla).
2. **Kurulun kararı:** YHK kararı **kesindir ve toplu iş sözleşmesi hükmündedir**; tarafları normatif olarak bağlar. Bu nedenle YHK aşaması fiilen TİS'in içeriğini belirler.
3. **Toplu hak uyuşmazlığı yargısı:** TİS'in yorumu, uygulanması veya ihlalinden doğan uyuşmazlık hak uyuşmazlığıdır → **İş Mahkemesi** görevlidir (7036 sayılı Kanun m.5). Bu davalarda TİS m.36 ışığında normatif/borç doğurucu hüküm ayrımı yapılır.
4. **Yetki itirazı ve diğer davalar:** Yetki tespitine itiraz (6356 m.43), TİS'in tarafı sıfatının tespiti, sendikal tazminat davaları da İş Mahkemesinde görülür; kararlara karşı istinaf (BAM) ve sınırlı temyiz yolu işler.
5. **Ara sonuç:** Menfaat uyuşmazlığı + grev yasağı/erteleme = YHK; mevcut TİS'ten doğan anlaşmazlık = İş Mahkemesi.

İçtihat için karararama.yargitay.gov.tr (9./22. HD, HGK); künyeler `[DOĞRULANMADI]`.

## Çıktı modülleri
- Yol ayrımı şeması (YHK mı, İş Mahkemesi mi).
- YHK başvuru dilekçesi iskeleti.
- TİS yorum davası dava planı (vakıa-hüküm-talep).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

