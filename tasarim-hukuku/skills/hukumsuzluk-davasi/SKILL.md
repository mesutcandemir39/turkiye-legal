---
argument-hint: ''
description: Tescilli tasarımın SMK m.77 sebepleriyle hükümsüzlüğünün talep edilmesi
  veya savunulması; yenilik/ayırt edicilik yokluğu, hak sahipliği veya koruma dışılık
  iddialarının dava yapısına oturtulması gerek
name: hukumsuzluk-davasi
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


# Hükümsüzlük Davası

## Görev
Tescilli tasarımı geçmişe etkili biçimde ortadan kaldırmak (veya savunmak): hükümsüzlük sebeplerini, husumeti, ispat yükünü ve sonuçlarını yönetmek. Çoğu kez tecavüz davasında karşı dava/savunma olarak kullanılır.

## Soğuk başlangıç (intake)
1. Hangi sebebe dayanılıyor: yenilik yokluğu, ayırt edicilik yokluğu, koruma dışılık, hak sahipliği, kötü niyet?
2. Önceki tasarım(lar) ve tarihleri elimizde mi (yenilik/ayırt edicilik için)?
3. Tasarım hâlen sicilde geçerli mi; koruma süresi devam ediyor mu?
4. Hükümsüzlüğü kim talep ediyor (menfaati olan kişi / Cumhuriyet savcısı / hak sahibi)?

## Denetim şeması
1. Hükümsüzlük sebepleri (SMK m.77/1): (a) m.55-59'daki koruma şartlarının bulunmaması (yenilik/ayırt edicilik yokluğu, koruma dışı görünüm), (b) gerçek hak sahibinin başkası olması (m.77/1-b; bu sebebi yalnız hak sahibi ileri sürebilir), (c) sonraki tasarımın önceki bir hakla çatışması, (ç) kötü niyetli tescil.
2. Husumet ve menfaat (SMK m.77/2-3): Menfaati olanlar, Cumhuriyet savcısı veya ilgili kamu kurumları dava açabilir; hak sahipliği sebebini ise yalnız gerçek hak sahibi/halefi ileri sürür. Dava sicildeki tasarım sahibine yöneltilir; sicilde hak sahibi görünenler de davaya dâhil edilir.
3. İspat yükü: Yenilik/ayırt edicilik yokluğunu ileri süren davacı, önceki tasarımı ve kamuya sunma tarihini ispatla yükümlüdür. Tasarım sahibi grace period (m.58/3) gibi def'ileri ileri sürebilir.
4. Kısmi hükümsüzlük (SMK m.77/5): Çoklu tasarımlarda yalnız bir kısmı için, ya da değişiklikle korunabilirlik sağlanabiliyorsa kısmi hükümsüzlük mümkündür.
5. Sonuç (SMK m.79): Hükümsüzlük kararı geçmişe etkilidir (ex tunc); tasarım hiç doğmamış sayılır. Kesinleşen karar herkese karşı hüküm doğurur ve sicilden terkin edilir. Kesinleşmiş ve uygulanmış tecavüz kararları, iyiniyetle yapılmış sözleşmeler gibi istisnalar saklıdır.
6. Görev/yetki: FSHHM (yoksa görevlendirilen asliye hukuk); yetki SMK m.156 ve HMK genel kuralları.

## Çıktı modülleri
- Hükümsüzlük dava dilekçesi iskeleti (sebep, önceki tasarım delilleri, talep).
- Önceki tasarım karşılaştırma tablosu ve ispat planı.
- Sonuç ve sicil terkini ile istisnalar notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

