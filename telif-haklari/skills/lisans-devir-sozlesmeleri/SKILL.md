---
argument-hint: ''
description: Mali hakların devri veya ruhsat/lisans verilmesine ilişkin sözleşme hazırlanması,
  incelenmesi veya yorumlanması gerektiğinde; FSEK m.48-52 şekil ve kapsam kurallarına
  uygunluğu ve hak zincirini denetl
name: lisans-devir-sozlesmeleri
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Telif Devir ve Lisans Sözleşmeleri

## Görev
Mali hakların devri (temlik) veya kullanım ruhsatı (lisans) sözleşmesini FSEK m.48-52 çerçevesinde hazırlamak, incelemek ve hak zincirini denetlemek.

## Soğuk başlangıç (intake)
- Hangi eser, hangi mali haklar devre/lisansa konu?
- Devir mi (temlik), münhasır lisans mı, basit lisans mı isteniyor?
- Coğrafi alan, süre, ücret, alt lisans yetkisi belirlendi mi?
- Eser henüz meydana gelmemiş mi (gelecekteki eser)?

## Denetim şeması
1. İşlemin niteliği: Mali hak devri (m.48 — tam temlik) mi, ruhsat/lisans (m.48-49 — münhasır/basit) mı belirlenir. Manevi haklar devredilemez; yalnızca kullanım yetkilendirilebilir (m.16/son).
2. Şekil şartı (m.52): Mali haklara ilişkin sözleşme ve tasarruflar yazılı olmak ve konuları olan hakların ayrı ayrı gösterilmesi zorunludur. Sayılmayan hak devredilmemiş sayılır; sözlü/zımni mali hak devri geçersizdir. Bu emredici şekil dosyada ilk kontroldür.
3. Kapsam ve dar yorum: Devir/lisans, açıkça yazılanla sınırlıdır; tereddütte eser sahibi lehine yorum yapılır. Yer-süre-içerik belirlenir; ileride çıkacak kullanım türleri için açık hüküm aranır.
4. Gelecekteki eser ve haklar: Henüz vücut bulmamış eser üzerindeki tasarruf sınırlıdır (m.48/3); ileride çıkarılacak mevzuatın tanıyacağı haklar baştan devredilemez (m.51).
5. Devralanın yetkileri ve cayma: Devralanın hakkı süresinde kullanmaması hâlinde eser sahibinin cayma hakkı (m.58); aşırı zarar hâlinde m.59 değerlendirilir. Alt devir/alt lisans ancak izinle (m.49).
6. Ara sonuç: Geçerli, kapsamı net, hak zinciri kesintisiz bir sözleşme; eksikse redline ve tamamlama önerisi.

İspat yükü: devir/lisans iddiasını ileri süren yazılı belgeyle ispatlar (m.52, HMK m.200 vd.).

## Çıktı modülleri
- Sözleşme taslağı/redline (hak listesi, yer-süre-ücret, alt lisans, cayma).
- m.52 şekil ve kapsam uygunluk kontrol listesi.
- Hak zinciri (chain of title) şeması.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

