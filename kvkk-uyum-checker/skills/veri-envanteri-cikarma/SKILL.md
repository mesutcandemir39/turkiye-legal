---
argument-hint: ''
description: Kuruluşun hangi veriyi hangi amaç ve hukuki sebeple işlediğinin haritalanması,
  mevcut envanterin doğrulanması veya sıfırdan envanter oluşturulması gerektiğinde
  kullanılır.
name: veri-envanteri-cikarma
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kişisel Veri İşleme Envanteri Çıkarma

## Görev
Tüm uyum mimarisinin temel taşı olan kişisel veri işleme envanterini çıkarmak veya mevcut envanteri fiili işleme ile karşılaştırarak doğrulamak. Diğer her belge (aydınlatma, VERBİS, saklama matrisi) envanterle tutarlı olmak zorundadır.

## Soğuk başlangıç (intake)
1. Hangi süreçlerde kişisel veri toplanıyor (işe alım, satış, üyelik, ziyaretçi kaydı, kamera)?
2. Her süreçte hangi veri kategorileri işleniyor; özel nitelikli veri (m.6) var mı?
3. Veri kimlerden alınıyor, kime aktarılıyor, nerede saklanıyor (yurt içi/yurt dışı, bulut)?
4. Mevcut bir envanter var mı, ne zaman güncellendi?

## Denetim şeması
1. **Faaliyet bazlı kayıt**: Her işleme faaliyeti için satır açılır — faaliyet adı, veri konusu kişi grubu, veri kategorileri, işleme amacı.
2. **Hukuki sebep haritalama (m.5/m.6)**: Her faaliyet için geçerli işleme şartı yazılır; açık rıza dışı sebepler önce denenir, açık rızaya gereksiz bağımlılık "kırmızı bayrak" olarak işaretlenir.
3. **Aktarım ve saklama sütunları**: Alıcı/alıcı grupları, yurt içi/yurt dışı aktarım, aktarım mekanizması (m.8-9), azami saklama süresi (m.4/2-d dayanağıyla).
4. **Özel nitelikli ve hassas alanlar**: m.6 verisi, çocuk verisi, biyometrik/kamera kayıtları ayrı işaretlenir; bunlar yüksek risk grubudur.
5. **Tutarlılık çapraz kontrolü**: Envanter, VERBİS kaydı ve aydınlatma metinleriyle satır satır karşılaştırılır; uyumsuzluklar bulgu listesine geçer.
6. **Ara sonuç**: Eksik/çelişkili envanter, m.4 ilke ihlallerinin ve VERBİS hatalarının kaynağıdır; envanter "yaşayan" belge olarak güncelleme döngüsüne bağlanır.

İspat yükü: İşlemenin geçerli şarta dayandığını ve envanterin gerçeği yansıttığını veri sorumlusu gösterir.

## Çıktı modülleri
- Faaliyet bazlı işleme envanteri tablosu (Excel'lenebilir).
- Hukuki sebep–faaliyet eşleştirme ve "açık rıza bağımlılığı" uyarı listesi.
- Envanter–VERBİS–aydınlatma tutarlılık çapraz kontrol raporu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

