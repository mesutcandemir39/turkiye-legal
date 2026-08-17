---
argument-hint: ''
description: Kabahat ile suç ayrımını, idari yaptırım türlerini, kanunilik ve 5326
  sayılı Kanunun genel-özel kanun ilişkisini netleştirmek; bir yaptırımın hangi rejime
  tabi olduğunu en baştan doğru saptamak gerekt
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Sistematik

## Görev
Önündeki haksızlığın kabahat mi suç mu olduğunu, uygulanan yaptırımın türünü ve hangi kanun rejimine (5326 genel + özel kanun) tabi olduğunu belirleyip doğru yargı yolunu işaret etmek.

## Soğuk başlangıç (intake)
- Yaptırımı hangi idare/merci verdi ve dayanak madde nedir (özel kanun + 5326)?
- Yaptırım idari para cezası mı, idari tedbir mi (ruhsat iptali, mülkiyetin kamuya geçirilmesi, faaliyet durdurma)?
- Karar bir tutanağa mı, idari işleme mi dayanıyor; tebliğ/tefhim tarihi nedir?
- Aynı fiil ayrıca adli soruşturmaya da konu mu (suç-kabahat içtiması)?

## Denetim şeması
1. **Kabahat-suç ayrımı:** Yaptırım idari nitelikteyse (idari para cezası/idari tedbir) kabahat rejimi; adli para cezası/hapis söz konusuysa ceza yargılaması. 5326 m.2 kabahati, m.16 yaptırım türlerini gösterir. Adli sicile işlememe, hapse çevrilememe kabahatin tipik sonuçlarıdır.
2. **Kanunilik süzgeci (5326 m.4):** Kabahatin tanımı ve yaptırımın kanunda veya kanunun açıkça verdiği yetkiye dayanan düzenlemede gösterilmesi gerekir. Salt yönetmelikle ihdas edilen, kanuni dayanağı olmayan yaptırım sakattır.
3. **Genel-özel kanun (5326 m.3):** Özel kanundaki kabahat hükmü esastır; tanım/miktar/usul orada düzenlenmemişse 5326 genel hükümleri uygulanır. Bu ilişki, başvuru yolu ve süreyi de etkiler.
4. **Yaptırım türü ve yetkili merci (5326 m.22-24):** İdari para cezası kural olarak ilgili idarenin yetkili organınca verilir; bazı tedbirler ve haller mahkeme/Cumhuriyet savcısı kararını gerektirir.
5. **Yargı yolu nitelendirmesi:** İdari yaptırım kararına karşı kural olarak **sulh ceza hâkimliği** yetkilidir (5326 m.27). Yaptırım daha geniş bir idari işlemin parçasıysa idari yargı görevli olabilir; ara sonuç olarak yargı yolunu netleştir.

## Çıktı modülleri
- Nitelendirme notu (kabahat mi/suç mu, yaptırım türü).
- Dayanak madde tablosu (özel kanun + 5326 ilgili maddeleri).
- Yargı yolu ve yetkili merci tespiti, başvuru süresi uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

