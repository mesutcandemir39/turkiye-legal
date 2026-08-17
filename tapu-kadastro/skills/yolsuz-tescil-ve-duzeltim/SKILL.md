---
argument-hint: ''
description: Tapu kaydındaki yolsuzluğun veya teknik/maddi hatanın (isim, soyadı,
  ada-parsel, pay, kimlik, mevki, yüzölçüm) giderilmesi gerektiğinde; idari düzeltme
  yolu ile düzeltim davası arasında ayrım yapmak v
name: yolsuz-tescil-ve-duzeltim
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
  - ad: Tapu Kanunu
    numara: '3402'
    tur: kanun
  - ad: Kat Özel Koşulu Olmak Üzere Yapılan Satış Mukavelelerine Dair Kanun
    numara: '2644'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yolsuz Tescil ve Tapu Kaydının Düzeltilmesi

## Görev
Yolsuz tescili veya kayıttaki maddi/teknik hatayı uygun yolla (idari düzeltme ya da düzeltim davası) gidermek; iyiniyetli üçüncü kişi korumasının sınırını çizmek.

## Soğuk başlangıç (intake)
- Hata türü ne: malik kimliği (ad-soyad-baba adı-TC), pay oranı, ada-parsel/mevki, yüzölçüm, sınır mı?
- Hata kayıttan mı (yazım/teknik) yoksa hukuki sebepten mi (geçersiz devir) kaynaklanıyor?
- Kayıt üzerinde sonradan iyiniyetli üçüncü kişi kazanımı oluşmuş mu?
- Tapu müdürlüğüne idari başvuru yapıldı mı, sonuç ne oldu?

## Denetim şeması
1. **Hatanın kaynağını ayır.** Salt yazım/teknik hata (kimlik bilgisi, yüzölçüm, mevki) → idari düzeltme yolu (2644 sayılı Tapu Kanunu m.31 ve Tapu Sicili Tüzüğü; tapu müdürlüğü re'sen veya talep üzerine düzeltir). Hukuki sebepten kaynaklanan yolsuzluk → düzeltim/iptal davası.
2. **Yolsuz tescili tanımla.** Bağlayıcı olmayan bir hukuki işleme dayanan veya hukuki sebepten yoksun tescil yolsuzdur (TMK m.1024). Gerçek hak sahibi düzeltme isteyebilir (TMK m.1025).
3. **Üçüncü kişi süzgeci.** Yolsuz tescile güvenerek iyiniyetle ayni hak kazanan üçüncü kişi korunur (TMK m.1023); düzeltim ona karşı ileri sürülemez, bu halde TMK m.1007 tazminatı gündeme gelir.
4. **İdari yolun sınırı.** İdari düzeltme yalnızca tarafların ve üçüncü kişilerin haklarını etkilemeyen, çekişmesiz teknik hatalarda mümkündür. Maliki/payı değiştirecek nitelikte ise dava şarttır.
5. **Görev/yetki ve husumet.** Düzeltim davasında görevli asliye hukuk, yetki taşınmaz yeri (HMK m.12); husumet kayıt maliki/ilgililer ve gerektiğinde Hazine.
6. **İspat.** Nüfus kaydı, veraset ilamı, eski akit tablosu, kadastro tutanağı, fen bilirkişisi (yüzölçüm/sınır).
7. **Ara sonuç.** İdari düzeltme yeterli mi yoksa dava mı; üçüncü kişi engeli var mı.

## Çıktı modülleri
- İdari yol mu / dava mı karar ağacı.
- Tapu müdürlüğüne düzeltme dilekçesi veya düzeltim davası iskeleti.
- İyiniyetli üçüncü kişi / TMK m.1007 tazminat alternatifi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

