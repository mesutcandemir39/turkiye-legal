---
argument-hint: ''
description: Bir kişinin birden çok suç işlediği veya tek fiille birden çok norm ihlal
  ettiği durumlarda zincirleme suç, fikri içtima ve bileşik suç kurallarını uygulamak
  gerektiğinde kullanılır.
name: ictima-suclarin-birlesmesi
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
  - ad: Türk Ceza Kanunu
    numara: '5237'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İçtima — Suçların Birleşmesi

## Görev
Birden fazla fiil veya tek fiille birden fazla norm ihlalinde, kaç suçtan ve hangi ceza ilkesiyle sorumluluk doğacağını (gerçek içtima, zincirleme suç, fikri içtima, bileşik suç) belirlemek.

## Soğuk başlangıç (intake)
- Kaç ayrı fiil var; bunlar aynı mağdura mı, farklı mağdurlara mı yöneldi?
- Fiiller aynı suç işleme kararının icrası mı, bağımsız kararlar mı?
- Tek bir fiil mi var, ama birden çok suç tanımına mı uyuyor?
- Bir suç, başka bir suçun unsuru ya da ağırlaştırıcı hâli mi?

## Denetim şeması
1. **Kural — gerçek içtima:** Birden çok fiille birden çok suç işleyen, her suçtan ayrı cezalandırılır; bu temel ilkedir, istisnalar aşağıdadır.
2. **Bileşik suç (m.42):** Biri diğerinin unsuru/ağırlaştırıcı nedeni olan suçlarda tek ceza; ayrıca içtima uygulanmaz (örn. yağmada cebir + alma).
3. **Zincirleme suç (m.43/1):** Aynı suç işleme kararıyla, aynı kişiye karşı değişik zamanlarda aynı suçun birden çok işlenmesinde tek ceza verilir ve artırılır. Aynı anda tek fiille birden çok kişiye karşı işlenmesi de değerlendirilir. Ara sonuç: tek karar bütünlüğü var mı?
4. **Zincirleme suç sınırı (m.43/3):** Yağma, kasten öldürme, kasten yaralama gibi sayılan suçlarda zincirleme hükmü uygulanmaz.
5. **Fikri içtima (m.44):** Tek fiille birden çok farklı suç oluşuyorsa, en ağır cezayı gerektiren suçtan cezalandırılır. Ara sonuç: fiil tek mi?
6. **Mağdur ve hukuki konu denetimi:** Korunan hukuki yararın çokluğu ve mağdur sayısı, içtima sonucunu doğrudan etkiler.

## Çıktı modülleri
- İçtima türü belirleme akış şeması.
- Suç sayısı ve ceza artırım/seçim notu.
- Zincirleme suç istisnaları kontrol listesi.
- Eksik vakıa ve `[DOĞRULANMADI]` içtihat ihtiyacı.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

