---
argument-hint: ''
description: Bir taşınmaz kredi/alacak için teminat gösterildiğinde, ipotek kurulurken
  ya da borç ödenmeyip ipoteğin paraya çevrilmesi veya fekki gerektiğinde; anapara/üst
  sınır ipoteği, derece ve takip yolu için
name: ipotek-rehin-teminat
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İpotek Tesisi, Derecesi ve Paraya Çevrilmesi

## Görev
Taşınmaz teminat ilişkisini kurmak ve yönetmek: ipoteğin geçerli tesisi, kapsamı, derecesi ve borç ödenmediğinde paraya çevrilmesi (icra) yolunu belirlemek; alacak sona erince fek (terkin) talebini değerlendirmek.

## Soğuk başlangıç (intake)
- Teminat altına alınan alacak mevcut ve belirli mi (anapara), yoksa doğacak/değişken mi (cari kredi → üst sınır)?
- İpotek hangi taşınmaz, hangi derecede; önceki/sonraki rehinler var mı?
- Borç muaccel ve ödenmedi mi; talep paraya çevirme mi, fek mi?
- Taşınmaz maliki ile borçlu aynı kişi mi (üçüncü kişi rehni var mı)?

## Denetim şeması
1. **Türler**: Taşınmaz rehni ipotek, ipotekli borç senedi ve irat senedi olarak kurulabilir (TMK m.881); uygulamada ipotek esastır.
2. **Anapara/üst sınır ipoteği (m.851)**: Mevcut ve belirli alacak için anapara ipoteği; doğacak veya tutarı belirsiz alacak için belirli azami meblağ (limit) üzerinden üst sınır ipoteği. Faiz ve giderlerin kapsamı bu ayrıma göre değişir.
3. **Kuruluş**: İpotek, tapu sicil müdürlüğünde resmî senet ve tescille doğar; rehin yükü taşınmazın bütünleyici parça ve eklentilerini de kapsar (m.862).
4. **Sıra/derece (m.870-871)**: Rehinler derece sistemine tabidir; sabit dereceler ilkesi ve boşalan dereceden yararlanma kayda göre belirlenir.
5. **Paraya çevirme**: Borç ödenmezse alacaklı, ipoteğin paraya çevrilmesi yoluyla takip başlatır (İİK m.145 vd.); ipotek bir ilama veya ilam niteliğindeki belgeye dayanıyorsa ilamlı, aksi hâlde ilamsız takip yolu izlenir. Doğrudan mülkiyet edinme (lex commissoria) yasaktır (TMK m.873/2).
6. **Fek/terkin (m.883)**: Alacak son bulunca malik ipoteğin terkinini isteyebilir; alacaklı yanaşmazsa fek davası açılır.
7. **Ara sonuç**: Geçerli kuruluş ve kapsamın tespiti; ihtilafta ya paraya çevirme takibi ya da fek davası.

## Çıktı modülleri
- İpotek tesis/fek talebi ve resmî senet kontrol listesi.
- Anapara/üst sınır ipoteği nitelendirme notu (faiz-gider kapsamı, derece).
- Rehnin paraya çevrilmesi takibine geçiş notu (İİK m.145 vd.).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

