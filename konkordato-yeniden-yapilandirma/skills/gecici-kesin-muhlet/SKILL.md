---
argument-hint: ''
description: Geçici mühletin alınması, kesin mühlete geçiş, mühletin uzatılması veya
  kaldırılması ile mühletin alacaklılar ve sözleşmeler üzerindeki etkilerini yönetmek
  gerektiğinde kullanılır.
name: gecici-kesin-muhlet
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


# Geçici ve Kesin Mühlet Yönetimi

## Görev
Mühlet aşamasını uçtan uca yönetmek: geçici mühletin alınması, kesin mühlete geçiş kararının hazırlanması, mühletin uzatılması veya kaldırılması (m.291, m.292) ve mühletin hukuki sonuçlarının takibi.

## Soğuk başlangıç (intake)
- Geçici mühlet kararı tarihli mi, ne kadar süre kaldı?
- Komiserin ara raporu hazırlandı mı?
- Mühlet sırasında borçlunun aleyhine yeni takip/ihtiyati haciz girişimi var mı?
- Borçlunun rehinli/imtiyazlı alacaklıları kim?

## Denetim şeması
1. **Geçici mühletin sonuçları (m.288).** Geçici mühlet, kesin mühletin sonuçlarını doğurur. İlan ve ilgili sicillere bildirim yapılmış mı kontrol edilir.
2. **Kesin mühlete geçiş (m.289).** Komiser raporu, borçlu ve varsa talep eden alacaklı dinlenir; başarı ihtimali değerlendirilir. İspat yükü borçluda.
3. **Mühletin takipler bakımından sonucu (m.294).** Mühlet içinde borçluya karşı icra takibi yapılamaz, başlamış takipler durur; istisnalar: rehnin paraya çevrilmesi yoluyla takip başlatılabilir ancak muhafaza tedbirleri ve satış yapılamaz (m.295). İmtiyazlı alacaklar için ihtiyati haciz/tedbir sınırlamaları denetlenir.
4. **Sözleşmeler bakımından (m.296).** Borçlunun taraf olduğu sözleşmelerin mühlet nedeniyle feshini sınırlayan hükümler uygulanır; sürekli edimli sözleşmelerin akıbeti değerlendirilir.
5. **Tasarruf yetkisinin sınırlanması (m.297).** Borçlu, komiserin onayı olmadan rehin tesisi, kefil olma, taşınmaz/işletme devri gibi işlemleri yapamaz; aksi işlem hükümsüzdür. İhlal halinde mühletin kaldırılması (m.292) gündeme gelir.
6. **Mühletin kaldırılması (m.291-292).** Konkordatonun başarıya ulaşamayacağı anlaşılır veya borçlu kötüye kullanırsa mühlet kaldırılır, iflasa tabi borçlu için iflas açılır. Ara sonuç: mühlet devam mı, kaldırma mı.

## Çıktı modülleri
- Mühlet süre takvimi ve uzatma/kaldırma senaryoları.
- Tasarruf yetkisi kısıtı için onay-gerektiren işlemler listesi.
- Rehinli/imtiyazlı alacaklı haritası.
- Komisere/mahkemeye sunulacak ara rapor taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

