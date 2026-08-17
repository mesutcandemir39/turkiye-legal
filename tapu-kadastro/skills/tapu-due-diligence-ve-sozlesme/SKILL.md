---
argument-hint: ''
description: Bir taşınmazın satın alınması, finansmanı veya devri öncesinde tapu kaydı,
  takyidat, imar ve nitelik yönünden risk taraması yapılırken; satış vaadi/satış işlemi,
  kapora ve devir güvenliği kurgulanırke
name: tapu-due-diligence-ve-sozlesme
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tapu İncelemesi (Due Diligence) ve Devir Sözleşmesi

## Görev
Taşınmaz devri öncesinde hak, yük ve sınır risklerini sistematik taramak; güvenli devir ve sözleşme yapısını kurmak.

## Soğuk başlangıç (intake)
- İşlem türü: doğrudan satış mı, taşınmaz satış vaadi mi, ipotekli/krediyle alım mı?
- Tapu kaydı, akit tablosu, takyidat listesi ve imar durumu temin edildi mi?
- Satıcı malik mi, vekil mi (vekâletnamenin kapsamı/güncelliği), tüzel kişi mi?
- Taşınmazın niteliği (arsa/tarla/bina), kat irtifakı/mülkiyeti, yapı kayıt/ruhsat durumu nedir?

## Denetim şeması
1. **Hak sahipliğini doğrula.** Güncel tapu kaydı ve akit tablosuyla malikin yetkisini, devir zincirini ve önceki yolsuzluk emarelerini kontrol et (TMK m.1020 aleniyet). Vekâletle işlemde 2644 sayılı Tapu Kanunu m.26 ve vekâletin kapsamı/iptal durumu.
2. **Takyidatları tara.** İpotek, haciz, ihtiyati tedbir, şerhler (satış vaadi, kira, önalım), beyanlar (aile konutu, kamulaştırma) — her takyidatın alıcıya etkisini (TMK m.1009-1010, m.1023) değerlendir.
3. **Nitelik ve imar süzgeci.** Orman/mera/kıyı niteliği, imar planı durumu, kaçak yapı/yapı kayıt belgesi (imar mevzuatı) devri ve kullanımı etkiler; bu skorlar ayrı imar/kat mülkiyeti incelemesine bağlanır.
4. **Şekil ve devir güvenliği.** Mülkiyet devri yalnız tapuda resmi senetle geçer (TMK m.706, m.705). Taşınmaz satış vaadi geçerlilik için resmi (noter) şekle tabidir (TBK m.237, Noterlik Kanunu m.60); vaadi güçlendirmek için tapuya şerh (TMK m.1009).
5. **Bedel ve risk dağıtımı.** Kapora/cayma parası (TBK m.177), ifa zamanı, takyidat temizleme yükümlülüğü, zapttan/ayıptan sorumluluk (TBK m.214 vd.) sözleşmede netleştirilir; emanet (escrow)/şartlı ödeme önerilir.
6. **Ara sonuç.** Devir güvenli mi, hangi takyidat temizlenmeli, hangi koşul kapanış şartı olmalı.

## Çıktı modülleri
- Tapu/takyidat risk skor tablosu (kırmızı/sarı/yeşil).
- Taşınmaz satış vaadi veya satış öncesi protokol iskeleti, kapanış şartları listesi.
- Kapanış öncesi giderilmesi gereken eksikler ve [doldurulacak] alanlar.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

