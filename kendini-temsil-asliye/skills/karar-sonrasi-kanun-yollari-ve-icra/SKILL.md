---
argument-hint: ''
description: Karar çıktıktan sonra istinaf-temyiz başvurusu yapmak, lehine kararı
  icraya koymak veya aleyhine kararın icrasını durdurmak isteyen taraf için kullanılır.
name: karar-sonrasi-kanun-yollari-ve-icra
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
  - ad: Hukuk Muhakemeleri Kanunu
    numara: '6100'
    tur: kanun
  version: 0.1.0
user-invocable: true
---


# Karar Sonrası Kanun Yolları ve İcra

## Görev
Kararı aldıktan sonraki adımları yönetmek: itiraz (istinaf/temyiz) süresini korumak; lehe kararı icra etmek; aleyhe kararda zarar görmemek.

## Soğuk başlangıç (intake)
- Karar lehinize mi, aleyhinize mi sonuçlandı?
- Gerekçeli karar tebliğ edildi mi, tarihi nedir?
- Karara itiraz mı etmek istiyorsunuz, yoksa icraya mı koyacaksınız?
- Uyuşmazlık değeri istinaf/temyiz sınırının üstünde mi?
- Karşı taraf ödeme yapmaya yanaşıyor mu?

## Denetim şeması
1. **İstinaf (HMK m.341-360):** İlk derece kararına karşı kanun yolu istinaftır. Süre, gerekçeli kararın tebliğinden itibaren **iki haftadır** (m.345). Miktar/değer belli bir parasal sınırın altındaysa karar kesindir, istinafa gidilemez — sınır yıllık güncellenir, **[DOĞRULANMADI]**. İstinaf dilekçesinde sebepler açıkça gösterilir (m.342).
2. **Temyiz (HMK m.361 vd.):** İstinaf kararına karşı, kanunda öngörülen parasal sınırın üzerindeki uyuşmazlıklarda temyiz yolu açıktır; süre tebliğden iki haftadır. Bazı kararlar kesindir (m.362).
3. **İcranın durması:** İstinaf/temyiz başvurusu kural olarak icrayı kendiliğinden durdurmaz; kararı veren para/teslim ilamı icra edilebilir. Aleyhine karar olan taraf, teminat göstererek icranın geri bırakılmasını (tehir-i icra) talep edebilir (İİK m.36).
4. **Lehe kararın icrası (2004 sayılı İİK):** Kesinleşmesi gerekmeyen para ilamları için ilamlı icra takibi başlatılır (İİK m.24 vd.); icra dairesine başvurularak icra emri çıkarılır.
5. **Ara sonuç:** Süre korunur (itiraz edilecekse) veya icra takibi açılır; aleyhe kararda tehir-i icra değerlendirilir.

## Çıktı modülleri
- İstinaf/temyiz dilekçesi iskeleti (sebepler bölümüyle) ve süre uyarısı.
- İlamlı icra takip yol haritası (lehe karar).
- Tehir-i icra/teminat seçeneği notu (aleyhe karar).



## Kaynak kuralı (katı)

- **İçtihat yalnızca doğrulanmış künyeyle.** Her karar mahkeme + daire + **esas/karar numarası** + tarih + doğrulanabilir kaynak ile.
- **MCP araçları varsa resmî metni onlardan çek.** `turkiye-legal-mevzuat-mcp` kuruluysa `madde_getir` / `kanun_metni_getir` ile getir; `turkiye-legal-ictihat-mcp` kuruluysa `ictihat_ara` / `karar_getir` ile.
- **Varsayımları açıkça işaretle.**

