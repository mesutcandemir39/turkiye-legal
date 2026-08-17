---
argument-hint: ''
description: Bir alacağın taşınmaz teminatına bağlanması, ipoteğin kurulması/derecesi/paraya
  çevrilmesi veya fekki gündeme geldiğinde; ipotek, ipotekli borç senedi ayrımı, üst
  sınır ipoteği ve takip yolu için kull
name: tasinmaz-rehni-ipotek
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
  version: 0.1.0
user-invocable: true
---


# Taşınmaz Rehni ve İpotek

## Görev
Taşınmaz rehni ilişkisini kurmak ve yönetmek: ipoteğin tesisi, kapsamı, derecesi ve paraya çevrilmesi (icra) yolunu belirlemek; anapara ve üst sınır (azami meblağ) ipoteği ayrımını yapmak.

## Soğuk başlangıç (intake)
- Teminat altına alınan alacak mevcut/belirli mi, yoksa doğacak/değişken bir borç mu (örn. cari kredi)?
- İpotek hangi taşınmaz üzerinde, hangi derecede kuruluyor; başka rehinler var mı?
- Borç ödenmedi mi; talep ipoteğin paraya çevrilmesi mi, yoksa fek (terkin) mi?
- Taşınmaz sahibi ile borçlu aynı kişi mi (üçüncü kişi rehni var mı)?

## Denetim şeması
1. **Türler (TMK m.881)**: Taşınmaz rehni ipotek, ipotekli borç senedi ve irat senedi şeklinde kurulabilir; uygulamada ipotek esastır.
2. **Anapara/üst sınır ipoteği (m.851)**: Mevcut ve belirli alacak için anapara ipoteği; doğacak veya tutarı belirsiz alacak için belirli azami meblağ üzerinden üst sınır (limit) ipoteği kurulur. Faiz ve giderler kapsamı bu ayrıma göre değişir.
3. **Kuruluş**: İpotek resmî senet ve tapuya tescille doğar; rehin yükü taşınmazın bütünleyici parça ve eklentilerini de kapsar (m.862).
4. **Sıra ve derece (m.870-871)**: Rehin hakları derece sistemine tabidir; boşalan dereceden yararlanma (sabit dereceler ilkesi) kayıtla belirlenir.
5. **Paraya çevirme**: Borç ödenmezse alacaklı, rehnin paraya çevrilmesi yoluyla takip (İİK m.145 vd.) başlatır; doğrudan mülkiyeti edinmeyi öngören lex commissoria yasaktır (m.873/2).
6. **Fek/terkin**: Alacak sona erince malik ipoteğin terkinini isteyebilir (m.883); alacaklı terkine yanaşmazsa dava açılır.
7. **Ara sonuç**: Geçerli kuruluş ve kapsamın tespiti; ihtilafta ya paraya çevirme takibi ya da fek davası.

## Çıktı modülleri
- İpotek tesis/fek talebi ve resmî senet kontrol listesi.
- Anapara/üst sınır ipoteği nitelendirme notu (faiz-gider kapsamı).
- Rehnin paraya çevrilmesi takibine geçiş notu (İİK m.145 vd.).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

