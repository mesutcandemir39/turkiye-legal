---
argument-hint: ''
description: Kamuya sunmadan doğan 3 yıllık tescilsiz koruma kapsamının, taklit/kopyalama
  unsurunun ve ispat sorununun değerlendirilmesi; tescil yokken hızlı tüketilen ürünler
  veya fuarda ilk kez sergilenen tasarı
name: tescilsiz-tasarim-korumasi
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tescilsiz Tasarım Koruması

## Görev
Tescil olmadan, yalnızca kamuya sunma ile doğan korumayı işletmek: koruma süresini, kapsamını (taklit/kopyalamaya karşı) ve kamuya sunmanın ispatını yönetmek. Moda, mobilya, ambalaj gibi hızlı yenilenen sektörlerde kritiktir.

## Soğuk başlangıç (intake)
1. Tasarım kamuya ilk kez ne zaman, nerede, hangi belgeyle sunuldu (fuar fotoğrafı, katalog, web arşivi, fatura)?
2. Bu sunma Türkiye'de ilgili sektör çevrelerince makul şekilde bilinebilir nitelikte miydi (SMK m.57/3 anlamında)?
3. Karşı tarafın ürünü, korunan tasarımı bilerek/kopyalayarak mı üretti, yoksa bağımsız tasarım mı?
4. 3 yıllık süre dolmuş mu?

## Denetim şeması
1. Korumanın doğumu (SMK m.55/4): Tescilsiz tasarım, Türkiye'de kamuya ilk sunulduğu tarihte korunmaya başlar. "Kamuya sunma" SMK m.57/3'e göre tanımlanır (yayım, sergileme, ticarette kullanım vb.).
2. Süre (SMK m.69/2): Kamuya ilk sunma tarihinden itibaren 3 yıl. Bu süre uzatılamaz; süre dolmuşsa koruma talebi reddedilir.
3. Koruma kapsamı (SMK m.57/2, m.59): Tescilsiz tasarım sadece, korunan tasarımın aynısının veya genel izlenim itibarıyla ondan ayırt edilemeyen bir tasarımın "kopyalanması/taklidi" sonucu kullanımına karşı koruma sağlar. Bağımsız yaratım tecavüz değildir.
4. Kopyalama unsuru: Tescilliden farklı olarak, davalının önceki tasarımı bilerek kullandığı (kopyaladığı) ortaya konmalıdır. Benzerliğin yüksekliği ve davalının tasarıma erişim imkânı kopyalama karinesini güçlendirir.
5. Yenilik/ayırt edicilik: Tescilsiz korumanın da geçerli olması için tasarım yine SMK m.56-57 şartlarını taşımalıdır; karşı taraf bunların yokluğunu def'i olarak ileri sürebilir.
6. Ara sonuç: Süre içinde miyiz, kamuya sunma ispatlanabilir mi, kopyalama unsuru var mı — üçü birlikte karşılanmıyorsa koruma işlemez.

## Çıktı modülleri
- Kamuya sunma delil dosyası (tarih damgalı görsel, fuar/katalog kaydı, web arşivi).
- 3 yıllık süre takvimi ve kalan süre.
- Kopyalama/bağımsız yaratım değerlendirme notu ve strateji.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

