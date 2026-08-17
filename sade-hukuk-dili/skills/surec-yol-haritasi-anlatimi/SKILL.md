---
argument-hint: ''
description: Müvekkile bir davanın veya idari/icra sürecinin aşamalarını, tahmini
  sürelerini ve her aşamada ne olacağını yalın bir yol haritası olarak anlatmak gerektiğinde
  kullanılır.
name: surec-yol-haritasi-anlatimi
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


# Dava ve Süreç Yol Haritası Anlatımı

## Görev
Müvekkile önündeki sürecin (hukuk davası, idari dava, icra takibi, soruşturma) hangi aşamalardan
geçeceğini, kabaca ne kadar süreceğini ve her aşamada kendisinden ne beklendiğini anlaşılır bir
yol haritasıyla anlatmak; takvim ve beklenti yönetimi sağlamak.

## Soğuk başlangıç (intake)
1. Hangi süreç ve hangi yargı kolu (HMK, İYUK, CMK, İİK)?
2. Süreç hangi aşamada başlıyor (henüz açılmadı / derdest / karar sonrası)?
3. Müvekkilin aktif katkı vermesi gereken adımlar var mı (delil, ifade, vekâletname)?
4. Zorunlu ön adım var mı (dava şartı arabuluculuk gibi)?

## Denetim şeması
1. AŞAMALARI DİZ: Süreç sıralı adımlara bölünür. Örn. hukuk davasında: (varsa) dava şartı
   arabuluculuk (HUAK 6325 s. m.18/A — ticari/iş/tüketici uyuşmazlıklarında), dava açılışı, cevap
   ve dilekçeler aşaması, ön inceleme (HMK m.137 vd.), tahkikat, hüküm, istinaf, temyiz.
2. SÜRE BEKLENTİSİ: Her aşama için gerçekçi tahmini süre verilir; "tahmini" olduğu vurgulanır,
   kesin süre vaadi yapılmaz.
3. MÜVEKKİL GÖREVLERİ (ispat/katkı): Hangi aşamada müvekkilden ne istendiği (delil teslimi, tanık
   bildirimi, duruşmaya katılım, ödeme) işaretlenir.
4. KRİTİK SÜRELER: Kanun yolu süreleri ve hak düşürücü süreler takvim mantığıyla anlatılır
   (örn. istinaf iki hafta — HMK m.345).
5. ÇIKIŞ/UZLAŞMA NOKTALARI: Her aşamada sulh/uzlaşma veya vazgeçme imkânı varsa belirtilir.
6. ARA SONUÇ: Yol haritası tüm aşamaları, müvekkil görevlerini ve kritik süreleri kapsıyor mu;
   gerçekçi mi.

## Çıktı modülleri
- Aşama aşama akış (zaman çizelgesi mantığında).
- Her aşamada "ne olacak / sizden ne beklenir / tahmini süre" satırı.
- Kritik süre uyarıları.
- Olası çıkış/uzlaşma noktaları ve belirsizlik notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

