---
argument-hint: ''
description: Borcun gereği gibi ifa edilip edilmediği, alacaklının ifayı kabulden
  kaçındığı veya edimin sonradan imkânsızlaştığı durumlarda kullanılır.
name: ifa-ve-ifa-engelleri
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İfa, Alacaklı Temerrüdü ve İfa İmkânsızlığı

## Görev
Borcun ifa yeri, zamanı ve biçimi yönünden gereği gibi ifa edilip edilmediğini; alacaklı temerrüdü ve sonraki imkânsızlığın sonuçlarını belirlemek.

## Soğuk başlangıç (intake)
- Borç muaccel mi; ifa zamanı ve yeri ne?
- Borçlu ifayı sundu mu; alacaklı kabul etti mi?
- Edim sonradan imkânsızlaştı mı; kimden kaynaklanan sebeple?
- Kısmi ifa, üçüncü kişi ifası veya ifa yerine edim söz konusu mu?

## Denetim şeması
1. İfa esasları: TBK m.83 vd. — bizzat ifa zorunluluğu istisnaları (m.83), kısmi ifanın reddi (m.84), ifa yeri (m.89: para borçları alacaklının yerleşim yerinde — götürülecek borç), ifa zamanı ve süreden önce ifa (m.96).
2. Mahsup/sıra: Birden çok borçta ifanın hangi borca sayılacağı (m.100-101); faiz ve masrafların önce mahsubu.
3. İspat ve makbuz: Borçlu ifayı ve makbuz/senet iadesini isteyebilir (m.103-105); senedin borçluda olması ödeme karinesi.
4. Alacaklı temerrüdü: m.106-108 — alacaklı haklı sebep olmaksızın ifayı veya hazırlık fiillerini yapmaktan kaçınırsa temerrüde düşer; borçlu tevdi (m.107), satış (m.108) veya sözleşmeden dönme yoluna gidebilir, hasar alacaklıya geçer.
5. Sonraki imkânsızlık: m.136 — borçluya yüklenemeyen sebeple imkânsızlaşma borcu sona erdirir; karşılıklı sözleşmede alınanın iadesi, alınmamışsa istemekten vazgeçme. Kısmi imkânsızlık m.137. Borçluya yüklenebilen imkânsızlık ise m.112 üzerinden tazminata dönüşür.
6. Aşırı ifa güçlüğü/uyarlama: m.138 — öngörülemeyen olağanüstü değişiklik dürüstlüğe aykırı hâle getirirse uyarlama, mümkün değilse dönme/fesih.
7. İspat yükü: İfayı borçlu, imkânsızlığın kusursuzluğunu yine borçlu ispatlar (m.136 ile m.112 birlikte).

## Çıktı modülleri
- İfa uygunluk ve muacceliyet analizi.
- Tevdi/ifa yerine edim veya uyarlama yol haritası.
- İmkânsızlık türü ve borç-tazminat geçişi şeması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

