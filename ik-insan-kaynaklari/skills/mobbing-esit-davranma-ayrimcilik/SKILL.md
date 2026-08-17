---
argument-hint: ''
description: İşyerinde ayrımcılık, eşit davranma borcu, mobbing/psikolojik taciz iddiası
  veya bu iddiaları önleyecek süreç tasarımı gündeme geldiğinde kullanılır.
name: mobbing-esit-davranma-ayrimcilik
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
  - ad: İş Kanunu
    numara: '4857'
    tur: kanun
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Eşit Davranma, Ayrımcılık ve Mobbing Riski

## Görev
İşverenin eşit davranma borcuna uyumunu sağlamak; ayrımcılık ve mobbing (psikolojik taciz) iddialarını değerlendirmek ve önleyici şikâyet/soruşturma mekanizması kurmak; ispat yükü dağılımını doğru yönetmek.

## Soğuk başlangıç (intake)
1. İddia ne (ücret/terfide ayrımcılık, sendikal ayrım, sistematik yıldırma)?
2. Karşılaştırılabilir emsal çalışan ve farklı muamele somut mu?
3. Davranış süreklilik/sistematiklik taşıyor mu (mobbing ölçütü)?
4. İşyerinde şikâyet/etik hattı ve soruşturma süreci var mı?

## Denetim şeması
1. **Eşit davranma (4857 m.5)**: İşveren, esaslı sebep olmadıkça çalışanlara eşit davranmak zorunda; ihlalde işçi **4 aya kadar ücret tutarında** ayrımcılık tazminatı ve yoksun kaldığı haklarını isteyebilir.
2. **İspat yükü (m.5/son)**: İşçi ayrımcılığı **güçlü olasılıkla** ortaya koyarsa, böyle bir muamelenin olmadığını **işveren** ispatlar. Bu yüzden objektif kriter belgesi şart.
3. **Mobbing**: Yargı, sistematik, süreklilik arz eden, yıldırma kastlı davranışları mobbing sayar; tazminat TBK haksız fiil/kişilik hakkı (TBK m.49, m.58; TMK m.24-25) ve işverenin gözetme borcu (TBK m.417) temelinde değerlendirilir.
4. **İşverenin önleme yükümlülüğü (TBK m.417)**: İşçinin kişiliğini koruma ve sağlıklı ortam sağlama borcu; şikâyeti soruşturmamak başlı başına sorumluluk doğurur.
5. **Süreç tasarımı**: Yazılı şikâyet kanalı, tarafsız soruşturma, tanık beyanı ve karar tutanağı; misilleme yasağı.
6. **Ara sonuç**: Kriter belgesi ve soruşturma kaydı yoksa işveren ispat yükü altında ezilir; tazminat + manevi tazminat riski.

## Çıktı modülleri
- Şikâyet ve iç soruşturma prosedürü taslağı.
- Ayrımcılık/mobbing risk değerlendirme notu.
- Objektif terfi/ücret kriteri çerçevesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

