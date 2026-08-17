---
argument-hint: ''
description: Bağımsız bölüm üzerinde dönem dönem (devre mülk) yararlanma hakkının
  kurulması/kullanılması ya da kat mülkiyetinin sona erdirilmesi (anayapının yok olması,
  kamulaştırma, terk veya maliklerin istemiyle
name: devre-mulk-ve-kat-mulkiyetinin-sona-ermesi
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
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Devre Mülk ve Kat Mülkiyetinin Sona Ermesi

## Görev
İki ayrı özel kurumu yönetmek: (1) bir mesken nitelikli bağımsız bölümde dönemsel yararlanma sağlayan devre mülk hakkının kuruluş ve kullanım rejimi (KMK m.57-65); (2) kat mülkiyetinin/kat irtifakının sona ermesi hâlleri ve sonuçları (KMK m.46-54).

## Soğuk başlangıç (intake)
- Devre mülk mü kuruluyor/kullanılıyor, yoksa mevcut kat mülkiyetinin sona ermesi mi söz konusu?
- Devre mülkte: hak müşterek mülkiyet payına bağlı dönem hakkı olarak resmî senetle mi kuruldu?
- Sona ermede sebep ne: anayapının tamamen yok olması, kamulaştırma, malik istemi, yoksa kat irtifakının terkini mi?
- Anayapı kısmen mi tamamen mi harap; sigorta/yeniden yapım gündemde mi?

## Denetim şeması
1. **Devre mülk niteliği (KMK m.57-58)**: Devre mülk hakkı, mesken olarak kullanılmaya elverişli bir yapı veya bağımsız bölümün **ortak mülkiyet payına bağlı** olarak yılın belli dönemlerinde yararlanma hakkı sağlayan bir **irtifak hakkıdır** (m.57). Devre mülk hakkı ancak **mesken** nitelikli yerlerde kurulabilir (m.58).
2. **Kuruluş ve sözleşme (m.59-61)**: Hak, tapuda resmî senetle ve dönem tahsisini gösterir biçimde kurulur; dönemler bölünemez ve devir/miras yoluyla geçebilir. Yönetim ve kullanım için ayrı bir devre mülk sözleşmesi/planı düzenlenir.
3. **Kat mülkiyetinin sona ermesi (KMK m.46-47)**: Kat mülkiyeti, kütükteki kaydın silinmesiyle (maliklerin istemi/oybirliğiyle, m.46) veya **anayapının tamamen yok olması ya da harap olması** (m.47) hâlinde sona erer. Anayapı kısmen harap olur ve bağımsız bölümlerin yarısı kullanılmaz hâle gelirse özel rejim işler (m.47/2-3).
4. **Kamulaştırma (m.48, m.46)**: Bağımsız bölümün veya ortak yerin kamulaştırılması hâlinde arsa payı ve değer esasına göre paylaştırma yapılır.
5. **Sona ermenin sonuçları (m.49-50)**: Kat mülkiyeti sona erince anagayrimenkul, kat maliklerinin **arsa payları oranında paylı mülkiyetine** döner; tasfiye ve paylaşma TMK paylı mülkiyet hükümlerine göre yapılır.
6. **Yenileme/onarım yükümü (m.19, m.47)**: Tamamen yok olmamış yapıda onarım kurul kararına ve gider rejimine tabidir; harabiyet iddiası keşif-bilirkişi ile saptanır.
7. **Ara sonuç**: Devre mülkte geçerli kuruluş + dönem tahsisi; sona ermede sebep tespiti + paylı mülkiyete dönüş ve tasfiye.

## Çıktı modülleri
- Devre mülk kuruluş/sözleşme kontrol listesi (mesken şartı, dönem tahsisi).
- Sona erme sebebi tespit notu (m.46-48) ve paylaşma çerçevesi.
- Harabiyet/yeniden yapım için keşif-bilirkişi talebi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

