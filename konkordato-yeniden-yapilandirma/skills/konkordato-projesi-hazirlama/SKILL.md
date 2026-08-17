---
argument-hint: ''
description: Konkordato ön projesini ve projesini ekonomik olarak gerçekçi, tasdik
  şartlarını karşılayacak biçimde hazırlamak veya mevcut projeyi denetlemek gerektiğinde
  kullanılır.
name: konkordato-projesi-hazirlama
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Konkordato Projesi ve Ön Proje Hazırlama

## Görev
İİK m.286'ya uygun konkordato ön projesini ve nihai projeyi hazırlamak veya denetlemek; tenzilat/vade/karma yapısını, kaynak planını ve alacaklı sınıflandırmasını tasdik şartlarına (m.305) uyacak şekilde kurmak.

## Soğuk başlangıç (intake)
- Önerilen yapı: alacaktan indirim mi, vade mi, karma mı? Oran ve süreler?
- Ödeme kaynağı: işletme faaliyeti, sermaye artırımı, varlık satışı, yeni finansman?
- Alacaklı sınıfları: rehinli, imtiyazlı (m.206), adi alacaklılar nasıl dağılıyor?
- Makul güvence veren denetim raporu mevcut mu?

## Denetim şeması
1. **Ön proje içeriği (m.286/a).** Alacaklıların hangi oranda alacağından vazgeçeceği veya vadenin nasıl tanınacağı, ödeme planı; ödemelerin nasıl finanse edileceği açıkça gösterilmeli.
2. **Belge seti (m.286/b-e).** Mal varlığı durumunu gösteren belgeler, finansal tablolar, ara bilanço, alacaklı/alacak listesi, makul güvence veren bağımsız denetim raporu (KGK denetim standartları). İspat: projenin sayısal varsayımları belgeyle desteklenmeli.
3. **Kaynak gerçekçiliği.** Nakit akış projeksiyonu ile ödeme planı tutarlı mı? İmtiyazlı alacakların (m.206) tam ödeneceği güvenceye bağlanmış mı (m.305 şartı)?
4. **Alacaklı eşitliği.** Aynı sınıftaki alacaklılara eşit muamele; farklı sınıflar arasında haklı ayrım gerekçesi. Rehinli alacaklılarla yapılan ayrı düzenleme (m.308/h) ayrıca ele alınır.
5. **Tasdik süzgeci.** Teklifin borçlunun kaynaklarıyla orantılılığı (m.305/1-a), çoğunluk (m.302) ve depo şartları önceden test edilir. Ara sonuç: proje tasdik edilebilir nitelikte mi.

## Çıktı modülleri
- Konkordato ön projesi taslağı (yer tutuculu).
- Ödeme planı ve nakit akış tablosu iskeleti.
- Alacaklı sınıflandırma ve oran tablosu.
- Tasdik şartı uyum kontrol listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

