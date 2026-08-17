---
argument-hint: ''
description: Bir spor kararına itiraz veya dava açma yolunu belirlemek, federasyon
  iç hukuk yolu, tahkim kurulu, CAS ve istisnai yargı/AYM seçeneklerini ve sıralarını
  çıkarmak gerektiğinde kullanın.
name: federasyon-tahkim-yargi-yolu
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
  - ad: Çalışma ve Sosyal Güvenlik Bakanlığı Kuruluş ve Görevleri Hakkında Kanun
    numara: '7405'
    tur: kanun
  - ad: Tıbbi Deontoloji Tüzüğü Hakkında Kanun
    numara: '6222'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Federasyon, Tahkim Kurulu ve Yargı Yolu Haritası

## Görev
Bir spor kararına (disiplin, transfer, uygunluk, idari) karşı izlenecek itiraz ve dava yolunu sırasıyla belirlemek; iç hukuk yolu, federasyon tahkim kurulu, CAS ve istisnai devlet yargısı/AYM seçeneklerini görev-yetki ve süre ekseninde haritalamaktır.

## Soğuk başlangıç (intake)
1. Karar hangi merciden çıktı (disiplin kurulu, yönetim kurulu, federasyon)?
2. Karar tebliğ tarihi nedir; itiraz/başvuru süresi başladı mı?
3. Futbol mu, başka branş mı?
4. Milletlerarası unsur (FIFA, uluslararası federasyon) var mı?
5. İç başvuru yolları tüketildi mi?

## Denetim şeması
1. **İç hukuk yolu**: Çoğu federasyonda önce disiplin kurulu kararına karşı federasyon içi itiraz/üst kurul yolu tüketilir. Tüketilmeden tahkime gidilemez.
2. **Tahkim Kurulu**: Futbolda **5894 sayılı Kanun m.6** uyarınca TFF Tahkim Kurulu nihai ve kesin mercidir; kararlarına karşı kural olarak yargı yolu kapalıdır. Diğer branşlarda 3289 sayılı Kanun ve federasyon ana statüsündeki tahkim kurulu görevlidir.
3. **Süre**: Tahkim başvuru süreleri talimatlarda kısadır (genelde tebliğden itibaren günlerle); hak düşürücü kabul edilir, kaçırılması başvuruyu reddettirir.
4. **Milletlerarası boyut**: FIFA/uluslararası federasyon organları kararlarına karşı **CAS** (Lozan) yolu; CAS kararının iptali sınırlı olarak İsviçre Federal Mahkemesi önünde gündeme gelir.
5. **İstisnai devlet yargısı/AYM**: Tahkim kararlarının kesinliği nedeniyle devlet yargısı kural olarak kapalıdır; ancak adil yargılanma/mülkiyet gibi temel hak ihlali iddiasıyla **AYM bireysel başvurusu** (6216 sayılı Kanun) gündeme gelebilir; süre ve başvuru yolu tüketme şartları kontrol edilir.
6. **Ara sonuç**: Akış şeması (merci → süre → bir sonraki adım) ve uygulanabilir/uygulanamaz yollar netleştirilir.

## Çıktı modülleri
- Yol haritası şeması (merci → süre → karar türü)
- Süre takvimi (tebliğ tarihinden geriye sayım)
- Başvuru/itiraz dilekçesi iskeleti
- İçtihat notu `[DOĞRULANMADI]`



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

