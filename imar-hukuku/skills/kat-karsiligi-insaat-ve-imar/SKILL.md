---
argument-hint: ''
description: Arsa payı karşılığı (kat karşılığı) inşaat sözleşmesi ile imar süreçleri
  kesiştiğinde; ruhsat-iskân yükümlülükleri, ayıplı/eksik ifa, gecikme ve sözleşmenin
  imar engeline takılması gündeme geldiğinde
name: kat-karsiligi-insaat-ve-imar
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
  - ad: İmar Kanunu
    numara: '3194'
    tur: kanun
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kat Karşılığı İnşaat ve İmar Kesişimi

## Görev
Kat karşılığı inşaat sözleşmesinin imar boyutuyla (ruhsat, iskân, projeye uygunluk) kesişen yükümlülüklerini analiz etmek ve ihtilafta tarafların pozisyonunu kurmak.

## Soğuk başlangıç (intake)
- Sözleşme tarihi, paylaşım oranı ve teslim süresi ne?
- Ruhsat alındı mı, inşaat ruhsata/projeye uygun mu, iskân var mı?
- Gecikme, eksik veya ayıplı ifa ya da imar engeli (plan değişikliği, durdurma) var mı?
- Tapu/arsa payı devri ve kat irtifakı kuruldu mu?

## Denetim şeması
1. **Sözleşmenin niteliği ve şekli**: Kat karşılığı inşaat, eser ve gayrimenkul satış vaadi unsurlarını birleştiren karma sözleşmedir; taşınmaz devri içerdiğinden **resmî şekilde (düzenleme şeklinde, noterde)** yapılması gerekir (TBK m.237, TMK tapu şekli). Şekil eksikliği ve ifa ilişkisi (TMK m.2) tartışılır.
2. **Yüklenicinin imar yükümü**: Yüklenici, **ruhsata ve onaylı projeye uygun** yapı yapmak, iskân almakla yükümlüdür; ruhsatsız/projeye aykırı imalat hem idari yaptırım (3194 m.32, m.42) hem sözleşmesel ayıp/eksik ifa doğurur (TBK m.474 vd. eser hükümleri).
3. **İmar engeli ve imkânsızlık**: Sözleşme sonrası plan değişikliği, emsal düşüşü veya inşaat durdurma yükümün ifasını etkilerse, kusur ve **uyarlama/imkânsızlık** (TBK m.136, m.138) çerçevesinde risk dağıtımı yapılır.
4. **Gecikme ve gecikme tazminatı**: Teslim süresinin geçmesi temerrüt doğurur; cezai şart, kira kaybı/gecikme tazminatı ve arsa sahibinin seçimlik hakları (aynen ifa, dönme) değerlendirilir.
5. **Yargı kolu ve ispat**: Sözleşme uyuşmazlığı **adli yargıda (asliye hukuk)**; imar işlemleri (ruhsat/yıkım/ceza) idari yargıda. Ruhsat, iskân, hakediş, bilirkişi (inşaat mühendisi) ve fiziki tespit delildir. Eksik/ayıbı arsa sahibi, ifa engelini ileri sürerse yüklenici ispatlar.
6. **Ara sonuç**: İmar boyutu (ruhsat/iskân) ile sözleşmesel ifa birlikte değerlendirilip, ifa/dönme/tazminat seçenekleri ve idari risk müvekkile sunulur. Yargıtay 15./23. HD ilkesel atıfları `[DOĞRULANMADI]`.

## Çıktı modülleri
- Sözleşme-imar yükümlülük haritası.
- Ruhsat/iskân ve projeye uygunluk denetim notu.
- İmar engeli/uyarlama risk değerlendirmesi.
- İfa/dönme/tazminat seçenek tablosu ve ihtar/dava taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

