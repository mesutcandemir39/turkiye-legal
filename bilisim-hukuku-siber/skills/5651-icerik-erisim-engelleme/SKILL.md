---
argument-hint: ''
description: İnternette yer alan hukuka aykırı içeriğe karşı içeriğin çıkarılması,
  erişimin engellenmesi ve özel hayatın korunması başvurularını; içerik/yer/erişim
  sağlayıcı sorumluluğunu çözmek gerektiğinde kulla
name: hukum-5651-icerik-erisim-engelleme
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# 5651 İçerik Kaldırma ve Erişim Engelleme

## Görev
İnternet ortamındaki hukuka aykırı içeriğe karşı 5651 sayılı Kanun yollarını seçmek; doğru başvuru merciini, usulü ve süreyi belirlemek; sağlayıcı sorumluluğunu değerlendirmek.

## Soğuk başlangıç (intake)
1. İçerik ne ve nerede? (URL, platform, yayın tarihi?)
2. İhlal türü ne? (kişilik hakkı, özel hayat, hakaret, telif, katalog suç?)
3. Önce sağlayıcıya başvuruldu mu, yanıt geldi mi?
4. Acil mi (özel hayat, gecikmesinde sakınca) yoksa olağan mı?

## Denetim şeması
1. **Sağlayıcı sıfatı.** 5651'de içerik, yer, erişim ve toplu kullanım sağlayıcı tanımları (m.2) sorumluluk ve muhatabı belirler. Yer sağlayıcı kural olarak içeriği denetlemekle yükümlü değildir ancak uyar-kaldır yükümlülüğü doğabilir.
2. **İçeriğin çıkarılması / erişimin engellenmesi (m.9).** Kişilik hakkı ihlal edilen kişi önce içerik/yer sağlayıcıya başvurabilir; sonuç alınamazsa sulh ceza hâkimliğine başvurarak içeriğin çıkarılması ve/veya erişimin engellenmesini isteyebilir. Hâkim kararını talepten itibaren kanunda öngörülen kısa sürede (24 saat) verir; karara karşı itiraz yolu açıktır.
3. **Özel hayatın gizliliği (m.9/A).** Özel hayatın gizliliğinin ihlali halinde doğrudan BTK'ya başvurarak erişimin engellenmesi istenebilir; gecikmesinde sakınca bulunan hallerde BTK Başkanı resen tedbir uygulayıp 24 saat içinde hâkim onayına sunar.
4. **Katalog suçlar ve resen engelleme (m.8).** Kanunda sayılan katalog suçlara ilişkin içerikte hâkim/savcı veya BTK kararıyla erişim engellenir. Ölçülülük gereği URL bazlı engelleme tercih edilir; aşırı geniş engelleme hukuka aykırı olabilir.
5. **İspat ve ara sonuç.** İhlal ve içeriğin varlığı başvurucu tarafından belgelenir (ekran görüntüsü + URL + tarih, mümkünse noter/teknik tespit). Doğru yol (m.9 / m.9/A / m.8), mercі ve süre belirlenir.

## Çıktı modülleri
- Yol seçim tablosu (sağlayıcı başvurusu / sulh ceza / BTK).
- İçerik çıkarma-erişim engelleme başvuru/dilekçe taslağı.
- İtiraz dilekçesi iskeleti ve ölçülülük argümanı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

