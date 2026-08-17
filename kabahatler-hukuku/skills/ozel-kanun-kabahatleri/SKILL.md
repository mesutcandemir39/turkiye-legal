---
argument-hint: ''
description: Trafik, belediye-zabıta, tütün, çevre, gıda, iş sağlığı gibi özel kanunlardaki
  kabahatlerde özel hüküm ile 5326 genel hükümleri arasındaki ilişkiyi kurmak ve sektöre
  özgü usulü uygulamak gerektiğinde
name: ozel-kanun-kabahatleri
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


# Özel Kanun Kabahatleri ve Sektörel Uygulama

## Görev
Özel kanunla düzenlenmiş bir kabahatte (KTK, belediye/zabıta, tütün, çevre vb.), özel hükmün önceliğini ve 5326 genel hükümlerinin tamamlayıcı uygulamasını kurarak doğru usulü işletmek.

## Soğuk başlangıç (intake)
- Hangi özel kanun ve hangi madde uygulanmış?
- Özel kanun başvuru yolunu/süreyi ayrıca düzenlemiş mi?
- Yaptırımı veren idare özel kanunda yetkili kılınmış mı?
- Tutanak/karar özel kanunun aradığı şekil şartlarını taşıyor mu?

## Denetim şeması
1. **Genel-özel ilişkisi (5326 m.3):** Tanım, miktar ve usul özel kanunda varsa o uygulanır; boşluk kalan her noktada 5326 genel hükümleri (kast-taksir m.9, içtima m.15, zamanaşımı m.20-21, başvuru m.27) tamamlar.
2. **Trafik (2918 KTK):** İdari para cezası tutanağı; başvuru yolu kural olarak sulh ceza hâkimliği (5326 m.27), ancak sürücü belgesi geri alma gibi işlemlerde idari yargı görev ayrımını kontrol et.
3. **Belediye/zabıta (5393, 1608):** Zabıta tutanaklarına dayanan idari yaptırımlar; encümen/belediye yetkisi ve tebligat denetlenir.
4. **Çevre (2872):** İdari para cezaları ve idari tedbirler; bazı işlemler idari yargının görev alanına girebilir (5326 m.27/8 ayrımı belirleyici).
5. **Tütün (4207), gıda, İSG (6331):** Özel kanundaki miktar ve nispi/maktu yapı esas alınır; takdir ölçütleri (5326 m.17/2) gösterilmeli.
6. **Yargı yolu kontrolü:** Özel kanun aksini öngörmedikçe başvuru sulh ceza hâkimliğine; idari işlemle bütünleşen yaptırımlarda idari yargı. Ara sonuç olarak doğru mercii sabitle.

İspat yükü idarede; sektöre özgü teknik tespitlerin (cihaz, numune) usulü ayrıca denetlenir.

## Çıktı modülleri
- Özel kanun + 5326 eşleştirme tablosu.
- Yargı yolu tespiti (sulh ceza mı / idari yargı mı).
- Sektörel şekil-şart kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

