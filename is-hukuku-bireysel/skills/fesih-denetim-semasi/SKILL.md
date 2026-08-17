---
argument-hint: ''
description: İş sözleşmesinin feshinin haklı, geçerli ya da usulsüz olup olmadığını
  adım adım ayırmak gerektiğinde; fesheden tarafa, sebebe, bildirime ve usule göre
  feshi nitelendirip doğacak tazminat ve davaları
name: fesih-denetim-semasi
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Fesih Denetim Şeması (Haklı / Geçerli / Usulsüz)

## Görev
Feshi türüne göre ayırmak: süreli (önelli) fesih mi, geçerli sebebe dayalı fesih mi, haklı (derhal) fesih mi; usule uygunluk ve sonuçlarını (tazminat, işe iade) belirlemek.

## Soğuk başlangıç (intake)
1. Sözleşmeyi kim feshetti, hangi tarihte, hangi gerekçeyle?
2. Fesih yazılı mı, sebep açıkça gösterildi mi (İş K. m.19)?
3. İşçi savunması alındı mı (davranış/verimsizlik halinde)?
4. İşyeri 30+ işçi çalıştırıyor mu, işçinin kıdemi 6 ayı aştı mı?

## Denetim şeması
1. **Fesheden tarafı belirle.**
2. **Haklı fesih kontrolü:**
   - İşçi yönünden: İş K. m.24 (sağlık, ahlak ve iyiniyete aykırılık — örn. ödenmeyen ücret, mobbing, zorlayıcı sebep).
   - İşveren yönünden: İş K. m.25 (özellikle m.25/II ahlak ve iyiniyete aykırılık).
   - **Hak düşürücü süre:** m.26 — öğrenmeden itibaren altı işgünü ve her halde bir yıl. Süre geçmişse haklı fesih hakkı düşer.
3. **Geçerli fesih kontrolü (m.18):** Haklı sebep yoksa, işçinin yetersizliği, davranışı veya işletme gereklerine dayalı geçerli sebep var mı? İşletme gereğinde feshin son çare (ultima ratio) olması aranır. İspat yükü işverende (m.20/2).
4. **Usul (m.19):** Fesih yazılı yapılmalı ve sebep açık-kesin gösterilmeli; m.25/II hariç davranış/verimsizlik feshinde işçinin savunması alınmalı. Usulsüzlük geçerli sebebi dahi etkisiz kılabilir.
5. **Ara sonuç ve sonuçlar:**
   - Haklı fesih (işveren m.25/II): Kıdem ve ihbar doğmaz (m.25/II ise kıdem de yok); işçinin haklı feshinde (m.24) kıdem doğar, ihbar doğmaz.
   - Usulsüz (önelsiz) fesih: İhbar tazminatı doğar (m.17).
   - Geçersiz fesih + güvence kapsamı: İşe iade davası (m.20-21) yolu açılır.

## Çıktı modülleri
- Fesih nitelendirmesi tablosu (taraf / sebep / usul / sonuç).
- Hangi tazminat kalemlerinin doğduğu.
- İşe iade yolu açık mı değerlendirmesi.
- Risk ve eksik delil notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

