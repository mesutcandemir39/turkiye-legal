---
argument-hint: ''
description: Kasten/taksirle yaralama, öldürme, tehdit, şantaj, cebir ve kişiyi hürriyetinden
  yoksun kılma gibi kişi varlığına yönelik suçların unsurlarını ve nitelikli hallerini
  denetlemek gerektiğinde kullanılır
name: kisilere-karsi-suclar
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kişilere Karşı Suçlar (Yaralama, Tehdit, Hürriyet)

## Görev
Hayata, vücut dokunulmazlığına ve hürriyete karşı suçlarda tipiklik unsurlarını, nitelikli halleri ve cezayı etkileyen halleri madde metniyle altlamak.

## Soğuk başlangıç (intake)
- Yaralanma var mı; basit tıbbi müdahaleyle giderilebilir mi, kemik kırığı/çıkığı veya yaşamsal tehlike var mı?
- Fiil kasten mi taksirle mi (trafik, iş kazası vb.) gerçekleşti?
- Tehdit/cebir varsa neyle, hangi içerikle yapıldı; silah kullanıldı mı?
- Mağdur belli bir süre serbestçe hareket edemedi mi?

## Denetim şeması
1. Kasten yaralama (TCK m.86): Hareket + vücutta acı/sağlık bozulması neticesi + kast. Basit tıbbi müdahaleyle giderilebilirse m.86/2 (şikâyete bağlı). Nitelikli haller m.86/3 (silahla, kamu görevlisine karşı, canavarca hisle). Neticesi sebebiyle ağırlaşmış yaralama m.87 (duyu/organ kaybı, kemik kırığı m.87/3, çocuk düşürme, ölüm m.87/4).
2. Taksirle yaralama (TCK m.89): Dikkat-özen yükümlülüğü ihlali, öngörülebilir netice; bilinçli taksir (m.22/3) cezayı artırır. Kural olarak şikâyete bağlı; bilinçli taksir hali şikâyet aranmaz.
3. Kasten öldürme (TCK m.81) ve nitelikli halleri (m.82: tasarlama, canavarca, kan gütme, töre saiki, kamu görevlisine karşı). Ölümle yaralanma sınırı: failin kastının yöne(l)imi ve eylemin elverişliliği (kast-taksir ayrımı m.21-22) belirleyicidir.
4. Tehdit (TCK m.106): Bir kötülüğün gerçekleştirileceğinin bildirilmesi; malvarlığına yönelikse alt sınır farklı. Silahla/birden fazla kişiyle m.106/2 nitelikli. Şantaj m.107, cebir m.108 ile sınırı çiz.
5. Hürriyetten yoksun kılma (TCK m.109): Kişinin hareket serbestisinin hukuka aykırı kısıtlanması; cebir/tehditle, kamu görevlisi tarafından veya cinsel amaçla nitelikli hal. Etkin pişmanlık m.110.
6. Ispat yükü ve ara sonuç: ATK/adli rapor yaralanmanın derecesini belirler; tehditte içerik ve mağdur üzerindeki etki delillendirilmeli. Hangi maddenin hangi fıkrasının uygulanacağını ve şikâyet/uzlaştırma durumunu sonuçlandır.

## Çıktı modülleri
- Unsur altlama tablosu (fiil, netice, manevi unsur, nitelikli hal) madde atıflı.
- Adli rapor değerlendirme notu (yaralanmanın hukuki nitelendirmesi).
- Şikâyet/uzlaştırma ve olası ceza aralığı özeti.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

