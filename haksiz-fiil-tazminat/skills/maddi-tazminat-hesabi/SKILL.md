---
argument-hint: ''
description: Sorumluluk kurulduktan sonra maddi zararın kalemlerini ayrıştırmak, fiili
  zarar ve yoksun kalınan kârı hesaplatmak ve hâkimin takdir yetkisini değerlendirmek
  gerektiğinde kullanılır.
name: maddi-tazminat-hesabi
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


# Maddi Tazminatın Belirlenmesi ve Hesabı

## Görev
Maddi zararı kalem kalem belirlemek (fiili zarar + yoksun kalınan kâr), tazminatın kapsamını TBK m.50-51 çerçevesinde tespit etmek ve hâkimin zararı tam ispatlanamayan hallerde takdir yetkisini (m.50/2) doğru konumlandırmak. Hesaplar daima dayanağıyla gösterilir.

## Soğuk başlangıç (intake)
- Zarar kalemleri neler (onarım/yenileme bedeli, gelir kaybı, masraflar)?
- Belge/fatura/ekspertiz var mı; zarar tam belgelenebiliyor mu?
- Zarar görenin kusuru veya zararı artıran davranışı var mı?
- Sigorta/üçüncü kişi ödemesi yapıldı mı (denkleştirme)?

## Denetim şeması
1. **Zarar kavramı.** Malvarlığında istem dışı azalma; farazi (zarar olmasaydı) malvarlığı ile gerçek malvarlığı arasındaki fark. Fiili zarar (doğrudan kayıp) ve yoksun kalınan kâr (mahrum kalınan kazanç) ayrılır.
2. **Tazminatın kapsamı (m.51).** Hâkim, tazminatın kapsamını ve ödenme biçimini zararın ağırlığı ile kusurun derecesini göz önünde tutarak belirler. Kural tam tazmin; zararı aşan zenginleşme verilmez.
3. **İspat ve takdir (m.50).** Zarar görenin zararını ispatı asıldır; zararın gerçek miktarı kesin ispat edilemiyorsa hâkim olayların olağan akışını ve zarar görenin aldığı önlemleri göz önünde tutarak hakkaniyetle belirler (m.50/2).
4. **Denkleştirme (yararların mahsubu).** Aynı olaydan doğan ve zararı azaltan yararlar (kurtarılan değer, bazı ödemeler) belirli ölçüde mahsup edilebilir; sosyal güvenlik/sigorta ödemelerinin etkisi ve rücu ilişkisi ayrıca incelenir.
5. **Faiz ve dönem.** Haksız fiilde temerrüt kural olarak fiil/zarar tarihinde başlar; talep edilen faiz türü ve başlangıcı belirtilir.
6. **Ara sonuç.** Kalem-tutar-dayanak tablosu kurulur; belgesiz kalemler için bilirkişi/ekspertiz ihtiyacı ve m.50/2 takdiri işaretlenir. Karmaşık hesaplarda aktüer/bilirkişi yönlendirmesi yapılır.

## Çıktı modülleri
- Zarar kalemleri ve tutar-dayanak tablosu.
- Bilirkişi/ekspertiz soru listesi (belirsiz kalemler için).
- Faiz türü-başlangıç notu ve talep sonucu rakamı taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

