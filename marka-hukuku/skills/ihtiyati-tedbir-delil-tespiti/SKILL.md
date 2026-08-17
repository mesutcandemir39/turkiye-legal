---
argument-hint: ''
description: Devam eden tecavüzün acilen durdurulması, kanıtların kaybolmadan tespiti
  veya taklit ürünün ithalat/ihracatta durdurulması gerekiyorsa; m.159 tedbir ve gümrük
  süreçlerini yürütmek için kullanılır.
name: ihtiyati-tedbir-delil-tespiti
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
  - ad: Sınai Mülkiyet Kanunu
    numara: '6769'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# İhtiyati Tedbir, Delil Tespiti ve Gümrük Önlemleri

## Görev
Tecavüzün yarattığı acil zararı önlemek için SMK m.159 ihtiyati tedbir, HMK m.400 vd. delil tespiti ve gümrükte el koyma süreçlerini yürütmek. Amaç, esas dava sonuçlanana kadar mevcut durumu korumak ve kanıt kaybını engellemektir.

## Soğuk başlangıç (intake)
- Tecavüz devam ediyor mu, gecikmede tehlike somut mu?
- Taklit ürün üretiliyor/satılıyor/ithal mi ediliyor?
- Kanıtlar kaybolma/değiştirilme riski altında mı?
- Talep esas davadan önce mi, dava sırasında mı?

## Denetim şeması
1. **Tedbir şartları (m.159, HMK m.389).** Tescilli marka hakkına tecavüz veya ciddi tecavüz tehlikesi; verilecek hükmün etkinliğini sağlama gerekliliği; gecikmede tehlike. Yaklaşık ispat yeterlidir.
2. **Tedbir içeriği (m.159/2).** Tecavüz oluşturan fiillerin durdurulması/önlenmesi, taklit ürünlere/araçlara el konulması ve muhafazası, teminat. Talep esas davadan önce de istenebilir; bu halde m.159/HMK uyarınca süresinde dava açılması gerekir.
3. **Teminat ve tazminat.** Tedbir kural olarak teminat karşılığı; haksız tedbirde karşı tarafın zararından sorumluluk doğar.
4. **Delil tespiti (HMK m.400 vd.).** Tecavüz delillerinin (ürün, fatura, üretim) mahkemece tespiti; ileride kaybolma riskine karşı.
5. **Gümrükte el koyma (m.159 ve Gümrük mevzuatı).** Hak sahibinin başvurusuyla, marka hakkını ihlal eden eşyaya gümrük idaresince el konulabilir; süresinde dava/işlem yapılmazsa eşya serbest bırakılır.
6. **Görev/yetki.** FSHHM (m.156); tedbir talebi esas davayı görecek mahkemeden istenir.

## Çıktı modülleri
- Tedbir şartları altlama notu (tecavüz + gecikme tehlikesi + etkinlik).
- Tedbir/delil tespiti talep dilekçesi iskeleti.
- Gümrük başvurusu ve süre takip listesi.



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

