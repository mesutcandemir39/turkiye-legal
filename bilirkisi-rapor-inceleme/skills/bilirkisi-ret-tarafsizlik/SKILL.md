---
argument-hint: ''
description: Bilirkişinin tarafsızlığından şüphe edilen, hâkimin reddi sebeplerine
  benzer durumların bulunduğu veya bilirkişinin yasak işlerle uğraştığı hâllerde ret
  talebi ve tarafsızlık itirazı hazırlamak istend
name: bilirkisi-ret-tarafsizlik
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
  - ad: Sağlık Turizmi Kanunu
    numara: '6754'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Bilirkişinin Reddi ve Tarafsızlık Denetimi

## Görev
Bilirkişinin kişisel tarafsızlığını ve bağımsızlığını denetlemek; HMK'nın hâkimin reddine ilişkin sebeplerinin bilirkişiye uygulanması yoluyla (HMK m.272) ret talebi ya da rapora itibar edilmemesi itirazı kurmak.

## Soğuk başlangıç (intake)
- Bilirkişinin taraflarla akrabalık, husumet, menfaat veya iş ilişkisi var mı?
- Bilirkişi daha önce aynı işte taraflardan biri için görüş/danışmanlık vermiş mi?
- Ret sebebini ne zaman ve nasıl öğrendiniz (süre yönünden)?
- Tarafsızlık şüphesini somutlaştıran belge/olgu nedir?

## Denetim şeması
1. **Ret rejimine yollama (HMK m.272):** Hâkimin reddini gerektiren sebepler bilirkişi için de ret sebebidir; bilirkişi ayrıca kendisini reddedebilecek sebepleri bildirmekle yükümlüdür. Sebepler HMK m.34-36 ölçütleriyle değerlendirilir.
2. **Tarafsızlık ve etik (6754 s.K. m.3):** Bilirkişi bağımsızlık, tarafsızlık ve objektiflik ilkelerine tabidir; menfaat çatışması veya taraf lehine eğilim ret/itiraz sebebidir.
3. **Süre ve usul:** Ret sebebi öğrenildikten sonra gecikmeksizin, ilgili usul kuralları çerçevesinde ileri sürülür; sebep dilekçede somut olgularla gösterilir (soyut şüphe yetmez).
4. **Yasak işler/devir (HMK m.277):** Görevin başkasına yaptırılması bağımsızlık ihlali olarak ayrıca ileri sürülür.
5. **Ara sonuç:** Ret kabul edilirse yeni bilirkişi atanır; ret süresi geçmiş veya reddi gerektirmeyen ama tarafsızlığı zedeleyen durumda rapora itibar edilmemesi/yeni heyet talep edilir (HMK m.281, m.282).

## Çıktı modülleri
- Ret sebebi-olgu-dayanak eşleştirmesi.
- Ret dilekçesi iskeleti (HMK m.272 atıflı, somut olgularla).
- Süre değerlendirmesi ve sunum yolu notu.
- Alternatif olarak tarafsızlık temelli esasa itiraz paragrafı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

