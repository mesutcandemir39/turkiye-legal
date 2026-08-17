---
argument-hint: ''
description: Hakkında takip başlatılan borçlu için savunma haritası kurmak, taahhüt-mal
  beyanı yükümlülüklerini ve İİK'nın icra suçlarını (taahhüdü ihlal, mal kaçırma)
  değerlendirmek; ödeme/yapılandırma ve uzlaşma
name: borclu-savunma-stratejisi-ve-icra-suclari
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
  - ad: İcra ve İflas Kanunu
    numara: '2004'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Borçlu Savunma Stratejisi ve İcra Ceza

## Görev
Borçlu/müvekkil cephesinde takibe karşı bütünsel savunma kurmak; itiraz/şikâyet/menfi tespit seçeneklerini sıralamak; mal beyanı ve ödeme taahhüdü yükümlülüklerini ve İİK'nın icra suçlarını (m.331 vd.) yönetmek.

## Soğuk başlangıç (intake)
- Borç gerçekte var mı; itiraz/menfi tespit dayanağı var mı?
- Ödeme emri türü ve süresi nedir; itiraz süresi geçti mi?
- Mal beyanı verildi mi; ödeme taahhüdü imzalandı mı?
- Haciz/satış riski hangi malları kapsıyor; haczedilmezlik var mı?

## Denetim şeması
1. **Savunma yolu sıralaması**: Önce takibi durduran yollar (ilamsızda itiraz m.62; kambiyoda teminatla durdurma m.169/a); ardından menfi tespitle teminatla icranın durdurulması (m.72); usul hatalarında şikâyet (m.16).
2. **Mal beyanı (m.74-76)**: Borçlu süresinde gerçek mal beyanında bulunmalı; bulunmama veya gerçeğe aykırı beyan icra ceza boyutunu doğurur. Haczedilmezlik itirazları zamanında ileri sürülür (m.82-83).
3. **Ödeme taahhüdü ve ihlali (m.111, m.340)**: İcra dairesinde alacaklının kabulüyle yapılan ödeme taahhüdünün ihlali, şikâyet üzerine tazyik hapsi gündeme getirir; taahhüdün geçerlilik şartları (miktar, tarih, kabul) sıkı denetlenir.
4. **İcra suçları (m.331 vd.)**: Mal kaçırma/gizleme, alacaklıyı zarara sokma, gerçeğe aykırı beyan gibi fiiller için icra ceza mahkemesi görevlidir; şikâyet süreleri ve tazyik hapsi koşulları değerlendirilir.
5. **Yapılandırma/uzlaşma**: Taksitlendirme, haczin kaldırılması karşılığı ödeme, sulh ve gerektiğinde konkordato seçeneği tartılır.
6. **Ara sonuç**: Risk-fayda dengesine göre savunma planı ve ceza riski haritası çıkarılır.

## Çıktı modülleri
- Savunma yolu öncelik sıralaması (durdurucu etkilere göre).
- Mal beyanı/taahhüt risk notu ve icra ceza kontrolü.
- Ödeme/yapılandırma senaryoları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

