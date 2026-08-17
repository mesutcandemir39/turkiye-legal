---
argument-hint: ''
description: İcracı sanatçı, fonogram veya film yapımcısı ile yayın kuruluşunun hakları
  söz konusu olduğunda ya da toplu hak yönetimi/meslek birliği yetkisi tartışıldığında;
  bağlantılı hakların kapsamını ve tarife
name: baglantili-haklar-meslek-birlikleri
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Bağlantılı Haklar ve Meslek Birlikleri

## Görev
Eser sahipliğinden ayrı olan bağlantılı (komşu) hakların kapsamını belirlemek ve toplu hak yönetimi yapan meslek birliklerinin yetki, tarife ve takip sistemini değerlendirmek.

## Soğuk başlangıç (intake)
- Hak sahibi icracı sanatçı, fonogram yapımcısı, film yapımcısı mı, yayın kuruluşu mu?
- Kullanım nerede gerçekleşiyor (mekânda müzik yayını, yayın, çoğaltma, çevrimiçi)?
- Eser sahibinin hakkı mı, bağlantılı hak mı, yoksa ikisi birden mi ihlal ediliyor?
- Karşı taraf meslek birliğiyle sözleşme/tarife ilişkisi içinde mi?

## Denetim şeması
1. Bağlantılı hak süjeleri (m.80): İcracı sanatçılar, fonogram (ses taşıyıcısı) yapımcıları, film (ilk tespit) yapımcıları ve radyo-televizyon kuruluşları; her birinin tespit, çoğaltma, yayma, umuma iletim üzerinde komşu hakları vardır. Bunlar eser sahibinin haklarına halel getirmez (m.80/son).
2. Eser sahibiyle ilişki: Bir müzik kullanımı hem eser sahibinin (besteci/söz yazarı) mali hakkını hem icracı ve fonogram yapımcısının bağlantılı hakkını ilgilendirebilir; izinler ayrı ayrı alınır.
3. İcracının manevi hakları: İcracının adının belirtilmesi ve icrasının tahrif edilmemesi hakları (m.80 atfıyla manevi koruma) gözetilir.
4. Meslek birlikleri (m.42 vd.): Hak sahipleri toplu hak yönetimi için meslek birliği kurar; birlik üyeleri adına izin verme, tarife belirleme ve takip yetkisine sahiptir. Umuma açık mahallerde (m.41) eser/bağlantılı hak kullanımı için sözleşme ve ödeme zorunluluğu değerlendirilir.
5. Tarife ve uyuşmazlık: Birliğin ilan ettiği tarife esas alınır; tarifeye itiraz/uzlaşma süreci ve aktif husumetin birliğe ait olduğu hâller (üyelik kapsamı) kontrol edilir.
6. Ara sonuç: İhlal edilen bağlantılı hak, sahibi, gerekli izinler ve yetkili meslek birliği belirlenir.

İspat yükü: birlik yetkisini ve hak sahipliğini ileri süren ispatlar; kullanım iznini/ödemeyi savunan taraf belgeler.

## Çıktı modülleri
- Bağlantılı hak ve eser sahibi hakkı ayrım tablosu (gerekli izinler).
- Meslek birliği yetki ve tarife değerlendirme notu.
- Umuma açık mahal kullanımı uyum/sözleşme önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

