---
argument-hint: ''
description: Müvekkili dosyanın seyri, riskleri ve seçenekleri hakkında bilgilendirme
  yazısı veya teklif/kapsam mektubu (engagement letter) hazırlanırken ve beklenti
  yönetimi gerektiğinde kullanılır.
name: muvekkil-iletisimi-ve-bilgilendirme
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
  - ad: Avukatlık Kanunu
    numara: '1136'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Müvekkil İletişimi ve Bilgilendirme

## Görev
Müvekkili dosyanın durumu, hukuki riskler, olası sonuçlar, süreler ve maliyetler hakkında sade ve doğru biçimde bilgilendirmek; beklentiyi yönetmek ve önemli kararları yazılı onaya bağlamak.

## Soğuk başlangıç (intake)
1. Bilgilendirmenin konusu ne (yeni iş teklifi, gelişme bildirimi, strateji kararı, olumsuz haber)?
2. Müvekkilin hukuki bilgi düzeyi ve tercih ettiği dil/ton nedir?
3. Müvekkilden bir karar/onay isteniyor mu (örn. sulh teklifi, kanun yoluna başvurma)?
4. Aktarılacak risk veya maliyet kalemleri neler?

## Denetim şeması
1. **Özen ve sadakat (TBK m.506; 1136 özen yükümü)**: Müvekkile dürüst, gerçekçi ve zamanında bilgi verilir; başarı garantisi verilmez, riskler gizlenmez.
2. **Kapsam netliği**: Engagement/kapsam mektubunda işin sınırı, dahil olmayan işler ve varsayımlar yazılır.
3. **Risk ve seçenek sunumu**: Her seçenek için olası sonuç, süre, maliyet ve risk dengeli biçimde aktarılır; karar müvekkilindir.
4. **Karar onayı**: Kritik kararlar (sulh, davadan feragat, kanun yolundan vazgeçme) yazılı talimata bağlanır (talimata uyma — TBK m.505); bu hem müvekkili korur hem de avukatın sorumluluğunu sınırlar.
5. **Sır ve gizlilik (1136 m.36)**: İletişim kanalı ve içeriği sır kapsamında; üçüncü kişilere paylaşım yapılmaz.
6. **Ara sonuç**: Doğru bilgi + dengeli risk + gereken yerde yazılı onay sağlanmışsa bilgilendirme tamamdır.

## Çıktı modülleri
- Müvekkil bilgilendirme/gelişme yazısı (sade dil).
- Kapsam/teklif mektubu (engagement letter) taslağı.
- Karar onay formu ([doldurulacak] seçenek ve sonuçları ile).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

