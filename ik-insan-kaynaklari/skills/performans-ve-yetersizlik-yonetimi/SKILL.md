---
argument-hint: ''
description: Yetersizlik veya performans düşüklüğü gerekçesiyle fesih hazırlanıyorsa,
  performans kriterleri, ölçüm, uyarı ve iyileştirme planı (PIP) kurgulanacaksa kullanılır.
name: performans-ve-yetersizlik-yonetimi
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


# Performans ve Yetersizlik Yönetimi

## Görev
Performans/yetersizlik gerekçeli feshi, geçerli sebep eşiğini karşılayacak ölçülebilir veri ve son çare adımlarıyla desteklemek; salt sübjektif değerlendirmeye dayanan ve işe iadeyle sonuçlanan feshi önlemek.

## Soğuk başlangıç (intake)
1. Pozisyonun ölçülebilir hedef/kriterleri tanımlı mı, çalışana önceden bildirildi mi?
2. Performans düşüklüğü hangi objektif veriyle gösteriliyor (satış, hata oranı, teslim süresi)?
3. Daha önce yazılı uyarı/geri bildirim verildi mi?
4. İyileştirme için eğitim, mentorluk veya yer değişikliği denendi mi?

## Denetim şeması
1. **Kriterin önceden varlığı**: Yetersizlik feshinin geçerli sebep sayılması için performans ölçütleri objektif, çalışana **önceden** bildirilmiş ve ulaşılabilir olmalı (4857 m.18 geçerli sebep — içtihat, `[DOĞRULANMADI]`).
2. **Objektif ölçüm**: Beklentinin altında kalış, kıyaslanabilir veriyle (emsal çalışan, dönemsel hedef) gösterilmeli; "verimsiz" gibi soyut nitelendirme yetmez.
3. **Uyarı ve makul süre**: Çalışana yazılı geri bildirim + düzeltme için makul süre tanı; bu, son çare ilkesinin (ultima ratio) belgesidir.
4. **İyileştirme planı (PIP)**: Eğitim/mentorluk/görev yeri değişikliği gibi destek adımları belgelendiğinde, sonuçsuz kalan süreç feshi güçlendirir.
5. **Savunma ve usul (m.19)**: Fesih anında yazılı bildirim + (davranışsal boyut varsa) savunma; salt yetersizlikte de yazılı sebep şart.
6. **İspat (m.20/2)**: Performans verisinin gerçekliği ve sürecin işletildiği işverence ispatlanır.
7. **Ara sonuç**: Ölçütsüz/uyarısız fesih → geçersiz sayılma ve işe iade riski yüksektir.

## Çıktı modülleri
- Performans kriteri ve hedef tanım belgesi.
- Yazılı performans uyarısı ve PIP (iyileştirme planı) taslağı.
- Yetersizlik gerekçeli fesih bildirimi taslağı ve son çare notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

