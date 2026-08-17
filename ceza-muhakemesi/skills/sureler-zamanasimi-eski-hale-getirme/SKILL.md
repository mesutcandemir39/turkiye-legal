---
argument-hint: ''
description: Dava ve ceza zamanaşımı, kanun yolu ve usul süreleri ile süre kaçırıldığında
  eski hale getirme başvurusu hesaplanırken kullanılır.
name: sureler-zamanasimi-eski-hale-getirme
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
  - ad: Ceza Muhakemesi Kanunu
    numara: '5271'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve Eski Hale Getirme

## Görev
Ceza muhakemesinde işleyen tüm süreleri (zamanaşımı, kanun yolu, usul süreleri) hesaplamak; süre kaçırma riskini ve eski hale getirme imkânını değerlendirmek.

## Soğuk başlangıç (intake)
- Suç tarihi ve suçun cezası nedir (zamanaşımı için)?
- Hangi usul/kanun yolu süresi söz konusu, başlangıç tarihi ne?
- Kişi tutuklu mu (denetim süreleri için)?
- Süre kaçırıldıysa kusursuz bir engel var mıydı?
- Şikâyete bağlı suç mu (TCK m.73 altı aylık süre)?

## Denetim şeması
1. **Dava zamanaşımı.** Suçun gerektirdiği cezaya göre TCK m.66'da süreler belirlenir; süre suçun işlendiği günden işler (m.66/6). Kesen ve durduran sebepler m.67'de düzenlenir; kesilmeden sonra süre yeniden işler, ancak en fazla yarısına kadar uzar.
2. **Ceza zamanaşımı.** Kesinleşen cezanın infaz edilememesi halindeki süreler TCK m.68'de gösterilir.
3. **Şikâyet süresi.** Şikâyete bağlı suçlarda fail ve fiilin öğrenilmesinden itibaren 6 ay (TCK m.73); geçerse soruşturma/kovuşturma şartı düşer.
4. **Kanun yolu süreleri.** İtiraz 7 gün (CMK m.268), istinaf 7 gün (m.273), temyiz 15 gün (m.291); başlangıç tefhim, yoklukta tebliğdir. Süreler gün olarak hesaplanır, tatil günü sonaysa ertesi iş gününe uzar (m.39).
5. **Eski hale getirme.** Kusuru olmaksızın süreyi geçiren kişi, engelin kalkmasından itibaren 7 gün içinde eski hale getirme isteyebilir; istem, süreye uyulduğunda yapılması gereken işlemle birlikte sunulur (CMK m.40-42).
6. **Ara sonuç.** Süre hâlâ işliyorsa hemen işlem yapılır; kaçırılmışsa eski hale getirme koşulları (kusursuzluk + 7 gün) denetlenir.

## Çıktı modülleri
- Süre takvimi tablosu (zamanaşımı + kanun yolu + denetim süreleri).
- Zamanaşımı hesabı ve kesen/duran sebep notu.
- Eski hale getirme dilekçesi taslağı (m.40-42 dayanaklı).
- Kritik son tarih uyarısı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

