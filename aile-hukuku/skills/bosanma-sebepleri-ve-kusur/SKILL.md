---
argument-hint: ''
description: Boşanma davasının özel veya genel sebebe dayandırılması, kusur dağılımının
  kurgulanması ve buna bağlı tazminat-nafaka sonuçlarının öngörülmesi gerektiğinde
  kullanılır; anlaşmalı ve çekişmeli boşanma a
name: bosanma-sebepleri-ve-kusur
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
  - ad: Ailenin Korunması ve Kadına Karşı Şiddetin Önlenmesine Dair Kanun
    numara: '6284'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Boşanma Sebepleri ve Kusur Analizi

## Görev
Somut olayı doğru boşanma sebebine oturtmak (TMK m.161-166), kusur dağılımını delil temelinde kurgulamak ve bunun tazminat (m.174) ile yoksulluk nafakasına (m.175) etkisini öngörmek.

## Soğuk başlangıç (intake)
1. Boşanma talebi karşı tarafça kabul ediliyor mu (anlaşmalı mı, çekişmeli mi)?
2. Hangi olgular var: zina, şiddet, hakaret, terk, güven sarsıcı davranış, ekonomik şiddet?
3. Bu olgular ne zaman öğrenildi/gerçekleşti (süre hesabı için)?
4. Tarafların ekonomik-sosyal durumu ve kusur dengesi hakkındaki ilk değerlendirme nedir?

## Denetim şeması
1. **Özel sebep var mı?** Zina (m.161) → dava hakkı, öğrenmeden başlayarak 6 ay, her halde 5 yıl içinde düşer (m.161/2); af halinde dava hakkı yoktur. Hayata kast/pek kötü/onur kırıcı davranış (m.162) → aynı 6 ay-5 yıl hak düşürücü süre. Suç işleme ve haysiyetsiz hayat sürme (m.163), terk (m.164: ihtar şartı, en az 6 ay ayrı yaşama + 2 ay ihtar süresi), akıl hastalığı (m.165).
2. **Özel sebep yoksa genel sebep.** Evlilik birliğinin temelinden sarsılması (m.166/1-2): birlik ortak hayatı sürdürmeleri beklenmeyecek derecede sarsılmış olmalı; davacının kusuru daha ağırsa davalının itiraz hakkı (m.166/2 son cümle) tartışılır.
3. **Kusur tespiti ve ispat.** Her bir vakıa tanık, mesaj/kayıt, rapor ile kanıtlanır; ispat yükü iddia edene aittir (TMK m.6, HMK m.190). Kusur dengesi tazminat ve yoksulluk nafakasının ön şartıdır: tazminat isteyen kusursuz/az kusurlu olmalı (m.174), yoksulluk nafakası isteyen daha fazla kusurlu olmamalıdır (m.175).
4. **Anlaşmalı boşanma (m.166/3).** En az 1 yıl evlilik + tarafların hâkim önünde iradesi + hâkimce uygun bulunan protokol (mali sonuçlar ve çocuk düzenlemeleri) şarttır.
5. **Ara sonuç.** Sebep + kusur oranı + fer'i sonuçlar birlikte raporlanır.

## Çıktı modülleri
- Sebep-vakıa-delil eşleştirme tablosu ve kusur dengesi değerlendirmesi.
- Süre/hak düşürücü süre kontrol listesi.
- Anlaşmalı boşanma protokolü iskelet uyarısı veya çekişmeli strateji notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

