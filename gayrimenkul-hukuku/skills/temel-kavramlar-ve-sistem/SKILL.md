---
argument-hint: ''
description: Taşınmaza ilişkin bir işi ilk kez ele alırken; talebin ayni hakka mı
  borç ilişkisine mi idari boyuta mı dayandığını, hangi sözleşme/dava tipinin söz
  konusu olduğunu ayırmak ve doğru hukuki temeli kurm
name: temel-kavramlar-ve-sistem
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
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  - ad: Kat Mülkiyeti Kanunu
    numara: '634'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Temel Kavramlar ve Gayrimenkul İşlem Sistematiği

## Görev
Önündeki taşınmaz işini doğru eksene oturtmak: talebin ayni hakka mı (mülkiyet, irtifak, rehin), borç ilişkisine mi (satış vaadi, inşaat, kira), yoksa kamusal/idari boyuta mı (imar, kamulaştırma, kat mülkiyeti) dayandığını belirlemek. Doğru nitelendirme; şekil, süre, görev-yetki ve ispatın tamamını belirler.

## Soğuk başlangıç (intake)
- Taşınmazın türü ne: arsa, tarla, bina, bağımsız bölüm (daire/dükkân), devre mülk?
- Müvekkilin talebi tapuyu/mülkiyeti elde etmek/iptal ettirmek mi, para/tazminat mı, yoksa bir kullanımı durdurmak/sağlamak mı?
- İşin dayanağı bir sözleşme mi (satış vaadi, inşaat, kira), bir tapu kaydı mı, yoksa idari bir işlem mi (imar, kamulaştırma)?
- Tapu kaydı kimin adına; üzerinde ipotek, haciz, şerh, beyan var mı?

## Denetim şeması
1. **Eksen tespiti**: Mülkiyet ve sınırlı ayni haklar mutlaktır, herkese karşı ileri sürülür ve sınırlı sayı (numerus clausus) ilkesine tabidir. Buna karşılık satış vaadi, inşaat ve kira nispi (borç) ilişkileridir; tek başlarına ayni hak doğurmaz.
2. **Kazanım kuralı**: Taşınmaz mülkiyeti kural olarak tapuya tescille kazanılır (TMK m.705/1, m.1021). Miras, mahkeme kararı, cebrî icra, kamulaştırma tescilden önce kazandırır (m.705/2). Bu ayrım, satış vaadi alacaklısının doğrudan malik olamayacağını; tescil davası gerektiğini gösterir.
3. **Şekil süzgeci**: Mülkiyeti devir sözleşmeleri resmî senetle (tapu önünde) yapılır (TMK m.706; TBK m.237). Satış vaadi noterde resmî şekle tabidir (TBK m.29; Noterlik K. m.60/3) ve tapuya şerh edilebilir (TMK m.1009). Şekle aykırılık kural olarak kesin hükümsüzlüktür (TBK m.27).
4. **Takyidat haritası**: Tapu kaydındaki ipotek, haciz, şerh (satış vaadi, kira), beyan ve kat irtifakı/mülkiyeti durumu işin tüm seyrini etkiler; ilk işte mutlaka çıkarılır.
5. **Ara sonuç**: İşin baskın ekseni, uygulanacak sözleşme/dava tipi ve doğru hukuki dayanak belirlenir; ispat yükü hakkı iddia edene aittir (TMK m.6).

## Çıktı modülleri
- Nitelendirme notu (eksen, sözleşme/dava tipi, dayanak madde).
- Tapu/takyidat kontrol listesi (malik, ipotek, haciz, şerh-beyan, irtifak).
- İlgili uzman beceriye yönlendirme (satış vaadi, inşaat, tapu iptali, kat mülkiyeti, kamulaştırma).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

