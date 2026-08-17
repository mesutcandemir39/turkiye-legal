---
argument-hint: ''
description: Donatan/gemi işletme müteahhidinin deniz alacaklarına karşı sorumluluğunu
  küresel olarak sınırlandırması (LLMC sınırlı sorumluluk fonu) ya da alacaklının
  bu sınırı aşmaya çalışması söz konusu olduğund
name: donatan-sorumlulugun-sinirlandirilmasi
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
  version: 0.1.0
user-invocable: true
---


# Donatanın Sorumluluğu ve Sınırlandırılması

## Görev
Donatanın deniz alacaklarına karşı topluca (global) sorumluluğunu sınırlandırma hakkını değerlendirmek; sınırlı sorumluluk fonunun kurulması ve dağıtımını planlamak veya alacaklı adına sınırın aşılabileceği halleri araştırmak.

## Soğuk başlangıç (intake)
- Talepler hangi nitelikte (yük, can/beden, liman tesisi zararı, kirlilik)?
- Donatan/gemi işletme müteahhidi sıfatı kimde; geminin tonajı (gros ton) nedir?
- Sınırlandırmaya tabi olmayan veya sınırı kaldıran bir kusur (kasıt/pervasızlık) iddiası var mı?
- Fon kurulacak mı; başka ülkede paralel takip/fon var mı?

## Denetim şeması
1. **Sorumluluğun temeli**: Donatanın gemi adamlarının kusurundan sorumluluğunu (TTK m.1062) ve gemi işletme müteahhidinin konumunu (TTK m.1065) belirle.
2. **Sınırlandırmaya tabi alacaklar**: Hangi alacakların topluca sınırlandırmaya tabi olduğunu (TTK m.1328 vd., 1976 LLMC esaslı) tespit et; mürettebat alacakları, kurtarma ücreti ve bazı kirlilik alacakları gibi sınır dışı kalanları ayır.
3. **Sınır miktarı (fon)**: Geminin tonajına göre, can zararı ve diğer zararlar için ayrı limit dilimlerini hesapla; sınırlı sorumluluk fonunun kurulması, fona başvuru ve dağıtım sırasını belirt.
4. **Sınırın kalkması**: Zararın, donatanın bizzat **kasten veya pervasızca ve muhtemelen böyle bir zararın doğacağı bilinciyle** yaptığı fiilden doğduğu ispatlanırsa sınırlandırma hakkı düşer; bu yüksek eşiği değerlendir.
5. **İspat ve ara sonuç**: Sınırlandırma hakkını donatan ileri sürer; sınırın kalkmasını iddia eden alacaklı ağır kusuru ispatlar. Çıktıda fon tutarını, sınır dışı alacakları ve sınırın aşılma ihtimalini gerekçeli sonuca bağla.

## Çıktı modülleri
- Sınırlandırmaya tabi/sınır dışı alacaklar tablosu
- Tonaja göre fon limiti hesap taslağı
- Fon kurma veya sınırı aşma strateji notu



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

