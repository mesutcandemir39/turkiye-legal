---
argument-hint: ''
description: Yeni bir kira sözleşmesi, tahliye/temerrüt ihtarnamesi, dava veya cevap
  dilekçesi ya da kira tespiti talebi taslağı hazırlanması gerektiğinde bu beceriyi
  kullan.
name: kira-sozlesmesi-ve-dilekce-taslak
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


# Kira Sözleşmesi, İhtarname ve Dilekçe Taslağı

## Görev
Kira hukukuna özgü belgeleri emredici hükümlere uygun, eksiksiz ve uygulanabilir şekilde taslaklamak: kira sözleşmesi, noter ihtarnamesi, dava/cevap dilekçesi, kira tespiti ve tahliye taleplerini üretmek.

## Soğuk başlangıç (intake)
- Hangi belge isteniyor (sözleşme, ihtar, dilekçe)?
- Taraf ve taşınmaz bilgileri net mi; bilinmeyen alanlar?
- Belgenin amacı/dayanağı hangi madde (m.315, m.350-352, m.344-345)?
- Süre/şekil kısıtı var mı (noter, taahhütlü tebliğ)?

## Denetim şeması
1. **Sözleşme taslağı**: Taraf-taşınmaz-bedel-süre-teslim; emredici sınırlara uyum — güvence en çok üç aylık kira (m.342), gecikme cezası/muacceliyet kaydı **konulamaz** (m.346), artış kaydı TÜFE on iki aylık ortalama tavanına bağlanır (m.344). Bağlantılı edim eklenmez (m.340).
2. **İhtarname**: Temerrüt ihtarında en az otuz günlük süre ve fesih uyarısı (m.315); içerik kesin ve belirli; noterden/iadeli taahhütlü gönderim; tebliğ tarihi delillendirilir.
3. **Dava dilekçesi (HMK m.119)**: Mahkeme, taraflar, konu, vakıalar, hukuki sebepler (ilgili TBK/İİK maddeleri), deliller ve **talep sonucu**; basit yargılama gereği delillerin dilekçeyle sunulması; arabuluculuk son tutanağının eklenmesi.
4. **Kira tespiti talebi**: Süre penceresi (m.345), emsal ve oran dayanağı, yeni bedel talebi ve karar etkisinin dönem başına bağlanması.
5. **Yer tutucu disiplini**: Bilinmeyen her veri `[doldurulacak]` ile işaretlenir; tarih, tutar, ada/parsel uydurulmaz.
6. **Ara sonuç**: Belge + dayanak maddeler + eksik veri listesi.

## Çıktı modülleri
- İstenen belgenin tam taslağı (yer tutuculu).
- Dayanak madde listesi.
- Gönderim/sunum talimatı (noter, harç, ek belgeler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

