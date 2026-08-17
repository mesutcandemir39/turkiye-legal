---
argument-hint: ''
description: İhale sürecindeki bir işleme karşı idareye şikâyet ve Kamu İhale Kurumuna
  itirazen şikâyet başvurusunun süre, şekil ve içerik yönünden hazırlanması gerektiğinde
  kullanılacak temel usul becerisidir.
name: sikayet-ve-itirazen-sikayet
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
  - ad: Koruma Amaçlı Imar Planları Hakkında Kanun
    numara: '4734'
    tur: kanun
  - ad: Tarih Medeniyetini Koruma Kanunu
    numara: '4735'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Şikâyet ve İtirazen Şikâyet (KİK Yolu)

## Görev
İhale işlemlerine karşı zorunlu idari başvuru yolunu (idareye şikâyet → KİK'e itirazen şikâyet) süre ve şekil şartlarına uygun kurmak; başvuru ehliyeti ve menfaat ilişkisini denetlemek.

## Soğuk başlangıç (intake)
1. Şikâyete konu işlem ne ve hangi tarihte öğrenildi/bildirildi?
2. Başvuran istekli/istekli olabilecek/aday sıfatını taşıyor mu (menfaat)?
3. İdareye şikâyet yapıldı mı, idare cevap verdi mi/sustu mu?
4. Başvuru bedeli yatırıldı mı; itirazen şikâyet dilekçesi süresinde mi?

## Denetim şeması
1. **Şikâyet (m.55):** İhale sürecindeki işlem/eylemlere karşı, hukuka aykırılığın farkına varıldığı veya farkına varılması gereken tarihten itibaren 10 gün içinde idareye yazılı şikâyet edilir. Sözleşme imzalanmadan başvurulmalıdır. İdare 10 gün içinde gerekçeli karar verir.
2. **İtirazen şikâyet (m.56):** İdarenin kararına veya 10 günlük süre içinde karar vermemesine (zımni ret) karşı, tebliğ/sürenin bitiminden itibaren 10 gün içinde KİK'e itirazen şikâyet edilir. Başvuru bedeli (m.53'e göre, güncel tutar) yatırılır.
3. **Ehliyet-menfaat:** Başvuran, ihaleye teklif veren istekli ya da istekli olabilecek/aday sıfatıyla menfaat ilişkisini taşımalıdır. Doküman aykırılığına itirazda istekli olabilecekler de başvurabilir.
4. **KİK kararı:** Kurul düzeltici işlem, ihalenin iptali veya itirazen şikâyetin reddine karar verir. Karar, ilgili idare ve tarafları bağlar.
5. **Dava aşaması:** KİK kararına karşı Ankara idare mahkemelerinde 2577 sayılı İYUK'a göre iptal davası açılır; süre kararın tebliğinden itibaren 30 gündür.
6. **Ara sonuç:** Süre hak düşürücüdür; kaçırılan başvuru esasa girilmeden reddedilir.

İspat yükü: Başvuran iddiasını belge ve doküman atfıyla somutlaştırır.

## Çıktı modülleri
- Süre takvimi (öğrenme → şikâyet → idare cevabı → itirazen şikâyet → dava).
- Şikâyet/itirazen şikâyet dilekçe taslağı (talep + gerekçe + dayanak).
- Ehliyet/menfaat değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

