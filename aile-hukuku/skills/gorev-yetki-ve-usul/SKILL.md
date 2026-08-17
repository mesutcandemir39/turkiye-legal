---
argument-hint: ''
description: Açılacak davanın görevli mahkemesini (aile mahkemesi), yetkili yer mahkemesini,
  yargılama usulünü, tedbir taleplerini ve harç durumunu belirlemek; istinaf-temyiz
  yolunu planlamak gerektiğinde kullanıl
name: gorev-yetki-ve-usul
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Aile Davalarında Görev, Yetki ve Usul

## Görev
Aile hukuku uyuşmazlığında doğru mahkemeyi, yetkili yeri, yargılama usulünü, geçici hukuki korumayı ve kanun yolu rejimini belirleyerek usuli hataları önlemek.

## Soğuk başlangıç (intake)
1. Talep türü nedir (boşanma, nafaka, velayet, tasfiye, soybağı, koruma)?
2. Tarafların yerleşim yeri ve son birlikte oturdukları yer neresi?
3. Yabancı unsur veya yurt dışında verilmiş karar var mı (tanıma-tenfiz)?
4. Acil tedbir (tedbir nafakası, çocukla kişisel ilişki, 6284) gerekiyor mu?

## Denetim şeması
1. **Görev.** Aile hukukundan doğan dava ve işlerde görevli mahkeme **aile mahkemesidir** (4787 sK. m.4); aile mahkemesi bulunmayan yerlerde asliye hukuk mahkemesi bu sıfatla bakar. Görev kamu düzenindendir, re'sen gözetilir (HMK m.114/1-c, m.115).
2. **Yetki.** Boşanma/ayrılıkta yetkili mahkeme, eşlerden birinin yerleşim yeri veya davadan önce son defa altı aydan beri birlikte oturdukları yer mahkemesidir (TMK m.168). Nafaka davalarında nafaka alacaklısının yerleşim yeri mahkemesi de yetkilidir (HMK m.9 ve özel kural). 6284 başvurusunda mağdurun yerleşim yeri/şiddetin yapıldığı yer aile mahkemesi yetkilidir.
3. **Usul.** Boşanma ve fer'ileri yazılı yargılama usulüne (HMK m.118 vd.); dilekçeler aşaması, ön inceleme (m.137-142), tahkikat sırasıyla işler. Boşanmada hâkim re'sen araştırma ilkesini sınırlı uygular; tarafların üzerinde serbestçe tasarruf edemeyeceği konularda (çocuk, kamu düzeni) re'sen delil toplanabilir.
4. **Geçici hukuki koruma.** Dava süresince eş ve çocuk için tedbir nafakası, velayet, kişisel ilişki ve barınma tedbirleri (TMK m.169, m.182); ihtiyati tedbir (HMK m.389 vd.) mal kaçırma riskinde.
5. **Kanun yolu.** Aile mahkemesi kararlarına karşı istinaf (HMK m.341 vd.) ve kesinlik sınırı üstünde temyiz (m.361 vd.). Boşanma hükmü kesinleşmeden nüfusa işlenmez; fer'iler de bu ana bağlıdır.
6. **Yabancı unsur.** Yurt dışı boşanma kararının tanınması-tenfizi (5718 sK. MÖHUK m.50 vd.) veya nüfusta tescili (idari yol).

## Çıktı modülleri
- Görev-yetki-usul tespit notu ve dayanak maddeler.
- Geçici tedbir talep listesi.
- Kanun yolu ve süre takvimi (istinaf/temyiz) ile tanıma-tenfiz uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

