---
argument-hint: ''
description: Tereke borca batık ya da belirsizken mirasçının sorumluluktan korunması
  için ret, defter tutma veya resmi tasfiye seçeneklerini değerlendirmek; üç aylık
  süre, hükmen ret ve mirasçıların borçtan soruml
name: mirasin-reddi-ve-tereke-koruma
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
  - ad: Türk Medeni Kanunu
    numara: '4721'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Mirasın Reddi, Defter Tutma ve Tereke Koruma

## Görev
Mirasçıyı külli halefiyetin getirdiği borç sorumluluğundan korumak; ret (gerçek/hükmen), tutulan defterle kabul ve resmi tasfiye yollarını TMK m.589-636 çerçevesinde değerlendirmek.

## Soğuk başlangıç (intake)
- Mirasbırakan ne zaman öldü? Mirasçı ölümü/sıfatını ne zaman öğrendi?
- Terekenin aktif/pasif durumu biliniyor mu? Borca batık mı?
- Mirasçı terekeye karıştı, tereke malını sahiplendi mi (m.610)?
- Daha önce mirasçılardan reddeden oldu mu? (sıra ve sonuç)
- Mirasçı küçük/kısıtlı mı? (yasal temsilci ve izin)

## Denetim şeması
1. **Süreyi sabitle (m.606):** Ret, mirasın açıldığını/mirasçılık sıfatını öğrenmeden itibaren üç ay içinde sulh hukuk mahkemesine sözlü/yazılı beyanla yapılır. Süre hak düşürücüdür.
2. **Hükmen reddi değerlendir (m.605/2):** Ölümü anında mirasbırakanın ödemeden aczi açıkça belli veya resmen tespit edilmişse, miras reddedilmiş sayılır; bu, alacaklıya karşı tespit/menfi tespit davasıyla ileri sürülür ve üç aylık süreye tabi değildir.
3. **Ret hakkının düşmesi (m.610):** Süre içinde reddetmeyen, tereke işlerine olağan dışı karışan, malları gizleyen/sahiplenen mirasçı reddedemez.
4. **Ret sonuçları (m.611-613):** Reddeden, miras açılmadan önce ölmüş gibi; payı diğer mirasçılara/sonraki zümreye geçer. En yakın mirasçıların tamamı reddederse tereke iflas hükümlerine göre tasfiye edilir (m.612).
5. **Defter tutma (m.619-631):** İstemle tereke yazımı; deftere geçmeyen borçtan sorumluluk sınırlanır (m.629). Resmi tasfiye (m.632-636) borçtan kişisel sorumluluğu kaldırır.
6. **Ara sonuç:** uygun koruma yolu + süre durumu + dilekçe/başvuru türü. İspat: ölüm/öğrenme tarihi, borca batıklık delili (m.6).

## Çıktı modülleri
- Mirasın reddi beyan dilekçesi (sulh hukuk) taslağı
- Hükmen ret (mirasçı olmadığının tespiti) dava taslağı
- Defter tutma/resmi tasfiye talep dilekçesi
- Süre takvimi ve sorumluluk riski notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

