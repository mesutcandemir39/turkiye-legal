---
argument-hint: ''
description: Bir yapay zekâ sistemi (otonom karar, üretken çıktı, gömülü ürün) bir
  kişiye zarar verdiğinde geliştirici, kullanan ve veri sağlayıcı arasında sorumluluğun
  haksız fiil, kusursuz sorumluluk ve sözleşme
name: yapay-zeka-sorumluluk
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
  - ad: Kişisel Verilerin Korunması Kanunu
    numara: '6698'
    tur: kanun
  - ad: Türk Borçlar Kanunu
    numara: '6098'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Yapay Zekâ Kaynaklı Zarar ve Sorumluluk

## Görev
Yapay zekâ kaynaklı bir zararda sorumluluğun hukuki temelini (haksız fiil, kusursuz sorumluluk, sözleşmeye aykırılık) belirleyip geliştirici, sistemi kullanan ve veri sağlayıcı arasındaki dağılımı ve ispat yükünü çözümlemek.

## Soğuk başlangıç (intake)
1. Zarar nasıl doğdu: hatalı/önyargılı karar, yanlış üretken çıktı (uydurma bilgi), otonom cihaz/araç davranışı, veri sızıntısı?
2. Taraflar arasında sözleşme var mı (kullanım koşulları, hizmet sözleşmesi)?
3. Sistemi işleten kim; çıktı insan denetiminden geçti mi?
4. Zarar bedensel/mali/manevi mi; mağdur tüketici mi, işletme mi?

## Denetim şeması
1. **Sözleşme/haksız fiil ayrımı**: Taraflar arasında sözleşme varsa öncelik TBK m.112 vd. (gereği gibi ifa etmeme) ve sorumluluk sınırlaması/genel işlem koşulu denetimi (m.20-25). Sözleşme yoksa haksız fiil (m.49 vd.): fiil, hukuka aykırılık, kusur, zarar, illiyet. Ara sonuç: hangi rejim.
2. **Kusursuz sorumluluk**: Yapay zekâyı bir yardımcı kişi gibi kullanan işletme için **adam çalıştıranın sorumluluğu (TBK m.66)** ve riski yüksek otonom sistemlerde **tehlike sorumluluğu / tehlikeli işletme (TBK m.71)** tartışılır; bu hallerde kusur ispatı gerekmez, illiyet ve zarar yeter.
3. **İlliyet ve ispat**: YZ kararının "kara kutu" niteliği illiyetin ispatını zorlaştırır; bilirkişi, log ve model dokümanı kritik. İspat yükü kural olarak zarar görende; kusursuz sorumlulukta kusur dışındaki unsurlar yeterli.
4. **Üretken model çıktısı**: Yanlış/iftira niteliğinde çıktıda kişilik hakkı ihlali (TMK m.24-25, TBK m.58 manevi tazminat) ve sağlayıcının özen yükümlülüğü.
5. **Rücu ve dağıtım**: Müteselsil sorumlulukta (TBK m.61) iç ilişkide kusur/sözleşme uyarınca rücu; geliştirici-kullanan arası sözleşmedeki tazmin ve sorumluluk maddeleri belirleyici.

AB'de Ürün Sorumluluğu Direktifi reformu karşılaştırmalı kaynaktır, Türkiye'de doğrudan uygulanmaz. Künyeyi [DOĞRULANMADI] işaretle.

## Çıktı modülleri
- Sorumluluk temeli ve taraf matrisi.
- İspat ve delil (log/bilirkişi) gereksinim listesi.
- Tazminat talebi veya savunma stratejisi taslağı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

