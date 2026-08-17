---
argument-hint: ''
description: Tahkim ile arabuluculuk arasındaki temel ayrımı, iç/milletlerarası tahkim
  ve ihtiyari/dava şartı arabuluculuk rejimlerini ve uygulanacak normu belirlemek
  gerektiğinde kullanılır; bir uyuşmazlığın hang
name: temel-kavramlar-ve-sistem
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
  - ad: Şehircilik ve Şehir Plancılarının Statüsü Hakkında Kanun
    numara: '4686'
    tur: kanun
  - ad: Hukuk Uyuşmazlıklarında Arabuluculuk Kanunu
    numara: '6325'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Önüne gelen uyuşmazlığı doğru rejime oturtmak: tahkim mi arabuluculuk mu; tahkim ise iç
(HMK) mi milletlerarası (MTK) mi; arabuluculuk ise ihtiyari mi dava şartı mı. Yanlış
nitelendirme süre kaçırma ve usulden ret doğurur; bu beceri rejim haritasını çıkarır.

## Soğuk başlangıç (intake)
1. Uyuşmazlık konusu nedir, tarafların üzerinde serbestçe tasarruf edebileceği bir hak mı?
2. Taraflar arasında tahkim/arabuluculuk anlaşması var mı, varsa lafzı nedir?
3. Yabancılık unsuru var mı (taraf yerleşim yeri, tahkim yeri, edimin yapılacağı yer)?
4. Uyuşmazlık iş, ticari, tüketici, kira gibi dava şartı arabuluculuğa tabi bir alan mı?

## Denetim şeması
1. **Elverişlilik**: Tahkim için **HMK m.408** — taşınmaz üzerindeki ayni haklara veya
   iki tarafın iradesine tabi olmayan işlere ilişkin uyuşmazlıklar tahkime elverişsizdir.
   Arabuluculuk için **HUAK m.1/2** — tarafların serbestçe tasarruf edebileceği işler;
   aile içi şiddet iddiası içeren uyuşmazlıklar elverişsiz. Elverişsizse devlet yargısı.
2. **Tahkim/arabuluculuk ayrımı**: Bağlayıcı bir karar mı (tahkim, **HMK m.407 vd.** /
   **MTK**) yoksa tarafların ürettiği anlaşma mı (arabuluculuk, **HUAK**) isteniyor?
3. **Tahkim alt-rejimi**: Yabancılık unsuru (**MTK m.2**) varsa ve tahkim yeri Türkiye
   ise **4686 MTK**; yoksa **HMK m.407-444**. Tahkim yeri yurt dışıysa kararın tenfizi
   **MÖHUK m.60-63** ve **New York Sözleşmesi**.
4. **Arabuluculuk alt-rejimi**: İş (**7036 m.3**), ticari (**TTK m.5/A**), tüketici
   (**TKHK m.73/A**), kira/komşu/kat mülkiyeti (**HUAK m.18/B**) ise **dava şartı**;
   değilse **ihtiyari** (**HUAK m.13**). Dava şartı ise dava açmadan önce başvuru zorunlu.
5. **Ara sonuç**: Rejim + dayanak madde + yetkili merci + temel süre tek tabloda.

## Çıktı modülleri
- Rejim nitelendirme tablosu (tahkim/arabuluculuk, iç/MTK, ihtiyari/dava şartı).
- Uygulanacak norm listesi (madde atıflı).
- Bir sonraki adım ve süre uyarısı (iptal/dava açma süreleri).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

