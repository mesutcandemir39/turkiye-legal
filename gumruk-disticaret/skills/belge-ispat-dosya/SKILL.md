---
argument-hint: ''
description: Gümrük uyuşmazlığında ispat yükünü karşılayacak belge setini derlemek,
  ekspertiz/laboratuvar ve bilirkişi raporlarını değerlendirmek gerektiğinde; delil
  dizini ve eksik/çelişki kontrolü yapmak için ku
name: belge-ispat-dosya
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
  - ad: Gümrük Müsait Müşterek Gümrük Bölgeleri Hakkında Kanun
    numara: '4458'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Belge, İspat ve Dosya Hazırlığı

## Görev
Gümrük uyuşmazlığında ispat yükünü karşılayacak belge setini sistematik biçimde derlemek; ekspertiz, laboratuvar ve bilirkişi raporlarını denetlemek; delil dizini ile eksik ve çelişki listesi üretmek.

## Soğuk başlangıç (intake)
- Uyuşmazlık ekseni nedir (kıymet, menşe, sınıflandırma, rejim)?
- Hangi belgeler mevcut (beyanname, fatura, taşıma/sigorta, menşe ispat belgeleri, ödeme dekontu)?
- İdarenin dayandığı tespit nedir (ekspertiz, laboratuvar, sonradan kontrol raporu)?
- Bilirkişi/ATK incelemesi söz konusu mu?

## Denetim şeması
1. Belge envanteri: Beyanname ve ekleri, ticari fatura, proforma, sözleşme, navlun/sigorta belgeleri, banka ödeme kanıtları, menşe ispat belgeleri (EUR.1, A.TR, menşe şahadetnamesi, fatura beyanı), GTİP/BTB yazışmaları toplanır.
2. İspat yükü dağılımı: Beyanın doğruluğunu kural olarak yükümlü gösterir; idare beyanın aksini somut tespitle (kıymet araştırması, laboratuvar, sonradan kontrol) ortaya koymalıdır. Soyut iddia ispat değildir.
3. Ekspertiz/laboratuvar denetimi: Numune alma usulü, analiz yöntemi, GTİP sonucunun İzahname ile tutarlılığı ve raporun tarafların incelemesine açıklığı kontrol edilir; usule aykırı numune/analiz rapora itiraz gerekçesidir.
4. Bilirkişi raporu: Görev kapsamına uygunluk, kullanılan yöntem ve dayanak, hesap doğruluğu ve çelişki yönünden denetlenir (HMK/İYUK çerçevesinde); gerekirse ek rapor veya yeni bilirkişi talep edilir.
5. Çelişki ve eksik tespiti: Belgeler arası tutarsızlık (fatura-beyanname, menşe-sevk), eksik belge ve idare dosyasındaki boşluklar listelenir.
6. Ara sonuç: İspat stratejisini destekleyen delil dizini, eksik belge listesi ve rapor itiraz noktaları hazır hale gelir.

## Çıktı modülleri
- Delil dizini ve belge envanter tablosu
- Ekspertiz/laboratuvar ve bilirkişi raporu itiraz notu
- Eksik belge ve çelişki listesi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

