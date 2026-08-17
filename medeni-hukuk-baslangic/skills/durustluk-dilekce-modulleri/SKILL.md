---
argument-hint: ''
description: TMK m.2/m.3/m.4/m.6'ya dayanan bir dava, cevap veya layiha gerekçesi
  yazılırken; dürüstlük/kötüye kullanma/iyiniyet/ispat argümanını dilekçe diline dökmek
  ve yer tutucularla taslaklamak için kullanılı
name: durustluk-dilekce-modulleri
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


# Başlangıç Hükümleri Dilekçe ve Gerekçe Modülleri

## Görev
Başlangıç hükümlerine dayanan bir argümanı (dürüstlük, hakkın kötüye kullanılması, iyiniyet, hakkaniyet, ispat yükü) dilekçe/layiha gerekçesine uygun, altlamalı ve atıf disiplinli bir metne dönüştürmek.

## Soğuk başlangıç (intake)
- Metin kim için: dava dilekçesi, cevap, replik-düplik, istinaf gerekçesi mi?
- Hangi başlangıç hükmü argümanın merkezinde (m.2/1, m.2/2, m.3, m.4, m.6, m.7)?
- Hangi somut vakıalar bu hükmün şartlarını karşılıyor; karşı argüman ne?
- Talep sonucu (asıl talep) nedir ve başlangıç hükmü onu nasıl destekliyor/savunuyor?

## Denetim şeması
1. **Asıl talebe bağla** — Başlangıç hükmü tek başına talep sonucu olmaz; önce asıl talep (HMK m.119/1-ğ: açık talep sonucu) yazılır, başlangıç hükmü onun hukuki sebebi/savunması olarak konumlandırılır.
2. **Hukuki sebep — HMK m.119/1-g** — İlgili madde fıkra/bent ile gösterilir (ör. "TMK m.2/2 — hakkın açıkça kötüye kullanılması yasağı"); hâkim hukuku re'sen uygular ama dayanak açıkça anılır.
3. **Vakıa-şart altlaması** — Hükmün her şartı (ör. m.2/2 için çelişkili davranış + yaratılan güven + açıklık) somut vakıaya bağlanır; her vakıa için delil (HMK m.119/1-f) gösterilir, `[doldurulacak]` yer tutucularıyla eksik bilgi işaretlenir.
4. **İspat şeridi** — TMK m.6 dağılımına göre hangi vakıayı kimin ispatlayacağı; karine varsa (m.3, m.7) aksini ispat yükünün karşı tarafta olduğu vurgulanır.
5. **Karşı argüman karşılama** — "Davalı/davacı … ileri sürebilirse de …" kalıbıyla rakip okuma açıkça çürütülür; özellikle "açıklık" eşiği ve özen ölçütü tartışılır.
6. **Atıf hijyeni** — Mevzuat madde/fıkra ile; içtihat yalnızca ilke + `[DOĞRULANMADI]` künye (mahkeme/daire/E./K./T.). Karar numarası uydurulmaz; abartılı kesinlik ("kesin kazanırız") yerine olasılık dürüstçe nitelenir.

## Çıktı modülleri
- Talep sonucu + başlangıç hükmünün konumu (sebep/savunma).
- Hukuki sebep bloğu (madde/fıkra).
- Vakıa→şart altlama paragrafları + delil bağı + `[doldurulacak]`.
- İspat şeridi ve karşı argüman/çürütme + `[DOĞRULANMADI]` içtihat yeri.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

