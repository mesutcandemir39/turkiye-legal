---
argument-hint: ''
description: Kamulaştırma bedel tespiti, acele kamulaştırma ya da idarenin hukuki/fiili
  kamulaştırmasız el atması nedeniyle bedel/tazminat talebi gündeme geldiğinde; yargı
  kolu, bedel hesabı ve mülkiyet hakkı boyu
name: kamulastirma-ve-el-atma
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


# Kamulaştırma ve Kamulaştırmasız El Atma

## Görev
Taşınmaza idarenin müdahalesinin hukuki niteliğini (kamulaştırma / hukuki el atma / fiili el atma) belirlemek ve doğru bedel/tazminat yolunu kurmak.

## Soğuk başlangıç (intake)
- İdare usulüne uygun kamulaştırma yaptı mı, yoksa el atma mı var?
- El atma fiili (fiilen kullanma/yol-park yapımı) mı, hukuki (planda kamusal alanda bırakıp uygulamama) mı?
- Taşınmazın imar durumu ve plandaki fonksiyonu ne?
- İdari işlem (kamulaştırma kararı, acele kamulaştırma) tebliğ edildi mi?

## Denetim şeması
1. **Nitelik tespiti**: Usulüne uygun kamulaştırma → 2942 m.10 bedel tespiti ve tescil davası (idare açar). İdarenin **fiilen** el atması → kamulaştırmasız el atma bedeli (adli yargı, 2942 geçici m.6). Planda kamusal alana ayrılıp makul sürede kamulaştırılmayan taşınmaz → **hukuki el atma** (Uyuşmazlık Mahkemesi içtihadıyla idari yargıda tam yargı davası).
2. **Yargı kolu**: Fiili el atma adli yargıda (asliye hukuk), hukuki el atma idari yargıda (tam yargı) görülür; doğru kol seçimi görev retini önler. Acele kamulaştırma (m.27) ve kamulaştırma işleminin iptali ayrı denetlenir.
3. **Bedel tespiti (2942 m.11)**: Taşınmazın cinsi, yüzölçümü, imar durumu, emsal satışlar, gelir metodu (arazide), yapı bedeli; **dava tarihindeki** değer esas alınır, kıymet takdiri bilirkişi kuruluyla yapılır.
4. **Mülkiyet hakkı boyutu (Anayasa m.35, m.46)**: Kamulaştırmada **gerçek karşılık ve peşin/nakden ödeme** ilkesi; el atmada mülkiyetin özüne dokunma ve ölçüsüzlük AYM bireysel başvuru konusu olabilir (kararlarbilgibankasi.anayasa.gov.tr).
5. **İspat ve süre**: Tapu, imar durum belgesi, emsal satış kayıtları, keşif ve bilirkişi raporu. Acele kamulaştırma ve kamulaştırma işleminin iptalinde İYUK süreleri; el atma bedelinde zamanaşımı/faiz başlangıcı ayrıca kurulur.
6. **Ara sonuç**: Müdahalenin niteliğine göre doğru dava (bedel tespiti itirazı / kamulaştırmasız el atma bedeli / hukuki el atma tam yargı) ve yetkili mahkeme belirlenir; bilirkişi bedeline itiraz stratejisi hazırlanır. Yargıtay/Danıştay künyeleri `[DOĞRULANMADI]`.

## Çıktı modülleri
- El atma niteliği ve yargı kolu tespit notu.
- Bedel hesabı parametre listesi (emsal/imar durumu/yapı).
- Mülkiyet hakkı (Anayasa m.35) değerlendirme notu.
- İlgili dava türüne göre dilekçe iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

