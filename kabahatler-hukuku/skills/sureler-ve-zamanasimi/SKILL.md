---
argument-hint: ''
description: Soruşturma zamanaşımı, yerine getirme zamanaşımı, başvuru ve itiraz süreleri
  ile peşin ödeme süresini birlikte hesaplamak ve bir takvim çıkarmak gerektiğinde
  kullanılır; süre kaynaklı hak kayıplarını
name: sureler-ve-zamanasimi
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
  - ad: Kabahatler Kanunu
    numara: '5326'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Süreler ve Zamanaşımı

## Görev
Dosyadaki tüm süreleri (zamanaşımı + usul süreleri) ilk günden doğru hesaplayıp bir takvime bağlamak; resen dikkate alınan zamanaşımı savunmasını kaçırmamak.

## Soğuk başlangıç (intake)
- Kabahatin işlendiği/tamamlandığı tarih nedir?
- İdari yaptırım kararı ne zaman verildi, ne zaman tebliğ edildi?
- Ceza maktu mu nispi mi, tutarı ne (zamanaşımı süresi tutara bağlı)?
- Süreyi durduran/kesen bir işlem (dava, tebligat, ödeme) var mı?

## Denetim şeması
1. **Soruşturma zamanaşımı (5326 m.20):** İdari para cezasını gerektiren kabahatlerde, ceza miktarına göre kademeli süreler (örn. düşük tutarlarda kısa, yüksek tutarlarda daha uzun) öngörülür; süre fiilin işlenmesiyle (kabahat sonuçlu ise sonuçtan) başlar. Bu süre içinde karar verilip ilgiliye tebliğ edilmezse ceza verilemez. Süreleri madde metniyle birebir kontrol et.
2. **Yerine getirme (infaz) zamanaşımı (5326 m.21):** Kesinleşen idari para cezası, ceza miktarına göre belirlenen süre içinde tahsil edilmezse infaz edilemez. Süre kesinleşmeyle başlar.
3. **Başvuru süresi (5326 m.27/1):** Tebliğ/tefhimden itibaren **15 gün**; hak düşürücü.
4. **İtiraz süresi (5326 m.29):** Hâkimlik kararının tebliğinden **7 gün**.
5. **Peşin ödeme süresi (5326 m.17/6):** Tebliğden itibaren süresinde ödemede 1/4 indirim; süreyi kaçırmamak için takvime işle.
6. **Durma/kesilme:** Lehe kanun (5326 m.5 → TCK m.7) ve özel kanunlardaki özel süreler gözden geçirilir; süre hesabında tebligatın geçerliliği (7201) belirleyicidir.

Zamanaşımı, hak düşürücü süreden farklı olarak esasa ilişkindir ve resen incelenir; başvuru/itirazda öncelikle ileri sürülür.

## Çıktı modülleri
- Süre takvimi tablosu (zamanaşımı + usul süreleri, son günleriyle).
- Zamanaşımı savunması notu.
- Risk uyarısı (yaklaşan/geçen süreler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

