---
argument-hint: ''
description: Yurt içi/yurt dışı veri aktarım mekanizmalarının (7499 sonrası m.9) ve
  VERBİS kayıt yükümlülüğü ile kayıt içeriğinin doğruluğu denetlenirken kullanılır.
name: aktarim-ve-verbis-denetimi
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


# Aktarım ve VERBİS Kayıt Denetimi

## Görev
İki sık ihlal başlığını birlikte denetlemek: (1) yurt içi (m.8) ve 7499 ile yeniden kurgulanan yurt dışı (m.9) aktarımların doğru mekanizmaya dayanıp dayanmadığı; (2) VERBİS (m.16) kayıt yükümlülüğü ve kaydın envanterle tutarlılığı.

## Soğuk başlangıç (intake)
1. Veri kimlere aktarılıyor — yurt içi üçüncü kişi, yurt dışı alıcı, bulut/SaaS sağlayıcı?
2. Yurt dışı alıcının bulunduğu ülke Kurul'un yeterlilik kararı verdiği bir ülke mi?
3. Aktarım sürekli mi, arızi mi; mevcut bir aktarım sözleşmesi var mı?
4. Kuruluşun VERBİS kaydı var mı, güncel mi; istisna iddiası belgeli mi?

## Denetim şeması
1. **Yurt içi aktarım (m.8)**: Aktarım da işlemedir; m.5/m.6 şartına ve m.4 ilkelerine dayanmalı. Veri işleyene aktarımda m.12 sözleşmesi şart; eksikse bulgu.
2. **Yurt dışı hiyerarşisi (m.9, 7499 sonrası)**: Önce yeterlilik kararı (m.9/1); yoksa uygun güvenceler (m.9/3 — uluslararası anlaşma, Kurul onaylı bağlayıcı şirket kuralları, Kurul'un ilan ettiği standart sözleşme [imzadan itibaren 5 iş günü içinde Kurul'a bildirim], izinli taahhütname); bunlar yoksa yalnızca arızi haller (m.9/6). Sürekli aktarımda arızi haller mekanizması kullanılamaz — bu yaygın bir hatadır.
3. **VERBİS yükümlülük testi (m.16)**: İşlemeye başlamadan önce kayıt esastır. İstisna eşikleri (çalışan sayısı/yıllık mali bilanço, ana faaliyetin özel nitelikli veri işleme olmaması) Kurul kararıyla belirlenir [güncel eşikler doğrulanacak — kvkk.gov.tr]; yurt dışında yerleşik sorumlu için eşik aranmaz.
4. **Kayıt içeriği tutarlılığı**: VERBİS'teki amaç, veri kategorisi, alıcı grupları, aktarım ve saklama süreleri envanterle birebir karşılaştırılır; sapma bulgudur.
5. **Ara sonuç**: Yanlış aktarım mekanizması ve eksik/tutarsız VERBİS kaydı m.18 yaptırım sebebidir.

İspat yükü: Aktarım güvencelerinin ve VERBİS istisnasının varlığını (çalışan/bilanço belgeleriyle) veri sorumlusu ispatlar.

## Çıktı modülleri
- Aktarım envanteri (alıcı, ülke, mekanizma, dayanak, bildirim durumu).
- Yurt dışı aktarım karar akış şeması (yeterlilik → güvence → arızi hal).
- VERBİS–envanter tutarlılık raporu ve istisna değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

