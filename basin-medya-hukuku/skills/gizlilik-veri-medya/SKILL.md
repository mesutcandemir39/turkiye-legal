---
argument-hint: ''
description: Haber veya yayında özel hayatın gizliliği, görüntü-ses kaydının izinsiz
  yayını, kişisel verilerin işlenmesi ve KVKK ile basın özgürlüğü çatışması söz konusu
  olduğunda kullanılır.
name: gizlilik-veri-medya
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
  - ad: Basın Meslek İlkeleri ve Yapı İtibarı Hakkında Kanun
    numara: '5187'
    tur: kanun
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Özel Hayat, Kişisel Veri ve Medya

## Görev
Yayında özel hayatın gizliliği (Anayasa m.20), görüntü ve ses üzerindeki hak ile kişisel verilerin korunmasını (6698 sayılı KVKK) basın özgürlüğüyle dengelemek.

## Soğuk başlangıç (intake)
1. Yayımlanan içerik kişinin özel/aile hayatına mı ait?
2. Görüntü/ses rıza ile mi alındı, gizli mi kaydedildi?
3. İçerik kamusal tartışmaya katkı sunuyor mu?
4. Kişisel veri işleme gazetecilik istisnası kapsamında mı?

## Denetim şeması
1. **Özel hayat alanı**: Anayasa m.20 ve TMK m.24 koruması; kişinin gizli alanı, özel alanı ve kamuya açık alanı ayrımı yapılır. Kamuya mal olmuş kişilerde kamusal faaliyete ilişkin kısım daha düşük korumadan yararlanır.
2. **Görüntü ve ses**: İzinsiz kayıt ve yayım, rıza yoksa ve kamu yararı yoksa hukuka aykırıdır; TCK m.134 ve TMK m.24 birlikte değerlendirilir.
3. **KVKK çatışması**: Kişisel verilerin işlenmesi kural olarak rıza veya kanuni şarta bağlıdır (KVKK m.5). Ancak gazetecilik amacıyla işleme, ifade özgürlüğü kapsamında istisnaya tabidir; bu istisna kişilik hakkı ve özel hayat ölçüsünde sınırlıdır (KVKK m.28 değerlendirmesi).
4. **Tartım**: Kamuya katkı, kişinin tanınırlığı, elde etme yöntemi ve içeriğin biçimi ölçütleriyle menfaat dengesi kurulur.
5. **Ara sonuç**: Rıza/kamu yararı yoksa ihlal sabittir; gazetecilik istisnası ölçülü kalmamışsa KVKK koruması devreye girer.

## Çıktı modülleri
- Özel hayat alan sınıflandırması
- KVKK gazetecilik istisnası tartım notu
- İçerik kaldırma/tazminat yol önerisi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

