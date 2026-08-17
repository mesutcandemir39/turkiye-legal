---
argument-hint: ''
description: Mirasbırakanın sağlığında yasal mirasçılara yaptığı karşılıksız kazandırmaların
  paylaşmada hesaba katılması ya da terekeye iadesi gerektiğinde; çeyiz, kuruluş sermayesi,
  eğitim gideri ve malvarlığı de
name: denklestirme-ve-iade
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


# Denkleştirme (İade) Davası

## Görev
Yasal mirasçıların mirasbırakandan sağlararası aldıkları karşılıksız kazandırmaların paylaşmada denkleştirilmesini (iade veya hesaba katma) TMK m.669-675 uyarınca sağlamak.

## Soğuk başlangıç (intake)
- Kazandırmayı alan yasal mirasçı mı? (denkleştirme yalnızca yasal mirasçılar arası)
- Kazandırma türü: çeyiz, kuruluş sermayesi, borç ödeme, malvarlığı devri, eğitim gideri?
- Mirasbırakan iadeden açıkça bağışık tuttu mu (m.669/1)?
- Kazandırma tarihi ve ölüm tarihindeki değeri?
- Alan kişi mirası reddetti mi? (m.674 — reddedende iade yükü farklı)

## Denetim şeması
1. **İade yükümlülüğünü belirle (m.669):** Yasal mirasçılar, miras payına mahsuben yapılan kazandırmaları iadeyle yükümlüdür. Mirasbırakanın aksi iradesi (bağışıklık) açık olmalı; altsoya çeyiz/kuruluş sermayesi/malvarlığı devri için iade karinesi vardır (m.669/2).
2. **Kapsam dışını ayır (m.670):** Olağan eğitim-öğretim giderleri, mutat hediyeler kural olarak iadeye tabi değildir; aşırı olanlar tabidir.
3. **İade biçimini seç (m.671):** Mirasçı, aldığını aynen geri verebilir veya değerini miras payına mahsup edebilir; kazandırma miras payını aşsa bile aşan kısım — mirasbırakanın iradesi ve tenkis kuralları saklı — iade edilmeyebilir (m.672).
4. **Değerleme (m.673):** İade, kazandırmanın denkleştirme anındaki (paylaşma anı) değerine göre; elden çıkarılmışsa sürüm değeri esas alınır.
5. **Çocukların çocukları (m.675):** Önceden ölen mirasçının yerine geçenler, onun almadığı kazandırmaları iade etmez ama kendi aldıklarını iade eder. Ara sonuç: iadeye tabi tutar + biçim (aynen/mahsup) + paylaşmaya etkisi.

## Çıktı modülleri
- Denkleştirme hesap tablosu (kazandırma, değer, mahsup)
- Tenkis ile denkleştirme ayrımı notu (hangisi uygulanır)
- Paylaşma/ortaklığın giderilmesi davasına entegre talep
- İspat için kazandırma belgeleri dizini



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

