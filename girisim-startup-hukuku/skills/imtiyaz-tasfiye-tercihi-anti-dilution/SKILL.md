---
argument-hint: ''
description: Yatırımcıya verilen ekonomik ve yönetsel koruma hükümleri (tasfiye tercihi,
  oy/veto imtiyazı, anti-dilution, kâr payı imtiyazı) kurgulanır veya denetlenirken;
  bunların TTK imtiyaz rejimiyle ve esas sö
name: imtiyaz-tasfiye-tercihi-anti-dilution
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
  - ad: Türk Ticaret Kanunu
    numara: '6102'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İmtiyazlar, Tasfiye Tercihi ve Anti-Dilution

## Görev
Yatırımcı koruma hükümlerini TTK imtiyaz sınırları içinde geçerli biçimde kurmak: tasfiye tercihi, oy/veto imtiyazı, kâr payı imtiyazı ve sulandırmaya karşı koruma (anti-dilution).

## Soğuk başlangıç (intake)
1. Hangi koruma isteniyor: tasfiye tercihi, oyda imtiyaz, kâr payı imtiyazı, anti-dilution?
2. Tasfiye tercihi katı (non-participating) mı, katılımlı (participating) mı; çarpan kaç (1x, 2x)?
3. Anti-dilution tam koruma (full ratchet) mı, ağırlıklı ortalama mı?
4. İmtiyazlar esas sözleşmeye işlendi mi, yalnız SHA'da mı?
5. Pay grupları (A/B) tanımlı mı; imtiyazlı pay sahipleri kurulu öngörüldü mü?

## Denetim şeması
1. İmtiyazın kaynağı: İmtiyaz ancak esas sözleşmeyle ve pay grubu tanımıyla kurulur (TTK m.478); salt SHA'daki "imtiyaz" şirkete/üçüncü kişilere karşı imtiyaz doğurmaz, taraflar arası borçtur.
2. Oyda imtiyaz: m.479 — bir paya en çok 15 oy; istisnalar (kurumsal yönetim, haklı sebep). Bazı kararlarda oyda imtiyaz kullanılamaz (m.479/3: esas sözleşme değişikliği, ibra, sorumluluk davası).
3. Tasfiye/kâr payı imtiyazı: Kâr payı ve tasfiye payında imtiyaz (m.478-479; tasfiye payı dağıtımı m.543). Tasfiye tercihi pratikte tasfiye payı imtiyazı + SHA çıkış şelalesi (waterfall) ile kurulur; çarpan ve katılımlı/katılımsız ayrımı sözleşmesel.
4. Anti-dilution: Sonraki turun daha düşük değerlemeli (down round) olması halinde yatırımcının pay oranını koruma. Full ratchet veya ağırlıklı ortalama (broad/narrow) formülü SHA'da; uygulanışı yeni artırımda yatırımcıya ek/bonus pay (genellikle rüçhan + bedelsiz pay mekaniğiyle) gerektirir — TTK m.461 ve sermaye kuralları süzgeci.
5. İmtiyazlı pay sahipleri kurulu: m.454 — imtiyazı zedeleyen GK kararları bu özel kurulun onayına bağlı.
6. Eşit işlem: m.357 (eşit işlem ilkesi) ve dürüstlük sınırı imtiyazların üst çerçevesi.
7. İspat/şekil: İmtiyaz esas sözleşme + tescil; SHA ekonomik şelale yazılı. Çarpan/oranları [doldurulacak] bırak.

## Çıktı modülleri
- İmtiyaz/koruma matrisi (esas sözleşme mi SHA mı, madde atıflı).
- Tasfiye/çıkış şelalesi (waterfall) modeli iskeleti.
- Anti-dilution formülü ve down-round senaryo notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

