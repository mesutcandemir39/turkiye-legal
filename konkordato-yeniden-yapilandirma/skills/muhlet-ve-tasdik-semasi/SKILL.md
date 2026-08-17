---
argument-hint: ''
description: Geçici mühletten kesin mühlete, oradan tasdike kadar konkordato sürecinin
  her aşamasını madde madde denetlemek, şartların ve sürelerin sağlanıp sağlanmadığını
  kontrol etmek gerektiğinde kullanılır.
name: muhlet-ve-tasdik-semasi
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


# Mühlet ve Tasdik Denetim Şeması

## Görev
Konkordato sürecini talep-geçici mühlet-kesin mühlet-tasdik ekseninde adım adım denetlemek; her aşamada İİK'nın aradığı şartların, sürelerin ve çoğunlukların sağlanıp sağlanmadığını belirlemek.

## Soğuk başlangıç (intake)
- Süreç hangi aşamada: talep mi verildi, geçici mühlet mi var, tasdik aşaması mı?
- Talep belgeleri (İİK m.286) tam mı?
- Komiser atandı mı, alacaklılar kurulu kuruldu mu?
- Kabul için gerekli çoğunluk (m.302) sağlanıyor mu?

## Denetim şeması
1. **Talep ve belgeler (m.285-286).** Konkordato ön projesi, mal varlığı belgeleri, finansal tablolar, makul güvence veren denetim raporu (KGK standartlarına göre), alacaklı/alacak listesi eksiksiz mi? Eksik belge tamamlattırılır.
2. **Geçici mühlet (m.287).** Mahkeme belgeler tamamsa derhal geçici mühlet (kural üç ay; m.287/4 ile bir ay uzatma) verir ve geçici komiser atar. Geçici mühlet kesin mühletin sonuçlarını doğurur (m.288).
3. **Kesin mühlet (m.289).** Komiserin raporu ve borçlu/alacaklı dinlendikten sonra konkordatonun başarı ihtimali varsa bir yıllık kesin mühlet; güçlük halinde altı aya kadar uzatma. İspat yükü: borçlu, projenin başarı ihtimalini ortaya koymalıdır.
4. **Mühletin sonuçları (m.294-297).** Takip yasağı (rehinli alacaklılar bakımından istisna), faiz, sözleşmeler ve borçlunun tasarruf yetkisinin sınırlanması (m.297) denetlenir.
5. **Alacaklılar toplantısı ve çoğunluk (m.299-302).** Kaydedilmiş alacaklıların ve alacak miktarının yarısını ya da kaydedilmiş alacaklıların dörtte birini ve alacakların üçte ikisini aşan çoğunluk şartı (m.302/3) kontrol edilir.
6. **Tasdik şartları (m.305).** Teklifin borçlunun kaynaklarıyla orantılı olması, imtiyazlı alacakların tam ödenmesinin güvenceye bağlanması, yargılama gideri ve komiser ücretinin depo edilmesi. Ara sonuç: tasdik edilebilir mi, reddedilir mi (m.308) belirlenir.

## Çıktı modülleri
- Aşama bazlı kontrol listesi (yapıldı/eksik).
- Çoğunluk hesabı tablosu.
- Tasdik şartları denetim raporu.
- Eksik/risk listesi ve süre uyarıları.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

