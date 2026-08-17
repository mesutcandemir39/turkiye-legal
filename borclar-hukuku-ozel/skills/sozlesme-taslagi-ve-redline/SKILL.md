---
argument-hint: ''
description: Satış, kira, eser, vekâlet veya kefalet sözleşmesi taslağı hazırlamak
  ya da mevcut bir taslağı emredici hükümler ve risk dengesi açısından gözden geçirmek
  gerektiğinde kullanılır.
name: sozlesme-taslagi-ve-redline
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Sözleşme Taslağı ve Redline (İsimli Sözleşmeler)

## Görev
İsimli bir sözleşmenin taslağını üretmek veya mevcut metni TBK Özel Hükümler ve emredici tabanlar süzgecinden geçirip risk-dengeli redline önermek; geçersiz/asimetrik şartları tespit edip alternatif lafız sunmak.

## Soğuk başlangıç (intake)
- Sözleşme tipi ve taraflar (hangi tarafı temsil ediyoruz)?
- Edimler, bedel, vade ve teminat yapısı?
- Tüketici/konut kirası gibi emredici taban var mı?
- Müzakere gücü ve kabul edilebilir risk seviyesi?

## Denetim şeması
1. **Zorunlu/şekil unsurları.** Taşınmaz satışı/satış vaadi resmî şekil (TBK m.237, m.29 satış vaadi noter); kefalette el yazısı azami miktar + tarih + eş rızası (m.583-584); aksi halde hükümsüzlük.
2. **Emredici taban taraması.** Konut/çatılı işyeri kirasında kiracı aleyhine kayıt yasağı (m.346); muacceliyet/cezai şart geçersiz. Tüketici sözleşmelerinde haksız şart denetimi (6502 m.5). Genel işlem koşullarında yazılmamış sayılma (TBK m.20-25).
3. **Risk maddeleri.** Sorumluluk sınırlaması: ağır kusur/kasıt için sorumsuzluk anlaşması kesin geçersiz (TBK m.115); ayıptan sorumluluğu kaldıran kayıt satıcı ayıbı gizlemişse geçersiz (m.221). Cezai şart (m.179-182) ve aşırı cezanın indirilmesi (m.182/3).
4. **Denge kontrolü.** Fesih hakları simetrik mi; temerrüt faizi ve oranı (TBK m.120, ticari işte 3095 s.K.); teslim/kabul ve ayıp ihbar süreleri; mücbir sebep ve uyarlama (m.138) kaydı.
5. **Uyuşmazlık çözümü.** Yetkili mahkeme/tahkim şartı geçerlilik (HMK m.17 yetki sözleşmesi tacir şartı); arabuluculuk ön şartına atıf.
6. **Ara sonuç.** Madde madde risk skoru, geçersiz şart listesi, müzakere notu. İspat boyutu: ihtar/bildirim için yazılılık ve tebligat klozları eklenir.

## Çıktı modülleri
- Sözleşme taslağı veya redline (gerekçeli değişiklik notlarıyla).
- Geçersiz/riskli şart tablosu + alternatif lafız.
- Müzakere pozisyon notu (müvekkil lehine/karşı taraf beklentisi).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

