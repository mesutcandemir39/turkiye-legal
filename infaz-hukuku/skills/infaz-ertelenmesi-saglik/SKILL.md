---
argument-hint: ''
description: Hapis cezası infazının hastalık, gebelik, yaşlılık veya başka zorunlu
  nedenlerle ertelenmesi ya da geri bırakılması taleplerini değerlendirmek gerektiğinde
  kullanılır.
name: infaz-ertelenmesi-saglik
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
  - ad: Ceza ve Güvenlik Tedbirlerinin İnfazı Hakkında Kanun
    numara: '5275'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İnfazın Ertelenmesi ve Sağlık Nedeniyle Geri Bırakma

## Görev
Hapis cezasının infazının ertelenmesi (CMK m.16-17 ve 5275 m.16-17) için zorunlu nedenlerin varlığını, usulünü ve süre sınırlarını değerlendirmek.

## Soğuk başlangıç (intake)
- Erteleme talebinin sebebi nedir (hastalık, gebelik, yakının ağır hastalığı, eğitim, ekonomik)?
- Hükümlü tutuklu/hükümlü hangi statüde; infaza başlandı mı?
- Sağlık nedeniyse ATK/üniversite hastanesi raporu var mı?
- Daha önce erteleme verildi mi (süre sınırı için)?

## Denetim şeması
1. Hastalık nedeniyle geri bırakma: akıl hastalığı veya kurumda hayatı için kesin tehlike oluşturan hastalık hâlinde infaz geri bırakılır (5275 m.16). Gebe veya doğum yapmış kadın için kanunda belirtilen süre kadar geri bırakma (m.16/4). İspat: Adli Tıp Kurumu veya tam teşekküllü hastane sağlık kurulu raporu.
2. Zorunlu/olağan erteleme: hükümlünün istemiyle, belirli süreli hapiste ve belirli üst sınır altında, eğitim/aile/ekonomik gibi makul nedenlerle erteleme (5275 m.17); güvence istenebilir ve kaçma şüphesi yoksa uygulanır. Suç tipi ve mükerrirlik istisnaları kontrol edilir.
3. Süre ve tekrar: erteleme süreleri ve toplam üst sınır; sürenin sonunda hükümlü teslim olmazsa erteleme hükümsüz kalır.
4. Karar mercii: erteleme/geri bırakma kararı Cumhuriyet Başsavcılığınca verilir; reddine karşı infaz hâkimliği yolu (4675 sayılı Kanun) açıktır. Ara sonuç: yetkili makam ve başvuru yolu.
5. İlkesel içtihat: hastalık nedeniyle geri bırakmada raporun yeterliliği ve insani infaz ölçütleri için karararama.yargitay.gov.tr ve AYM kararları (kararlarbilgibankasi.anayasa.gov.tr); künye `[DOĞRULANMADI]`.
6. Ara sonuç: erteleme uygunluğu + dayanak rapor/belge + süre.

## Çıktı modülleri
- Erteleme sebebi ve dayanak tablosu.
- Rapor/güvence eksik listesi.
- Erteleme talebi ve red kararına itiraz dilekçesi tetiği.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

