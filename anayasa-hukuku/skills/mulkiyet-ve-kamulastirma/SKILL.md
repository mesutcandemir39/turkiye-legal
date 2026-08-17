---
argument-hint: ''
description: Mülkiyet hakkına (m.35) yönelik bir müdahalenin, kamulaştırmanın veya
  fiili el atmanın anayasaya uygunluğunu ve giderim boyutunu değerlendirmek; kamu
  yararı, kanunilik ve adil denge analizinin gerekti
name: mulkiyet-ve-kamulastirma
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
  - ad: Türkiye Cumhuriyeti Anayasası
    numara: '2709'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mülkiyet Hakkı ve Kamulaştırma

## Görev
Mülkiyet hakkına (Anayasa m.35, AİHS Ek 1 No.lu Protokol m.1) yönelik müdahaleleri — kamulaştırma (m.46), idari kısıtlama, fiili/hukuki el atma — anayasal çerçevede denetlemek ve giderim/tazminat boyutunu değerlendirmek.

## Soğuk başlangıç (intake)
1. Mülkiyet konusu ne (taşınmaz, taşınır, ekonomik değer/alacak) ve müdahale türü hangisi?
2. Usulüne uygun bir kamulaştırma işlemi mi, yoksa fiili/hukuki el atma mı söz konusu?
3. Müdahalenin dayandığı kamu yararı kararı ve kanuni dayanak var mı?
4. Bedel/tazminat ödendi mi, ödenecekse hangi usulle belirleniyor?

## Denetim şeması
1. **Mülk kavramı.** Mevcut mal, meşru beklenti ve ekonomik değer taşıyan alacaklar koruma alanındadır. Ara sonuç: koruma alanında mıyız?
2. **Müdahale türünü ayır.** (a) Mülkiyetten yoksun bırakma (kamulaştırma), (b) kullanımın düzenlenmesi (imar kısıtı vb.), (c) genel müdahale. Tür, denetim yoğunluğunu belirler.
3. **Kanunilik.** Müdahale erişilebilir ve öngörülebilir bir kanuna dayanmalı (m.13, m.35). Kamulaştırmada 2942 sayılı Kamulaştırma Kanunu usulüne uygunluk aranır.
4. **Kamu yararı.** Müdahale gerçek ve meşru bir kamu yararına dayanmalı; m.46 kamulaştırmada kamu yararı kararı şarttır.
5. **Adil denge / ölçülülük.** Bireysel yük ile kamu yararı arasında orantı kurulmalı; m.46 gerçek karşılığın (bedelin) peşin ve nakden ödenmesini öngörür. Karşılıksız ya da fahiş düşük bedelle el atma adil dengeyi bozar.
6. **Fiili/hukuki el atma.** İdarenin kamulaştırmasız el atması hukuka aykırıdır; bedel davası ve el atmanın önlenmesi yolları gündeme gelir. İmar kısıtlamasının süresiz/karşılıksız sürmesi (hukuki el atma) ayrı denetlenir.
İspat: müdahaleyi malik, kamu yararı ve usule uygunluğu idare gösterir. AYM/AİHM mülkiyet içtihadına ilke düzeyinde atıf yapın; künyeyi `[DOĞRULANMADI]` işaretleyin.

## Çıktı modülleri
- Müdahale türü nitelendirmesi ve uygulanacak denetim yoğunluğu.
- Kanunilik-kamu yararı-adil denge değerlendirme tablosu.
- Bedel/giderim yolu ve dava türü (idari/adli) önerisi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

