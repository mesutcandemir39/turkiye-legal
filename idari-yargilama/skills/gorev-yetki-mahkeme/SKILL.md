---
argument-hint: ''
description: Davanın idare mahkemesi, vergi mahkemesi yoksa ilk derece Danıştay'da
  görüleceğinin ve hangi yer mahkemesinin yetkili olduğunun belirlenmesinde kullanılır;
  yetki itirazı, gönderme kararı ve Danıştay i
name: gorev-yetki-mahkeme
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Görevli ve Yetkili Mahkemenin Belirlenmesi

## Görev
Davanın hangi ilk derece merciinde (idare mahkemesi, vergi mahkemesi veya ilk derece Danıştay) ve hangi yer mahkemesinde açılacağını belirlemek; yetkisizlik/görevsizlik halinde doğru usulü uygulamak.

## Soğuk başlangıç (intake)
- Uyuşmazlık vergi/gümrük/benzeri mali yükümlülükle mi ilgili?
- İşlem bir bakanlık/düzenleyici kurumun ülke geneli düzenleyici işlemi mi?
- İşlemi tesis eden idarenin bulunduğu yer ile işlemin uygulandığı yer neresi?
- Taşınmaza, kamu görevlisine veya tam yargıya ilişkin özel yetki kuralı var mı?

## Denetim şeması
1. **Görev — idare/vergi mahkemesi ayrımı** (2576 sayılı K. m.5-6): Vergi, resim, harç ve benzeri mali yükümlülükler ile bunların zam ve cezalarına ilişkin davalar **vergi mahkemesinde**; bunun dışındaki genel idari uyuşmazlıklar **idare mahkemesinde** görülür.
2. **İlk derece Danıştay görevi** (2575 sayılı K. m.24): Bakanlar Kurulu/Cumhurbaşkanı kararları, bakanlıkların düzenleyici işlemleri (yönetmelik vb.) ve kanunda sayılan ülke düzeyindeki işlemler ilk derece olarak Danıştay'da dava edilir.
3. **Yer yetkisi — genel kural** (İYUK m.32): Aksine hüküm yoksa yetkili mahkeme, dava konusu işlemi yapan **idari merciin bulunduğu yer** mahkemesidir.
4. **Özel yetki kuralları** (İYUK m.33-36): Kamu görevlilerine ilişkin işlemlerde görevlinin son görev yaptığı yer (m.33); taşınmaz mallara ilişkin davalarda taşınmazın bulunduğu yer (m.34); taşınır mallar ve tam yargı davalarında zararı doğuran işlem/eylemin yapıldığı yer veya ilgilinin ikametgâhı (m.35-36) gibi özel kurallar genel kurala önceliklidir.
5. **Görevsizlik/yetkisizlik** (İYUK m.15/1-a, m.43): Görev/yetki yönünden dava reddedilir ve dosya görevli/yetkili mahkemeye gönderilir; aynı yargı kolunda gönderme kararı verilir.
6. **Ara sonuç**: İki ayrı yer mahkemesi arasında yetki uyuşmazlığı çıkarsa bölge idare mahkemesi/Danıştay merci tayini ile çözer.

## Çıktı modülleri
- Görev (idare/vergi/Danıştay) tespiti
- Yetkili yer mahkemesi ve dayanak madde
- Yanlış mahkemeye açılma riski için gönderme senaryosu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

