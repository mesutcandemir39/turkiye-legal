---
argument-hint: ''
description: Konkordato sürecindeki tüm kanuni süreleri, mühlet ve uzatma takvimini,
  faiz ve zamanaşımı etkilerini hesaplamak ve takip etmek gerektiğinde kullanılır.
name: sureler-ve-zamanasimi
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


# Süreler, Mühlet Takvimi ve Zamanaşımı

## Görev
Konkordatonun süre yoğun yapısını kontrol altına almak: geçici/kesin mühlet süreleri ve uzatmaları, alacak bildirim ve toplantı süreleri, kanun yolu süreleri, mühletin zamanaşımı ve faize etkisi.

## Soğuk başlangıç (intake)
- Hangi kararın tarihi referans alınacak (geçici mühlet, kesin mühlet, tasdik)?
- Mühlet uzatması talep edildi mi?
- Bir kanun yolu süresi mi hesaplanacak?
- Faiz ve zamanaşımı bakımından hangi alacaklar inceleniyor?

## Denetim şeması
1. **Geçici mühlet (m.287).** Kural üç ay; mahkeme bir ay daha uzatabilir (toplam en çok dört ay). Başlangıç: geçici mühlet kararı tarihi.
2. **Kesin mühlet (m.289).** Bir yıl; güçlük halinde komiser raporuyla altı aya kadar uzatma (toplam en çok bir buçuk yıl). Uzatma talebinin mühlet bitmeden yapılması gerekir.
3. **Alacak bildirim ve toplantı süreleri (m.299, m.302).** Davet ilanındaki bildirim süresi ve projenin kabulü için tanınan süre takip edilir; sürelerin kaçırılması çoğunluk hesabını etkiler.
4. **Faiz (m.294).** Kesin mühlet içinde faiz işlemeye devam edip etmeyeceği alacağın türüne göre (rehinli/rehinsiz, sözleşme/kanun) değerlendirilir; faizin durması/işlemesi tasdik projesinde gösterilir.
5. **Zamanaşımı ve hak düşürücü süreler.** Mühletin zamanaşımını ve hak düşürücü süreleri durdurması/kesmesi (İİK ve TBK genel hükümleriyle birlikte) incelenir. Kanun yolu süreleri (istinaf/temyiz) gün gün hesaplanır; resmi tatil ve adli tatil etkisi gözetilir (HMK m.104, m.92-93). İspat: kararın tebliğ/ilan tarihi esas alınır. Ara sonuç: bağlayıcı tarihler takvimi.

## Çıktı modülleri
- Mühlet ve uzatma süre takvimi (tarih bazlı).
- Kanun yolu süre hesabı.
- Faiz ve zamanaşımı etki notu.
- Kritik tarih hatırlatma listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

