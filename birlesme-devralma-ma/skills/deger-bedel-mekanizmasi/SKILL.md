---
argument-hint: ''
description: İşlem bedelinin yapılandırılması, kapanış bilançosu düzeltmesi, locked-box,
  earn-out ve escrow mekanizmalarının hukuki olarak tasarlanması ve uyuşmazlık riskinin
  azaltılması için kullanılır.
name: deger-bedel-mekanizmasi
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


# Değerleme, Bedel ve Earn-Out Mekaniği

## Görev
İşlem bedelinin hukuki yapısını kurmak; düzeltme, earn-out ve teminat mekanizmalarını uyuşmazlığa dayanıklı biçimde tasarlamak.

## Soğuk başlangıç (intake)
- Bedel sabit mi, kapanış hesaplarına göre düzeltmeli mi?
- Locked-box mu, completion accounts mu tercih ediliyor?
- Earn-out hangi metriğe (ciro, FAVÖK) bağlanacak ve süresi ne?
- Bedelin bir kısmı escrow/teminatta tutulacak mı?

## Denetim şeması
1. **Bedel yapısı**: Satış bedeli TBK m.207 anlamında belirli veya belirlenebilir olmalıdır; belirlenebilir bedelde objektif formül şarttır, aksi halde geçersizlik/uyuşmazlık riski.
2. **Locked-box**: Referans bilanço tarihinden sonra değer kaçışına (leakage) karşı satıcı taahhüdü ve tazminatı.
3. **Completion accounts**: Kapanış sonrası net borç/işletme sermayesi düzeltmesi; uzman/bağımsız denetçi başvurma mekanizması (expert determination).
4. **Earn-out**: Metrik tanımı, ölçüm dönemi, alıcının işletmeyi olağan yürütme taahhüdü; manipülasyon riskine karşı iyiniyet (TMK m.2) ve özel koruyucu klozlar.
5. **Escrow**: Beyan-tekeffül ihlali tazminatına teminat; serbest bırakma takvimi ve şartları.
6. **Vergi etkisi**: Bedel yapısının değer artış kazancı/KDV/damga açısından sonuçları gözetilir.
7. **İspat yükü**: Düzeltme/earn-out talebini ileri süren taraf metriğin gerçekleştiğini ispatlar.

## Çıktı modülleri
- Bedel mekaniği şeması ve formül lafzı
- Earn-out koruyucu klozları
- Escrow sözleşmesi ana hatları
- Vergi etkisi notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

