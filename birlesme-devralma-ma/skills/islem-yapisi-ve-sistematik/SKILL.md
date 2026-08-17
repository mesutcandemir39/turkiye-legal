---
argument-hint: ''
description: Bir M&A işleminin temel iskeletini kurmak, pay devri ile varlık devri
  ile teknik birleşme arasında seçim yapmak, taraf-hedef-bedel-onay haritasını çıkarmak
  ve hangi norm kümelerinin devreye gireceğini
name: islem-yapisi-ve-sistematik
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
  - ad: Sermaye Piyasası Kanunu
    numara: '6362'
    tur: kanun
  - ad: Rekabetin Korunması Hakkında Kanun
    numara: '4054'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İşlem Yapısı ve M&A Sistematiği

## Görev
İşlemin hukuki gerçekleştirme biçimini (pay devri / varlık devri / TTK m.134 teknik birleşme / TTK m.159 bölünme) ve buna bağlı norm setini belirlemek; taraf-hedef-bedel-onay haritasını çıkarmak.

## Soğuk başlangıç (intake)
- Hedef hangi tür şirket (AŞ mı, limited mi)? Halka açık mı?
- Müvekkil alıcı mı, satıcı mı; payların tamamı mı azınlık mı devrediliyor?
- Bedel yapısı nedir (peşin / vadeli / earn-out / escrow)?
- Düzenlenmiş sektör (banka, enerji, sigorta, telekom) ve rekabet eşiği söz konusu mu?

## Denetim şeması
1. **Yapı tercihi**: Pay devri sözleşmesel ve hızlıdır, hedefin tüm pasifi (gizli borçlar dahil) devralanla birlikte kalır → beyan-tekeffül ve indemnity kritiktir. Varlık devrinde TBK m.202 uyarınca devralan, devraldığı malvarlığının borçlarından devredenle **müteselsilen** sorumlu olur (iki yıl); bu nedenle borç süzgeci gerekir.
2. **Teknik birleşme** (TTK m.136): Devralma veya yeni kuruluş yoluyla; külli halefiyet, birleşme sözleşmesi (TTK m.145), birleşme raporu (TTK m.147), genel kurul onayı (TTK m.151) ve alacaklıların korunması (TTK m.157) zorunludur.
3. **Şekil**: AŞ nama yazılı pay devri ciro + zilyetlik devri ve pay defteri kaydı (TTK m.490, m.499); limited pay devri **yazılı + noter onaylı** sözleşme ve genel kurul onayı (TTK m.595).
4. **Devir engelleri**: Esas sözleşmede bağlam (TTK m.491-492), ön alım hakkı, sözleşmelerde change-of-control klozları taranır.
5. **Ara sonuç**: Hangi izinlerin (rekabet, sektörel, ortaklık onayı) kapanış şartı olacağı ve hangi belgelerin (SPA, SHA, disclosure) hazırlanacağı belirlenir.

## Çıktı modülleri
- İşlem yapısı karar notu (pay/varlık/birleşme gerekçeli karşılaştırma)
- Taraf-hedef-bedel-onay haritası tablosu
- Gerekli onay ve şekil şartları kontrol listesi
- Yol haritası (signing → CP → closing → post-closing) takvimi



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

