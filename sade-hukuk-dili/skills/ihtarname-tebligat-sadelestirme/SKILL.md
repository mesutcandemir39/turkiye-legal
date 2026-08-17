---
argument-hint: ''
description: Alınan bir ihtarnameyi, tebligatı veya icra/ödeme emrini müvekkile açıklamak;
  ne istendiğini, hangi süre içinde ne yapılması gerektiğini ve yapılmazsa ne olacağını
  yalın anlatmak gerektiğinde kullanıl
name: ihtarname-tebligat-sadelestirme
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


# İhtarname ve Tebligat Sadeleştirme

## Görev
Müvekkile ulaşan ihtarname, tebligat, ödeme emri veya icra emrini; "kim, ne istiyor, kaç gün
içinde ne yapmalıyım, yapmazsam ne olur" sorularına net cevap verecek şekilde sadeleştirmek.
Bu belgelerde süreler hayati olduğu için doğruluk önceliklidir.

## Soğuk başlangıç (intake)
1. Belge türü nedir (noter ihtarı, ödeme emri, icra emri, tebliğ edilen dava/karar)?
2. Tebliğ tarihi nedir (süre bu tarihten işler)?
3. Talep edilen edim (ödeme, tahliye, ifa) ve miktarı?
4. Müvekkilin elinde itiraz/savunma için belge var mı?

## Denetim şeması
1. SÜRE BAŞLANGICI: Tebliğ tarihi sabitlenir; süreler bu tarihten işler. Ödeme emrine itiraz
   süresi (İİK m.62 — yedi gün), kambiyo takibinde itiraz (İİK m.168 — beş gün), kira temerrüt
   ihtarında ödeme süresi (TBK m.315) gibi süreler takvim tarihiyle yazılır.
2. TALEBİN NETLİĞİ: Ne istendiği (asıl alacak, faiz, masraf ayrımıyla) ve dayanağı yalın aktarılır.
3. SEÇENEKLER VE SONUÇLAR (risk): "Öderim / itiraz ederim / hiçbir şey yapmam" seçeneklerinin
   sonuçları açıkça yazılır. İtiraz edilmezse takibin kesinleşeceği (İİK m.62/son, m.78 haciz)
   net belirtilir; kambiyo takibinde itirazın icrayı durdurmadığı uyarılır.
4. YETKİ/İCRA DAİRESİ: Hangi icra dairesi/mahkeme, hangi merciye itiraz yapılacağı belirtilir.
5. İSPAT NOTU: İtiraz veya ödeme tarihinin ve şeklinin kanıtlanabilir olması gerektiği hatırlatılır.
6. ARA SONUÇ (istisna): Sade açıklama bilgilendirmedir; asıl bağlayıcı belge tebliğ edilen
   evraktır. Süre kaçırma riski varsa derhal vekille temas uyarısı eklenir.

## Çıktı modülleri
- "Size ne tebliğ edildi, kim, ne istiyor" özeti.
- Son tarih ve kalan gün (takvimli).
- Seçenekler / sonuçları tablosu.
- Acil yapılması gerekenler ve uyarı notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

