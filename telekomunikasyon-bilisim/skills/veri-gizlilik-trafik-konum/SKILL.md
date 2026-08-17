---
argument-hint: ''
description: Trafik ve konum verisi işleme, abone verisinin gizliliği, haberleşmenin
  gizliliği, ticari elektronik iletide rıza ve KVKK ile 5809 m.51 kesişimi söz konusu
  olduğunda kullanılır.
name: veri-gizlilik-trafik-konum
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
  - ad: Telekomunikasyon Kanunu
    numara: '5809'
    tur: kanun
  - ad: Elektronik Ticaretin Düzenlenmesine Dair Kanun
    numara: '5651'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Elektronik Haberleşmede Veri, Gizlilik ve Ticari İleti

## Görev
Telekom/internet faaliyetinde kişisel veri, trafik-konum verisi ve haberleşmenin gizliliği yükümlülüklerini 5809 m.51, KVKK (6698) ve ticari ileti rejimi (6563) çerçevesinde denetlemek; uyum veya ihlal sorumluluğunu belirlemek.

## Soğuk başlangıç (intake)
1. İşlenen veri türü: abone kimlik, trafik, konum, içerik/haberleşme verisi mi?
2. İşleme amacı (faturalama, pazarlama, güvenlik, yasal talep) ve dayanağı nedir?
3. Ticari elektronik ileti gönderiliyor mu; İYS kaydı ve rıza var mı?
4. Bir veri ihlali, talep (ilgili kişi/adli/idari) veya Kurul incelemesi var mı?

## Denetim şeması
1. **Çerçeve kesişimi**: 5809 m.51 — kişisel veri ve gizlilik; trafik/konum verisinin sınırlı amaçla işlenmesi ve anonimleştirme/silme. KVKK genel rejimi (6698 m.4-6 işleme şartları, m.5-6 hukuki sebepler) birlikte uygulanır. Ara sonuç: işleme dayanağı geçerli mi.
2. **Trafik ve konum verisi**: Faturalama ve hizmet dışında işleme için kural olarak abone/kullanıcı rızası; sürenin sonunda silme/anonimleştirme. Konum verisi katma değerli hizmette ek rıza gerektirir.
3. **Haberleşmenin gizliliği**: Anayasa m.22 ve 5809 — içeriğe erişim ancak hâkim kararı/yasal yetkiyle; yetkisiz dinleme/kayıt TCK m.132-138 ve m.243-245 ile yarışabilir.
4. **Ticari elektronik ileti**: 6563 — önceden onay (İYS kaydı), ileti içeriği ve red (ICODE/abonelikten çıkma) hakkı; onaysız ileti idari para cezası doğurur. KVKK pazarlama rızasıyla birlikte değerlendirilir.
5. **İhlal ve bildirim**: Veri ihlalinde KVKK m.12 bildirim (Kurul ve ilgili kişi); 5809 kapsamında BTK bildirim yükümlülükleri ayrıca işler. Yasal talepte (adli/idari) yetki ve ölçülülük denetlenir.

İspat açısından rıza kayıtları, İYS onayı, log ve silme/anonimleştirme süreçleri belirleyicidir.

## Çıktı modülleri
- Veri işleme uyum/boşluk notu (dayanak/süre/rıza).
- İhlal bildirimi veya ilgili kişi başvurusu yanıt taslağı.
- Ticari ileti ve İYS uyum kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

