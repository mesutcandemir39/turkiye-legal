---
argument-hint: ''
description: Müvekkil ile avukatlık sözleşmesi kurulurken, ücret ve masraf yapısı
  belirlenirken veya ücret uyuşmazlığı, azil-istifa halinde ücret hesabı yapılırken
  kullanılır.
name: vekalet-sozlesmesi-ve-ucret
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Avukatlık Sözleşmesi ve Vekâlet Ücreti

## Görev
Avukat-müvekkil ilişkisinin maddi çerçevesini kurmak: işin kapsamı, ücret tipi, masraf paylaşımı, azil/istifa halinde ücretin akıbeti ve karşı taraf vekâlet ücretini sözleşmeye doğru yansıtmak.

## Soğuk başlangıç (intake)
1. İş ne (dava/danışmanlık/işlem) ve değeri belirli mi?
2. Ücret nasıl kurgulanacak: maktu, nispi (değer üzerinden), saatlik, başarıya bağlı kısım?
3. Masraflar (harç, gider avansı, bilirkişi, yol) kim öder, avans alınacak mı?
4. İlişki şu an mı kuruluyor, yoksa süren bir işte azil/istifa mı söz konusu?

## Denetim şeması
1. **Sözleşmenin kurulması (1136 m.163)**: Avukatlık sözleşmesi serbestçe düzenlenir ancak yazılı olması ispat ve uyuşmazlık önleme açısından esastır. Kapsam (hangi dava/işlem, hangi aşamalar — istinaf/temyiz dahil mi) açıkça yazılır.
2. **Ücretin belirlenmesi (1136 m.164)**: Ücret sözleşme ile kararlaştırılır. Dava değerinin %25'ini aşan başarıya bağlı (nispi) kısım sınırlarına ve Avukatlık Asgari Ücret Tarifesi tabanına dikkat edilir; tarife altı geçersizdir, sözleşme yoksa tarife uygulanır.
3. **Karşı taraf vekâlet ücreti (1136 m.164/son)**: Yargılama gideri olarak hükmedilen vekâlet ücreti, aksi yazılmadıkça avukata aittir; bu kalem müvekkille ödenecek ücretten ayrıdır, sözleşmede netleştirilir.
4. **Masraf ve avans**: Harç/gider avansı (HMK m.120) ve masraflar müvekkile aittir; alınacak avans ve mahsup düzeni yazılır.
5. **Azil ve istifa (1136 m.174)**: Haklı sebep olmadan azil halinde ücretin tamamı; haksız istifada ücret talep edilemeyebilir. Hapis hakkı (m.166) ile dosya/evrak üzerinde ücret alacağı güvencesi değerlendirilir.
6. **Ara sonuç**: Kapsam + ücret tipi + masraf + sona erme senaryoları sözleşmede karşılanmışsa metin tamamdır.

## Çıktı modülleri
- Avukatlık sözleşmesi taslağı (kapsam, ücret, masraf, fesih/azil maddeleri).
- Ücret hesap tablosu (maktu/nispi/saatlik senaryoları).
- Azil/istifa halinde ücret değerlendirme notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

