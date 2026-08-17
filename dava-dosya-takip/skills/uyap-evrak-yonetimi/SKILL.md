---
argument-hint: ''
description: UYAP üzerinden gelen evrakı, e-tebligatları ve dosya dökümlerini düzenli
  bir evrak listesine bağlamak, tebliğ tarihlerini ve evrak bütünlüğünü doğrulamak
  gerektiğinde kullan.
name: uyap-evrak-yonetimi
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


# UYAP ve Evrak Yönetimi

## Görev
UYAP'tan gelen evrakı, e-tebligatları ve dosya safahatını numaralı, tarihli ve sayfa referanslı bir evrak listesine dönüştürmek; tebliğ tarihlerini ve evrak bütünlüğünü doğrulayarak süre takvimini beslemek.

## Soğuk başlangıç (intake)
- Elinde UYAP safahat dökümü, e-tebligat kayıtları veya taranmış evrak var mı?
- Hangi evrakın tebliğ tarihi kritik (karar, bilirkişi raporu, dava dilekçesi)?
- Evrak numaralandırılmış/sayfalanmış mı?
- Eksik veya okunaksız belge var mı?

## Denetim şeması
1. Evrak envanteri: her belgeye sıra no, tarih, tür, gönderen/alıcı ve sayfa aralığı ver; safahat dökümüyle eşleştir. Eksik sıra varsa [doldurulacak].
2. Tebliğ doğrulama: e-tebligatta tebliğ tarihi muhatabın elektronik adrese ulaşmasından itibaren beşinci günün sonu sayılır (7201 sayılı Tebligat Kanunu m.7/a); bu tarihi süre takvimine tetikleyici olarak aktar.
3. Bütünlük kontrolü: eki olduğu belirtilen ama dosyada bulunmayan ekler, imzasız/okunaksız sayfalar ayrı not.
4. Süre köprüsü: tebliğ tarihi belirlenen her evrak için tetiklediği süre (cevap, itiraz, kanun yolu) Süre Takvimi becerisine devredilir; çift kayıt önlenir.
5. Ara sonuç: numaralı evrak listesi + doğrulanmış tebliğ tarihleri + eksik/okunaksız liste. Tarihler UYAP kaydından alınır; tahmin edilmez.

## Çıktı modülleri
- Numaralı evrak listesi (no, tarih, tür, taraf, sayfa).
- Tebliğ tarihi doğrulama tablosu.
- Eksik/okunaksız evrak ve eklerin listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

