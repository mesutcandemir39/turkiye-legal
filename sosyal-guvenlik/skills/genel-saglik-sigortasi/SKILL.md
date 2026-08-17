---
argument-hint: ''
description: GSS kapsamı, tescil, prim borcu, bakmakla yükümlü olunan kişi statüsü
  ve sağlık yardımlarından yararlanma koşulları söz konusu olduğunda; özellikle GSS
  borç ve gelir testi uyuşmazlıklarında kullanılır
name: genel-saglik-sigortasi
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


# Genel Sağlık Sigortası (GSS)

## Görev
Kişinin GSS kapsamını, tescil ve prim yükümlülüğünü, bakmakla yükümlü olunan kişi statüsünü ve sağlık hizmetinden yararlanma hakkını çözümlemek; GSS prim borcuna ilişkin uyuşmazlığı yönetmek.

## Soğuk başlangıç (intake)
- Kişi sigortalı (4/a-b-c) mi, bağımsız GSS'li mi, yoksa bakmakla yükümlü olunan kişi mi?
- GSS prim borcu tebliğ edildi mi; gelir testi yapıldı mı?
- Sağlık hizmetinden yararlanma reddedildi mi (prim borcu/kapsam dışı)?
- Öğrenci, yabancı, vatansız veya uluslararası koruma statüsü var mı?

## Denetim şeması
1. Kapsam — 5510 m.60: GSS'li sayılanlar (sigortalılar, gelir/aylık alanlar, yeşil kart yerine geçen kapsam, ikamet eden yabancılar) belirlenir.
2. Bakmakla yükümlülük — m.3/10 ve m.60: Eş, çocuk ve ana-baba sigortalı üzerinden yararlanma koşulları; bu durumda ayrı GSS tescili gerekmez.
3. Gelir testi — m.60-61: Bağımsız GSS'lide prime esas kazanç, hane içi gelirin asgari ücretin üçte birine göre durumuna göre belirlenir; gelir testi sonucuna SGK'ya itiraz ve dava yolu açıktır.
4. Prim ve borç — m.67 ve m.88: Sağlık yardımından yararlanmada prim borcu olmama koşulu (belirli istisnalar/yapılandırmalar saklı); GSS borçlarında zamanaşımı m.93.
5. Yararlanma — m.67: Müstehaklık koşulları (gün şartı, prim borcu durumu). Ara sonuç: kapsam, borç ve müstehaklık durumu. İspat: SGK tescil/gelir testi kayıtları, hane bilgileri.

## Çıktı modülleri
- GSS kapsam ve statü tespiti.
- Gelir testi sonucuna itiraz/dava değerlendirmesi.
- Prim borcu ve müstehaklık durum notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

