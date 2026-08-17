---
argument-hint: ''
description: Patent, faydalı model veya tasarım hakkına tecavüz iddiasında istem/görünüm
  karşılaştırması, koruma kapsamı ve eşdeğerler doktrini ile yenilik-ayırt edicilik
  değerlendirmesi gerektiğinde kullanılır.
name: patent-tasarim-tecavuz
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


# Patent ve Tasarım Tecavüz Denetimi

## Görev
Patent/faydalı model veya tasarım hakkına tecavüz iddiasını koruma kapsamı (istem yorumu yahut tescilli görünüm) çerçevesinde teknik karşılaştırma ile denetlemek.

## Soğuk başlangıç (intake)
- Hak patent mi, faydalı model mi, tasarım mı; tescil no ve koruma süresi nedir?
- İhlal iddia edilen ürün/sürecin teknik özellikleri/görünümü nedir?
- Patentte bağımsız istemler nelerdir; tasarımda tescilli görseller hangileri?
- Hükümsüzlük (yenilik/buluş basamağı eksikliği) karşı iddiası var mı?

## Denetim şeması
1. Koruma kapsamı (patent): Kapsam istemlerle belirlenir; tarifname ve resimler yorumda kullanılır (SMK m.89). Bağımsız istemin tüm unsurları ürün/süreçte varsa birebir tecavüz; eşdeğerler doktrini (m.89/5) ile fonksiyon-yol-sonuç özdeşliği değerlendirilir.
2. Faydalı model: Buluş basamağı aranmaz (SMK m.142); tecavüz incelemesi istem temelli aynı mantıkla yapılır.
3. Tasarım: Koruma tescilli görünümle sınırlıdır; tecavüz, bilgilenmiş kullanıcıda aynı genel izlenimi yaratıp yaratmadığına göre belirlenir (SMK m.55-56, m.81). Seçenek özgürlüğü ölçütü dikkate alınır.
4. Hükümsüzlük savunması: Patentte yenilik/buluş basamağı/sanayiye uygulanabilirlik eksikliği (SMK m.138 atfıyla m.82-83); tasarımda yenilik ve ayırt edici nitelik eksikliği (m.77 atfıyla m.56). Tekniğin bilinen durumu delillerle (önceki yayın, kullanım) ortaya konur. İspat yükü hükümsüzlüğü ileri sürende.
5. Bilirkişi: Teknik karşılaştırma için uzman bilirkişi şarttır; istem haritalama tablosu hazırlanır.
6. Ara sonuç: Tecavüz sabit ve hak geçerliyse SMK m.149-151 talepleri kurgulanır; çalışan buluşu/ön kullanım hakkı (m.87) ayrıca tartılır.

## Çıktı modülleri
- İstem haritalama / görünüm karşılaştırma tablosu.
- Hükümsüzlük risk değerlendirmesi.
- Bilirkişi sorularının taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

