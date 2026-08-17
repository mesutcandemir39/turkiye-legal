---
argument-hint: ''
description: Eser, işleme, çoğaltma, umuma iletim, intihal veya yazılım kopyalama
  iddialarında FSEK çerçevesinde eser niteliği, mali-manevi hak ihlali ve ihlal eden
  fiilin tespiti gerektiğinde kullanılır.
name: telif-fsek-ihlal
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Telif Hakkı İhlali Denetimi (FSEK)

## Görev
Bir fikir ve sanat eseri üzerindeki mali veya manevi hakkın ihlal edilip edilmediğini FSEK çerçevesinde belirlemek ve ref'/men/tazminat taleplerini hazırlamak.

## Soğuk başlangıç (intake)
- İhlale konu yapıt nedir (yazı, müzik, yazılım, görsel, sinema eseri)?
- Yapıt FSEK m.1/B-2 anlamında "sahibinin hususiyetini taşıyan" eser mi; hangi türe girer (m.2-6)?
- Eser sahibi/hak sahibi kim; devir-lisans var mı; çalışan eseri (m.18/2) mi?
- İhlal çoğaltma, yayma, umuma iletim, işleme yoksa manevi hak (ad belirtme, bütünlük) ihlali mi?

## Denetim şeması
1. Eser niteliği: Yapıtın eser sayılması için fikrî çaba ve hususiyet aranır (FSEK m.1/B, m.2-6). Fikir değil ifade korunur; sıradan/teknik zorunluluk taşıyan unsurlar dışlanır.
2. Hak sahipliği: Eser sahibi onu meydana getirendir (m.8); çalışanın eseri işverene (m.18/2), sipariş üzerine eserlerde sözleşme belirleyici. Bağlantılı haklar (icracı, yapımcı, yayın) m.80.
3. İhlal edilen hak: Mali haklar — işleme (m.21), çoğaltma (m.22), yayma (m.23), temsil (m.24), umuma iletim/işaret-ses-görüntü nakli (m.25). Manevi haklar — umuma arz, adın belirtilmesi, eserde değişiklik yasağı (m.14-16).
4. İhlal fiili ve benzerlik: İntihal/kopyalamada esaslı benzerlik ve erişim ölçütü; yazılımda kaynak kod kopyalama veya yetkisiz çoğaltma. İstisnalar (iktibas m.35, kişisel kullanım m.38) denetlenir.
5. İspat yükü: Eser sahipliği ve ihlal davacıda; lisans/izin savunması davalıda. Tarih/öncelik için delil tespiti (HMK m.400) ve noter onayı.
6. Ara sonuç: İhlal sabitse tecavüzün ref'i (m.66-68), men'i (m.69) ve tazminat (m.68 üç kata kadar bedel; m.70 maddi-manevi) kurgulanır.

## Çıktı modülleri
- Eser niteliği ve hak sahipliği değerlendirmesi.
- İhlal edilen mali/manevi hak listesi (FSEK madde atıflı).
- Talep ve tazminat seçeneği notu (m.68/m.70).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

