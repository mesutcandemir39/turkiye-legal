---
argument-hint: ''
description: Mülkiyet, zilyetlik, kazandırıcı zamanaşımı, rehin-intifa ve miras kurumlarının
  Roma karşılıklarıyla (dominium, possessio, usucapio, hereditas) eşleştirilmesi;
  tapu, ayni hak ve tereke konularında tar
name: eshya-miras-kokleri
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


# Eşya ve Miras Hukukunun Roma Temelleri

## Görev
TMK eşya ve miras hukuku kurumlarını Roma karşılıklarıyla eşleştirmek ve mülkiyet, zilyetlik, kazandırıcı zamanaşımı ile küllî halefiyet gibi temel kurumların dönüşümünü açıklamak.

## Soğuk başlangıç (intake)
- Konu eşya hukuku mu (mülkiyet, zilyetlik, ayni haklar) yoksa miras mı?
- Somut kurum hangisi (kazanma yolları, zamanaşımı, tereke, saklı pay)?
- Çıktı akademik mi, yorum argümanı mı?

## Denetim şeması
1. Modern temeli sabitle: mülkiyet TMK m.683; zilyetlik TMK m.973 vd.; taşınmaz olağan kazandırıcı zamanaşımı TMK m.712, olağanüstü m.713; tescil ve iyiniyetli üçüncü kişi TMK m.1023; rehin TMK m.939 vd. (taşınır), ipotek TMK m.881 vd.; intifa TMK m.794. Miras: küllî halefiyet TMK m.599; yasal mirasçılık m.495 vd.; saklı pay m.505-506; tenkis m.560 vd.
2. Eşya kurumlarını eşleştir: mülkiyet → dominium/proprietas; zilyetlik → possessio (animus + corpus); kazandırıcı zamanaşımı → usucapio (klasik) ve longi temporis praescriptio. Mülkiyetin kazanma yollarını ayır: aslen kazanma (occupatio, accessio, specificatio, usucapio) ve devren kazanma (traditio, mancipatio, in iure cessio). TMK'daki devren kazanmanın tescile bağlı oluşunu (TMK m.705) Roma'nın şekilci devir usulleriyle kıyasla.
3. Zilyetlik korumasını bağla: Roma'daki interdicta (possessoria) zilyetliğin ayrı korunması düşüncesinin kaynağıdır; TMK m.981 vd. zilyetliğin korunması davalarıyla eşleştir.
4. Rehin-intifa kataloğunu bağla: pignus/hypotheca → taşınır rehni/ipotek; usus fructus → intifa; servitutes → irtifak. numerus clausus ilkesini hatırlat.
5. Miras kurumunu kur: küllî halefiyet (TMK m.599) → hereditas; mirasçının tereke borçlarından sorumluluğu Roma'daki successio in universum ius düşüncesinden gelir. Saklı pay (TMK m.505-506) ve tenkis ile Roma'daki querela inofficiosi testamenti (mirasta hak ihlaline karşı dava) düşüncesini bağla. Vasiyet → testamentum; legatum → belirli mal vasiyeti (TMK m.517 muayyen mal vasiyeti).
6. Ara sonuç: kurumu doğru köke oturt; dönüşümü (ör. tescil sisteminin Roma'da bulunmayışı, modern tapu sicilinin yeni bir katman oluşu) işaretle.

İspat/dayanak: TMK m.683, m.705, m.712-713, m.1023, m.599, m.505-506 ile; Roma kurumları fragmanla; doktrin [DOĞRULANMADI].

## Çıktı modülleri
- Eşya hukuku eşleştirme tablosu (TMK maddesi / Roma kurumu / kazanma yolu).
- Miras küllî halefiyet ve saklı pay soykütüğü.
- Dönüşüm uyarısı (tapu sicili gibi modern eklentiler).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

