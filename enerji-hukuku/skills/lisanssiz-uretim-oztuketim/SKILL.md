---
argument-hint: ''
description: Çatı GES, kendi tüketimini karşılayan tesisler, mahsuplaşma ve lisanssız
  üretim eşikleri ile bağlantı başvuruları söz konusu olduğunda ve lisanssız üretim
  uyuşmazlıklarında kullanılır.
name: lisanssiz-uretim-oztuketim
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
  - ad: Elektrik Piyasası Kanunu
    numara: '6446'
    tur: kanun
  - ad: Mühendislik ve Mimarlık Meslek Kanunu
    numara: '4646'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Lisanssız Üretim ve Öz Tüketim

## Görev
Lisans almaksızın üretim yapma rejiminin (özellikle çatı/cephe GES ve öz tüketim) koşullarını, başvuru sürecini ve mahsuplaşma/ihtiyaç fazlası satış esaslarını denetlemek.

## Soğuk başlangıç (intake)
1. Tesis tipi ve kurulu güç; tüketim tesisiyle ilişkisi nedir?
2. Başvuru ilgili şebeke işletmecisine (dağıtım/OSB) yapıldı mı?
3. Üretim, tüketimi karşılamaya mı yönelik, ihtiyaç fazlası satış var mı?
4. Bağlantı görüşü/çağrı mektubu alındı mı?

## Denetim şeması
1. **Rejim ve eşik**: 6446 m.14 ve Lisanssız Elektrik Üretimi Yönetmeliği — lisans ve şirket kurma muafiyeti kapsamı ve güç sınırları. Ara sonuç: faaliyet lisanssız rejime giriyor mu.
2. **Tüketim bağı**: Öz tüketim esası; üretim tesisinin bir tüketim tesisiyle ilişkilendirilmesi ve aynı dağıtım bölgesi/ölçüm noktası koşulları. Bağ kurulamıyorsa rejim dışı kalınır.
3. **Başvuru ve bağlantı**: Şebeke işletmecisine başvuru, teknik değerlendirme, bağlantı görüşü ve çağrı mektubu; kapasite tahsisi sınırlı olduğundan ret gerekçeleri (trafo/fider kapasitesi) teknik veriyle sınanır.
4. **Mahsuplaşma ve ihtiyaç fazlası**: Aylık mahsuplaşma esasları ve ihtiyaç fazlası enerjinin görevli tedarik şirketince satın alınması; bedel ve süre yönetmelik/ilgili dönem tarifesine göre belirlenir (tarih kilidi).
5. **İhlal sonuçları**: Lisanssız sınırın aşılması veya öz tüketim koşulunun kaybı lisanslı faaliyet sayılarak yaptırım riski doğurur.

Şebeke işletmecisinin ret işlemine karşı önce idari başvuru/şikâyet, ardından duruma göre adli veya idari yargı yolu değerlendirilir.

## Çıktı modülleri
- Lisanssız uygunluk ve eşik kontrol notu.
- Bağlantı başvuru/itiraz dilekçesi taslağı.
- Mahsuplaşma ve ihtiyaç fazlası satış hesap özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

