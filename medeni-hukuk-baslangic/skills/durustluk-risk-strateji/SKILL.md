---
argument-hint: ''
description: Bir talebin veya savunmanın yalnızca TMK m.2/m.3 gibi esnek başlangıç
  hükümlerine dayandığı hâllerde; bu argümanın gücünü, başarı olasılığını ve alternatif
  dayanakları tartmak için kullanılır.
name: durustluk-risk-strateji
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
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Başlangıç Hükümleri Temelli Risk ve Strateji Değerlendirmesi

## Görev
Dürüstlük kuralı, hakkın kötüye kullanılması veya iyiniyet gibi esnek/takdire açık başlangıç hükümlerine dayanan bir argümanın gerçekçi başarı şansını değerlendirmek; daha sağlam alternatif dayanakları ve ispat risklerini ortaya koymak.

## Soğuk başlangıç (intake)
- Argüman *yalnızca* başlangıç hükmüne mi dayanıyor, yoksa daha güçlü bir özel norm da var mı?
- Başlangıç hükmünün şartları (özellikle m.2/2 "açıklık" eşiği) somut olayda gerçekten karşılanıyor mu?
- İspat yükü (m.6) bizde mi; ispat araçları yeterli mi?
- Hâkimin takdiri (m.4) ne yöne meyledebilir; emsal eğilim nedir?

## Denetim şeması
1. **Önce sağlam dayanak ara** — Esnek başlangıç hükmü, mümkünse asıl dayanak değil destek olmalıdır. Somut bir özel norm (sözleşme ihlali, ayıp, geçersizlik, mülkiyet) varsa o öne çıkarılır; m.2/m.3 ikincil savunma katmanı tutulur.
2. **"Açıklık" riski** — TMK m.2/2 yalnızca *açık* kötüye kullanmada korur; eşik yüksektir. Sıradan menfaat çatışmasını kötüye kullanma diye sunmak zayıf argümandır ve güven kaybı yaratır.
3. **Takdir belirsizliği — m.4** — Hakkaniyet/takdir alanı sonucu öngörülemez kılar; bu belirsizlik dürüstçe müvekkile aktarılır. Sonuç "tartışmalı / hâkimin takdirine bağlı" diye nitelenir, abartılı kesinlik verilmez.
4. **İspat zafiyeti — m.6** — Çelişkili davranış, güven, kötüniyet gibi vakıaların ispatı güçtür; yazılı delil, yazışma, tanık ve karine durumu envanterlenir. İspatlanamayan vakıa "gerçekleşmemiş" sayılır.
5. **Senaryo ve alternatif** — En iyi/orta/en kötü senaryo; başlangıç hükmü tutmazsa devreye girecek yedek dayanak; sulh/uzlaşma penceresi. İçtihat eğilimi tek cümlede dürüstçe (lehe karar seçip aleyhe gizlemeden) özetlenir.
6. **Etik sınır** — Zayıf bir m.2 argümanını "kesin" diye sunmak meslek kurallarına ve dürüst danışmanlığa aykırıdır; risk açıkça paylaşılır.

## Çıktı modülleri
- Dayanak haritası (asıl norm + başlangıç hükmü katmanı).
- Şart/eşik ve ispat riski değerlendirmesi.
- Senaryo tablosu (iyi/orta/kötü) + olasılık nitelemesi.
- Yedek strateji + sulh penceresi + ilkesel içtihat eğilimi `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

