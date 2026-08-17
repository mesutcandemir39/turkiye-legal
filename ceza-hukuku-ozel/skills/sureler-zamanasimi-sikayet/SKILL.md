---
argument-hint: ''
description: Bir suçta dava ve ceza zamanaşımını hesaplamak, şikâyete bağlılık ve
  şikâyet süresini belirlemek ve uzlaştırma kapsamını kontrol etmek gerektiğinde kullanılır.
name: sureler-zamanasimi-sikayet
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler, Zamanaşımı ve Şikâyet

## Görev
Suç bazında dava/ceza zamanaşımını, şikâyete bağlılığı ve süresini, uzlaştırma ve önödeme kapsamını belirleyerek usuli zamanaşımı risklerini önceden tespit etmek.

## Soğuk başlangıç (intake)
- Suç tipi ve uygulanacak fıkra (cezanın üst sınırı) nedir?
- Suç ne zaman işlendi (kesintisiz/zincirleme suçta sona erme tarihi)?
- Suç şikâyete bağlı mı; mağdur fiili ve faili ne zaman öğrendi?
- Daha önce kesen/durduran bir işlem (iddianame, savunma alınması) yapıldı mı?

## Denetim şeması
1. Dava zamanaşımı (TCK m.66): Suçun gerektirdiği cezanın üst sınırına göre kademeli süreler (örn. beş yıldan fazla olmayan hapis için 8 yıl, vb.). Çocuklarda süreler indirilir (m.66/2). Başlangıç m.66/6 (tamamlanma/sona erme/netice anı).
2. Zamanaşımını kesen/durduran haller (TCK m.67): Şüphelinin sorgusu, iddianame düzenlenmesi, mahkûmiyet kararı gibi işlemler keser; kesilmeden sonra süre yeniden işler ancak yarısından fazla uzayamaz (m.67/4). Durma sebepleri (izin/karar bekleme) ayrıca değerlendirilir.
3. Şikâyet (TCK m.73): Şikâyete bağlı suçlarda fiili ve faili öğrenmeden itibaren 6 ay içinde şikâyet; süre geçerse soruşturma yapılamaz. Şikâyetten vazgeçme davayı/cezayı düşürür (kabul şartıyla). Birden çok mağdur/fail halinde bölünebilirlik kuralları.
4. Hangi suçlar şikâyete bağlı: Basit yaralama (TCK m.86/2), hakaret (m.131, kamu görevlisine görevden dolayı hariç), tehdit değil ama bazı malvarlığı suçlarında akrabalık hali (m.167) gibi. Her tip için madde metnini teyit et.
5. Uzlaştırma ve önödeme: Uzlaştırma kapsamındaki suçlar CMK m.253-254 listesine göre belirlenir (şikâyete bağlı suçlar ve sayılan bazı suçlar); önödeme TCK m.75 kapsamındaki hafif suçlarda. Bunlar zamanaşımından ayrı süreçlerdir.
6. Ceza zamanaşımı (TCK m.68) ve ara sonuç: Kesinleşmiş cezanın infaz edilebilirliği için süreler. Olayda dava açma/şikâyet/zamanaşımı son tarihlerini takvimle ve riskli tarihleri işaretle.

## Çıktı modülleri
- Zamanaşımı ve şikâyet takvimi (suç, başlangıç tarihi, son tarih, kesen işlemler).
- Şikâyete bağlılık ve uzlaştırma/önödeme uygunluk tablosu.
- Riskli tarih uyarıları ve gerekli işlem listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

