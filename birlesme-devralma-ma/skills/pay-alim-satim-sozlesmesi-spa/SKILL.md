---
argument-hint: ''
description: Pay veya varlık devri için SPA taslağını kurmak, bedel mekaniği, kapanış
  öncesi ve sonrası taahhütler, beyan-tekeffül ve tazminat mimarisini madde madde
  tasarlamak için kullanılır.
name: pay-alim-satim-sozlesmesi-spa
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


# Pay Alım Satım Sözleşmesi (SPA) Tasarımı

## Görev
TBK temelinde, işlem yapısına uygun bir SPA iskeleti kurmak; bedel, kapanış, beyan-tekeffül ve tazminat hükümlerini dengeli biçimde tasarlamak.

## Soğuk başlangıç (intake)
- Müvekkil alıcı mı satıcı mı; pazarlık gücü nasıl?
- Bedel sabit mi, kapanış bilançosuna göre düzeltmeli mi (locked-box / completion accounts)?
- Earn-out, escrow veya vadeli ödeme var mı?
- Tabi hukuk Türk hukuku mu, uyuşmazlık tahkim mi mahkeme mi?

## Denetim şeması
1. **Konu ve devir taahhüdü**: Devredilen pay/varlığın tanımı, mülkiyetin geçiş anı, pay defteri kaydı taahhüdü (TTK m.499).
2. **Bedel ve düzeltme**: Sabit bedel veya kapanış hesaplarına göre düzeltme; earn-out formülü ve ölçüm; escrow ile teminat. TBK m.207 vd. satış hükümleri kıyasen.
3. **Kapanış öncesi taahhütler (covenants)**: İmza-kapanış arası olağan işletme yürütümü, negatif taahhütler, CP'lerin sağlanması (rekabet/sektörel izin).
4. **Kapanış mekaniği (closing)**: Eş zamanlı teslim edilecek belgeler, ödeme, pay devri işlemleri; eksik kapanış halinde sonuçlar.
5. **MAC klozu**: Önemli olumsuz değişiklik halinde kapanıştan dönme hakkı.
6. **Tazminat rejimi**: Beyan-tekeffül ihlalinde TBK m.112 vd. çerçevesinde tazminat; cezai şart eklenirse TBK m.179-182 ve hâkimin indirim yetkisi (TBK m.182/3) gözetilir.
7. **İspat yükü**: İhlali ve zararı ileri süren taraf ispatlar (TMK m.6, HMK m.190).
8. **Ara sonuç**: Risk dağılımı (cap, basket, sandbagging) müvekkilin tarafına göre ayarlanır.

## Çıktı modülleri
- SPA madde başlıkları iskeleti ([doldurulacak] yer tutucularla)
- Bedel/earn-out/escrow mekaniği şeması
- CP ve closing deliverables listesi
- Müzakere notu (asimetrik/riskli klozlar)



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

