---
argument-hint: ''
description: Kanun hâkime takdir alanı bıraktığında ya da durumun gereğini, haklı
  sebepleri veya hakkaniyeti gözetmeyi emrettiğinde; bu takdirin hangi ölçütlere göre
  ve hangi sınırlar içinde kullanılacağını belirl
name: hakimin-takdir-yetkisi-tmk-4
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


# Hâkimin Takdir Yetkisi ve Hakkaniyet (TMK m.4)

## Görev
Kanunun takdir yetkisi tanıdığı veya hakkaniyeti emrettiği hâllerde, hâkimin hukuka ve hakkaniyete uygun kararının dayanması gereken ölçütleri belirlemek ve takdirin sınırlarını/denetlenebilirliğini göstermek.

## Soğuk başlangıç (intake)
- Hangi kanun hükmü takdir yetkisi/hakkaniyet atfı içeriyor (ör. manevi tazminat TBK m.56, tazminatın indirilmesi TBK m.51-52, nafaka, cezai şartın tenkisi TBK m.182/3)?
- Takdiri etkileyecek somut vakıalar neler (kusur derecesi, ekonomik durum, olayın özellikleri)?
- Taraflar takdir için hangi ölçütleri öne sürüyor?
- Karar gerekçesinde takdir nasıl denetlenebilir kılınacak?

## Denetim şeması
1. **Takdir yetkisinin kaynağı** — TMK m.4: hâkim, kanunun takdir yetkisi tanıdığı veya durumun gereğini ya da haklı sebepleri göz önünde tutmayı emrettiği hâllerde, *hukuka ve hakkaniyete göre* karar verir. Önce kanunun böyle bir alan açıp açmadığı belirlenir.
2. **Keyfîlik yasağı** — Takdir, sınırsız serbestlik değildir; somut olayın özellikleri, tarafların durumu ve hükmün amacı gözetilerek gerekçelendirilir. Gerekçesiz takdir, denetime kapalı olduğu için hukuka aykırıdır.
3. **Tipik uygulama alanları** — Manevi tazminat miktarı (TBK m.56), tazminattan indirim (TBK m.51-52: kusurun ve durumun gereği), cezai şartın aşırılığı (TBK m.182/3), uyarlama, nafaka takdiri; her birinde kendi özel ölçütleri esas alınır.
4. **Hakkaniyet ölçütleri** — Tarafların ekonomik-sosyal durumu, kusur dereceleri, olayın ağırlığı, caydırıcılık ve zenginleşme yasağı dengesi gibi ölçütler somut biçimde tartılır.
5. **Denetlenebilirlik** — İlk derece takdiri, istinaf/temyizde "takdirin sınırlarının aşılıp aşılmadığı" yönünden denetlenir; ölçütler kararda açıkça gösterilmelidir.
6. **m.1 ile fark** — m.1 boşluk hâlinde kural *yaratma*dır; m.4 var olan bir kuralın hâkime bıraktığı alanın *doldurulması*dır.

## Çıktı modülleri
- Takdir/hakkaniyet atfı içeren hükmün tespiti.
- Somut takdir ölçütleri listesi (olaya uyarlanmış).
- Gerekçeli takdir önerisi (denetlenebilir).
- Üst yargı denetimi notu + ilkesel içtihat `[DOĞRULANMADI]`.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

