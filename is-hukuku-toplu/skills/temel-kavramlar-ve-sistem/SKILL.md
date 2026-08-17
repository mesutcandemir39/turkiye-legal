---
argument-hint: ''
description: Toplu iş hukukunun çatısını, sendika-TIS-uyusmazlik ucgenini ve 6356
  sayili Kanunun yapisini kavramak; bir sorunun toplu mu bireysel mi, hak mi menfaat
  uyusmazligi mi oldugunu nitelendirmek gerektigin
name: temel-kavramlar-ve-sistem
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


# Temel Kavramlar ve Sistematik

## Görev
Toplu iş hukukunun üç sütununu (sendika özgürlüğü, toplu iş sözleşmesi, toplu uyuşmazlık) tanıtmak ve önündeki olayı doğru kategoriye yerleştirmek. Yanlış nitelendirme tüm usul yolunu sakatlar; bu beceri ilk süzgeçtir.

## Soğuk başlangıç (intake)
- Taraflar kim: işçi/sendika/işveren/işveren sendikası mı?
- Uyuşmazlık mevcut bir TİS'in yorum-uygulamasından mı (hak), yoksa yeni TİS şartlarından mı (menfaat) doğuyor?
- İşyeri/işletme düzeyi ne; hangi işkolundasınız?
- Yürürlükte TİS var mı, süresi nedir?

## Denetim şeması
1. **Toplu mu bireysel mi?** Talep kişisel işçilik alacağıysa (kıdem, fazla mesai) bireysel iş hukukudur (4857). Örgütlenme, TİS, grev/lokavt söz konusuysa 6356 uygulanır. Sendikal tazminat (6356 m.25) bireysel sonuç doğursa da toplu hukukun güvencesidir.
2. **Hak mı menfaat uyuşmazlığı mı?** TİS m.36 anlamında mevcut sözleşmenin yorumu/ihlali = hak uyuşmazlığı → yargı yolu (İş Mahkemesi). Yeni veya yenilenecek TİS'in içeriği = menfaat uyuşmazlığı → toplu görüşme, arabuluculuk (m.50), grev/lokavt.
3. **Düzey belirleme:** 6356 m.34 — TİS işyeri, işletme (aynı işkolundaki birden çok işyeri) veya grup düzeyinde yapılabilir. Bir işyerinde aynı dönemde yalnızca bir TİS yürürlükte olabilir.
4. **İşkolu:** 6356 m.2 ve İşkolları Yönetmeliği. İşkolu, hem sendika faaliyet alanını hem baraj hesabını belirler; yanlış işkolu yetki tespitini çökertir.
5. **Ara sonuç:** Olay (a) bir TİS'in normatif/borç doğuran hükmünün ihlali mi, (b) örgütlenme/güvence sorunu mu, (c) yeni TİS pazarlığı mı? Cevaba göre ilgili uzmanlık becerisine yönlendirilir.

İspat yükü: sendikal nedenin varlığında işçi iddiayı ortaya koyar, işveren feshin başka geçerli nedene dayandığını ispatlar (6356 m.25/7-8 mantığı).

## Çıktı modülleri
- Nitelendirme notu (toplu/bireysel, hak/menfaat, düzey, işkolu).
- İlgili 6356 madde haritası.
- Sonraki adım ve görevli/yetkili mercii önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

