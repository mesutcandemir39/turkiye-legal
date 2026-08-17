---
argument-hint: ''
description: Kira uyuşmazlığında hangi delillerin gerekli olduğu, ispat yükünün kimde
  olduğu, senetle ispat zorunluluğu veya kira alacağı ve diğer taleplerde zamanaşımı
  süreleri tartışıldığında bu beceriyi kullan.
name: ispat-delil-ve-zamanasimi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Zamanaşımı

## Görev
Kira uyuşmazlığında ispat yükünü dağıtmak, gerekli delilleri belirlemek ve uygulanabilir zamanaşımı sürelerini saptamak; delil planını talep türüne göre kurmak.

## Soğuk başlangıç (intake)
- Çekişmeli vakıa ne (ödeme, ihtar, ayıp, ihtiyaç)?
- Elde hangi yazılı belgeler var (sözleşme, makbuz, banka, ihtar)?
- Talep türü ne ve doğum tarihi/dönemi?
- Karşı tarafın savunması/def'ileri biliniyor mu?

## Denetim şeması
1. **İspat yükü (HMK m.190; TMK m.6)**: Bir vakıadan kendi lehine hak çıkaran onu ispatla yükümlüdür. Kiraya veren ihtar/temerrüt/ihtiyaç vakıasını; kiracı ödemeyi, taahhüdün geçersizliğini ispatlar.
2. **Senetle ispat (HMK m.200-201)**: Belirli parasal sınırı aşan hukuki işlemler senetle ispatlanır; senede/yazılı sözleşmeye karşı tanık dinlenemez (istisnalar saklı). Ödeme banka kaydı/makbuzla; ihtar noter belgesiyle ispatlanır.
3. **Delil türleri**: Yazılı sözleşme, kira ve aidat ödeme kayıtları, noter ihtarnameleri, tahliye taahhüdü, keşif-bilirkişi (ayıp/emsal kira), tanık (sınırlar dahilinde).
4. **Zamanaşımı**: Kira bedeli alacağı **beş yıllık** zamanaşımına tabidir (TBK m.147/1 — kira bedelleri). Diğer sözleşme kaynaklı tazminat/iade talepleri kural olarak **on yıl** (TBK m.146); haksız fiil benzeri talepler için ayrı süreler. Tahliye davaları zamanaşımına değil, ilgili **hak düşürücü** dava sürelerine (m.351, m.353) tabidir.
5. **Ara sonuç**: Çekişmeli vakıa-ispat yükü-delil eşleştirmesi + uygulanabilir zamanaşımı/hak düşürücü süre.

## Çıktı modülleri
- Delil matrisi (vakıa / yük / delil / durum).
- Zamanaşımı-hak düşürücü süre tablosu.
- Delil toplama/sunma eylem listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

