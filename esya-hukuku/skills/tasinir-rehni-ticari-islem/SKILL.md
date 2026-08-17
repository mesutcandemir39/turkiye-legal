---
argument-hint: ''
description: Taşınır mal, alacak veya işletme varlığının teminat gösterilmesi söz
  konusu olduğunda; klasik teslime bağlı taşınır rehni ile 6750 sayılı Kanun kapsamında
  teslimsiz (sicil) rehin ayrımı ve paraya çevi
name: tasinir-rehni-ticari-islem
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


# Taşınır Rehni ve Ticari İşlemlerde Taşınır Rehni

## Görev
Taşınır teminat yapılarını kurmak: TMK'daki teslime bağlı taşınır rehni ile 6750 sayılı Ticari İşlemlerde Taşınır Rehni Kanunu kapsamındaki teslimsiz (sicile tescilli) rehni ayırmak; hapis hakkı ve alacak rehnini değerlendirmek.

## Soğuk başlangıç (intake)
- Rehnedilecek değer ne: somut taşınır mal mı, alacak mı, ticari işletme/stok mu?
- Taraflar tacir/esnaf gibi 6750 kapsamına giren kişiler mi?
- Rehinli malın zilyetliği alacaklıya devredilecek mi, yoksa borçluda mı kalacak?
- Borç ödenmediğinde hızlı paraya çevirme isteniyor mu?

## Denetim şeması
1. **Klasik taşınır rehni (TMK m.939 vd.)**: Kural teslime bağlı rehindir; rehin, malın zilyetliğinin alacaklıya (veya üçüncü kişiye) devriyle doğar (m.939). Borçluda kalan teslimsiz rehin geçersizdir (m.939/2).
2. **Alacak ve hak rehni (m.954 vd.)**: Devredilebilen alacak ve haklar rehnedilebilir; senede bağlı alacaklarda senedin teslimi/ciro gerekir.
3. **6750 sayılı Kanun (ticari işlemlerde taşınır rehni)**: Tacir/esnaf vb. arasında, mülkiyeti devretmeden ve teslim olmaksızın taşınır varlıklar (makine, stok, alacak, ticari işletme) Rehinli Taşınır Sicili'ne tescille rehnedilebilir. Aleniyet sicil tescili ile sağlanır.
4. **Lex commissoria yasağı**: Borç ödenmezse alacaklının rehinli malın mülkiyetini doğrudan edinmesini öngören anlaşma kural olarak geçersizdir (m.949 mantığı; 6750'de de sınırlı istisnalarla).
5. **Hapis hakkı (m.950-953)**: Alacaklı, zilyetliğindeki taşınırı, alacağı ile bağlantılı olmak koşuluyla borç ödenene dek alıkoyabilir ve gereğinde paraya çevirebilir.
6. **Paraya çevirme**: Klasik rehinde İİK m.145 vd. (rehnin paraya çevrilmesi); 6750 rehninde Kanun'un öngördüğü usule göre.
7. **Ara sonuç**: Doğru rehin tipi seçimi (teslimli/teslimsiz), aleniyetin sağlanması ve paraya çevirme yolunun belirlenmesi.

## Çıktı modülleri
- Rehin sözleşmesi/tescil başvurusu iskeleti (teslimli veya 6750 sicil).
- Rehin tipi seçim tablosu (zilyetlik, taraf sıfatı, aleniyet).
- Paraya çevirme/icra yolu notu.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

