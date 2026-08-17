---
argument-hint: ''
description: TBK haksız fiil (m.49 vd.) ve sebepsiz zenginleşme (m.77 vd.) kurumlarının
  Roma delictum ve condictio sistematiğine bağlanması; kusur, hukuka aykırılık ve
  iade dogmatiğinde tarihî temel gerektiğinde k
name: haksiz-fiil-sebepsiz-zenginlesme-kokleri
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
  sources: []
  version: 0.1.0
user-invocable: true
---


# Haksız Fiil ve Sebepsiz Zenginleşmenin Roma Kökleri

## Görev
Sözleşme dışı borç kaynaklarını — haksız fiil ve sebepsiz zenginleşme — Roma'nın delictum ve condictio kurumlarına bağlamak; kusur, hukuka aykırılık ve iade dogmatiğini tarihî temelleriyle açıklamak.

## Soğuk başlangıç (intake)
- Konu haksız fiil mi, sebepsiz zenginleşme mi, ikisinin yarışması mı?
- Hangi unsur tartışılıyor (kusur, illiyet, hukuka aykırılık, iade kapsamı)?
- Çıktı akademik mi, yorum argümanı mı?

## Denetim şeması
1. Modern temeli sabitle: haksız fiilin unsurları TBK m.49 vd. — fiil, hukuka aykırılık, kusur, zarar, illiyet bağı; manevi tazminat TBK m.58. Sebepsiz zenginleşme TBK m.77 vd. — haklı bir sebep olmaksızın malvarlığı kayması, iade; iade kapsamı TBK m.79, kötüniyetli zenginleşen TBK m.80.
2. Haksız fiilin Roma kökünü kur: delictum (özel hukuk haksız fiili) — furtum (hırsızlık), rapina, iniuria (kişiliğe saldırı), damnum iniuria datum. Mala verilen zarar için lex Aquilia temel düzenlemedir; modern damnum (zarar) ve culpa (kusur) kavramları buradan gelir. Kusur dereceleri (dolus, culpa lata, culpa levis) modern kast-ihmal ayrımının atasıdır.
3. Hukuka aykırılığı bağla: damnum iniuria datum'daki iniuria (hukuka aykırılık) unsuru, TBK m.49/f.1'deki hukuka aykırılık şartının kökenidir. Salt zarar değil, hukuka aykırı zarar aranır.
4. Sebepsiz zenginleşmenin Roma kökünü kur: condictio davaları — condictio indebiti (borç olmayanın ödenmesi), condictio causa data causa non secuta (gerçekleşmeyen sebep), condictio ob turpem vel iniustam causam. Bunlar TBK m.77'deki geçerli olmayan/gerçekleşmeyen/sona eren sebep ayrımının kaynağıdır.
5. Yarışmayı çöz: aynı maddi olayda haksız fiil ve sebepsiz zenginleşme taleplerinin yarışması (TBK m.60 benzeri seçimlik haklar mantığı) Roma'daki actio'lar yarışması düşüncesiyle bağlanır; ancak çözümü yürürlükteki maddeye göre ver.
6. Ara sonuç: somut talebi doğru köke oturt; unsurları madde sırasına göre denetle.

İspat/dayanak: TBK m.49, m.58, m.77, m.79-80 ile; Roma kurumları (lex Aquilia, condictio) fragmanla; doktrin [DOĞRULANMADI].

## Çıktı modülleri
- Unsur soykütüğü tablosu (TBK unsuru / Roma karşılığı).
- Kusur dereceleri karşılaştırması (dolus-culpa / kast-ihmal).
- condictio tipleri ile TBK m.77 sebep ayrımı eşlemesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

