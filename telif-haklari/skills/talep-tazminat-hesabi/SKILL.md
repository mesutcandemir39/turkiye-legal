---
argument-hint: ''
description: Hangi taleplerin (tecavüzün ref'i, men'i, tazminat, kazancın iadesi,
  m.68 bedel) ileri sürüleceğini ve tazminatın nasıl hesaplanacağını belirlemek gerektiğinde;
  kusur şartı ve üç katına kadar bedel se
name: talep-tazminat-hesabi
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
  - ad: Fikir ve Sanat Eserleri Kanunu
    numara: '5846'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Talep Türleri ve Tazminat Hesabı

## Görev
İhlal karşısında ileri sürülebilecek talepleri sıralamak, koşullarını test etmek ve tazminat/bedel kalemlerini madde dayanaklı biçimde hesaplamak.

## Soğuk başlangıç (intake)
- İhlal devam ediyor mu, durmuş mu (men ya da ref ihtiyacı)?
- Davalının kusuru var mı; ihlalden kazanç elde etti mi?
- Eser için emsal lisans/sözleşme bedeli var mı?
- Manevi zarar (ad belirtmeme, eserin tahrifi) söz konusu mu?

## Denetim şeması
1. Tecavüzün ref'i (m.66-68): Devam eden veya sonuçları süren ihlalin giderilmesi. Kusur şart değildir. Mali hak ihlalinde eser sahibi, sözleşme yapılsaydı isteyebileceği bedelin veya emsal bedelin üç katını talep edebilir (m.68/1) — bu, ihlalin caydırılması işlevini görür ve ayrı bir tazminat hesabı gerektirmeden uygulanabilir.
2. Tecavüzün men'i (m.69): Muhtemel veya devam eden ihlalin önlenmesi; kusur ve zarar şartı aranmaz.
3. Maddi tazminat (m.70/1-2): Manevi hak ihlalinde m.70/1; mali hak ihlalinde kusur varsa uğranılan zararın tazmini (TBK m.49 vd. atfıyla). Davacı m.68 bedeli ile m.70 tazminatı arasında lehine olanı seçer; mükerrer talep edilmez.
4. Manevi tazminat (m.70/1): Manevi hakların ihlalinde duyulan elem-üzüntü için; takdiri hâkime aittir (TBK m.58 ölçütleriyle).
5. Kazancın iadesi/temin (m.70/3): Kusur aranmadan, ihlal edenin elde ettiği kârın talebi; vekâletsiz iş görme hükümleri kıyasen uygulanır.
6. Hesap unsurları: Emsal lisans bedeli, kullanım süresi/adedi, mecra, eserin niteliği belirlenir; bilirkişiyle desteklenir. Faiz başlangıcı (haksız fiilde olay tarihi) ve zamanaşımı (TBK m.72) kontrol edilir.

İspat yükü: zarar ve miktarı davacı ispatlar; m.68 bedelinde emsal/sözleşme bedeli esas alınır.

## Çıktı modülleri
- Talep matrisi (ref/men/tazminat/m.68 bedel/kazanç — koşul — kusur şartı).
- Tazminat ve m.68 bedel hesap tablosu (emsal, çarpan, faiz).
- Seçimlik haklar arası tercih notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

