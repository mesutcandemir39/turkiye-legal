---
argument-hint: ''
description: Yapay zekâ modeli geliştirme, lisanslama, API kullanımı, SaaS veya entegrasyon
  sözleşmeleri hazırlanırken ya da incelenirken sorumluluk, veri kullanımı, fikri
  mülkiyet, performans garantisi ve tazmina
name: yz-sozlesmeleri-risk-dagitimi
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yapay Zekâ Sözleşmeleri ve Sözleşmesel Risk Dağıtımı

## Görev
Yapay zekâ geliştirme/lisans/SaaS/API sözleşmelerinde tarafların risk, veri, fikri mülkiyet ve sorumluluk dengesini TBK çerçevesinde tasarlamak veya incelemek; eksik, asimetrik veya geçersiz şartları tespit edip redline önermek.

## Soğuk başlangıç (intake)
1. Sözleşme tipi: model geliştirme/eser, lisans, API/SaaS abonelik, entegrasyon/danışmanlık?
2. Müvekkil hangi taraf: sağlayıcı mı, kullanan/alıcı mı?
3. Eğitim/girdi/çıktı verisi kime ait, modeli iyileştirmede kullanılıyor mu?
4. Çıktı üzerinde fikri hak kime; ticari sır ve KVKK boyutu var mı?

## Denetim şeması
1. **Konu ve tip tayini**: Eser/geliştirme ağırlıklıysa TBK eser sözleşmesi (m.470 vd.) ve ayıba karşı tekeffül; sürekli hizmet/lisans ise hizmet/atipik sözleşme. Ara sonuç: hangi tip ve emredici hükümler.
2. **Veri ve KVKK maddeleri**: Girdi verisinin model eğitiminde kullanımı için açık yetki; veri işleyen sıfatı doğuyorsa KVKK m.12 uyumlu veri işleme sözleşmesi ve m.9 aktarım taahhütleri. Eksikse uyum açığı.
3. **Fikri mülkiyet**: Çıktı ve modelin hak sahipliği, lisans kapsamı, üçüncü kişi açık kaynak/lisans uyumu (FSEK/SMK). "Çıktı üzerinde hak garanti edilemez" gerçeğini sözleşmeye yansıt.
4. **Performans ve sorumluluk**: SLA, doğruluk/halüsinasyon riskine ilişkin garanti sınırları; sorumluluk sınırlaması maddeleri TBK m.115 (ağır kusur/kasıtta geçersizlik) ve genel işlem koşulu denetimi (m.20-25) süzgecinden geçirilir.
5. **Tazminat/rücu**: Üçüncü kişi taleplerinde tazmin (indemnity), veri ihlali ve fikri hak ihlali için tahsis; cezai şart ve fesih.

Emredici hüküm ve tüketici işlemi varsa 6502 TKHK ek denetimi. İçtihat künyesini [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Risk maddesi haritası (veri/IP/sorumluluk/SLA).
- Redline ve alternatif lafız önerileri.
- Müzakere notu ve risk skoru.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

