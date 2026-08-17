---
argument-hint: ''
description: Kiralananda teslimden önce/sonra ayıp, onarım yükümlülüğü, kira indirimi,
  giderlerin kime ait olduğu veya kiracının kullanımdan yoksun kalması söz konusu
  olduğunda bu beceriyi kullan.
name: kiralanan-ayip-onarim-kullanim
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Kiralananın Ayıbı, Onarım ve Kullanıma Elverişlilik

## Görev
Kiralananın sözleşmeye uygun, kullanıma elverişli halde tutulması yükümlülüğünü ve ayıp hükümlerini uygulamak; kiracının kira indirimi, onarım, gider ve tazminat taleplerini; tarafların bakım-onarım yükünü saptamak.

## Soğuk başlangıç (intake)
- Ayıp teslim anında mı vardı, sonra mı doğdu?
- Ayıbın niteliği ne (kullanımı engelleyen mi, küçük mü)?
- Kiracı kiraya vereni bildirim/ihtarla uyardı mı?
- Hangi onarımlar yapıldı, masrafı kim karşıladı?

## Denetim şeması
1. **Teslim ve elverişli halde bulundurma (TBK m.301)**: Kiraya veren, kiralananı sözleşmede amaçlanan kullanıma elverişli halde teslim eder ve kira süresince bu halde **bulundurur**.
2. **Teslim sırasında ayıp (TBK m.304)**: Kiralanan önemli ayıpla teslim edilirse, kiracı genel hükümlere (ifa etmeme) başvurabilir; önemsiz ayıpta kullanım sürerken ayıbın giderilmesi istenebilir.
3. **Sonradan doğan ayıp (TBK m.305-306)**: Kiracı seçimlik haklar kullanabilir — ayıbın giderilmesi, kira bedelinden **orantılı indirim** (m.307), **zararın giderimi** (m.308) ve şartları varsa **fesih**. Ayıbı kiraya verene bildirme yükü kiracıdadır.
4. **Ayıbın giderilmesi/kiracının onarımı (m.306)**: Kiraya veren makul sürede gidermezse, kiracı ayıbı giderip masrafı kiradan düşebilir veya benzer kiralanan temin edebilir.
5. **Temizlik ve küçük onarımlar (TBK m.317)**: Olağan kullanımın gerektirdiği temizlik ve bakım giderleri kiracıya; esaslı onarım kiraya verene aittir.
6. **Üçüncü kişinin/üstün hakkın ileri sürülmesi (TBK m.309-312)**: Zapt benzeri durumlarda kiracının hakları.
7. **İspat ve ara sonuç**: Ayıbın varlığı ve niteliği (keşif/bilirkişi), bildirim, indirim/gider hesabı.

## Çıktı modülleri
- Ayıp türü-seçimlik hak eşleştirmesi.
- Kira indirimi/gider hesabı taslağı.
- Kiraya verene ayıp bildirim ihtarnamesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

