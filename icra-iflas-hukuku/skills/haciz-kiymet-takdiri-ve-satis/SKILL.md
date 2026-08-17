---
argument-hint: ''
description: Takip kesinleştikten sonra mal/alacak/maaş haczi yapmak, kıymet takdirine
  itiraz etmek ve taşınır-taşınmaz satış (açık artırma) sürecini yürütmek gerektiğinde;
  haciz kapsamı, hacizli malların satışı v
name: haciz-kiymet-takdiri-ve-satis
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Haciz, Kıymet Takdiri ve Satış

## Görev
Kesinleşen takipte borçlunun mal, alacak ve haklarını haczetmek; haczedilemezlik sınırlarını gözetmek; kıymet takdiri ve açık artırma yoluyla satışı yürütmek; ihalenin feshi/şikâyet risklerini yönetmek.

## Soğuk başlangıç (intake)
- Takip kesinleşti mi, haciz isteme süresi (m.78) içinde miyiz?
- Haczedilecek mal taşınır mı, taşınmaz mı, maaş/banka alacağı mı?
- Haczedilmezlik iddiası var mı (m.82, m.83 — maaşta 1/4 sınırı)?
- Kıymet takdiri yapıldı mı, itiraz süresi geçti mi?

## Denetim şeması
1. **Haciz isteme (m.78)**: Kesinleşmeden itibaren 1 yıl içinde haciz istenmezse dosya işlemden kalkar; yenileme gerekir. Haciz mahalde fiilen veya kayden (tapu, trafik, banka) yapılır.
2. **Haczedilmezlik (m.82-83)**: Zorunlu ev eşyası, mesleki araçlar, kısmen maaş (1/4) gibi mallar denetlenir; aşkın/usulsüz haciz şikâyet konusudur (m.16).
3. **Hacze iştirak ve istihkak**: Diğer alacaklıların iştiraki (m.100, m.101) ve üçüncü kişinin istihkak iddiası (m.96-99) ayrıca yönetilir.
4. **Kıymet takdiri (m.87, m.128/a)**: Bilirkişiyle değer biçilir; takdire karşı icra mahkemesine süresinde itiraz edilir (7 gün).
5. **Satış (m.106 vd., m.123 vd.)**: Talep süreleri ve elektronik açık artırma usulü gözetilir; taşınmazda m.126 vd., ihalenin feshi m.134 (7 gün içinde icra mahkemesi, fesih sebepleri: usulsüzlük, zarar, fahiş fiyat farkı).
6. **Ara sonuç**: Satış takvimi, beklenen bedel ve fesih riski belirlenir; paranın paylaştırılmasına (sıra cetveli) geçiş hazırlanır.

## Çıktı modülleri
- Haciz talebi ve haczedilmezlik şikâyeti taslağı.
- Kıymet takdirine itiraz dilekçesi.
- Satış/ihale takvimi ve ihalenin feshi risk notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

