---
argument-hint: ''
description: 4646 sayılı Kanun kapsamında doğal gaz lisansları, iletim-dağıtım-depolama-ithalat
  faaliyetleri, tarife ve dağıtım bölgesi uyuşmazlıkları ele alındığında kullanılır.
name: dogal-gaz-piyasasi
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Doğal Gaz Piyasası Uygulaması

## Görev
Doğal gaz piyasasındaki faaliyetleri 4646 sayılı Kanun ve ikincil mevzuat çerçevesinde lisans, tarife ve faaliyet ayrımı yönünden denetlemek; dağıtım ve ithalat/toptan uyuşmazlıklarını çözmek.

## Soğuk başlangıç (intake)
1. Faaliyet türü: ithalat, toptan satış, iletim, dağıtım, depolama, CNG/LNG?
2. Müvekkil lisans sahibi mi; dağıtım bölgesi/ihale durumu?
3. Uyuşmazlık tarife, abonelik, bağlantı bedeli mi, yoksa lisans/yaptırım mı?
4. Tartışmalı dönem ve EPDK işlemi var mı?

## Denetim şeması
1. **Faaliyet ayrımı**: 4646 — iletim, dağıtım, depolama, ithalat, toptan ve perakende satış faaliyetlerinin ayrılığı (unbundling) ilkesi ve her biri için ayrı lisans. Ara sonuç: faaliyet doğru lisansla mı yürütülüyor.
2. **Dağıtım bölgesi**: Dağıtım lisansının ihale ile verilmesi, bölge tekeli, yatırım ve hizmet yükümlülükleri; bölge dışı faaliyet ve devir sınırları.
3. **Tarife**: Bağlantı, iletim, dağıtım, depolama ve satış tarifeleri EPDK onayına tabi; abone bağlantı bedeli ve güvence bedeli uygulamaları yönetmelikle sınırlıdır. Onaylı tarife dışı bedel itiraza açık.
4. **Abonelik ve bağlantı**: Dağıtım şirketinin bağlantı/abonelik yükümlülüğü ve red sebepleri; teknik uygunluk ispatı dağıtıcıda.
5. **Yaptırım ve dava**: 4646 idari yaptırımları; EPDK işlemine karşı İYUK m.7 süresinde idari dava. Özel hukuk nitelikli abonelik/bedel uyuşmazlığı adli yargıda görülebilir; görev ayrımı netleştirilir.

## Çıktı modülleri
- Faaliyet/lisans uyum notu.
- Tarife/abonelik bedeli itiraz değerlendirmesi.
- İlgili merci ve dava/başvuru yol haritası.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

