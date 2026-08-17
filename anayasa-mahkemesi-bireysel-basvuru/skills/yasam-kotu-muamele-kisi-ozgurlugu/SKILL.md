---
argument-hint: ''
description: Yaşam hakkı, işkence/kötü muamele yasağı ile kişi hürriyeti ve güvenliği
  (gözaltı, tutukluluk, uzun tutukluluk) bağlamında negatif ve pozitif yükümlülük
  ihlalleri iddia edildiğinde kullanılır.
name: yasam-kotu-muamele-kisi-ozgurlugu
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
  - ad: Anayasa Mahkemesinin Kuruluşu ve Yargılama Usulü Hakkında Kanun
    numara: '6216'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yaşam, Kötü Muamele ve Kişi Özgürlüğü

## Görev
m.17 (yaşam, maddi-manevi varlık, kötü muamele yasağı) ve m.19 (kişi hürriyeti ve güvenliği) kapsamında Devletin negatif ve pozitif (koruma + etkili soruşturma) yükümlülüklerinin ihlalini değerlendirmek.

## Soğuk başlangıç (intake)
- Olay nedir (ölüm/yaralanma, gözaltı/tutuklama, kötü muamele iddiası)?
- Devlet görevlisi mi sorumlu, yoksa Devletin koruma/önleme/soruşturma ihmali mi var?
- Özgürlükten yoksun bırakma hangi sebebe ve hangi karara dayanıyor?
- Tutukluluk ne kadar sürdü; etkili bir başvuru/itiraz imkânı tanındı mı?

## Denetim şeması
1. Yaşam hakkı (m.17) — negatif yükümlülük: Devletin kasten veya orantısız güç kullanımıyla ölüme yol açmaması. Pozitif yükümlülük: yaşamı koruma ve ölümü/ağır yaralanmayı aydınlatan ETKİLİ, bağımsız, ivedi soruşturma.
2. Kötü muamele yasağı — eşik: muamelenin asgari ağırlık eşiğini aşması. Maddi boyut (muamelenin kendisi) ve usuli boyut (etkili soruşturma) ayrı incelenir; ispat "makul şüphenin ötesinde", gözetim altındaki kişide ispat yükü Devlete kayar.
3. Kişi özgürlüğü (m.19) — yoksun bırakma yalnızca m.19/2-3'teki sınırlı sebeplerle ve kanunda gösterilen usulle mümkündür.
4. Tutuklama denetimi — makul suç şüphesi (somut delil), tutuklama nedenlerinin (kaçma, delil karartma) varlığı, ölçülülük ve adli kontrolün yetersizliği; tutukluluğun makul süreyi aşması (m.19/7) ihlaldir.
5. Usuli güvenceler — yakalanma sebebinin bildirilmesi, hâkim önüne çıkarılma, tutukluluğa etkili itiraz ve tazminat hakkı (m.19/8-9).

İspat yükü: gözaltı/tutukluluk koşullarında ve resmî gözetimde Devlete; aksi halde başvurucuya ağırlıklı olarak düşer.

Ara sonuç: ihlalin maddi mi usuli mi olduğu ve dayanak.

## Çıktı modülleri
- Negatif/pozitif yükümlülük ayrımı.
- Soruşturmanın etkililiği değerlendirmesi.
- Tutukluluk için makul şüphe–neden–süre denetimi.
- İlke kararlarına atıf [DOĞRULANMADI].



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

