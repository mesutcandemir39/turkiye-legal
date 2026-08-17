---
argument-hint: ''
description: Kamu görevlilerinin işlediği zimmet, irtikâp, rüşvet ve görevi kötüye
  kullanma suçlarının unsurlarını, görevli sıfatını ve etkin pişmanlığı değerlendirmek
  gerektiğinde kullanılır.
name: kamu-idaresine-karsi-suclar
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kamu İdaresine Karşı Suçlar (Zimmet, Rüşvet, Görevi Kötüye Kullanma)

## Görev
Kamu görevlilerinin görevle bağlantılı suçlarında fail sıfatını, fiilin niteliğini ve görevi kötüye kullanma ile özel suçlar arasındaki sınırı madde metniyle belirlemek.

## Soğuk başlangıç (intake)
- Fail kamu görevlisi mi (TCK m.6/1-c anlamında)?
- Fiil zilyetliği görev nedeniyle devredilmiş malın mal edinilmesi mi, menfaat temini mi, görevin gereklerine aykırılık mı?
- Bir menfaat anlaşması (rüşvet) var mı, yoksa görevlinin baskısıyla mağdurdan menfaat mi sağlandı (irtikâp)?
- Bir kamu zararı veya kişilerin mağduriyeti/haksız menfaati doğdu mu?

## Denetim şeması
1. Fail sıfatı: Bu suçlar özgü suçtur; fail kamu görevlisi olmalıdır (TCK m.6). Sıfat yoksa zimmet yerine güveni kötüye kullanma (m.155) gündeme gelebilir.
2. Zimmet (TCK m.247): Görevi nedeniyle zilyetliği devredilen veya koruma ile görevlendirilen malın mal edinilmesi. Suçun açığa çıkmamasını sağlamaya yönelik hileli davranış nitelikli hal (m.247/2). Kullanma zimmeti daha az ceza (m.247/3). Etkin pişmanlıkla iade m.248.
3. İrtikâp (TCK m.250): Görevin sağladığı nüfuzun kötüye kullanılarak kişinin hataya düşürülmesi veya icbar yoluyla menfaat sağlanması/vaadi alınması. İcbar/ikna/hatadan yararlanma biçimlerini ayır.
4. Rüşvet (TCK m.252): Görevin gereklerine aykırı veya uygun bir iş için kamu görevlisi ile iş sahibi arasında menfaat anlaşması; veren ve alan ayrı cezalandırılır. Etkin pişmanlık m.254 (durumu bildirme şartları farklı).
5. Görevi kötüye kullanma (TCK m.257): Tamamlayıcı/ikincil suç. Görevin gereklerine aykırı hareketle kişilerin mağduriyeti, kamu zararı veya haksız menfaat doğması şarttır; daha özel bir suç (zimmet, rüşvet, irtikâp) oluşuyorsa m.257 uygulanmaz.
6. Ara sonuç: Fail sıfatı tespiti + uygulanacak özel suç veya tamamlayıcı m.257 + etkin pişmanlık imkânı + soruşturma izni (4483 sayılı Kanun) gerekip gerekmediği.

## Çıktı modülleri
- Fail sıfatı ve suç tipi belirleme notu (madde atıflı).
- Zimmet/rüşvet/irtikâp/m.257 sınır ayrımı.
- Etkin pişmanlık ve soruşturma izni süreç notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

