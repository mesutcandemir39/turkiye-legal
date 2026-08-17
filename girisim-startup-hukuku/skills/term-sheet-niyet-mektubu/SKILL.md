---
argument-hint: ''
description: Bir yatırım turunun ön anlaşma belgesi (term sheet / niyet mektubu) müzakere
  edilir veya hazırlanırken; hangi maddelerin bağlayıcı olduğunu, münhasırlık ve gizlilik
  hükümlerini, değerleme ve temel kor
name: term-sheet-niyet-mektubu
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Term Sheet ve Niyet Mektubu

## Görev
Yatırım turunun çatısını kuran term sheet'i hazırlamak/müzakere etmek; bağlayıcı ve bağlayıcı olmayan hükümleri ayırmak; değerleme, tur büyüklüğü ve temel koruma şartlarını çerçevelemek.

## Soğuk başlangıç (intake)
1. Tur büyüklüğü, ön/son para değerlemesi (pre/post-money) ve yatırımcı tipi nedir?
2. Enstrüman ne: doğrudan equity, SAFE, dönüştürülebilir borç?
3. İstenen koruma kalemleri: tasfiye tercihi, anti-dilution, veto, yönetim koltuğu?
4. Münhasırlık (exclusivity) ve gizlilik isteniyor mu; ne süreyle?
5. Due diligence ve kapanış için öngörülen takvim ne?

## Denetim şeması
1. Bağlayıcılık ayrımı: Term sheet kural olarak bağlayıcı değildir (niyet beyanı); ancak münhasırlık, gizlilik, masraf paylaşımı ve uygulanacak hukuk maddeleri açıkça bağlayıcı kılınmalıdır. TBK m.1 vd. — irade beyanı yorumu; tarafların belgeyi bağlayıcı sayma iradesi metinde net olmalı.
2. Müzakerede dürüstlük: Münhasırlık süresince haklı sebep olmadan müzakereyi koparma culpa in contrahendo (TBK m.35 atıf alanı, dürüstlük TMK m.2) sorumluluğu doğurabilir — bunu bilinçli kurgula.
3. Değerleme ve havuz: Post-money mı pre-money mı; opsiyon havuzunun turdan önce mi sonra mı açılacağı (kimi sulandıracağı) açıkça yazılmalı.
4. Koruma kalemleri başlığı: Tasfiye tercihi, anti-dilution (tam/ağırlıklı ortalama), veto/onay konuları, bilgi alma, yönetim temsili — bunlar burada ilkesel, kesin sözleşmede (SHA) ayrıntılı kurgulanır.
5. Kapanış ön şartları: DD tamamlanması, kurumsal onaylar (GK/YK), gerekiyorsa rekabet izni (4054 m.7) ve üçüncü kişi onayları.
6. İspat/şekil: Yazılı; bağlayıcı maddeler için imza. Sayısal değerleri [doldurulacak] bırak.

## Çıktı modülleri
- Term sheet taslağı (bağlayıcı/bağlayıcı olmayan ayrımı işaretli).
- Münhasırlık ve gizlilik madde önerileri.
- Değerleme/havuz/sulandırma açıklama notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

