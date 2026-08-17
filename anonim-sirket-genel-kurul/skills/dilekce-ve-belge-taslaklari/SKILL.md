---
argument-hint: ''
description: Genel kurul cevresinde gerekli olan cagri metni, gundem, vekaletname,
  tutanak, muhalefet serhi, iptal dava dilekcesi ve ihtarname gibi belgelerin yer
  tutucu disipliniyle taslaklari uretilecekse kullan
name: dilekce-ve-belge-taslaklari
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Dilekçe ve Belge Taslakları

## Görev
Genel kurul sürecinin tüm belge ihtiyaçlarını — çağrı, gündem, vekâletname, tutanak, muhalefet şerhi, iptal/butlan dilekçesi, ihtarname — usule uygun ve `[doldurulacak]` yer tutucu disipliniyle üretmek.

## Soğuk başlangıç (intake)
1. Hangi belge isteniyor (toplantı öncesi/anı/sonrası)?
2. Şirket ve taraf bilgileri (unvan, MERSİS, merkez, pay oranları) elde mevcut mu?
3. Görevli/yetkili mahkeme ve süre durumu nedir (dava belgeleri için)?
4. Elektronik genel kurul/Bakanlık temsilcisi gibi özel gereklilik var mı?

## Denetim şeması
1. **Belge-norm eşleştirmesi:** Her belgeyi dayandığı maddeyle bağla — çağrı/gündem (m.413-414), vekâletname (m.425), hazır bulunanlar listesi (m.415), tutanak (m.422), muhalefet şerhi (m.446/1-b), iptal dilekçesi (m.445-448), azlık ihtarı (m.411).
2. **Dava dilekçesi mimarisi:** İptal/butlan dilekçesinde HMK m.119 zorunlu unsurları eksiksiz olmalı: taraflar, dava konusu, vakıalar (toplantı kronolojisi), hukuki sebepler (TTK m.445/447), deliller (tutanak, hazır bulunanlar listesi, TTSG ilanı), talep sonucu (kararın iptali/butlanın tespiti). Görevli mahkeme: asliye ticaret (TTK m.5); yetkili: şirket merkezi (m.448).
3. **Yer tutucu disiplini:** Doğrulanamayan her veri köşeli parantezle işaretlenir: `[karar tarihi]`, `[pay oranı]`, `[muhalefet şerhi metni]`. Uydurma tarih/oran/künye yazılmaz.
4. **İçtihat hijyeni:** Dilekçede ilkesel atıf yapılır; Yargıtay 11. HD kararları için künye `[DOĞRULANMADI]` bırakılır ve karararama.yargitay.gov.tr kaynağı anılır. Sahte esas/karar numarası asla yazılmaz.
5. **İspat/delil bağlama:** Her vakıa, dilekçede onu ispatlayan belgeyle (tutanak madde no, ilan tarihi) eşleştirilir; ispat yükü TMK m.6 ve HMK çerçevesinde dağıtılır.
6. **Ara sonuç:** Belge teslimden önce süre (üç ay), davacı sıfatı (muhalefet şerhi) ve görev-yetki yeniden kontrol edilir.

## Çıktı modülleri
- İstenen belgenin tam taslağı (başlık-imza blokları dahil).
- Eksik bilgi listesi (`[doldurulacak]` envanteri).
- Sonraki adım ve süre uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

