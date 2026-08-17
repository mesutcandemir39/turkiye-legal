---
argument-hint: ''
description: Sendikanin TIS yapma yetkisini, isyeri/isletme/iskolu barajlarini, yetki
  tespiti basvurusunu ve yetki belgesini ele alir; sendikanin coklugu, baraj ve yetki
  belgesi sorunlarinda kullanilir.
name: tis-yetki-tespiti
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


# Toplu İş Sözleşmesi Yetkisi ve Yetki Tespiti

## Görev
Bir sendikanın TİS yapma yetkisini barajlar üzerinden değerlendirmek, yetki tespiti sürecini yürütmek ve yetki belgesine giden yolu kurmak. Toplu pazarlığın kapısıdır.

## Soğuk başlangıç (intake)
- Hangi işkolu, hangi işyeri/işletme düzeyi?
- İşyerinde/işletmede toplam işçi sayısı ve sendika üye sayısı nedir?
- Sendikanın işkolu barajını (%1) tutan güncel istatistiği var mı?
- Daha önce yetki tespiti veya itiraz oldu mu?

## Denetim şeması
1. **İşkolu barajı:** 6356 m.41/1 — sendikanın kurulu bulunduğu işkolundaki işçilerin en az **%1**inin üyesi olması (geçici m.6 ile geçmişte farklı oranlar uygulanmıştı; güncel %1). Baraj, Bakanlığın Ocak/Temmuz işkolu istatistik tebliğleriyle saptanır.
2. **İşyeri/işletme çoğunluğu:** 6356 m.41/1 — işyeri TİS için o işyerindeki işçilerin **yarıdan fazlasının (%50+1)**; işletme TİS için işletme kapsamındaki işçilerin **%40**ının üyesi olmak.
3. **Yetki tespiti başvurusu:** 6356 m.42 — sendika Çalışma ve Sosyal Güvenlik Bakanlığına başvurur; Bakanlık tespiti tarafların kayıtlarına göre yapar ve ilgililere bildirir.
4. **Yetki itirazı:** 6356 m.43 — taraflar veya işveren, tespite karşı kararın tebliğinden itibaren **6 işgünü** içinde görevli mahkemeye (İş Mahkemesi) itiraz edebilir; itiraz, kayıt yetersizliği veya başka sendikanın çoğunluğu gibi nedenlere dayanır.
5. **Yetki belgesi:** 6356 m.44 — itiraz süresi geçtikten veya itiraz reddedildikten sonra Bakanlık yetki belgesi verir. Belge alınmadan TİS bağıtlanamaz.
6. **Ara sonuç:** Barajlar tutuyorsa yetki tespiti talep edilir; tartışmalıysa kayıt düzeltme / itiraz stratejisi kurulur.

İspat: üyelik kayıtları (e-Devlet, sendika defterleri), Bakanlık istatistikleri ve işyeri işçi sayısı belirleyicidir.

## Çıktı modülleri
- Baraj hesap tablosu (işkolu %1, işyeri %50+1 / işletme %40).
- Yetki tespiti başvuru veya yetki itirazı dilekçesi iskeleti.
- Süre/usul takvimi (6 işgünü itiraz, tebligat tarihleri).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

