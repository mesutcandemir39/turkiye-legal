---
argument-hint: ''
description: Cevap, itiraz, istinaf, temyiz gibi usul süreleri ile zamanaşımı/hak
  düşürücü sürelerin son günlerini dayanak maddeyle hesaplayıp takvime bağlamak gerektiğinde
  kullan.
name: sure-takvimi-ve-zamanasimi
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süre Takvimi ve Zamanaşımı

## Görev
Dosyadaki tüm usul sürelerini ve maddi zamanaşımı/hak düşürücü süreleri başlangıç olayı, dayanak madde ve son günüyle birlikte takvime dönüştürmek; süre kaçırma riskini sıfırlamak.

## Soğuk başlangıç (intake)
- Hangi yargı kolu: hukuk (HMK), ceza (CMK), icra (İİK), idari (İYUK)?
- Süreyi başlatan olay ve tarihi belli mi (tebligat, öğrenme, karar tarihi)?
- Hangi süreler işliyor (cevap, itiraz, kanun yolu, bilirkişiye itiraz)?
- Adli tatil veya resmî tatil araya giriyor mu?

## Denetim şeması
1. Süre kalemini tanımla ve dayanağını yaz: cevap dilekçesi 2 hafta (HMK m.127); bilirkişi raporuna itiraz 2 hafta (HMK m.281); hukukta istinaf 2 hafta (HMK m.345), temyiz 2 hafta (HMK m.361). Cezada itiraz 7 gün (CMK m.268), istinaf 7 gün (CMK m.273), temyiz 15 gün (CMK m.291). İcrada itiraz 7 gün (İİK m.62), kambiyoda 5 gün (İİK m.168); itirazın iptali 1 yıl (İİK m.67). İdaride 60 gün (İYUK m.7).
2. Başlangıç olayını sabitle: süre kural olarak tebliğ/öğrenme ile başlar; tarihi evraktan al, yoksa [doldurulacak].
3. Tatil ve son gün: adli tatilin (HMK m.102-104) süreye etkisini ve son günün tatile rastlamasını (uzama) kontrol et. Hesabı dayanak maddeyle göster.
4. Zamanaşımı/hak düşürücü süre: maddi hukuk süresini ilgili alanın kanunundan al (ör. genel zamanaşımı TBK m.146 on yıl; haksız fiil TBK m.72). Bu süreler usul süresinden ayrı izlenir.
5. Ara sonuç: her süre için son gün ve risk seviyesi; hesabın kullanıcıca doğrulanması istenir. Tarih uydurulmaz.

## Çıktı modülleri
- Süre-başlangıç-dayanak madde-son gün-durum kolonlu takvim tablosu.
- Yaklaşan/kritik süreler uyarı listesi.
- Hesap doğrulama notu ([DOĞRULANMADI] son günler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

