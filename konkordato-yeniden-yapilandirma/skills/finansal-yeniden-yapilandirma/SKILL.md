---
argument-hint: ''
description: Mahkeme dışı, sözleşmesel finansal yeniden yapılandırma (FYY çerçeve
  anlaşmaları, banka/alacaklı müzakereleri) ile konkordato arasında seçim ve yapılandırma
  sözleşmesi kurgusu gerektiğinde kullanılır.
name: finansal-yeniden-yapilandirma
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


# Finansal Yeniden Yapılandırma (Mahkeme Dışı)

## Görev
Mahkeme dışı yeniden yapılandırmayı kurgulamak: 5411 sayılı Bankacılık Kanunu Geçici m.32 ve Finansal Yeniden Yapılandırma (FYY) çerçeve anlaşmaları kapsamında banka/finans alacaklılarıyla yapılan yapılandırmayı veya genel sözleşmesel yapılandırmayı (TBK çerçevesinde) tasarlamak.

## Soğuk başlangıç (intake)
- Alacaklılar ağırlıklı olarak banka/finansal kuruluş mu, ticari alacaklı mı?
- Borçlu FYY çerçeve anlaşması kapsamına giren bir teşebbüs mü?
- Mevcut teminat yapısı ve toplam borç büyüklüğü nedir?
- Mahkeme süreci (konkordato) yerine sözleşmesel çözüm tercih ediliyor mu?

## Denetim şeması
1. **Kapsam tespiti.** Finansal kuruluşlara olan borçlar baskınsa FYY çerçeve anlaşması (5411 s.K. Geçici m.32, ilgili BDDK Yönetmeliği) uygulanabilir mi denetlenir. Genel ticari alacaklarda TBK genel hükümleriyle yapılandırma (tecil, ibra, yenileme — TBK m.133) kullanılır.
2. **Konkordato ile karşılaştırma.** FYY mahkeme dışıdır, gizlilik ve hız avantajı sunar; ancak tüm alacaklıları bağlamaz, çoğunluk düzenlemesi sözleşme/çerçeve anlaşma ile sınırlıdır. Konkordato ise mahkeme tasdikiyle tüm alacaklıları bağlar.
3. **Yapılandırma araçları.** Vade uzatımı, faiz indirimi, anapara silme/ibra, teminat güçlendirme, borcun sermayeye dönüştürülmesi (debt-to-equity), yeni finansman. Her aracın TTK/TBK ve vergi sonuçları (örn. ibranın vergisel etkisi) değerlendirilir.
4. **Sözleşme tekniği.** Yapılandırma sözleşmesinde temerrüt halleri, çapraz temerrüt, teminat paketi, taahhüt ve beyanlar, fesih ve hızlandırma (acceleration) maddeleri kurgulanır. İspat: borçlunun mali tablolarıyla yapılandırmanın sürdürülebilirliği gösterilir.
5. **Başarısızlık senaryosu.** Sözleşmesel yapılandırma çökerse konkordatoya geçiş köprüsü hazırlanır. Ara sonuç: mahkeme dışı mı, konkordato mı; hibrit yol mümkün mü.

## Çıktı modülleri
- Konkordato vs. FYY karar matrisi.
- Yeniden yapılandırma sözleşmesi/protokol taslağı (yer tutuculu).
- Teminat ve taahhüt listesi.
- Başarısızlık halinde konkordato geçiş planı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

