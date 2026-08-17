---
argument-hint: ''
description: Karşı tarafa, kamu kurumuna veya üçüncü kişiye gönderilecek resmi ama
  anlaşılır bir yazışma, talep veya sulh teklifi metni hazırlamak; tonu ve hukuki
  pozisyonu koruyarak yalın anlatmak gerektiğinde ku
name: muzakere-iletisim-metni
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Karşı Taraf ve Müzakere İletişim Metni

## Görev
Karşı tarafa, kuruma veya üçüncü kişiye gönderilecek bir yazıyı (talep, sulh teklifi, açıklama,
yanıt) hukuki pozisyonu ve uygun tonu koruyarak anlaşılır, profesyonel ve fazla agresif olmayan
bir dille hazırlamak; iletişimin amacına (anlaşma, baskı, bilgi) göre üslubu ayarlamak.

## Soğuk başlangıç (intake)
1. Muhatap kim (karşı taraf, vekili, kamu kurumu, müşteri)?
2. Amaç ne (sulh, talep, savunma, bilgi verme)?
3. Hukuki pozisyon nedir ve nereye kadar açık edilecek?
4. Yazının ileride delil olma ihtimali var mı (ton ve içerik buna göre)?

## Denetim şeması
1. AMAÇ VE TON: Hedef belirlenir (kapı açık tutan sulh dili mi, net talep mi). Müzakerede aşırı
   sertlik kapatır, aşırı yumuşaklık pozisyon zayıflatır; denge kurulur.
2. POZİSYON KORUMA (ispat/çekince): Yazı ileride aleyhe delil olmamalı; gereksiz ikrar veya hak
   feragati içermez. Sulh görüşmelerinde "haklılığı kabul anlamına gelmez / her türlü hakkımız
   saklıdır (ihtirazi kayıt)" kaydı düşülür.
3. HUKUKİ DAYANAK ÖZÜ: Talep, dayandığı temel norma kısaca bağlanır (madde atfı gerekiyorsa)
   ama karşı tarafa ders verir tonundan kaçınılır.
4. NET TALEP VE SÜRE: Ne istendiği ve hangi süre içinde yanıt beklendiği açıkça yazılır;
   verilen süre makul ve takip edilebilir olmalıdır.
5. GİZLİLİK/UYUM: Müzakere yazışmalarında gizlilik kaydı; meslek kuralları gereği karşı taraf
   vekili varsa doğrudan müvekkille temastan kaçınma (TBB Meslek Kuralları) gözetilir.
6. ARA SONUÇ: Metin amaca hizmet ediyor mu; aleyhe ikrar/feragat içeriyor mu; ton uygun mu.

## Çıktı modülleri
- Resmi başlık ve muhatap.
- Bağlam + net talep + süre.
- İhtirazi kayıt / haklar saklı / gizlilik kaydı.
- Alternatif yumuşak ve sert ton versiyonları (gerekirse).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

