---
argument-hint: ''
description: Vergi uyuşmazlığında ispat yükünün dağılımını, ekonomik yaklaşım ilkesini
  ve defter-belge-banka kayıtları gibi delillerin değerlendirilmesini ele almak için
  kullanılır.
name: ispat-delil-ve-belge-duzeni
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
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat, Delil ve Belge Düzeni

## Görev
Vergi uyuşmazlığında ispat yükünün taraflar arasında nasıl dağıldığını belirlemek; ekonomik yaklaşım ve ispat serbestisi çerçevesinde delilleri (defter, belge, banka, POS, sözleşme) değerlendirip savunmaya bağlamak.

## Soğuk başlangıç (intake)
1. İdare iddiasını hangi tespite dayandırıyor (inceleme raporu, karşıt inceleme, bilgi formu)?
2. Mükellef defter ve belgeleri tam mı; banka/POS/stok kayıtları mevcut mu?
3. Uyuşmazlık sahte belge, kayıt dışı hasılat mı yoksa nitelendirme/yorum farkı mı?
4. Hangi belgeler eksik veya çelişkili?

## Denetim şeması
1. **Genel ilke.** VUK m.3/B — vergilendirmede vergiyi doğuran olay ve muamelelerin **gerçek mahiyeti** esastır; ispat serbesttir, ancak **yemin** delil olamaz. İktisadi, ticari ve teknik icaplara uymayan veya olayın özelliğine göre normal olmayan durumu iddia eden ispatla yükümlüdür.
2. **İspat yükünün dağılımı.** Matrah farkını/ziyaı iddia eden idare somut tespit getirmekle; bu tespite karşı çıkan mükellef karşı delil sunmakla yükümlü. Sahte belge iddiasında idarenin somut delili (düzenleyen hakkında tespit, ödeme-emtia hareketi yokluğu) ile mükellefin gerçeklik delili (ödeme, taşıma, stok) karşılaştırılır.
3. **Defter ve belgenin ispat gücü.** Usulüne uygun tutulan defterler sahibi lehine de delil olabilir; ibraz edilmeyen defter re'sen tarh sebebidir (VUK m.30). İbraz mücbir sebep (VUK m.13) varsa farklı değerlendirilir.
4. **Tamamlayıcı deliller.** Banka kayıtları, POS, sözleşme, irsaliye, randıman/karşılaştırma analizleri delil olarak sunulur; çelişkiler giderilir veya idare aleyhine kullanılır.
5. **Bilirkişi.** Hesap ve teknik konularda bilirkişi incelemesi talep edilir; rapordaki metodoloji ve dayanak denetlenir. Ara sonuç: hangi vakıanın kim tarafından ispatlanması gerektiği ve mevcut delilin yeterliliği belirlenir.

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa / yükümlü taraf / mevcut delil).
- Delil dizini ve eksik/çelişki listesi.
- Bilirkişi/karşı delil talep notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

