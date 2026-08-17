---
argument-hint: ''
description: Fikri-sınai hak uyuşmazlığında hakkın türünü (marka, patent, tasarım,
  eser, bağlantılı hak), tescilli/tescilsiz ayrımını ve uygulanacak rejimi (SMK mi
  FSEK mi) belirleyip doğru kanun ve yargı yoluna y
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Somut olayda hangi fikri/sınai hakkın söz konusu olduğunu, hakkın kaynağını ve uygulanacak hukuki rejimi (SMK 6769 / FSEK 5846) doğru saptamak; bunu görev-yetki, ispat yükü ve talep seçimine bağlamak.

## Soğuk başlangıç (intake)
- Uyuşmazlık konusu nedir: marka, patent/faydalı model, tasarım, coğrafi işaret yoksa edebî/sanatsal/yazılım eseri mi?
- Hak tescilli mi (TÜRKPATENT no, koruma süresi) yoksa tescilsiz koruma mı (eser, tanınmış marka, tescilsiz tasarım) iddia ediliyor?
- Müvekkil hak sahibi mi, lisans alan mı, devralan mı, yoksa tecavüzle suçlanan taraf mı?
- Talep tazminat mı, tecavüzün durdurulması mı, hükümsüzlük mü, yoksa tedbir mi?

## Denetim şeması
1. Hakkın niteliğini ayır: Sınai haklar SMK ile (marka m.4-7, patent m.82 vd., tasarım m.55 vd.); fikir ve sanat eserleri FSEK m.1/B-2 anlamında "sahibinin hususiyetini taşıyan" ürünler. Yazılım FSEK kapsamında eser (m.2/1), ancak teknik etki içeriyorsa patent boyutu da incelenir.
2. Koruma var mı: Tescilli haklarda sicil ve koruma süresi (marka m.23 yenileme, patent m.101 koruma, tasarım m.69) doğrulanır. Tescilsiz korumada hakkın varlığı davacıya ispat yükü olarak yüklenir (HMK m.190).
3. Hak sahipliği/sıfat: Devir-lisans şerhi sicilden kontrol edilir; lisans alanın dava ehliyeti SMK m.158 ile sınırlıdır (inhisari/basit lisans ayrımı).
4. Rejim çatışması: Aynı ürün hem eser hem tasarım/marka konusu olabilir; kümülatif koruma mümkündür, ancak her hak için ayrı şartlar ve ayrı talep değerlendirilir.
5. Ara sonuç: Uygulanacak kanun, görevli mahkeme türü (FSHM) ve hak sahipliği netleşmeden esas talep kurgulanmaz.

## Çıktı modülleri
- Hak haritası tablosu (hak türü / kaynak / tescil no / koruma süresi / sahip).
- Uygulanacak norm listesi (SMK ve/veya FSEK madde atıflarıyla).
- Eksik bilgi ve doğrulama listesi (sicil kaydı, devir zinciri).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

