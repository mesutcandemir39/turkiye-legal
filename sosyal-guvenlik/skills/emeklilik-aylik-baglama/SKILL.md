---
argument-hint: ''
description: Yaşlılık, malullük veya ölüm aylığı bağlanma koşullarının (yaş, prim
  günü, sigortalılık süresi) hesaplanması ve kademeli geçiş kurallarının uygulanması
  gerektiğinde kullanılır.
name: emeklilik-aylik-baglama
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
  - ad: Sosyal Sigortalar ve Genel Sağlık Sigortası Kanunu
    numara: '5510'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Emeklilik ve Aylık Bağlama Koşulları

## Görev
Sigortalının yaşlılık/malullük/ölüm aylığına hak kazanıp kazanmadığını, hangi tarihte ve hangi mevzuatla emekli olabileceğini koşul koşul belirlemek.

## Soğuk başlangıç (intake)
- İlk sigortalılık (işe giriş) tarihi nedir? (Kademeli geçişte belirleyici.)
- Toplam prim ödeme gün sayısı ve sigortalılık süresi ne kadar?
- Statü 4/a, 4/b yoksa 4/c mi; statüler arası birleştirme gerekiyor mu?
- Malullük/ölüm aylığı mı, normal yaşlılık aylığı mı talep ediliyor?

## Denetim şeması
1. Uygulanacak rejim: İlk sigortalılık tarihine göre 506/1479/5434 veya 5510 ve geçici maddeleri belirlenir. 08.09.1999 ve 30.04.2008 eşik tarihleri kademeyi değiştirir.
2. Yaşlılık aylığı — 5510 m.28: Yaş + prim günü + sigortalılık süresi üçlüsü. Kademeli geçiş (5510 geçici m.6 vd.) ile ilk sigortalılık tarihine bağlı yaş/gün tabloları uygulanır.
3. Malullük aylığı — m.25-27: En az %60 çalışma gücü kaybı, asgari sigortalılık süresi ve prim günü; malullük Kurum sağlık kurulu raporuyla saptanır.
4. Ölüm aylığı — m.32-34: Sigortalının ölümünde gün/koşul şartı ve hak sahipliği (eş, çocuk, ana-baba) ile pay oranları.
5. Hizmet birleştirme: 2829 sayılı Kanun/5510 ile farklı statü hizmetleri birleştirilir; son yedi yıllık hizmete göre aylığı bağlayacak kurum belirlenir. Ara sonuç: hak kazanma tarihi ve aylık türü. İspat: SGK hizmet dökümü, sağlık kurulu raporu.

## Çıktı modülleri
- Emeklilik koşulu hesap tablosu (yaş/gün/süre — gerçekleşen vs. gerekli).
- Hak kazanma tarihi ve eksik koşul tespiti.
- Borçlanma ile koşul tamamlama senaryosu (gerekiyorsa ilgili beceriye yönlendirme).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

