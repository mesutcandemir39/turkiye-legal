---
argument-hint: ''
description: Olaya uygulanacak açık bir kural bulunamadığında ya da var olan kural
  amacına aykırı biçimde eksik kaldığında; boşluğun türünü belirleyip TMK m.1/2-3
  uyarınca kural kurmak için kullanılır.
name: kanun-boslugu-ve-hukuk-yaratma
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
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kanun Boşluğu ve Hâkimin Hukuk Yaratması

## Görev
Boşluğun varlığını ve türünü doğru teşhis etmek, doldurma aracını seçmek ve gerekirse TMK m.1 uyarınca hâkimin koyacağı kuralı genelleştirilebilir biçimde formüle etmek.

## Soğuk başlangıç (intake)
- Olaya doğrudan uyan bir hüküm var mı; yoksa benzer bir ilişkiye dair hüküm var mı?
- Susan kanun gerçekten mi susuyor, yoksa "aksiyle kanıt" ile bilinçli bir tercih mi (suskunluk = kural)?
- Konu emredici/kanunilik alanı mı (ceza, vergi: kıyas yasağı)?
- Örf-âdet hukuku veya yerleşik içtihat var mı?

## Denetim şeması
1. **Boşluk var mı?** Önce yorumla (lafzî+amaçsal) çözümü dene. Susmanın bilinçli olduğu hâllerde *argumentum a contrario* uygulanır; bu durumda boşluk yoktur.
2. **Boşluğun türü** — (a) Gerçek (açık) boşluk: hiç kural yok. (b) Örtülü/kanun içi boşluk: kural var ama amacı, kapsamı dışına taşmasını gerektiriyor; burada amaca uygun daraltma (teleolojik redüksiyon) veya genişletme yapılır.
3. **Kaynak sırası — TMK m.1**: Önce kanun (yorum/kıyas), sonra örf ve âdet hukuku (sürekli uygulama + genel inanç + yaptırım gücü), sonra hâkimin kuralı.
4. **Doldurma araçları** — Kıyas (benzer olaya konan kuralın taşınması), evleviyet (*a maiore ad minus / a minore ad maius*), TMK m.5 ile genel hükümlerin yayılması, hukukun genel ilkeleri (dürüstlük, ahde vefa, sebepsiz zenginleşme yasağı).
5. **Hukuk yaratma — TMK m.1/2-3 ve m.4**: Hâkim kanun koyucu gibi, hak ve nısfetle, bilimsel görüş ve içtihattan yararlanarak kural kurar. Kural; somut olayı aşan, her benzer olayda aynı sonucu verecek genellikte olmalıdır.
6. **Sınır** — Anayasa m.138 (hâkimin hukuka bağlılığı) ve kanunilik ilkesi; ceza/vergide aleyhe kıyas ve hukuk yaratma yasaktır.

## Çıktı modülleri
- Boşluk teşhisi: var/yok, türü, gerekçe.
- Seçilen araç (kıyas/evleviyet/genel ilke) ve uygulanışı.
- Önerilen kural lafzı + genelleştirilebilirlik testi.
- Karşı görüş ve `[DOĞRULANMADI]` içtihat yeri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

