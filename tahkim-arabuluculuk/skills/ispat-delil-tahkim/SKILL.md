---
argument-hint: ''
description: Tahkim yargılamasında delil sunumu, tanık ve bilirkişi, belge ibrazı
  ile ispat yükünün dağılımını planlamak; arabuluculuk beyanlarının delil yasağını
  gözetmek gerektiğinde kullanılır.
name: ispat-delil-tahkim
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


# Tahkimde İspat ve Delil Yönetimi

## Görev
Tahkimde delil stratejisini kurmak: hangi vakıayı kimin ispatlayacağı, hangi delillerin
nasıl sunulacağı ve usul güvencelerinin (hukuki dinlenilme, eşit muamele) korunması.
Ayrıca arabuluculuk beyanlarının sonraki davada kullanılamayacağını gözetmek.

## Soğuk başlangıç (intake)
1. Tahkim iç (HMK) mi MTK mı, kurumsal kurallar (ör. ISTAC, ICC) uygulanıyor mu?
2. Çekişmeli vakıalar neler, ispat yükü kimde?
3. Tanık, bilirkişi, belge ibrazı ihtiyacı var mı?
4. Daha önce arabuluculuk yapıldıysa orada açıklanan beyan/belge var mı?

## Denetim şeması
1. **İspat yükü**: Genel kural **TMK m.6** — iddia eden ispatla yükümlüdür; tahkimde de
   esastır. Çekişmeli vakıalar ve karşı tarafın ikrarı ayrıştırılır.
2. **Delil sunumu ve usul**: Hakem heyeti delillerin toplanmasını yönetir; taraflara
   **eşit muamele** ve **hukuki dinlenilme hakkı** tanınmalıdır (**HMK m.423**,
   **MTK m.8/A**). Bu ilkelerin ihlali iptal sebebidir (**HMK m.439/2-ç**, **MTK m.15/A**).
3. **Mahkeme yardımı**: Hakem heyeti tanığı zorla getiremez veya üçüncü kişiden belge
   ibrazını cebren sağlayamaz; bunun için **delil toplanmasında mahkeme yardımı** istenir
   (**HMK m.432**). Kurumsal kurallarda belge ibrazı (örn. IBA Delil Kuralları) tarafların
   anlaşmasıyla uygulanabilir.
4. **Arabuluculuk delil yasağı**: Arabuluculukta ileri sürülen görüş, öneri, kabul ve
   belgeler sonraki yargılamada/tahkimde **delil olarak kullanılamaz** (**HUAK m.5**); bu
   sınır delil listesinde işaretlenir.
5. **Ara sonuç**: İspat yükü tablosu, delil planı ve usul riski uyarıları.

## Çıktı modülleri
- Vakıa-delil-ispat yükü matrisi.
- Tanık/bilirkişi/belge ibraz talep taslakları.
- Mahkeme yardımı (HMK m.432) başvuru notu; HUAK m.5 delil yasağı uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

