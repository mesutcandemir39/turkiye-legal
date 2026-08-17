---
argument-hint: ''
description: Bir hukuki analizi okunaklı, izlenebilir ve gerekçeli bir metne dökmek
  gerektiğinde; mütalaa, layiha gerekçesi ya da hukuki görüşün argüman mimarisini
  kurmak için kullanılır.
name: gerekceli-hukuki-akil-yurutme-metni
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
  - ad: Türk Medeni Kanunu
    madde: '1'
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Gerekçeli Hukuki Akıl Yürütme Metni (IRAC/Altlama Üslubu)

## Görev
Yapılmış bir hukuki analizi; sorunu, kuralı, uygulamayı ve sonucu açıkça birbirinden ayıran, atıf disiplinli ve karşı argümanı karşılayan gerekçeli bir metne dönüştürmek.

## Soğuk başlangıç (intake)
- Metin kim için: mahkeme (layiha), müvekkil (mütalaa), iç değerlendirme mi?
- Çözülecek hukuki soru tek mi, çok başlıklı mı?
- Lehe ve aleyhe argümanlar hazır mı; tartışmalı içtihat var mı?
- İstenen ton: kesin görüş mü, seçenekli risk analizi mi?

## Denetim şeması
1. **Olay (Facts)** — Hukuken önemli vakıalar yansız ve kronolojik verilir; nitelendirme bu aşamada yapılmaz, çekişmeli vakıa işaretlenir.
2. **Sorun (Issue)** — Çözülecek hukuki soru(lar) tek cümlelik, cevaplanabilir biçimde çerçevelenir; birden çok sorun ayrı başlıklara bölünür.
3. **Kural (Rule)** — Uygulanacak norm madde/fıkra/bent ile; yorum gerekiyorsa yöntem belirtilir; içtihat yalnızca doğrulanabilir künye veya `[DOĞRULANMADI]` ile, ilke vurgusuyla anılır. Yürürlükteki kural ile doktrin görüşü ayrılır.
4. **Uygulama (Application)** — Altlama: her norm unsuru eldeki vakıaya bağlanır; ispat yükü (TMK m.6/HMK m.190) gösterilir; karşı argüman açıkça ele alınıp çürütülür ("ileri sürülebilirse de...").
5. **Sonuç (Conclusion)** — Net cevap; belirsizlik varsa olasılık dürüstçe ("kuvvetle muhtemel / tartışmalı") nitelenir, abartılı kesinlikten kaçınılır.
6. **Risk ve öneri** — Mütalaada eylem önerisi, alternatif strateji ve `[doldurulacak]` yer tutucularıyla eksik bilgi açıkça işaretlenir.

## Çıktı modülleri
- Başlıklı IRAC iskeleti (Olay/Sorun/Kural/Uygulama/Sonuç).
- Atıf listesi (mevzuat madde + içtihat `[DOĞRULANMADI]`).
- Karşı argüman/çürütme bloğu.
- Risk haritası ve öneri (mütalaa ise).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

