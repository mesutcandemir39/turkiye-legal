---
argument-hint: ''
description: İdarenin işlem veya eyleminden doğan maddi-manevi zararın tazmini için
  tam yargı davasını ve idarenin kusurlu/kusursuz sorumluluk rejimini değerlendirmek
  amacıyla kullanılır; zarar gören kişiye tazmin
name: tam-yargi-davasi
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  - ad: İdari Yargılama Usulü Kanunu
    numara: '2577'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Tam Yargı Davası ve İdarenin Sorumluluğu

## Görev
İdarenin işlem/eyleminden doğan zararın tazmini için tam yargı davasını kurgulamak ve idarenin sorumluluk türünü (hizmet kusuru / kusursuz sorumluluk) belirlemek. İYUK m.2/1-b ve Anayasa m.125/son ekseninde çalışır.

## Soğuk başlangıç (intake)
1. Zarar bir idari işlemden mi, idari eylemden mi (fiili faaliyet/ihmal) doğuyor?
2. Zararın türü (maddi/manevi) ve miktarı belirlenebiliyor mu; belgeleri var mı?
3. Zarar tarihi ve idarenin zarara yol açan davranışı ne zaman öğrenildi?
4. İYUK m.13 ön başvurusu (eylemlerde) yapıldı mı?

## Denetim şeması
1. **Sorumluluğun kaynağı.** İşlemden doğan zararda iptal + tazmin birlikte istenebilir; eylemden doğan zararda İYUK m.13 uyarınca **önce idareye başvuru** zorunludur (eylemin/zararın öğrenilmesinden itibaren bir yıl ve her halde beş yıl içinde).
2. **Sorumluluk türü.** (a) **Hizmet kusuru:** hizmetin kötü işlemesi, geç işlemesi veya hiç işlememesi. (b) **Kusursuz sorumluluk:** risk ilkesi ve fedakârlığın denkleştirilmesi (sosyal risk dâhil belirli hallerde). Kusursuz sorumlulukta kusur aranmaz, illiyet ve zarar yeterlidir.
3. **Unsurlar.** Zarar (gerçek, kesin, kişisel), idareye yüklenebilir davranış ve **illiyet bağı**. İlliyeti kesen mücbir sebep, beklenmeyen hal, zarar görenin/üçüncü kişinin ağır kusuru sorumluluğu kaldırabilir veya azaltabilir.
4. **Süre.** İşlemden doğan tazminatta dava süresi iptal davası süresine bağlanır (İYUK m.7, m.12); eylemde m.13 başvurusu üzerine ret/zımni ret sonrası dava süresi işler.
5. **İspat.** Re'sen araştırma (İYUK m.20) geçerli olsa da zarar ve illiyeti davacı ortaya koymalı; tazminat hesabında bilirkişi sıkça devreye girer.
6. **Ara sonuç.** Sorumluluk türü + unsurların karşılanma durumu + talep edilebilir tazminat kalemleri (maddi/manevi, faiz başlangıcı).

## Çıktı modülleri
- Sorumluluk türü ve gerekçesi.
- Unsur (zarar/illiyet/yüklenebilirlik) değerlendirme tablosu.
- İYUK m.13 başvuru dilekçesi taslağı (eylem halinde).
- Tazminat kalemleri ve faiz talebi notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

