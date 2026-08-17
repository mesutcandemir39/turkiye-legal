---
argument-hint: ''
description: 6183 sayılı Kanun kapsamında ödeme emri, haciz, teminat, tecil-taksitlendirme
  ve ihtiyati haciz işlemlerine karşı korunma ve dava yollarını planlamak için kullanılır.
name: tahsilat-odeme-emri-haciz
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
  - ad: Vergi Usul Kanunu
    numara: '213'
    tur: kanun
  - ad: Gelir Vergisi Kanunu
    numara: '193'
    tur: kanun
  - ad: Kurumlar Vergisi Kanunu
    numara: '5520'
    tur: kanun
  - ad: Katma Değer Vergisi Kanunu
    numara: '3065'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tahsilat, Ödeme Emri ve Haciz (AATUHK)

## Görev
Kesinleşmiş ya da kesinleşmemiş kamu alacağının cebri tahsili aşamasında (ödeme emri, haciz, teminat, ihtiyati haciz) mükellefin korunma yollarını ve dava stratejisini kurmak.

## Soğuk başlangıç (intake)
1. Elde ödeme emri mi, haciz/ihtiyati haciz mi, teminat istemi mi var?
2. Asıl borç kesinleşti mi (dava açıldı/sonuçlandı mı)?
3. Ödeme emri hangi tarihte tebliğ edildi?
4. İtiraz sebebi "borcum yok / kısmen ödedim / zamanaşımına uğradı" mı?
5. Tecil-taksitlendirme veya yapılandırma talebi düşünülüyor mu?

## Denetim şeması
1. **Ödeme emri ve süre:** AATUHK m.55 ödeme emri tebliğ edilir; m.58 — ödeme emrine karşı 15 gün içinde vergi mahkemesinde dava açılır. İtiraz sebepleri sınırlıdır: "böyle bir borç yoktur, kısmen ödedim veya zamanaşımına uğradı".
2. **Tahsil zamanaşımı:** AATUHK m.102 — vadeyi izleyen takvim yılı başından itibaren 5 yıl; m.103 zamanaşımını kesen haller (ödeme, haciz, cebren tahsil, mal bildirimi vb.). Zamanaşımı ödeme emrine karşı temel savunmadır.
3. **Teminat ve ihtiyati haciz:** AATUHK m.9, m.13 — teminat istenmesi ve ihtiyati haciz şartları (henüz tahakkuk etmemiş ya da kesinleşmemiş alacakta), m.15 ihtiyati hacze itiraz 7 gün içinde.
4. **Haciz:** AATUHK m.62 vd.; haczedilemeyecek mallar (m.70), haczin kaldırılması, paraya çevirme. Usulsüz haciz ve hacze yetki sınırları denetlenir.
5. **Tecil-taksitlendirme:** AATUHK m.48 — çok zor durum şartıyla tecil; teminat ve tecil faizi. Yapılandırma kanunları (varsa yürürlükteki af/yapılandırma) ayrıca değerlendirilir.
6. **Sorumluluk genişlemesi:** Kanuni temsilci (VUK m.10), limited şirket ortağı (AATUHK m.35) ve yöneticilerin (AATUHK mük.35) ikincil sorumluluğu; takibin muhatabı doğru mu? Ara sonuç: hangi işleme, hangi sürede, hangi sebeple itiraz/dava açılır.

## Çıktı modülleri
- Ödeme emri itiraz sebebi tablosu (üç sınırlı sebep ile eşleştirme).
- Tahsil zamanaşımı hesap çizelgesi (vade, kesen haller, dolum tarihi).
- Tecil/teminat/ihtiyati haciz seçenek notu.
- İtiraz/dava dilekçesi iskeleti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

