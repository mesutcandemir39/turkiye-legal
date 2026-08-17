---
argument-hint: ''
description: İlk derece mahkemesi kararına karşı bölge adliye mahkemesine istinaf
  başvurusu yapılması, sebeplerin belirlenmesi ve süre denetimi gerektiğinde kullanılır.
name: istinaf-kanun-yolu
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


# İstinaf Kanun Yolu

## Görev
İlk derece hükmüne karşı istinaf yolunun açık olup olmadığını, süresini ve sebeplerini belirlemek; bölge adliye mahkemesi (BAM) önündeki incelemeyi yönlendirmek.

## Soğuk başlangıç (intake)
- Hüküm ne zaman tefhim/tebliğ edildi (süre başlangıcı)?
- Verilen ceza istinaf sınırının üzerinde mi (kesin hüküm mü)?
- Başvuru sebepleri neler: maddi vakıa, hukuka aykırılık, ceza tayini?
- Sanık duruşmada hazır mıydı (süre tefhimden mi tebliğden mi)?
- Yeni delil/tanık talebi var mı?

## Denetim şeması
1. **Süre ve başvuru.** İstinaf, hükmün tefhiminden, yokluğunda verilmişse tebliğinden itibaren 7 gün içinde mahkemeye dilekçeyle veya zabıt kâtibine beyanla yapılır (CMK m.273).
2. **Kesinlik sınırı.** 3.000 TL'ye kadar (yürürlükteki tutar güncellenmiştir, m.272/3 — `[doğrulanacak: güncel parasal sınır]`) adli para cezaları ve bazı kararlar kesindir; bu hallerde istinaf yolu kapalıdır. Beraat kararına karşı da sınırlar gözetilir (m.272).
3. **Sebepler.** İstinaf dilekçesinde hukuka aykırılık nedenleri ve dayanılan vakıalar gösterilir (m.273/4). BAM hem maddi olayı hem hukuku denetler (m.280).
4. **İnceleme ve karar.** BAM ceza dairesi başvuruyu esastan reddedebilir, düzelterek/yeniden hüküm kurabilir veya duruşma açar (m.280, m.289-294 bağlamı). Kovuşturma genişletilebilir.
5. **Aleyhe bozma yasağı.** Yalnız sanık lehine başvuruda ceza ağırlaştırılamaz (m.283).
6. **Ara sonuç.** Süre içinde ve sebepli başvuru hazırlanır; kesinlik sınırı altındaysa istinaf yerine itiraz/yargılamanın yenilenmesi değerlendirilir.

## Çıktı modülleri
- Süre ve kesinlik denetim notu (başlangıç tarihi hesabı).
- İstinaf dilekçesi iskeleti (sebepler + dayanak vakıalar).
- Yeni delil/duruşma talebi gerekçesi.
- Aleyhe bozma yasağı ve risk değerlendirmesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

