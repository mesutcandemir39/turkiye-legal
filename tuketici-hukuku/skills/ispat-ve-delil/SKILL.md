---
argument-hint: ''
description: Tüketici uyuşmazlığında ispat yükünün kimde olduğunu, hangi delillerin
  gerektiğini ve karinelerin nasıl kullanılacağını planlamak gerektiğinde; özellikle
  ayıp, haksız şart ve masraf iadelerinde kullan
name: ispat-ve-delil
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
  - ad: Tüketicinin Korunması Hakkında Kanun
    numara: '6502'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İspat ve Delil Stratejisi

## Görev
Tüketici uyuşmazlığında ispat yükünü doğru dağıtmak, lehe karineleri kullanmak, gerekli delilleri belirlemek ve delil bağlama mimarisini kurmak.

## Soğuk başlangıç (intake)
- İspatlanması gereken çekirdek vakıa ne (ayıbın varlığı, masrafın tahsili, şartın müzakere edilmediği)?
- Elde hangi belgeler var (fatura, sözleşme, ekran görüntüsü, yazışma, ödeme dekontu)?
- Teknik bir tespit gerekiyor mu (bilirkişi, servis raporu)?
- Karşı tarafın elinde tutulan belge var mı (sözleşme nüshası, hesap dökümü)?

## Denetim şeması
1. **Genel kural (TMK m.6):** Kanunda aksi öngörülmedikçe, iddiasını dayandırdığı olguyu ispat yükü iddia eden taraftadır.
2. **Ayıpta karine (TKHK m.10):** Teslimden itibaren altı ay içinde ortaya çıkan ayıp teslim anında var sayılır; bu süre içinde ispat satıcıdadır. Altı aydan sonra ayıbın varlığını ve eskiden geldiğini tüketici ispatlar; malın ayıpsız olduğunun ispatı ise satıcıya aittir (m.10/2).
3. **Haksız şartta karine (TKHK m.5/3):** Standart sözleşmedeki şartın müzakere edildiğini ispat satıcı/sağlayıcıya düşer; tüketici şartın matbu olduğunu göstermesi yeterlidir.
4. **Masraf/ücret iadesinde:** Tahsil edilen masrafın hizmet karşılığı ve hukuken öngörülmüş olduğunu ispat, bunu alan bankaya/sağlayıcıya aittir.
5. **Delil türleri (HMK m.199 vd.):** Senet (sözleşme, fatura), elektronik veri (e-posta, SMS, sipariş kaydı), tanık, bilirkişi, keşif. Tüketici işlemlerinde basit usulün esnekliği ve dosyaya hâkim somut delil önemlidir.
6. **Belge istetme (HMK m.219-220):** Sözleşme nüshası, hesap dökümü gibi karşı taraf veya üçüncü kişide bulunan belgeler için ibraz talebi; ibraz edilmezse aleyhe sonuç değerlendirmesi.
7. **Ara sonuç:** Hangi vakıayı kim ispatlayacak, hangi delil hangi vakıayı bağlıyor, bilirkişi gerekli mi?

## Çıktı modülleri
- İspat yükü dağılım tablosu (vakıa → taraf → delil).
- Delil/belge ihtiyaç listesi ve eksik tespiti.
- Bilirkişi/servis raporu talep notu.
- Karşı tarafa belge ibraz talebi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

