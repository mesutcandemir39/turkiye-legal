---
argument-hint: ''
description: Bir patentin/faydalı modelin hükümsüz kılınması ya da tecavüz davasında
  geçersizlik savunması gündeme geldiğinde kullanılır; sebep envanteri ve geçmişe
  etkili sonuçların değerlendirilmesi için temel b
name: hukumsuzluk-denetimi
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
  version: 0.1.0
user-invocable: true
---


# Patent ve Faydalı Model Hükümsüzlüğü

## Görev
SMK m.138 hükümsüzlük sebeplerini envanterlemek, dava şartlarını ve husumet ilişkisini kurmak, hükümsüzlüğün SMK m.139 geçmişe etkili sonuçlarını değerlendirmek.

## Soğuk başlangıç (intake)
1. Hangi sebep ileri sürülüyor: yenilik/buluş basamağı yokluğu, yetersiz açıklama, kapsam aşımı, gasp?
2. Elde yeni prior art belgesi var mı; tarihi başvuru/rüçhandan önce mi?
3. Talep eden kimin menfaati var; gerçek hak sahibi iddiası mı?
4. Patentin verdiği zarar/lisans/tecavüz davası var mı (menfaat için)?

## Denetim şeması
1. **Sebepler (SMK m.138/1).** (a) m.82-83 patentlenebilirlik şartının yokluğu (yenilik, buluş basamağı, sanayiye uygulanabilirlik); (b) buluşun yeterince açık ve tam tarif edilmemesi (m.92/4); (c) konunun başvuru kapsamını aşması; (d) patent sahibinin gerçek hak sahibi olmaması (gasp). Ara sonuç: hangi sebep(ler) somut olayda var?
2. **Kısmî hükümsüzlük (SMK m.138/6).** Sebep istemlerin bir kısmına ilişkinse yalnızca o istemler iptal edilir; patent sahibine istem sınırlandırma imkânı tanınır.
3. **Husumet ve menfaat.** Hükümsüzlük davasını menfaati olanlar açabilir; gasp sebebine dayalı hükümsüzlüğü yalnızca gerçek hak sahibi ileri sürebilir (m.138/2-3).
4. **Süre ve sonuç (SMK m.139).** Hükümsüzlük kararı geçmişe etkilidir; koruma baştan doğmamış sayılır. Ancak kesinleşmiş tecavüz kararları, ödenmiş tazminat ve uygulanmış lisans bedellerinde dengeleme (m.139/2-3) ve iyiniyetin korunması değerlendirilir.
5. **Def'i olarak ileri sürme.** Tecavüz davasında hükümsüzlük bir def'i/karşı dava olarak ileri sürülebilir; FSHM'de birlikte görülebilir.

## Çıktı modülleri
- Hükümsüzlük sebebi envanteri (madde-bent eşlemeli).
- Prior art / açıklama / kapsam analizi özeti.
- Kısmî hükümsüzlük ve istem sınırlandırma senaryosu.
- Geçmişe etkili sonuç ve dengeleme uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

